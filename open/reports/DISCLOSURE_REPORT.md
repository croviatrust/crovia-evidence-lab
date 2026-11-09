# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W46** | Generated 2026-11-09 10:31:22 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8928 |
| Models | 8042 |
| Datasets | 886 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1605 | 7323 | **18.0%** |
| **Declared Datasets** | 1947 | 6981 | **21.8%** |
| **License** | 6453 | 2475 | **72.3%** |
| **README Accessible** | 7389 | 1539 | **82.8%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7848
- **Gated targets:** 330 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **177.6M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **63.1M** | ABSENT | 1 |
| `argmaxinc/whisperkit-coreml` | model | **51.6M** | ABSENT | 0 |
| `BAAI/bge-small-en-v1.5` | model | **48.0M** | ABSENT | 0 |
| `Comfy-Org/MiniMax-H3` | model | **32.3M** | ABSENT | 0 |
| `openai-community/gpt2` | model | **31.8M** | PRESENT | 0 |
| `google-bert/bert-base-uncased` | model | **31.0M** | PRESENT | 2 |
| `BAAI/bge-m3` | model | **29.8M** | PRESENT | 0 |
| `autogluon/chronos-2` | model | **28.8M** | PRESENT | 2 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **27.1M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **63.1M** | OK |
| `argmaxinc/whisperkit-coreml` | **51.6M** | OK |
| `BAAI/bge-small-en-v1.5` | **48.0M** | OK |
| `Comfy-Org/MiniMax-H3` | **32.3M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **27.1M** | OK |
| `Qwen/Qwen3-0.6B` | **21.0M** | OK |
| `openai/clip-vit-base-patch32` | **17.7M** | OK |
| `jonatasgrosman/wav2vec2-large-xlsr-53-japanese` | **16.2M** | OK |
| `BAAI/bge-reranker-v2-m3` | **14.7M** | OK |
| `Qwen/Qwen3-14B` | **12.9M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 245 | 0 (0%) | 74 (30%) | 205 (84%) |
| **facebook** | 186 | 25 (13%) | 74 (40%) | 177 (95%) |
| **Qwen** | 183 | 4 (2%) | 0 (0%) | 180 (98%) |
| **google** | 166 | 61 (37%) | 47 (28%) | 157 (95%) |
| **nvidia** | 157 | 84 (54%) | 57 (36%) | 149 (95%) |
| **microsoft** | 142 | 44 (31%) | 20 (14%) | 118 (83%) |
| **allenai** | 130 | 6 (5%) | 76 (58%) | 109 (84%) |
| **openbmb** | 118 | 5 (4%) | 43 (36%) | 82 (69%) |
| **tiiuae** | 112 | 22 (20%) | 21 (19%) | 104 (93%) |
| **Salesforce** | 110 | 32 (29%) | 20 (18%) | 107 (97%) |
| **EleutherAI** | 109 | 84 (77%) | 100 (92%) | 106 (97%) |
| **BAAI** | 109 | 11 (10%) | 19 (17%) | 102 (94%) |
| **unsloth** | 108 | 8 (7%) | 2 (2%) | 105 (97%) |
| **apple** | 106 | 20 (19%) | 15 (14%) | 106 (100%) |
| **internlm** | 106 | 1 (1%) | 22 (21%) | 102 (96%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 134 |
| **Changes (30 days)** | 503 |
| **Targets with changes** | 402 |

---

## ℹ️ Methodology

This report aggregates publicly observable data from HuggingFace:

- **Training Section**: Detected via `## Training` heading in README
- **Declared Datasets**: From `cardData.datasets` in model/dataset card
- **License**: From `cardData.license`
- **Downloads/Likes**: From HuggingFace API

**What this report does NOT do:**
- Make accusations
- Infer compliance or non-compliance
- Judge quality or intent
- Assign scores or rankings

---

*Report fingerprint: `c8e7f63f22acc12f...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*