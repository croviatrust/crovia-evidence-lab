# Crovia · Open Plane — Evidence Absence Signals

This dataset does **not** accuse anyone.

It records a single, verifiable fact:

> Whether publicly auditable AI training evidence is present or absent.

---

## What this is

The **Open Plane** is the public observation layer of Crovia.

It contains:
- **Presence signals** (GREEN / RED)
- **Absence receipts** (forensic, time-bucketed)
- No raw logs
- No repository names
- No attribution claims

Only **absence as an observable condition**.

---

## What GREEN means (precisely)

A **GREEN** verdict means at least one public evidence artefact is discoverable.

There are two public GREEN types:

- **GREEN (pointer)**: `EVIDENCE.pointer.json` exists — evidence is **declared** and hosted externally (Open Plane / forensic dataset).
- **GREEN (hosted)**: `EVIDENCE.json` and/or bundles exist — evidence is **hosted** locally and directly auditable in-repo.

This dataset records **presence**, not completeness.

---

## What RED means (precisely)

A **RED** verdict means:

- No `EVIDENCE.json` was publicly discoverable  
- No `trust_bundle.v1.json` was publicly discoverable  
- No `cep_capsule.v1.json` was publicly discoverable  

within the observation window.

It does **not** mean:
- wrongdoing
- policy violation
- misuse

It means **absence of proof**.

---

## Structure

open/
├─ signal/
│  └─ presence_latest.jsonl
└─ forensic/
   └─ absence_receipts_7d.jsonl

---

### signal/presence_latest.jsonl

High-level presence signals:
- anonymized project keys
- verdict (GREEN / RED)
- detected artefact names only

---

### forensic/absence_receipts_7d.jsonl

Forensic absence receipts:
- time-bucketed (7d)
- severity bucketed
- missing artefact classes

---

## Why this exists

AI systems increasingly depend on:
- third-party datasets
- public corpora
- scraped or aggregated sources

Yet today, **absence of evidence is not observable**.

Crovia makes absence **measurable**, **versioned**, and **auditable**.

---

## How this connects to Crovia

This Open Plane is:
- fed by passive observation (Presence Spider)
- independent from self-declarations
- compatible with Crovia WEDGE (self-issued evidence)

Projects that adopt Crovia tooling can turn RED into GREEN  
by publishing verifiable evidence artefacts.

---

## License & usage

This dataset is provided for:
- research
- governance analysis
- compliance tooling
- audit continuity

No inference about intent should be drawn from this data alone.

---

**If AI is trained on data, there should be a receipt.**
