# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W18** | Generated 2026-04-27 08:09:55 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4283 |
| Models | 3448 |
| Datasets | 835 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 671 | 3612 | **15.7%** |
| **Declared Datasets** | 859 | 3424 | **20.1%** |
| **License** | 3286 | 997 | **76.7%** |
| **README Accessible** | 3703 | 580 | **86.5%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 4110
- **Gated targets:** 167 (3.9%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **215.8M** | PRESENT | 21 |
| `Qwen/Qwen3-VL-2B-Instruct` | model | **141.1M** | ABSENT | 0 |
| `google-bert/bert-base-uncased` | model | **58.8M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **49.5M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **38.9M** | ABSENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **34.9M** | PRESENT | 21 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **30.5M** | ABSENT | 1 |
| `Falconsai/nsfw_image_detection` | model | **29.2M** | PRESENT | 0 |
| `BAAI/bge-small-en-v1.5` | model | **26.4M** | ABSENT | 0 |
| `openai/clip-vit-large-patch14` | model | **24.0M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `Qwen/Qwen3-VL-2B-Instruct` | **141.1M** | OK |
| `google/electra-base-discriminator` | **49.5M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **38.9M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **30.5M** | OK |
| `BAAI/bge-small-en-v1.5` | **26.4M** | OK |
| `openai/clip-vit-large-patch14` | **24.0M** | OK |
| `openai/clip-vit-base-patch32` | **20.4M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **19.4M** | OK |
| `Qwen/Qwen3-0.6B` | **18.2M** | OK |
| `FacebookAI/xlm-roberta-base` | **17.4M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 163 | 3 (2%) | 0 (0%) | 161 (99%) |
| **facebook** | 111 | 18 (16%) | 46 (41%) | 105 (95%) |
| **google** | 94 | 32 (34%) | 24 (26%) | 91 (97%) |
| **microsoft** | 88 | 25 (28%) | 14 (16%) | 70 (80%) |
| **timm** | 85 | 0 (0%) | 65 (76%) | 85 (100%) |
| **nvidia** | 82 | 40 (49%) | 34 (41%) | 78 (95%) |
| **allenai** | 70 | 3 (4%) | 31 (44%) | 60 (86%) |
| **unsloth** | 67 | 4 (6%) | 1 (1%) | 65 (97%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **lmstudio-community** | 53 | 0 (0%) | 4 (8%) | 53 (100%) |
| **Salesforce** | 52 | 11 (21%) | 6 (12%) | 51 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **BAAI** | 46 | 7 (15%) | 9 (20%) | 42 (91%) |
| **mradermacher** | 46 | 0 (0%) | 10 (22%) | 37 (80%) |
| **EleutherAI** | 45 | 34 (76%) | 41 (91%) | 45 (100%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 40 |
| **Changes (30 days)** | 780 |
| **Targets with changes** | 421 |

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

*Report fingerprint: `09d7d01631fc3cbd...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*