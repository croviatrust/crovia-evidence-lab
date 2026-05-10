# Crovia Continuity Leaderboard

Frozen weekly snapshots of the longest-silent AI models on the public registry.

- **Live web archive (browse all weeks):** https://croviatrust.com/registry/data/leaderboard/
- **Live registry homepage:**             https://croviatrust.com/registry/
- **Per-model dossier:**                  https://croviatrust.com/m/&lt;org&gt;/&lt;model&gt;/

## What is "silence"?

A model is *silent* when no new public observation has been recorded since
its first documented absence on the [Crovia registry](https://croviatrust.com/registry/).
Each row in `top_silent.csv` corresponds to a signed `AX.ABS` axiom in the
public ledger. The ledger is anchored to OpenTimestamps for tamper-evidence.

## Format

Every Monday at 02:13 UTC, a new folder `YYYY-Www/` appears with:

- `top_silent.csv` — ranked top-100 silent models (rank, target_id, silence_days, first_seen, last_seen)
- `vendors.csv` — per-vendor rollup
- `snapshot.json` — manifest with SHA-256 of each CSV
- `README.md` — human-readable summary of the week

Past weeks are **never edited**. The folder is append-only.

## How to verify any line

```bash
# Pick a snapshot
curl -s https://croviatrust.com/registry/data/leaderboard/latest/snapshot.json | jq

# Verify CSV integrity against the manifest
sha256sum top_silent.csv  # must match snapshot.json sha256.top_silent.csv

# Resolve any target_id back to its signed AX.ABS axiom
curl -s "https://croviatrust.com/registry/api/axiom/<axiom_id>.json" | jq .signature
```

## License

Data: **CC-BY-4.0**. Attribute as: *"Crovia continuity leaderboard, week YYYY-Www"*.

---

*Auto-published by the [observation pipeline](../scripts/) of crovia-evidence-lab.*
## Latest snapshot

Week **2026-W19** — longest-silent target `meta-llama/Llama-3.1-8B` at 112 days. See [2026-W19](./2026-W19/) for the data.
