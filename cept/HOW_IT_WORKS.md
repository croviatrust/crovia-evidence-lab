# How CEPT works

CEPT is an **observation-only** test.

## Input
A closed list of **official public sources**:
- model documentation (model cards, papers, system cards)
- dataset documentation pages

## Method (deterministic)
1. Fetch sources (HTTP GET)
2. Extract text (HTML/PDF → TXT)
3. Search for a fixed set of terms (e.g., dataset names)
4. Produce an observation log with snippets (match/no-match)
5. Derive CEPT records from the log (no manual edits)
6. Seal the run:
   - hash-chain over log + records
   - signed records (HMAC)
   - MANIFEST sha256 for all artifacts

## Output
A frozen run that can be independently verified offline.

## What “absence” means
Absence means **not publicly documented in the selected official sources at the time of observation**.
It does not imply anything else.

