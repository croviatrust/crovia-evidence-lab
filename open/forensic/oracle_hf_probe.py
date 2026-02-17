#!/usr/bin/env python3
"""Dry-run HuggingFace disclosure probe using CROVIA PRO OmissionOracle.

Purpose:
- Fetch HF cardData for a sample of model/dataset targets
- Run OmissionOracle (PRO) locally
- Produce a JSONL report with verifiable anchors (HF API URL + card hash) and Oracle proofs

IMPORTANT:
- This script does NOT write to the TPR database.
- It is for internal evaluation of what signal we can extract.

Usage (Windows/PowerShell):
  python open/forensic/oracle_hf_probe.py --limit-models 10 --limit-datasets 10

Output:
  open/forensic/output/oracle_hf_probe_<UTC>.jsonl
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

# Ensure we can import PRO modules from local workspace
REPO_ROOT = Path(__file__).resolve().parents[2]
PRO_ROOT = REPO_ROOT / "crovia-pro-engine"
if str(PRO_ROOT) not in sys.path:
    sys.path.insert(0, str(PRO_ROOT))

from croviapro.oracle.omission_oracle import OmissionOracle  # noqa: E402


HF_TIMEOUT_SECS = 15
HF_HEADERS = {
    "User-Agent": "CroviaOracleProbe/1.0 (evidence-first; contact: croviatrust.com)",
}


def utc_now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def load_targets(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict) and "targets" in data:
        targets = data.get("targets") or []
        if not isinstance(targets, list):
            raise ValueError("targets must be a list")
        return targets

    if isinstance(data, list):
        return data

    raise ValueError("Unsupported targets file format")


def is_internal_target(target_id: str) -> bool:
    t = (target_id or "").strip().lower()
    return t.startswith("crovia/") or t.startswith("croviatrust/")


def fetch_hf_api(kind: str, target_id: str) -> Tuple[Optional[Dict[str, Any]], Dict[str, Any]]:
    """Fetch HF API JSON.

    Returns:
      (json_or_none, meta)
    """
    if kind == "model":
        url = f"https://huggingface.co/api/models/{target_id}"
    elif kind == "dataset":
        url = f"https://huggingface.co/api/datasets/{target_id}"
    else:
        raise ValueError(f"Unsupported kind: {kind}")

    meta: Dict[str, Any] = {"url": url}

    try:
        r = requests.get(url, headers=HF_HEADERS, timeout=HF_TIMEOUT_SECS)
        meta["http_status"] = r.status_code
        meta["fetched_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        if r.status_code != 200:
            meta["error"] = f"HTTP {r.status_code}"
            return None, meta
        j = r.json()
        return j, meta
    except Exception as e:
        meta["error"] = f"{type(e).__name__}: {e}"
        return None, meta


def oracle_result_to_dict(result) -> Dict[str, Any]:
    """Convert OracleResult dataclass to JSON-safe dict."""
    out = result.to_dict() if hasattr(result, "to_dict") else asdict(result)

    # Reduce payload size: keep only a subset of raw YAML keys (still verifiable by card hash)
    decl = out.get("declarations") or {}
    if "raw_yaml" in decl and isinstance(decl["raw_yaml"], dict):
        # keep only a small allowlist of keys
        keep_keys = {"license", "datasets", "language", "tags", "pipeline_tag", "model-index"}
        decl["raw_yaml"] = {k: v for k, v in decl["raw_yaml"].items() if k in keep_keys}
        out["declarations"] = decl

    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--targets-file",
        default=str(REPO_ROOT / "crovia-automation" / "targets_merged_450.json"),
    )
    p.add_argument("--limit-models", type=int, default=10)
    p.add_argument("--limit-datasets", type=int, default=10)
    p.add_argument("--out-dir", default=str(REPO_ROOT / "open" / "forensic" / "output"))
    p.add_argument("--include-internal", action="store_true")
    args = p.parse_args()

    targets_path = Path(args.targets_file)
    targets = load_targets(targets_path)

    # Build sample lists
    models: List[str] = []
    datasets: List[str] = []

    for t in targets:
        tid = (t or {}).get("target_id")
        ttype = (t or {}).get("tipo_target")
        if not tid or not ttype:
            continue
        if not args.include_internal and is_internal_target(tid):
            continue

        if ttype == "model" and len(models) < args.limit_models:
            models.append(tid)
        elif ttype == "dataset" and len(datasets) < args.limit_datasets:
            datasets.append(tid)

        if len(models) >= args.limit_models and len(datasets) >= args.limit_datasets:
            break

    oracle = OmissionOracle()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"oracle_hf_probe_{utc_now_compact()}.jsonl"

    run_meta = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "targets_file": str(targets_path),
        "sample": {"models": len(models), "datasets": len(datasets)},
    }

    with out_path.open("w", encoding="utf-8") as f:
        f.write(json.dumps({"type": "run_meta", **run_meta}, ensure_ascii=False) + "\n")

        for tid in models:
            api_json, meta = fetch_hf_api("model", tid)
            row: Dict[str, Any] = {
                "type": "probe_result",
                "target_id": tid,
                "tipo_target": "model",
                "hf": meta,
            }
            if api_json is not None:
                try:
                    result = oracle.analyze_model(api_json, generate_evidence=True)
                    row["oracle"] = oracle_result_to_dict(result)
                except Exception as e:
                    row["oracle_error"] = f"{type(e).__name__}: {e}"
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

        for tid in datasets:
            api_json, meta = fetch_hf_api("dataset", tid)
            row = {
                "type": "probe_result",
                "target_id": tid,
                "tipo_target": "dataset",
                "hf": meta,
            }
            if api_json is not None:
                try:
                    result = oracle.analyze_dataset(api_json, generate_evidence=True)
                    row["oracle"] = oracle_result_to_dict(result)
                except Exception as e:
                    row["oracle_error"] = f"{type(e).__name__}: {e}"
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"[CROVIA] wrote: {out_path}")
    print(f"[CROVIA] sample: models={len(models)} datasets={len(datasets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
