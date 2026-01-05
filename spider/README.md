# Spider — Evidence Presence / Absence Observation

Spider records whether **publicly declared evidence artifacts**
are present or absent at a given point in time.

Spider does not interpret.
Spider does not infer intent.
Spider does not enforce rules.

It only observes.

---

## What Spider observes

Spider checks for the **existence** of declared public artifacts, such as:

- EVIDENCE.json
- trust_bundle.v1.json
- cep_capsule.v1.json
- declared hashes or receipts

The output is strictly binary:

- PRESENT
- ABSENT

---

## What Spider does NOT do

Spider does NOT:
- scrape private systems
- inspect model weights
- infer training behavior
- assign responsibility
- imply wrongdoing

Absence is **not** a violation.
Presence is **not** compliance.

They are facts, not judgments.

---

## Observation model

Each Spider observation records:

- target identifier (URL, dataset, reference)
- timestamp
- artifact type checked
- presence / absence result

No raw content is stored.
No attribution is performed.

---

## Time matters

Spider supports **temporal observation**.

This allows recording:
- when an artifact appeared
- when it disappeared
- how long absence persisted

Time does not imply cause.

---

## Why absence matters

Absence is an **observable condition**.

Spider does not say *why* something is missing.
It only records *that* it was missing at observation time.

Interpretation belongs elsewhere.

---

## Relationship to CRC-1

Spider outputs can be sealed into CRC-1 capsules.

CRC-1 guarantees:
- integrity
- reproducibility

Spider contributes:
- presence / absence facts

Together they form **verifiable observation**, not accusation.

---

## Legal posture

Spider is designed to be:

- non-invasive
- non-interpretative
- non-accusatory

It records publicly observable states only.

---

## License

Spider artifacts inherit the repository license unless stated otherwise.
