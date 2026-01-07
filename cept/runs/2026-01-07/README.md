# CEPT Run — 2026-01-07

This directory contains a **frozen, hash-verified public evidence presence test**
executed on 2026-01-07.

All artifacts are reproducible, auditable offline, and covered by a SHA256
manifest and hash-chains.

---

## Note on Dynamic (JavaScript-Gated) Sources

Some official sources included in this run (notably certain OpenAI pages)
return a JavaScript / cookie–gated placeholder when retrieved as static documents.

Example observed content:
> “Enable JavaScript and cookies to continue”

This run intentionally records **only the statically retrievable content**
accessible via non-interactive HTTP retrieval.

No browser automation, authenticated sessions, or dynamic rendering
were used, in order to preserve:

- reproducibility
- auditability
- byte-level verifiability

As a result, the absence of semantic content in such files is itself
an **observable property of the disclosure channel**, not an inference
about the underlying system.

Dynamic or context-dependent disclosures are **out of scope** for this run
and may be addressed in future, explicitly labeled auxiliary analyses.
