# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W11** | Generated 2026-03-09 08:05:46 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 4035 |
| Models | 3272 |
| Datasets | 763 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 650 | 3385 | **16.1%** |
| **Declared Datasets** | 842 | 3193 | **20.9%** |
| **License** | 3064 | 971 | **75.9%** |
| **README Accessible** | 3483 | 549 | **86.3%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 3862
- **Gated targets:** 155 (3.8%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **200.2M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **67.1M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **48.4M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **41.2M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **27.5M** | PRESENT | 21 |
| `timm/mobilenetv3_small_100.lamb_in1k` | model | **24.8M** | ABSENT | 1 |
| `FacebookAI/roberta-large` | model | **23.0M** | PRESENT | 2 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **22.8M** | ABSENT | 0 |
| `Qwen/Qwen2.5-7B-Instruct` | model | **21.9M** | ABSENT | 0 |
| `laion/clap-htsat-fused` | model | **21.7M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **48.4M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **24.8M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **22.8M** | OK |
| `Qwen/Qwen2.5-7B-Instruct` | **21.9M** | OK |
| `laion/clap-htsat-fused` | **21.7M** | OK |
| `FacebookAI/xlm-roberta-base` | **19.5M** | OK |
| `openai/clip-vit-base-patch32` | **19.1M** | OK |
| `Bingsu/adetailer` | **17.8M** | OK |
| `pyannote/wespeaker-voxceleb-resnet34-LM` | **15.0M** | OK |
| `pyannote/segmentation-3.0` | **14.8M** | FORBIDDEN |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 155 | 4 (3%) | 0 (0%) | 151 (97%) |
| **facebook** | 106 | 16 (15%) | 43 (41%) | 100 (94%) |
| **microsoft** | 88 | 24 (27%) | 12 (14%) | 71 (81%) |
| **timm** | 86 | 0 (0%) | 66 (77%) | 86 (100%) |
| **google** | 85 | 33 (39%) | 23 (27%) | 82 (96%) |
| **allenai** | 71 | 3 (4%) | 31 (44%) | 61 (86%) |
| **nvidia** | 67 | 32 (48%) | 29 (43%) | 63 (94%) |
| **OpenMed** | 53 | 0 (0%) | 0 (0%) | 53 (100%) |
| **unsloth** | 52 | 4 (8%) | 1 (2%) | 49 (94%) |
| **Salesforce** | 51 | 11 (22%) | 6 (12%) | 50 (98%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **deepseek-ai** | 44 | 0 (0%) | 0 (0%) | 36 (82%) |
| **mradermacher** | 44 | 0 (0%) | 8 (18%) | 35 (80%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 38 |
| **Changes (30 days)** | 993 |
| **Targets with changes** | 840 |

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

*Report fingerprint: `0d953031c1388717...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*