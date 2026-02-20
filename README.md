# Crovia Evidence Lab

**Public, reproducible evidence artifacts for AI training provenance.**

Auto-synced hourly from the [Crovia Temporal Proof Registry](https://croviatrust.com).

[![Sync Status](https://img.shields.io/badge/sync-hourly-blue)]()
[![License](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)

---

> It does not accuse. It does not infer intent. It does not judge compliance.
> It records **what can be objectively observed and verified**.

---

## Live Numbers

Check [`SYNC_STATUS.json`](SYNC_STATUS.json) for the latest counts, or visit the [live registry](https://registry.croviatrust.com/registry/).

---

## Repository Structure

```
crovia-evidence-lab/
├── open/                    # Live observation data (auto-synced hourly)
│   ├── drift/               # DDF drift detection snapshots
│   ├── forensic/            # Absence receipts and forensic analysis
│   ├── reports/             # Disclosure reports and weekly indexes
│   ├── canon/               # Target watchlist
│   ├── signal/              # Signal detection artifacts
│   └── temporal/            # Temporal proof chains
├── snapshots/               # Latest registry state (auto-synced hourly)
│   ├── registry_stats.json  # Current observation counts
│   ├── merkle_proof.json    # Merkle root for integrity verification
│   └── recent_observations.json
├── badges/                  # SVG trust badges per model
├── cep-capsules/            # Cryptographic Evidence Protocol packages
├── SYNC_STATUS.json         # Last sync timestamp and observation counts
└── sync_from_server.sh      # Sync script (runs hourly on production server)
```

---

## Evidence Layers

### 1. `open/` — Live Observations (auto-updated)

The `open/` directory contains the latest data from the Crovia autonomous observer. It is updated every hour from the Hetzner production server.

- **`drift/`** — Drift Detection Framework snapshots. Tracks changes in model documentation over time.
- **`forensic/`** — Absence receipts. Cryptographically timestamped records of missing training evidence.
- **`reports/`** — Weekly disclosure reports and indexes.
- **`signal/`** — Signal detection artifacts from multi-source analysis.
- **`temporal/`** — Temporal proof chains (append-only, immutable).

### 2. `snapshots/` — Registry State (auto-updated)

Real-time snapshots of the registry's state, pulled directly from the API:

```bash
# Verify locally
curl https://registry.croviatrust.com/api/registry/stats
curl https://registry.croviatrust.com/api/registry/merkle
```

### 3. `badges/` — Trust Badges

SVG badges showing the observation status of individual AI models. Generated from the NEC# (Necessary Evidence Criteria) framework.

### 4. `cep-capsules/` — Cryptographic Evidence Packages

Self-contained, verifiable evidence capsules. Each CEP contains:
- Observation data
- Merkle proof
- Timestamp chain
- Reproducibility manifest

### 5. `SYNC_STATUS.json` — Live Counts

Updated every hour with the current observation count and unique targets. Machine-readable.

---

## How to use this data

### For researchers
```bash
git clone https://github.com/croviatrust/crovia-evidence-lab.git
# Browse open/forensic/ for absence receipts
# Browse snapshots/ for current registry state
```

### For auditors
```bash
# Verify merkle integrity
python3 -c "
import json
m = json.load(open('snapshots/merkle_proof.json'))
print(f'Root: {m[\"merkle_root\"]}')
print(f'Observations: {m[\"total_observations\"]}')
"
```

### For regulators
The `open/reports/` directory contains structured disclosure reports aligned with the EU AI Act transparency requirements. Each report references the NEC# framework — 10 standardized documentation criteria.

---

## Sync mechanism

This repository is automatically updated every hour by the Crovia production server:

1. Autonomous observer records observations (presence/absence of training evidence)
2. Data is exported to structured JSONL/JSON
3. `sync_from_server.sh` pushes changes to this repository
4. Each commit is tagged with observation count and timestamp

The server-side observer runs independently, 24/7, without human intervention.

---

## What is deliberately missing

- Pricing or commercial features
- Attribution rules or legal conclusions
- Intent analysis or compliance judgments
- Private or gated data

Everything here is public, verifiable, and reproducible.

---

## Related

- [Live Registry](https://registry.croviatrust.com/registry/) — real-time observation stream
- [CEP Terminal](https://registry.croviatrust.com/registry/cep/) — generate evidence capsules
- [Crovia Home](https://croviatrust.com) — project overview
- [Omission Ledger](https://registry.croviatrust.com/registry/omissions) — targets without evidence
- [NEC# Framework](https://registry.croviatrust.com/registry/compliance/) — documentation criteria

---

## License

Apache 2.0 — see [LICENSE](LICENSE).

Evidence is not accusation. Observation is not judgment.
Crovia Evidence Lab exists to **make facts inspectable**, not to tell anyone what they mean.
