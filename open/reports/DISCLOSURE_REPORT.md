# 📊 Crovia Disclosure Transparency Report

> **Week 2026-W10** | Generated 2026-03-02 08:01:03 UTC
>
> *This is observational data only. No inference, judgment, or accusation.*

---

## 📈 Coverage

| Metric | Value |
|--------|-------|
| **Targets Monitored** | 3940 |
| Models | 3220 |
| Datasets | 720 |

---

## 🔍 Disclosure Observations

| Field | Present | Absent | % Present |
|-------|---------|--------|-----------|
| **Training Section** | 639 | 3301 | **16.2%** |
| **Declared Datasets** | 836 | 3104 | **21.2%** |
| **License** | 3009 | 931 | **76.4%** |
| **README Accessible** | 3422 | 518 | **86.9%** |

---

## 📥 Popularity Observations

- **Targets with download data:** 3772
- **Gated targets:** 154 (3.9%)

### Top Targets by Downloads

| Target | Type | Downloads | Training Section | Declared Datasets |
|--------|------|-----------|------------------|-------------------|
| `sentence-transformers/all-MiniLM-L6-v2` | model | **191.7M** | PRESENT | 21 |
| `google-bert/bert-base-uncased` | model | **61.6M** | PRESENT | 2 |
| `google/electra-base-discriminator` | model | **48.6M** | ABSENT | 0 |
| `Falconsai/nsfw_image_detection` | model | **41.0M** | PRESENT | 0 |
| `sentence-transformers/all-mpnet-base-v2` | model | **26.9M** | PRESENT | 21 |
| `FacebookAI/xlm-roberta-base` | model | **25.0M** | ABSENT | 0 |
| `timm/mobilenetv3_small_100.lamb_in1k` | model | **24.2M** | ABSENT | 1 |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | model | **21.7M** | ABSENT | 0 |
| `FacebookAI/roberta-large` | model | **21.4M** | PRESENT | 2 |
| `laion/clap-htsat-fused` | model | **19.9M** | ABSENT | 0 |

### High-Download Targets Without Training Section

*Factual observation: these targets have >10K downloads and no detected training section.*

| Target | Downloads | README |
|--------|-----------|--------|
| `google/electra-base-discriminator` | **48.6M** | OK |
| `FacebookAI/xlm-roberta-base` | **25.0M** | OK |
| `timm/mobilenetv3_small_100.lamb_in1k` | **24.2M** | OK |
| `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | **21.7M** | OK |
| `laion/clap-htsat-fused` | **19.9M** | OK |
| `openai/clip-vit-base-patch32` | **19.6M** | OK |
| `Qwen/Qwen2.5-7B-Instruct` | **19.3M** | OK |
| `Bingsu/adetailer` | **16.0M** | OK |
| `pyannote/wespeaker-voxceleb-resnet34-LM` | **15.8M** | OK |
| `pyannote/segmentation-3.0` | **15.4M** | FORBIDDEN |

---

## 🏢 By Organization

| Organization | Targets | Training Section | Declared Datasets | License |
|--------------|---------|------------------|-------------------|---------|
| **Qwen** | 148 | 4 (3%) | 0 (0%) | 144 (97%) |
| **facebook** | 105 | 16 (15%) | 43 (41%) | 99 (94%) |
| **microsoft** | 88 | 24 (27%) | 12 (14%) | 71 (81%) |
| **google** | 84 | 32 (38%) | 23 (27%) | 81 (96%) |
| **timm** | 84 | 0 (0%) | 65 (77%) | 84 (100%) |
| **allenai** | 72 | 3 (4%) | 32 (44%) | 62 (86%) |
| **nvidia** | 66 | 31 (47%) | 29 (44%) | 62 (94%) |
| **OpenMed** | 52 | 0 (0%) | 0 (0%) | 52 (100%) |
| **Salesforce** | 51 | 11 (22%) | 6 (12%) | 50 (98%) |
| **unsloth** | 49 | 4 (8%) | 1 (2%) | 46 (94%) |
| **MaziyarPanahi** | 47 | 2 (4%) | 0 (0%) | 6 (13%) |
| **bigscience** | 46 | 7 (15%) | 8 (17%) | 19 (41%) |
| **BAAI** | 45 | 7 (16%) | 9 (20%) | 41 (91%) |
| **mradermacher** | 44 | 0 (0%) | 8 (18%) | 35 (80%) |
| **EleutherAI** | 43 | 31 (72%) | 38 (88%) | 43 (100%) |

---

## 📉 Drift Observations

| Metric | Value |
|--------|-------|
| **Changes (7 days)** | 51 |
| **Changes (30 days)** | 1143 |
| **Targets with changes** | 844 |

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

*Report fingerprint: `95c3d189e060af31...`*

*Source: [Crovia Training Provenance Registry](https://registry.croviatrust.com)*