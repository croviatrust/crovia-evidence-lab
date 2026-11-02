# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W45** | Generated 2026-11-02 10:31:28 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 8904 |
| Models | 8019 |
| Datasets | 885 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 1605 | 7299 | **18.0%** |
| **Declared Datasets** | 1945 | 6959 | **21.8%** |
| **License** | 6433 | 2471 | **72.2%** |
| **README Accessible** | 7360 | 1544 | **82.7%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 7830
- **Gated targets:** 327 (3.7%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **182.5M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **66.9M** | ABSENT | 1 |
| `BAAI/bge-small-en-v1.5` | model | **50.5M** | ABSENT | 0 |
| `BAAI/bge-m3` | model | **30.3M** | PRESENT | 0 |
| `Comfy-Org/MiniMax-H3` | model | **30.2M** | ABSENT | 0 |
| `openai-community/gpt2` | model | **29.3M** | PRESENT | 0 |
| `google-bert/bert-base-uncased` | model | **29.2M** | PRESENT | 2 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **28.4M** | ABSENT | 0 |
| `argmaxinc/whisperkit-coreml` | model | **27.3M** | ABSENT | 0 |
| `Qwen/Qwen3-0.6B` | model | **23.4M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **66.9M** | OK |
| `BAAI/bge-small-en-v1.5` | **50.5M** | OK |
| `Comfy-Org/MiniMax-H3` | **30.2M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **28.4M** | OK |
| `argmaxinc/whisperkit-coreml` | **27.3M** | OK |
| `Qwen/Qwen3-0.6B` | **23.4M** | OK |
| `google/electra-base-discriminator` | **17.6M** | OK |
| `openai/clip-vit-base-patch32` | **17.6M** | OK |
| `jonatasgrosman/wav2vec2-large-xlsr-53-japanese` | **16.2M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **15.1M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **mradermacher** | 246 | 0 (0%) | 74 (30%) | 206 (84%) |
| **facebook** | 187 | 26 (14%) | 74 (40%) | 178 (95%) |
| **Qwen** | 181 | 4 (2%) | 0 (0%) | 178 (98%) |
| **google** | 166 | 61 (37%) | 47 (28%) | 157 (95%) |
| **nvidia** | 158 | 83 (53%) | 56 (35%) | 150 (95%) |
| **microsoft** | 143 | 44 (31%) | 20 (14%) | 119 (83%) |
| **allenai** | 130 | 6 (5%) | 76 (58%) | 109 (84%) |
| **openbmb** | 119 | 5 (4%) | 43 (36%) | 83 (70%) |
| **tiiuae** | 112 | 22 (20%) | 21 (19%) | 104 (93%) |
| **Salesforce** | 110 | 32 (29%) | 20 (18%) | 107 (97%) |
| **EleutherAI** | 109 | 84 (77%) | 100 (92%) | 106 (97%) |
| **BAAI** | 109 | 11 (10%) | 19 (17%) | 102 (94%) |
| **apple** | 106 | 20 (19%) | 15 (14%) | 106 (100%) |
| **internlm** | 106 | 1 (1%) | 22 (21%) | 102 (96%) |
| **bigscience** | 105 | 15 (14%) | 23 (22%) | 41 (39%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 79 |
| **Changes (30 days)** | 402 |
| **Targets with changes** | 323 |

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

*Report fingerprint: `8c440279c30dd930...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*