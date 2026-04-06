# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W15** | Generated 2026-04-06 08:13:33 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4213 |
| Models | 3380 |
| Datasets | 833 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 678 | 3535 | **16.1%** |
| **Declared Datasets** | 862 | 3351 | **20.5%** |
| **License** | 3214 | 999 | **76.3%** |
| **README Accessible** | 3605 | 597 | **85.6%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 4032
- **Gated targets:** 164 (3.9%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **196.6M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **68.9M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **49.1M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **39.3M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **29.2M** | PRESENT | 21 |
| `openai/clip-vit-large-patch14` | model | **28.0M** | ABSENT | 0 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **27.7M** | ABSENT | 0 |
| `laion/clap-htsat-fused` | model | **22.2M** | ABSENT | 0 |
| `FacebookAI/roberta-large` | model | **20.5M** | PRESENT | 2 |
| `openai/clip-vit-base-patch32` | model | **20.4M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **49.1M** | OK |
| `openai/clip-vit-large-patch14` | **28.0M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **27.7M** | OK |
| `laion/clap-htsat-fused` | **22.2M** | OK |
| `openai/clip-vit-base-patch32` | **20.4M** | OK |
| `FacebookAI/xlm-roberta-base` | **19.9M** | OK |
| `Bingsu/adetailer` | **16.3M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **15.5M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **14.5M** | OK |
| `Qwen/Qwen3-0.6B` | **14.2M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 160 | 3 (2%) | 0 (0%) | 158 (99%) |
| **facebook** | 111 | 17 (15%) | 45 (41%) | 103 (93%) |
| **timm** | 90 | 0 (0%) | 70 (78%) | 90 (100%) |
| **google** | 89 | 31 (35%) | 25 (28%) | 86 (97%) |
| **microsoft** | 88 | 21 (24%) | 13 (15%) | 71 (81%) |
| **nvidia** | 79 | 39 (49%) | 34 (43%) | 75 (95%) |
| **allenai** | 74 | 3 (4%) | 32 (43%) | 63 (85%) |
| **unsloth** | 65 | 4 (6%) | 1 (2%) | 63 (97%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **Salesforce** | 52 | 11 (21%) | 6 (12%) | 51 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **mradermacher** | 47 | 0 (0%) | 12 (26%) | 38 (81%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **EleutherAI** | 44 | 33 (75%) | 40 (91%) | 44 (100%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 56 |
| **Changes (30 days)** | 145 |
| **Targets with changes** | 100 |

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

*Report fingerprint: `1eda534f5b9cdf81...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*