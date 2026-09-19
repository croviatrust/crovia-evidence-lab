# Crovia Evidence Lab

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)

**Crovia records what AI providers disclose about training data, and the
absence of it, as signed, Bitcoin-anchored facts.** This repository is the
public data plane of the Crovia substrate: hourly exports of observations and
reports, weekly leaderboard snapshots, and the frozen experiments (CEPT,
CRC-1, DSSE, Spider) from which the current registry grew.

It does not accuse, infer intent or judge compliance. It records what can be
observed and verified.

## What updates, and when

| Path | Cadence | Source |
|---|---|---|
| `open/` (drift, forensic, reports, canon, signal, temporal) | hourly | `sync_from_server.sh` on the production host |
| `snapshots/` (registry state, Merkle root, recent observations) | hourly | same |
| `badges/`, `cep-capsules/` | hourly when changed | same |
| `SYNC_STATUS.json` | hourly | same; `last_sync` is the timestamp to check |
| `leaderboard/<ISO week>/` | weekly (Monday 02:13 UTC) | `weekly_leaderboard.py`; also mirrored at [croviatrust.com/registry/data/leaderboard/](https://croviatrust.com/registry/data/leaderboard/) |

If `last_sync` in `SYNC_STATUS.json` is older than a few hours the sync has
stalled; the sync log on the host is `/var/log/crovia/evidence_lab_sync.log`.
(The sync was stalled from 2026-05-17 to 2026-09-19 by an orphaned
`.git/index.lock`; the backlog was pushed on 2026-09-19.)

## Frozen layers (historical, not updated)

| Path | Last change | What it is |
|---|---|---|
| `cept/` | 2026-01 | Crovia Evidence Presence Test: repeatable observation runs with `reproduce.sh` |
| `CRC-1/` | 2026-01 | Crovia Reproducible Contract v1: deterministic, offline-verifiable evidence contract and demo |
| `dsse/` | 2026-02 | Dynamic Semantic Separation Evidence: datasets, tools and evidence files |
| `spider/` | 2026-02 | Presence/absence observation layer (raw and normalised GitHub presence data) |
| `proofs/` | 2026-01 | Mechanical evidence of state and change (drift proofs) |
| `experiments/` | 2026-03 | `cds/`, `zk_gdna/`: exploratory work |
| `zk_bridge_tests/` | 2026-01 | ZK bridge evidence tests (notes only) |

These directories are kept for reproducibility of past publications. The
live protocol work moved to [crovia-seal](https://github.com/croviatrust/crovia-seal)
(the Seal standard) and [countersign](https://github.com/croviatrust/countersign)
(witnessing and TACET).

## Verify what you download

```bash
# Current Merkle root of the AXIOM ledger, as published hourly
curl -s https://croviatrust.com/registry/data/substrate/latest_seal.json

# Registry counters behind snapshots/registry_stats.json
curl -s https://croviatrust.com/api/registry/stats
curl -s https://croviatrust.com/api/registry/merkle
```

Headline figures (LACUNA records, days of documented silence, signed
observations, Bitcoin anchors) are defined in
[CANON.md §4](https://github.com/croviatrust/countersign/blob/main/CANON.md)
and are recomputable from the public data files. Counts in this repository
(`SYNC_STATUS.json`, `snapshots/registry_stats.json`) are raw registry
counters, not the canonical headline figures.

## Crovia surfaces

| Surface | URL |
|---|---|
| Ledger and registry | https://croviatrust.com/registry/ |
| LACUNA (absence records) | https://croviatrust.com/registry/lacuna/ |
| Crovia Seal: spec, verifier, log | https://croviatrust.com/registry/seal/ |
| Machine-readable index | https://croviatrust.com/llms.txt |
| Canon (source of truth for names, numbers, endpoints) | https://github.com/croviatrust/countersign/blob/main/CANON.md |

Repositories: [crovia-seal](https://github.com/croviatrust/crovia-seal) (the standard) ·
[crovia-core-engine](https://github.com/croviatrust/crovia-core-engine) (the substrate) ·
[countersign](https://github.com/croviatrust/countersign) (witnessing and TACET) ·
[crovia-evidence-lab](https://github.com/croviatrust/crovia-evidence-lab) (this repository: public data) ·
[causari](https://github.com/croviatrust/causari) (sibling product: code provenance).

## Licence

This repository is licensed under Apache 2.0 (`LICENSE`). Exported data files
that carry their own `license` field (for example `CC-BY-4.0` in
`snapshots/global_ranking.json`) state their own terms; attribution is
"Crovia Trust, https://croviatrust.com".

Contact: info@croviatrust.com
