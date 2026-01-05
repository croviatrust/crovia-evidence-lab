# DSSE — Dynamic Semantic Separation Evidence

DSSE records **observable semantic separation** between declared data groups.

It does not infer usage.
It does not infer intent.
It does not infer legality.

DSSE only measures **distance and divergence** in representation space.

---

## What DSSE represents

DSSE answers a single technical question:

> Are two declared semantic groups measurably distinct?

The result is an **observation**, not a conclusion.

---

## What DSSE is NOT

DSSE does NOT:
- detect training
- detect memorization
- detect infringement
- detect compliance

It only measures **relative semantic structure**.

---

## Core DSSE concept

Given:
- Group A (declared semantic set)
- Group B (declared semantic set)

DSSE computes:
- centroid distance
- dispersion overlap
- angular divergence
- stability across snapshots

These metrics are **repeatable and deterministic**.

---

## DSSE artifacts

Typical DSSE evidence includes:

- snapshot NDJSON
- drift timelines
- metric summaries
- neutral flags (no labels, no verdicts)

All DSSE outputs are:
- append-only
- reproducible
- verifiable offline

---

## Temporal dimension

DSSE supports **time-based comparison**.

This allows observation of:
- separation persistence
- convergence
- divergence
- neutral mutation

Time does not imply cause.

---

## Example interpretation (neutral)

DSSE may show:
- Group A and B are far apart
- Group A and B converge over time
- Group A splits into sub-groups

None of these imply wrongdoing.

They are **observable properties**, not claims.

---

## Why DSSE exists

DSSE exists to provide:

- a neutral semantic lens
- a non-accusatory signal
- a foundation for higher-level reasoning (outside DSSE)

DSSE deliberately stops **before interpretation**.

---

## Relationship to CRC-1

DSSE outputs can be embedded into CRC-1 capsules.

CRC-1 guarantees:
- integrity
- reproducibility

DSSE contributes:
- semantic observation

Together, they remain **interpretation-free**.

---

## License

DSSE artifacts inherit the repository license unless stated otherwise.
