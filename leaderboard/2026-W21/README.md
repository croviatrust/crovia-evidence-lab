# Crovia AI Continuity Leaderboard — 2026-W21

A frozen weekly snapshot of the longest-silent AI models on the public registry.

This dataset is **append-only** and **week-stamped**: every Monday at 02:00 UTC a new
folder appears with the state of the world at that moment. Past weeks are never edited.

## What is "silence"?

A model is *silent* when no new public observation has been recorded since its first
documented absence on the [Crovia registry](https://croviatrust.com/registry/).
Each row in `top_silent.csv` corresponds to a signed AX.ABS axiom in the public ledger.

## This week's headline

- **Real targets tracked:** 2,934
- **Cumulative target-time observed:** 273,496 target-days
- **Median silence per target:** 89 days
- **Longest-silent target:** `meta-llama/Llama-3.1-8B` — 120 days, since 2026-01-17

## Files

- `top_silent.csv` — ranked top-100 silent models (rank, target_id, silence_days, first_seen, last_seen)
- `vendors.csv` — per-vendor rollup
- `snapshot.json` — machine manifest with SHA-256 of each CSV

## How to verify

Every entry corresponds to one AX.ABS axiom in `axiom_ledger.jsonl`, which is signed and
optionally anchored to OpenTimestamps. To verify a single line:

```python
from huggingface_hub import hf_hub_download
import csv
fp = hf_hub_download("crovia/continuity-leaderboard", "2026-W21/top_silent.csv", repo_type="dataset")
for row in csv.DictReader(open(fp)):
    print(row["target_id"], row["silence_days"])
```

Or directly:

```bash
curl https://croviatrust.com/registry/data/leaderboard/2026-W21/snapshot.json | jq
```

## Live data

This snapshot is a frozen view. For real-time data:

- **Live registry:** https://croviatrust.com/registry/
- **Per-model dossier:** https://croviatrust.com/m/&lt;org&gt;/&lt;model&gt;/
- **Embed widget:** https://croviatrust.com/embed/

## License

Data: **CC-BY-4.0**. Attribute as: "Crovia continuity leaderboard, week 2026-W21".

---

*Generated automatically. No human curation. Methodology: https://croviatrust.com/registry/api/*
