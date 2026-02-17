#!/usr/bin/env python3
"""
hubble_continuum.py — Hubble Continuum Orchestrator (HCO) v0.2
OPEN-GRADE: Observable, Persistent, Evidence-based Neutral Grading of Absence Data Evolution.
Interval-based absence history + lineage + neutral mutation metrics + neutral temporal clusters.

What this file DOES:
- Ingests AbsenceAtoms (negative observations)
- Builds living GapIntervals (open/closed) with lineage (parent -> child on mutation)
- Computes neutral mutation metrics (e.g., mutations_30d, chain_length, mutation_density)
- Computes neutral temporal clusters (e.g., many models mutated on same day)

What this file does NOT do (by design):
- No intent attribution ("evasion", "fraud", "violation")
- No legal article mapping, no recommendations, no regulator narrative
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple
import math
import uuid

# -----------------------------
# Data models
# -----------------------------

@dataclass
class AbsenceAtom:
    ts: datetime
    crovia_id: str
    gap_id: str
    obs_strength: float                 # 0..1 (how hard we looked)
    signal_vector: Dict[str, float]     # deterministic features
    evidence_refs: List[str]            # snapshot/receipt ids etc.

@dataclass
class PresenceAtom:
    """
    Optional positive observation: used to close open intervals without changing history.
    If you don't have presence probes yet, you can ignore this and intervals remain open.
    """
    ts: datetime
    crovia_id: str
    gap_id: str
    evidence_refs: List[str]            # proof of presence

@dataclass
class GapInterval:
    interval_id: str
    crovia_id: str
    gap_id: str

    start: datetime
    end: Optional[datetime] = None
    last_seen: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    # evolution
    persistence_days: int = 1
    observations: int = 1
    obs_strength_sum: float = 0.0
    obs_strength_avg: float = 0.0

    # scoring (OPEN-grade: numeric only)
    severity: float = 0.0
    level: str = "OBSERVED"             # OBSERVED/PERSISTENT/STRUCTURAL/SYSTEMIC
    confidence: float = 0.0             # 0..1 (credibility of negative observation)

    # lineage
    parent_interval: Optional[str] = None
    lineage: List[str] = field(default_factory=list)   # chain ids (parents) leading to this interval
    mutation_count_total: int = 0                      # total mutations in this chain up to here
    mutations_30d: int = 0                             # mutations in last 30d window (chain-local)
    mutation_density_30d: float = 0.0                  # mutations_30d / 30

    # content
    fingerprint: Dict[str, float] = field(default_factory=dict)
    evidence_refs: List[str] = field(default_factory=list)

    # closure
    closure_reason: Optional[str] = None               # e.g., "closure_by_presence"
    closure_evidence_refs: List[str] = field(default_factory=list)

# -----------------------------
# Defaults / configuration
# -----------------------------

DEFAULT_GAP_BASE_WEIGHTS: Dict[str, float] = {
    "absence:evidence.training.disclosure": 3.0,
    "absence:license.traceability": 2.5,
    "absence:provenance.linkage": 2.0,
    "absence:model_card.completeness": 1.5,
}

LEVELS = ["OBSERVED", "PERSISTENT", "STRUCTURAL", "SYSTEMIC"]

def _nowz() -> datetime:
    return datetime.now(timezone.utc)

def _sigmoid(x: float) -> float:
    # stable-ish sigmoid
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)

def cosine_sim(a: Dict[str, float], b: Dict[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)

def update_fingerprint(old: Dict[str, float], new: Dict[str, float], alpha: float = 0.7) -> Dict[str, float]:
    """
    Exponential moving average on feature dict.
    alpha close to 1 = conservative (slow change).
    """
    out = dict(old)
    for k, v in new.items():
        out[k] = alpha * out.get(k, 0.0) + (1.0 - alpha) * float(v)
    return out

def compute_severity(persistence_days: int, observations: int, gap_weight: float) -> float:
    """
    OPEN-grade severity: numeric escalation only.
    (No intent, no legal mapping.)
    """
    P = math.log(1.0 + max(0, persistence_days))
    O = math.log(1.0 + max(0, observations))
    G = float(gap_weight)
    raw = 0.4 * P + 0.4 * O + 0.2 * G
    return _sigmoid(raw)

def compute_confidence(obs_strength_avg: float, observations: int) -> float:
    """
    Credibility of negative observation.
    - increases with mean obs_strength
    - increases with repetitions, but with diminishing returns
    """
    o = float(max(0, observations))
    rep = 1.0 - math.exp(-0.35 * o)          # asymptotes to 1
    base = max(0.0, min(1.0, float(obs_strength_avg)))
    return max(0.0, min(1.0, 0.6 * base + 0.4 * rep))

def promote_level(sev: float) -> str:
    if sev > 0.85:
        return "SYSTEMIC"
    if sev > 0.65:
        return "STRUCTURAL"
    if sev > 0.40:
        return "PERSISTENT"
    return "OBSERVED"

# -----------------------------
# Hubble Continuum Orchestrator
# -----------------------------

class HubbleContinuum:
    """
    Interval-based absence history, with lineage + neutral mutation metrics.

    You can run this as a library:
      hc = HubbleContinuum()
      hc.ingest_absence(atom)
      hc.ingest_presence(presence_atom)  # optional
      intervals = hc.export_intervals()
      clusters = hc.export_mutation_clusters()
    """

    def __init__(
        self,
        *,
        tau_in: float = 0.85,
        tau_mut: float = 0.60,
        ema_alpha: float = 0.7,
        gap_base_weights: Optional[Dict[str, float]] = None,
        mutation_window_days: int = 30,
    ):
        self.tau_in = float(tau_in)
        self.tau_mut = float(tau_mut)
        self.ema_alpha = float(ema_alpha)
        self.gap_base_weights = dict(gap_base_weights or DEFAULT_GAP_BASE_WEIGHTS)
        self.mutation_window_days = int(mutation_window_days)

        # all intervals (open + closed)
        self.intervals: List[GapInterval] = []
        # quick index by interval_id
        self._by_id: Dict[str, GapInterval] = {}

        # mutation events (neutral): list of {ts, crovia_id, gap_id, child_interval_id, parent_interval_id}
        self.mutation_events: List[Dict[str, Any]] = []

    # ---------
    # ingestion
    # ---------

    def ingest_absence(self, atom: AbsenceAtom) -> GapInterval:
        """
        Ingest a negative observation. Decides:
        - continue open interval (same crovia_id + gap_id) if similarity >= tau_in
        - mutate (close & open new linked interval) if similarity in [tau_mut, tau_in)
        - open new interval otherwise
        """
        atom_ts = self._ensure_tz(atom.ts)
        atom = AbsenceAtom(
            ts=atom_ts,
            crovia_id=str(atom.crovia_id),
            gap_id=str(atom.gap_id),
            obs_strength=float(atom.obs_strength),
            signal_vector=dict(atom.signal_vector),
            evidence_refs=list(atom.evidence_refs),
        )

        open_candidates = [
            i for i in self.intervals
            if i.crovia_id == atom.crovia_id and i.gap_id == atom.gap_id and i.end is None
        ]

        best: Optional[GapInterval] = None
        best_sim: float = -1.0

        for it in open_candidates:
            sim = cosine_sim(atom.signal_vector, it.fingerprint)
            if sim > best_sim:
                best_sim = sim
                best = it

        if best is not None and best_sim >= self.tau_in:
            self._continue_interval(best, atom)
            return best

        if best is not None and best_sim >= self.tau_mut:
            # mutation: close parent and open child with linkage
            child = self._mutate_interval(best, atom)
            return child

        # no suitable parent: open new
        child = self._open_new_interval(atom, parent=None)
        return child

    def ingest_presence(self, atom: PresenceAtom) -> Optional[GapInterval]:
        """
        Optional: close the currently open interval for (crovia_id, gap_id) using a positive observation.
        """
        ts = self._ensure_tz(atom.ts)
        crovia_id, gap_id = str(atom.crovia_id), str(atom.gap_id)
        refs = list(atom.evidence_refs)

        open_it = next(
            (i for i in self.intervals if i.crovia_id == crovia_id and i.gap_id == gap_id and i.end is None),
            None
        )
        if open_it is None:
            return None

        # close at ts (no deletion; history remains)
        open_it.end = ts
        open_it.closure_reason = "closure_by_presence"
        open_it.closure_evidence_refs.extend(refs)
        open_it.last_seen = ts
        open_it.persistence_days = max(1, (open_it.last_seen - open_it.start).days + 1)
        self._recalc_scores(open_it)
        return open_it

    # ---------
    # internals
    # ---------

    def _ensure_tz(self, dt: datetime) -> datetime:
        if dt.tzinfo is None:
            # assume UTC if naive (OPEN safety)
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)

    def _gap_weight(self, gap_id: str) -> float:
        return float(self.gap_base_weights.get(gap_id, 1.0))

    def _recalc_scores(self, it: GapInterval) -> None:
        it.severity = compute_severity(it.persistence_days, it.observations, self._gap_weight(it.gap_id))
        it.level = promote_level(it.severity)
        it.obs_strength_avg = (it.obs_strength_sum / max(1, it.observations))
        it.confidence = compute_confidence(it.obs_strength_avg, it.observations)

        # mutation metrics (chain-local)
        self._update_mutation_metrics(it)

    def _update_mutation_metrics(self, it: GapInterval) -> None:
        """
        Compute:
        - mutation_count_total: total mutations in lineage chain up to this interval
        - mutations_30d: count of mutation events in last N days relative to now (for open) or end (for closed)
        - mutation_density_30d: mutations_30d / N
        """
        chain_ids = list(it.lineage) + ([it.parent_interval] if it.parent_interval else [])
        chain_ids = [x for x in chain_ids if x]  # no Nones
        # total = number of parents in chain (each parent->child transition is a mutation)
        it.mutation_count_total = len(set(chain_ids))

        # windowed count based on mutation_events timestamps
        win = timedelta(days=self.mutation_window_days)
        t1 = _nowz() if it.end is None else it.end
        t0 = t1 - win
        cnt = 0
        for ev in self.mutation_events:
            if ev["crovia_id"] != it.crovia_id or ev["gap_id"] != it.gap_id:
                continue
            ts = ev["ts"]
            if t0 <= ts <= t1:
                cnt += 1

        it.mutations_30d = int(cnt)
        it.mutation_density_30d = float(cnt) / float(max(1, self.mutation_window_days))

    def _continue_interval(self, it: GapInterval, atom: AbsenceAtom) -> None:
        it.last_seen = atom.ts
        it.persistence_days = max(1, (it.last_seen - it.start).days + 1)
        it.observations += 1
        it.obs_strength_sum += max(0.0, min(1.0, atom.obs_strength))
        it.fingerprint = update_fingerprint(it.fingerprint, atom.signal_vector, alpha=self.ema_alpha)
        it.evidence_refs.extend(atom.evidence_refs)
        self._recalc_scores(it)

    def _mutate_interval(self, parent: GapInterval, atom: AbsenceAtom) -> GapInterval:
        # close parent just before atom timestamp (preserve causality)
        parent.end = atom.ts - timedelta(seconds=1)
        parent.last_seen = parent.end
        parent.persistence_days = max(1, (parent.last_seen - parent.start).days + 1)
        parent.closure_reason = "closure_by_mutation"
        self._recalc_scores(parent)

        # open child linked
        child = self._open_new_interval(atom, parent=parent)

        # record neutral mutation event
        self.mutation_events.append({
            "ts": atom.ts,
            "crovia_id": atom.crovia_id,
            "gap_id": atom.gap_id,
            "parent_interval_id": parent.interval_id,
            "child_interval_id": child.interval_id,
        })
        # update metrics again now that event exists
        self._recalc_scores(child)
        return child

    def _open_new_interval(self, atom: AbsenceAtom, parent: Optional[GapInterval]) -> GapInterval:
        interval_id = str(uuid.uuid4())
        lineage = []
        if parent is not None:
            lineage = list(parent.lineage) + [parent.interval_id]

        it = GapInterval(
            interval_id=interval_id,
            crovia_id=atom.crovia_id,
            gap_id=atom.gap_id,
            start=atom.ts,
            end=None,
            last_seen=atom.ts,
            persistence_days=1,
            observations=1,
            obs_strength_sum=max(0.0, min(1.0, atom.obs_strength)),
            fingerprint=dict(atom.signal_vector),
            evidence_refs=list(atom.evidence_refs),
            parent_interval=(parent.interval_id if parent else None),
            lineage=lineage,
        )
        self._recalc_scores(it)

        self.intervals.append(it)
        self._by_id[it.interval_id] = it
        return it

    # -----------------------------
    # Exports (HF-ready JSON)
    # -----------------------------

    def export_intervals(self) -> List[Dict[str, Any]]:
        """
        HF-ready list. Numeric, factual, neutral.
        """
        out: List[Dict[str, Any]] = []
        for it in self.intervals:
            out.append({
                "interval_id": it.interval_id,
                "crovia_id": it.crovia_id,
                "gap_id": it.gap_id,
                "start": it.start.isoformat(),
                "end": (it.end.isoformat() if it.end else None),
                "level": it.level,
                "severity": round(float(it.severity), 6),
                "confidence": round(float(it.confidence), 6),
                "days_open": int(it.persistence_days),
                "observations": int(it.observations),
                "obs_strength_avg": round(float(it.obs_strength_avg), 6),

                # lineage + mutation metrics (neutral)
                "parent_interval": it.parent_interval,
                "lineage": list(it.lineage),
                "mutation_count_total": int(it.mutation_count_total),
                f"mutations_{self.mutation_window_days}d": int(it.mutations_30d),
                f"mutation_density_{self.mutation_window_days}d": round(float(it.mutation_density_30d), 6),

                # evidence refs
                "evidence_refs": sorted(set(it.evidence_refs)),

                # closure (if any)
                "closure_reason": it.closure_reason,
                "closure_evidence_refs": sorted(set(it.closure_evidence_refs)),
            })
        return out

    def export_mutation_events(self) -> List[Dict[str, Any]]:
        """
        Neutral mutation event list (one per parent->child link).
        """
        out = []
        for ev in self.mutation_events:
            out.append({
                "ts": ev["ts"].isoformat(),
                "crovia_id": ev["crovia_id"],
                "gap_id": ev["gap_id"],
                "parent_interval_id": ev["parent_interval_id"],
                "child_interval_id": ev["child_interval_id"],
            })
        return out

    def export_mutation_clusters(self, *, min_models: int = 3, min_events: int = 3) -> List[Dict[str, Any]]:
        """
        Neutral temporal clusters:
        "On date D, X unique crovia_id had a mutation for gap_id G"
        No intent, no accusations.
        """
        # date -> gap_id -> set(crovia_id), list(child_interval_id)
        buckets: Dict[str, Dict[str, Dict[str, Any]]] = {}

        for ev in self.mutation_events:
            day = ev["ts"].date().isoformat()
            gap_id = ev["gap_id"]
            crovia_id = ev["crovia_id"]

            buckets.setdefault(day, {})
            buckets[day].setdefault(gap_id, {"models": set(), "intervals": []})

            buckets[day][gap_id]["models"].add(crovia_id)
            buckets[day][gap_id]["intervals"].append(ev["child_interval_id"])

        clusters: List[Dict[str, Any]] = []
        for day, per_gap in sorted(buckets.items()):
            for gap_id, meta in per_gap.items():
                models = meta["models"]
                events = len(meta["intervals"])
                if len(models) < int(min_models) or events < int(min_events):
                    continue
                clusters.append({
                    "date": day,
                    "gap_id": gap_id,
                    "models_affected": sorted(models),
                    "unique_models": len(models),
                    "mutation_events": events,
                    "child_interval_ids": meta["intervals"],
                })

        return clusters

# -----------------------------
# Minimal self-test (optional)
# -----------------------------
if __name__ == "__main__":
    # Minimal smoke-test (kept tiny; you’ll do real tests externally)
    hc = HubbleContinuum()

    base = {"f1": 0.9, "f2": 0.2, "f3": 0.7}
    mut  = {"f1": 0.9, "f2": 0.2, "f3": 0.1, "f4": 0.5}

    t0 = datetime(2025, 1, 1, tzinfo=timezone.utc)
    crovia_id = "model-123"
    gap_id = "absence:evidence.training.disclosure"

    # 3 atoms: continue
    for k in range(3):
        hc.ingest_absence(AbsenceAtom(
            ts=t0 + timedelta(days=k * 3),
            crovia_id=crovia_id,
            gap_id=gap_id,
            obs_strength=0.9,
            signal_vector=base,
            evidence_refs=[f"scan-{k}"],
        ))

    # 2 atoms: mutate
    for k in range(3, 5):
        hc.ingest_absence(AbsenceAtom(
            ts=t0 + timedelta(days=k * 3),
            crovia_id=crovia_id,
            gap_id=gap_id,
            obs_strength=0.9,
            signal_vector=mut,
            evidence_refs=[f"scan-{k}"],
        ))

    intervals = hc.export_intervals()
    clusters = hc.export_mutation_clusters(min_models=1, min_events=1)

    print("[INTERVALS]", len(intervals))
    print(intervals[-2:])
    print("[CLUSTERS]", clusters)
