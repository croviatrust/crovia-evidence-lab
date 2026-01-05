# Crovia Evidence Lab

This repository contains **public, reproducible evidence artifacts**
produced using the Crovia Open Core.

It does not accuse.
It does not infer intent.
It does not judge compliance.

It records **what can be objectively observed and verified**.

---

## What this repository is

Crovia Evidence Lab is a **read-only evidence space**.

Everything here is:
- generated from declared inputs
- reproducible by anyone
- verifiable offline

No private logic.
No calibration.
No interpretation layer.

---

## How to read this repository

Think of this repository as **layers of observation**.

Each layer answers **one narrow technical question**.

---

## 1️⃣ Spider — Presence / Absence

📁 `spider/`

Spider records whether **declared public evidence markers**
were observable at a given time.

Spider answers:
> Was marker X publicly present at time T?

Spider does NOT answer:
- why
- how
- whether something was used

Spider is binary and factual.

---

## 2️⃣ Proofs — Integrity & Continuity

📁 `proofs/`

Proofs ensure that observations:
- were not altered
- remain consistent over time
- can be verified offline

This includes:
- hashchains
- drift timelines
- continuity checks

Proofs do not add meaning.
They preserve integrity.

---

## 3️⃣ DSSE — Semantic Separation

📁 `dsse/`

DSSE measures **semantic separation** between declared groups.

It answers:
> Are two semantic groups measurably distinct?

DSSE does NOT infer:
- training
- copying
- infringement

It records distance and divergence only.

---

## 4️⃣ CRC-1 — Deterministic Evidence Contract

📁 `CRC-1/`

CRC-1 defines a **minimal, deterministic artifact contract**.

A CRC-1 capsule contains:
- declared inputs
- validation report
- integrity proofs
- manifest

CRC-1 guarantees:
- reproducibility
- offline verification
- immutability of evidence

CRC-1 does not embed conclusions.

---

## How layers relate

Each layer is independent.

They can be combined, but never fused.

Spider observes presence.
DSSE observes structure.
Proofs preserve integrity.
CRC-1 seals the result.

Interpretation is intentionally external.

---

## What is deliberately missing

This repository does NOT include:
- pricing
- attribution rules
- intent analysis
- legal conclusions

Those belong outside evidence.

---

## Who this is for

This repository is designed for:
- auditors
- researchers
- legal technical teams
- regulators
- independent reviewers

Anyone can reproduce the evidence locally.

---

## Reproducing evidence

All artifacts here can be verified using:

- `crovia-run` (to generate CRC-1 artifacts)
- `crovia-verify` (to verify them offline)

No network access required.

---

## Final note

Evidence is not accusation.
Observation is not judgment.

Crovia Evidence Lab exists to **make facts inspectable**,
not to tell anyone what they mean.

