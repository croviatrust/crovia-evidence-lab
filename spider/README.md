# Spider — Presence / Absence Observation Layer

Spider records **observable public presence or absence**
of declared evidence markers at a given point in time.

Spider does not interpret meaning.
Spider does not infer usage.
Spider does not infer intent.

Spider only observes **whether something is publicly discoverable**.

---

## What Spider observes

Spider answers a single binary question:

> Is a declared evidence artifact publicly present at time T?

The result is:
- PRESENT
- ABSENT

Nothing else.

---

## What Spider does NOT do

Spider does NOT:
- claim that data was used
- claim that data was copied
- claim that data was trained on
- claim non-compliance

Absence is **not an accusation**.
Presence is **not a validation**.

They are observable states.

---

## Evidence markers

Spider looks for **declared public markers**, such as:

- `EVIDENCE.json`
- `trust_bundle.v1.json`
- `cep_capsule.v1.json`
- declared hashes or receipts

Spider does not guess.
Spider does not scrape hidden data.
Spider does not bypass protections.

---

## Binary observation model

Spider outputs are intentionally minimal:

- timestamp
- target identifier
- marker type
- presence status

This minimalism is deliberate.

More information would introduce interpretation.

---

## Temporal observations

Spider observations are **time-indexed**.

This enables:
- historical presence timelines
- gap detection
- longitudinal analysis

Time records *when* something was observable,
not *why* it was or was not.

---

## Relationship to Proofs

Spider provides **snapshots**.

Proofs provide:
- integrity over snapshots
- drift and continuity analysis

Spider answers *what was visible*.
Proofs answer *what changed*.

---

## Relationship to CRC-1

Spider outputs can be sealed into CRC-1 artifacts.

CRC-1 guarantees:
- integrity of Spider observations
- offline verifiability

Spider itself remains a **pure observer**.

---

## Legal posture

Spider statements are factual:

- "marker X was not publicly present at time T"
- "marker Y was publicly present at time T"

They are **testable and repeatable**.

No legal conclusion is embedded.

---

## License

Spider artifacts inherit the repository license unless stated otherwise.
