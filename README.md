# Crovia Evidence Lab

This repository contains **public, offline-verifiable evidence artifacts**
produced by the Crovia open-core engine.

It is designed for:
- auditors
- regulators
- researchers
- dataset providers
- AI operators

No trust required.  
No execution required.  
No attribution claims.

---

## What this repository IS

Crovia Evidence Lab is a **forensic archive**.

It hosts:
- immutable evidence artifacts
- deterministic outputs
- hash-verifiable bundles
- documented absence/presence signals

Every artifact can be:
- inspected locally
- verified offline
- reproduced from declared inputs

---

## What this repository is NOT

This repository does **not**:
- accuse anyone
- claim policy violations
- infer intent
- require Crovia services
- phone home
- depend on a running system

All artifacts are **static**.

---

## Repository structure

crovia-evidence-lab/
│
├── CRC-1/      # Deterministic artifact contracts (offline verifiable)
├── dsse/       # Semantic separation & drift evidence
├── proofs/     # Hashes, lineage, temporal integrity
├── spider/     # Presence / absence observation (non-attributive)
└── README.md   # You are here

Each folder contains its own README explaining:
- what the evidence means
- how it was produced
- how to verify it

---

## Quick verification (60 seconds)

If you have Python installed, example:

pip install crovia-core-engine-open
crovia-verify CRC-1/demo-2025-11

Expected result:

✔ All artifacts present  
✔ trust_bundle JSON valid  
✔ Hashchain verified  
✔ CRC-1 VERIFIED  

No internet connection required.

---

## Evidence philosophy

Crovia evidence follows one principle:

Absence of proof is an observable condition — not an accusation.

This repository records **facts**, not interpretations.

---

## License

All contents are released under Apache-2.0 unless stated otherwise.

