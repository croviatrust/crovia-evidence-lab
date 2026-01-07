# CEPT Run — 2026-01-07

This run freezes official public sources and records whether **explicit, dataset-specific training evidence**
is publicly present at the time of observation.

The run is **immutable** once written.

No interpretation.  
No inference.  
Only frozen, observable facts.

---

## What this run contains

This directory captures a **complete snapshot** of the observation process.

Key files:

- `meta/run_index.json`  
  → Run metadata (date, scope, sources)

- `logs/observation_log.ndjson`  
  → Raw observation events (terms, snippets, timestamps)

- `records/evidence_records.ndjson`  
  → Normalized CEPT evidence records

- `records/evidence_records.signed.ndjson`  
  → Cryptographically signed evidence records

- `proofs/MANIFEST.sha256`  
  → Canonical file list with SHA-256 hashes

- `proofs/hashchain_*`  
  → Rolling hash-chains anchoring record order and integrity

---

## How to verify integrity (offline)

Run:

sha256sum -c proofs/MANIFEST.sha256

If verification passes:

- the run is complete
- the artifacts are untampered
- the observation is reproducible

If verification fails:

- at least one artifact was altered
- the run must be considered invalid

---

## What this run asserts

This run asserts **one thing only**:

> At this point in time, under sustained observation,  
> explicit dataset-specific training evidence was either  
> **publicly present** or **publicly absent**.

Nothing more.

