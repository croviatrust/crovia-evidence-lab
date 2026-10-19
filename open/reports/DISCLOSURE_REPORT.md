# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W43** | Generated 2026-10-19 10:28:34 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8840 |
| Models | 7960 |
| Datasets | 880 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1594 | 7246 | **18.0%** |
| **Declared Datasets** | 1942 | 6898 | **22.0%** |
| **License** | 6360 | 2480 | **71.9%** |
| **README Accessible** | 7297 | 1543 | **82.5%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7755
- **Gated targets:** 327 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **207.0M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **76.1M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **58.1M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **44.4M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **41.9M** | ABSENT | 0 |
| `BAAI/bge-m3` | model | **31.7M** | PRESENT | 0 |
| `google-bert/bert-base-uncased` | model | **30.2M** | PRESENT | 2 |
| `Qwen/Qwen3-0.6B` | model | **30.0M** | ABSENT | 0 |
| `Comfy-Org/MiniMax-H3` | model | **25.2M** | ABSENT | 0 |
| `google-t5/t5-small` | model | **24.4M** | PRESENT | 1 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **76.1M** | OK |
| `BAAI/bge-small-en-v1.5` | **58.1M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **44.4M** | OK |
| `google/electra-base-discriminator` | **41.9M** | OK |
| `Qwen/Qwen3-0.6B` | **30.0M** | OK |
| `Comfy-Org/MiniMax-H3` | **25.2M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **19.6M** | OK |
| `openai/clip-vit-base-patch32` | **17.7M** | OK |
| `jonatasgrosman/wav2vec2-large-xlsr-53-japanese` | **15.9M** | OK |
| `BAAI/bge-reranker-v2-m3` | **15.7M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 238 | 0 (0%) | 71 (30%) | 197 (83%) |
| **facebook** | 186 | 25 (13%) | 74 (40%) | 176 (95%) |
| **Qwen** | 180 | 4 (2%) | 0 (0%) | 177 (98%) |
| **google** | 169 | 61 (36%) | 47 (28%) | 160 (95%) |
| **nvidia** | 161 | 88 (55%) | 58 (36%) | 152 (94%) |
| **microsoft** | 143 | 44 (31%) | 20 (14%) | 119 (83%) |
| **allenai** | 130 | 6 (5%) | 76 (58%) | 108 (83%) |
| **openbmb** | 115 | 4 (3%) | 42 (37%) | 79 (69%) |
| **tiiuae** | 112 | 22 (20%) | 21 (19%) | 104 (93%) |
| **Salesforce** | 111 | 32 (29%) | 20 (18%) | 108 (97%) |
| **EleutherAI** | 109 | 84 (77%) | 100 (92%) | 106 (97%) |
| **BAAI** | 109 | 11 (10%) | 19 (17%) | 102 (94%) |
| **apple** | 106 | 20 (19%) | 15 (14%) | 106 (100%) |
| **internlm** | 106 | 1 (1%) | 22 (21%) | 102 (96%) |
| **bigscience** | 105 | 15 (14%) | 23 (22%) | 41 (39%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 87 |
| **Changes (30 days)** | 309 |
| **Targets with changes** | 255 |

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

*Report fingerprint: `7b6fccb096a63aeb...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*