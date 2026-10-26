# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W44** | Generated 2026-10-26 10:29:50 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8879 |
| Models | 7997 |
| Datasets | 882 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1598 | 7281 | **18.0%** |
| **Declared Datasets** | 1945 | 6934 | **21.9%** |
| **License** | 6397 | 2482 | **72.0%** |
| **README Accessible** | 7336 | 1543 | **82.6%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7796
- **Gated targets:** 325 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **190.2M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **70.6M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **53.6M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **39.2M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **31.3M** | ABSENT | 0 |
| `BAAI/bge-m3` | model | **29.7M** | PRESENT | 0 |
| `google-bert/bert-base-uncased` | model | **29.0M** | PRESENT | 2 |
| `Comfy-Org/MiniMax-H3` | model | **26.5M** | ABSENT | 0 |
| `google-t5/t5-small` | model | **24.9M** | PRESENT | 1 |
| `Qwen/Qwen3-0.6B` | model | **23.8M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **70.6M** | OK |
| `BAAI/bge-small-en-v1.5` | **53.6M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **39.2M** | OK |
| `google/electra-base-discriminator` | **31.3M** | OK |
| `Comfy-Org/MiniMax-H3` | **26.5M** | OK |
| `Qwen/Qwen3-0.6B` | **23.8M** | OK |
| `openai/clip-vit-base-patch32` | **16.8M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **16.4M** | OK |
| `jonatasgrosman/wav2vec2-large-xlsr-53-japanese` | **16.0M** | OK |
| `BAAI/bge-reranker-v2-m3` | **14.6M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 244 | 0 (0%) | 74 (30%) | 204 (84%) |
| **facebook** | 187 | 26 (14%) | 74 (40%) | 177 (95%) |
| **Qwen** | 181 | 4 (2%) | 0 (0%) | 178 (98%) |
| **google** | 167 | 61 (37%) | 47 (28%) | 158 (95%) |
| **nvidia** | 157 | 85 (54%) | 57 (36%) | 148 (94%) |
| **microsoft** | 143 | 44 (31%) | 20 (14%) | 119 (83%) |
| **allenai** | 130 | 6 (5%) | 76 (58%) | 108 (83%) |
| **openbmb** | 117 | 5 (4%) | 43 (37%) | 81 (69%) |
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
| **Changes (7 days)** | 108 |
| **Changes (30 days)** | 403 |
| **Targets with changes** | 322 |

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

*Report fingerprint: `97ffba152c9e1737...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*