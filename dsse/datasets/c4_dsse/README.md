---
license: apache-2.0
tags:
  - crovia
  - trust
  - provenance
  - auditability
  - dsse
  - c4
pretty_name: "C4 — Trust Drift Evidence (DSSE)"
datasets:
  - c4
---

# C4 — Trust Drift Evidence (DSSE)

This dataset contains **verifiable evidence** of trust drift measured on a public AI dataset (C4).

What you see here is **not a claim** and **not a benchmark**.

## Contents

- `DRIFT_SUMMARY.json`  
  → the measured drift signal

- `EVIDENCE.json`  
  → how the signal was produced (hashes, anchors, pipeline)

- `snapshot_A.json` / `snapshot_B.json`  
  → the two compared states

- `records_sample.ndjson`  
  → sample of analyzed records (extract from 1M stream)

## Principles

- No assumptions  
- No declared changes  
- No interpretation  

Only measurements.

Built with Crovia.
