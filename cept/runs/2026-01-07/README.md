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

---

## Important limitation (OpenAI pages)

Some OpenAI web pages fetched during this run do **not** return their real content to a non-browser client.
The extracted text files may contain only:

- “Enable JavaScript and cookies to continue”
- “Refresh (360 sec)”

In those cases, the run result **must be interpreted as**:

> “Source not observable via headless fetch at this time”  
> NOT “evidence is absent”.

Crovia CEPT records what is **observable** from the captured artifacts in `sources/` and `tmp/`.
If a source is gated (JS/cookies), the observation is still valid — but the *interpretation* must explicitly
separate:
- **absence observed**
from
- **access blocked / not observable**

Next runs should prefer stable, fetchable primary artifacts (e.g., PDFs, docs pages, repositories), or record
the gating as its own signal.


### Quick check: gated sources detected

```bash
grep -Rni "Enable JavaScript and cookies\|Refresh (360 sec)" "cept/runs/2026-01-07/tmp" || true
```
