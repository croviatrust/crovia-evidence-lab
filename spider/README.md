# Crovia Spider — Presence / Absence Evidence

Spider is a public observation tool.

It records **presence or absence of auditable AI training evidence**
from public sources (e.g. GitHub).

## What it does
- Observes public repositories
- Records whether evidence artifacts are present
- Produces normalized JSONL receipts
- Preserves raw observations for auditability

## What it does NOT do
- No attribution
- No intent inference
- No policy judgment
- No legal claims

Spider only records **observable conditions**.

## Implementation note

Spider currently exposes **presence-based observers only**.

The canonical GitHub observer is:
- `bin/presence/presence_spider_github.py`

No generic crawler is provided by design.
