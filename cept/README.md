# CEPT — Crovia Evidence Presence Test

A public, repeatable observation:

> **Are explicit, dataset-specific training evidence statements publicly present — or absent — in official sources?**

This is **not** a model audit.  
This makes **no legal claims**.  
This infers **no training usage**.

It records only what is **publicly documented** at a specific time.

---

## What CEPT does

CEPT performs **evidence presence tests** against official, public sources.

It checks whether **explicit training evidence statements** are:

- present
- absent
- unchanged over time

No inference.  
No interpretation.  
Only observable documentation state.

---

## Run archive

The `runs/` directory contains **frozen observation runs**.

Each run includes:

- official sources (as fetched at the time)
- extracted text
- observation log (term matches with snippets)
- derived CEPT records (canon + signed)
- hash-chains
- MANIFEST (sha256, scope, ordering)

Each run is **immutable** once written.

---

## Reproduce (one command)

From the `cept/` directory, run:

./reproduce.sh --date 2026-01-07

This will generate a new run folder under:

runs/<DATE>/

with the **exact same artifact layout**, including hashes and manifests.

---

## What CEPT is not

CEPT does **not**:

- audit AI models
- infer dataset usage
- assert compliance or non-compliance
- assign responsibility

It exists solely to answer:

> **Was explicit training evidence publicly documented at this point in time — yes or no?**

That’s it.
