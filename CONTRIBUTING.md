# Contributing

This is a data repository. Files under `open/`, `snapshots/`, `badges/` and
`cep-capsules/` are written by `sync_from_server.sh` every hour from the
production host; `leaderboard/` weekly. Pull requests that edit those files by
hand are closed: the next sync would overwrite them, and a hand-edited export
cannot be reproduced.

What is useful here:

- **Reproductions.** A notebook or script that recomputes a published figure
  from these files (or shows that it cannot be recomputed) belongs in
  `experiments/<your-topic>/` with a `README.md` stating the snapshot tag or
  `SYNC_STATUS.json` `last_sync` you used.
- **Schema questions.** If a file's shape is unclear, open an issue with the
  path and the field; the answer becomes a line in the file's schema in
  [crovia-core-engine/schemas](https://github.com/croviatrust/crovia-core-engine/tree/main/schemas).
- **Sync problems.** If `SYNC_STATUS.json` is stale by more than a few hours,
  open an issue with the `last_sync` value. Do not "fix" it in a PR.

For the live proofs of absence (TACET) go to
[countersign](https://github.com/croviatrust/countersign); for the signed
receipt format go to [crovia-seal](https://github.com/croviatrust/crovia-seal).

Data files are CC-BY-4.0 where they carry a `license` field; attribution is
"Crovia Trust, https://croviatrust.com". Code in this repository is Apache-2.0.
