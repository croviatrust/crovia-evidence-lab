# CRC-1 — Crovia Reproducible Contract v1

CRC-1 defines a **minimal, deterministic, offline-verifiable evidence contract**.

It specifies:
- which artifacts must exist
- how they relate to each other
- how integrity can be verified without trust

CRC-1 makes **no claims**.  
It only defines what can be proven.

---

## What CRC-1 represents

A CRC-1 directory is a **self-contained evidence capsule**.

It proves that:
- a declared input existed
- it was processed deterministically
- integrity has not been altered since generation

Nothing more. Nothing less.

---

## Required artifacts (CRC-1 contract)

Every CRC-1 capsule MUST contain:

- MANIFEST.json  
- receipts.ndjson  
- validate_report.md  
- hashchain.txt  
- trust_bundle.json  

All paths are relative to the CRC-1 directory.

---

## Artifact roles

### MANIFEST.json

The contract index.

Declares:
- schema version
- contract name (CRC-1)
- period (if applicable)
- expected artifacts

The manifest is the **starting point** for verification.

---

### receipts.ndjson

Declared input facts.

Each line represents a declared unit (e.g. dataset contribution, record group).  
No inference is made.

---

### validate_report.md

Structural validation report.

Shows:
- schema validity
- rule compliance
- error and warning counts

Human-readable by design.

---

### hashchain.txt

Rolling integrity proof.

Each line depends on the previous one.  
Any modification breaks the chain.

Verifiable offline.

---

### trust_bundle.json

Structured aggregation of declared facts.

This file:
- does not imply legality
- does not imply compliance
- does not imply intent

It only reflects **declared, validated structure**.

---

## How to verify a CRC-1 capsule

With Crovia open-core installed, example:

crovia-verify CRC-1/demo-2025-11

Verification checks:
- artifact presence
- manifest consistency
- hashchain integrity
- JSON structural validity

No network required.

---

## What CRC-1 does NOT say

CRC-1 does NOT state:
- that data was lawfully used
- that training occurred
- that obligations exist
- that compensation is due

CRC-1 only proves **observable structure and integrity**.

---

## Why CRC-1 exists

CRC-1 exists to answer one question:

Can this evidence be verified by anyone, anywhere, without trust?

If the answer is yes — **CRC-1 succeeded**.

---

## License

CRC-1 artifacts inherit the repository license unless otherwise stated.

