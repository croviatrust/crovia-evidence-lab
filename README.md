[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

# Crovia Evidence Lab

Crovia Evidence Lab is the **public, reproducible evidence layer** of Crovia.

All artifacts in this repository are generated using the
**Crovia Core Engine (Open Core)**, which defines the schemas,
validation rules, and integrity primitives used here.

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


---

## How to Reproduce Spider Evidence (Presence / Absence)

Crovia Spider is an **observation-only tool**.

It records whether **auditable AI training evidence artifacts**
are publicly present at a given point in time.

No inference. No attribution. No enforcement.

---

### What Spider observes

Spider checks for the presence of **public evidence markers**, such as:

- EVIDENCE.json
- trust_bundle.v1.json
- cep_capsule.v1.json
- declared receipts or hashes

The result is a **binary observable fact**:
- present
- absent

---

### 1. Inspect raw Spider observations

Raw observations are preserved verbatim:

cat spider/raw/presence/github_presence_raw.jsonl | head -n 5

These files contain:
- timestamp
- repository URL
- HTTP status
- discovery result

---

### 2. Inspect normalized presence receipts

Spider also produces normalized receipts:

cat spider/data/presence/github_presence_v1.jsonl | jq .

Each record includes:
- schema
- target
- observed_at
- presence: true | false
- source

---

### 3. What makes this verifiable

- Inputs are public URLs
- Observations are timestamped
- Raw data is preserved
- Normalized output is schema-bound
- Anyone can repeat the observation and compare results

---

## What This Does NOT Claim

- No claim of AI training usage
- No claim of wrongdoing
- No policy violation
- No legal judgment

Spider records absence as a condition, not as guilt.

---

## Why Absence Matters

If AI systems require transparency,
absence of evidence is itself observable.

Crovia records that absence
without interpretation.

