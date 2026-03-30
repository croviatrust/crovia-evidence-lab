# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W14** | Generated 2026-03-30 08:14:46 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4183 |
| Models | 3355 |
| Datasets | 828 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 682 | 3501 | **16.3%** |
| **Declared Datasets** | 855 | 3328 | **20.4%** |
| **License** | 3185 | 998 | **76.1%** |
| **README Accessible** | 3573 | 593 | **85.4%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 4007
- **Gated targets:** 162 (3.9%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **206.2M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **71.8M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **50.8M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **41.1M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **29.4M** | PRESENT | 21 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **26.8M** | ABSENT | 0 |
| `laion/clap-htsat-fused` | model | **26.2M** | ABSENT | 0 |
| `openai/clip-vit-large-patch14` | model | **24.5M** | ABSENT | 0 |
| `FacebookAI/xlm-roberta-base` | model | **20.8M** | ABSENT | 0 |
| `openai/clip-vit-base-patch32` | model | **20.6M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **50.8M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **26.8M** | OK |
| `laion/clap-htsat-fused` | **26.2M** | OK |
| `openai/clip-vit-large-patch14` | **24.5M** | OK |
| `FacebookAI/xlm-roberta-base` | **20.8M** | OK |
| `openai/clip-vit-base-patch32` | **20.6M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **18.3M** | OK |
| `Bingsu/adetailer` | **17.9M** | OK |
| `Qwen/Qwen2.5-7B-Instruct` | **17.9M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **15.2M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 159 | 3 (2%) | 0 (0%) | 157 (99%) |
| **facebook** | 111 | 17 (15%) | 45 (41%) | 102 (92%) |
| **timm** | 91 | 0 (0%) | 70 (77%) | 91 (100%) |
| **microsoft** | 88 | 23 (26%) | 13 (15%) | 71 (81%) |
| **google** | 84 | 31 (37%) | 24 (29%) | 81 (96%) |
| **nvidia** | 75 | 37 (49%) | 33 (44%) | 71 (95%) |
| **allenai** | 73 | 3 (4%) | 32 (44%) | 62 (85%) |
| **unsloth** | 59 | 4 (7%) | 1 (2%) | 57 (97%) |
| **Salesforce** | 53 | 12 (23%) | 6 (11%) | 52 (98%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **mradermacher** | 45 | 0 (0%) | 10 (22%) | 36 (80%) |
| **EleutherAI** | 43 | 32 (74%) | 39 (91%) | 43 (100%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 49 |
| **Changes (30 days)** | 185 |
| **Targets with changes** | 145 |

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

*Report fingerprint: `be8a9b89a9d396b8...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*