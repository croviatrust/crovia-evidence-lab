# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W13** | Generated 2026-03-23 08:09:42 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4143 |
| Models | 3320 |
| Datasets | 823 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 651 | 3492 | **15.7%** |
| **Declared Datasets** | 842 | 3301 | **20.3%** |
| **License** | 3131 | 1012 | **75.6%** |
| **README Accessible** | 3546 | 596 | **85.6%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 3963
- **Gated targets:** 157 (3.8%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **206.3M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **72.2M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **51.1M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **41.4M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **28.0M** | PRESENT | 21 |
| `laion/clap-htsat-fused` | model | **26.0M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **25.7M** | ABSENT | 0 |
| `timm/mobilenetv3_small_100.lamb_in1k` | model | **21.8M** | ABSENT | 1 |
| `Qwen/Qwen2.5-7B-Instruct` | model | **20.9M** | ABSENT | 0 |
| `openai/clip-vit-large-patch14` | model | **20.9M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **51.1M** | OK |
| `laion/clap-htsat-fused` | **26.0M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **25.7M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **21.8M** | OK |
| `Qwen/Qwen2.5-7B-Instruct` | **20.9M** | OK |
| `openai/clip-vit-large-patch14` | **20.9M** | OK |
| `FacebookAI/xlm-roberta-base` | **20.1M** | OK |
| `openai/clip-vit-base-patch32` | **20.0M** | OK |
| `Bingsu/adetailer` | **19.5M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **14.9M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 159 | 4 (3%) | 0 (0%) | 156 (98%) |
| **facebook** | 109 | 17 (16%) | 44 (40%) | 101 (93%) |
| **timm** | 88 | 0 (0%) | 68 (77%) | 88 (100%) |
| **microsoft** | 87 | 23 (26%) | 13 (15%) | 70 (80%) |
| **google** | 84 | 32 (38%) | 23 (27%) | 81 (96%) |
| **nvidia** | 75 | 36 (48%) | 32 (43%) | 71 (95%) |
| **allenai** | 72 | 3 (4%) | 31 (43%) | 61 (85%) |
| **unsloth** | 59 | 4 (7%) | 1 (2%) | 56 (95%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **Salesforce** | 52 | 12 (23%) | 6 (12%) | 51 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **mradermacher** | 44 | 0 (0%) | 9 (20%) | 35 (80%) |
| **NousResearch** | 43 | 8 (19%) | 15 (35%) | 35 (81%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 37 |
| **Changes (30 days)** | 170 |
| **Targets with changes** | 143 |

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

*Report fingerprint: `f93c55b9082d8b4f...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*