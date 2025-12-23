[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

# Crovia Evidence Lab

Crovia Evidence Lab is the **public, reproducible evidence layer** of Crovia.

This repository exists to demonstrate — with verifiable artifacts —
**what can be proven** about AI training transparency, without
introducing pricing, contracts, or private calibration logic.

## What lives here

- **DSSE (Open Evidence)**  
  Demonstrations of semantic drift measurement on public datasets
  (LAION, C4, DSSE-1M), with reproducible snapshots and hash anchors.

- **Spider (Presence / Absence Observation)**  
  Public observation tools and receipts recording whether auditable
  training evidence is present or absent in public repositories.

- **Proof Artifacts**  
  NDJSON snapshots, drift records, and hash-anchored files that can be
  verified offline by third parties.

## What does NOT live here

- Pricing or settlement logic
- Contract registries
- Enterprise calibration engines
- Proprietary attribution models

This repository demonstrates **evidence**.
The Crovia PRO Engine defines **settlement and governance**.

## External Evidence Datasets

Some datasets are included as **Git submodules** to preserve provenance
and independent verification:

- `dsse/datasets/hf_dsse_1m`
- `dsse/datasets/laion_dsse`

Clone with:

git clone --recurse-submodules <repo-url>


---

## How to Reproduce DSSE Evidence (Open)

This repository contains **fully reproducible, open-grade evidence**
generated with the Crovia DSSE open pipeline.

No credentials. No private engines. No hidden steps.

---

### Requirements

- Python 3.10+
- Linux / macOS (tested on Ubuntu)
- ~1 GB free disk space (for DSSE-1M datasets)

Optional:
- jq for inspection

---

### 1. Clone with submodules

git clone --recurse-submodules https://github.com/croviatrust/crovia-evidence-lab.git
cd crovia-evidence-lab

---

### 2. Run DSSE Open snapshot (example)

This produces a semantic snapshot over NDJSON input
using the open DSSE counters (non-PRO).

python dsse/tools/dsse_snapshot_builder.py \
  --in dsse/datasets/laion_dsse/snapshot_A.json \
  --out proofs/drift/dsse_snapshot_open.json

Expected output:

[DSSE-SNAPSHOT] wrote proofs/drift/dsse_snapshot_open.json

---

### 3. Generate trust drift (open)

python dsse/tools/trust_drift.py \
  --before proofs/drift/dsse_snapshot_open.json \
  --after proofs/drift/dsse_snapshot_open.json \
  --out proofs/drift/trust_drift_open.ndjson

This produces a neutral drift record:

- no attribution
- no legal inference
- no policy mapping

---

### 4. Inspect results

cat proofs/drift/trust_drift_open.ndjson | jq .

Fields of interest:

- schema
- inputs
- delta
- engine.method

---

## What This Proves

- DSSE snapshots are bounded-memory
- Drift can be computed offline
- Outputs are hash-addressable
- No PRO logic is required to verify integrity

---

## What This Does NOT Prove

- No attribution to model vendors
- No training confirmation
- No legal compliance claims

This is evidence of process, not accusation.

