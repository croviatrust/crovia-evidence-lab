# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W16** | Generated 2026-04-13 08:09:45 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4240 |
| Models | 3410 |
| Datasets | 830 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 687 | 3553 | **16.2%** |
| **Declared Datasets** | 864 | 3376 | **20.4%** |
| **License** | 3245 | 995 | **76.5%** |
| **README Accessible** | 3653 | 586 | **86.2%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 4058
- **Gated targets:** 168 (4.0%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **196.2M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **65.0M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **48.4M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **37.6M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **30.7M** | PRESENT | 21 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **30.5M** | ABSENT | 0 |
| `openai/clip-vit-large-patch14` | model | **28.7M** | ABSENT | 0 |
| `FacebookAI/roberta-large` | model | **20.8M** | PRESENT | 2 |
| `openai/clip-vit-base-patch32` | model | **20.7M** | ABSENT | 0 |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | model | **19.2M** | ABSENT | 1 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **48.4M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **30.5M** | OK |
| `openai/clip-vit-large-patch14` | **28.7M** | OK |
| `openai/clip-vit-base-patch32` | **20.7M** | OK |
| `cross-encoder/ms-marco-MiniLM-L6-v2` | **19.2M** | OK |
| `laion/clap-htsat-fused` | **19.0M** | OK |
| `FacebookAI/xlm-roberta-base` | **18.9M** | OK |
| `BAAI/bge-small-en-v1.5` | **17.4M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **15.3M** | OK |
| `Bingsu/adetailer` | **15.2M** | OK |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 159 | 3 (2%) | 0 (0%) | 157 (99%) |
| **facebook** | 111 | 17 (15%) | 44 (40%) | 103 (93%) |
| **google** | 91 | 31 (34%) | 25 (27%) | 88 (97%) |
| **timm** | 89 | 0 (0%) | 69 (78%) | 89 (100%) |
| **microsoft** | 88 | 23 (26%) | 13 (15%) | 71 (81%) |
| **nvidia** | 84 | 41 (49%) | 34 (40%) | 80 (95%) |
| **allenai** | 71 | 3 (4%) | 31 (44%) | 61 (86%) |
| **unsloth** | 66 | 4 (6%) | 1 (2%) | 64 (97%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **Salesforce** | 52 | 11 (21%) | 6 (12%) | 51 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **mradermacher** | 46 | 0 (0%) | 11 (24%) | 37 (80%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **lmstudio-community** | 45 | 0 (0%) | 4 (9%) | 42 (93%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 686 |
| **Changes (30 days)** | 792 |
| **Targets with changes** | 418 |

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

*Report fingerprint: `b66226426e05eff6...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*