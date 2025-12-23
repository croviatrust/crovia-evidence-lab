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

