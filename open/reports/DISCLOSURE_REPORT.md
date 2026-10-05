# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W41** | Generated 2026-10-05 10:28:48 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8820 |
| Models | 7950 |
| Datasets | 870 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1599 | 7221 | **18.1%** |
| **Declared Datasets** | 1947 | 6873 | **22.1%** |
| **License** | 6329 | 2491 | **71.8%** |
| **README Accessible** | 7272 | 1548 | **82.4%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7738
- **Gated targets:** 330 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **235.7M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **84.1M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **62.7M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **51.0M** | ABSENT | 0 |
| `google/electra-base-discriminator` | model | **45.9M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **38.7M** | PRESENT | 2 |
| `BAAI/bge-m3` | model | **34.4M** | PRESENT | 0 |
| `Qwen/Qwen3-0.6B` | model | **29.6M** | ABSENT | 0 |
| `google-t5/t5-small` | model | **24.7M** | PRESENT | 1 |
| `Comfy-Org/MiniMax-H3` | model | **23.3M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **84.1M** | OK |
| `BAAI/bge-small-en-v1.5` | **62.7M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **51.0M** | OK |
| `google/electra-base-discriminator` | **45.9M** | OK |
| `Qwen/Qwen3-0.6B` | **29.6M** | OK |
| `Comfy-Org/MiniMax-H3` | **23.3M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **22.2M** | OK |
| `openai/clip-vit-base-patch32` | **20.6M** | OK |
| `BAAI/bge-reranker-v2-m3` | **17.0M** | OK |
| `jonatasgrosman/wav2vec2-large-xlsr-53-japanese` | **16.3M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 237 | 0 (0%) | 70 (30%) | 196 (83%) |
| **facebook** | 185 | 25 (14%) | 74 (40%) | 175 (95%) |
| **Qwen** | 180 | 4 (2%) | 0 (0%) | 177 (98%) |
| **google** | 171 | 61 (36%) | 47 (27%) | 162 (95%) |
| **nvidia** | 159 | 87 (55%) | 60 (38%) | 151 (95%) |
| **microsoft** | 143 | 44 (31%) | 20 (14%) | 117 (82%) |
| **allenai** | 132 | 6 (5%) | 76 (58%) | 110 (83%) |
| **openbmb** | 116 | 5 (4%) | 43 (37%) | 80 (69%) |
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
| **Changes (7 days)** | 52 |
| **Changes (30 days)** | 236 |
| **Targets with changes** | 194 |

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

*Report fingerprint: `0108124da5886081...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*