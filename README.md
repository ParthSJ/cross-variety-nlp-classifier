# cross-variety-nlp-classifier
# 🌍 BESSTIE: Cross-Variety English Sarcasm & Sentiment Detector

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B)

## 📌 Overview
This repository contains the code, experiments, and deployment for the **COMM061 Natural Language Processing Coursework (University of Surrey, 2025-26)**. 

The project investigates how well NLP models trained on one regional variety of English generalize to unseen varieties. Specifically, we classify **Sentiment** and **Sarcasm** across three English dialects:
* 🇬🇧 British English (`en-UK`)
* 🇦🇺 Australian English (`en-AU`)
* 🇮🇳 Indian English (`en-IN`)

## 🧠 Models Implemented
The project scales from traditional machine learning baselines to modern Large Language Models:
1. **Baselines:** TF-IDF + Logistic Regression
2. **Transformer Fine-tuning:** RoBERTa-base / DistilRoBERTa
3. **Generative LLMs:** LLaMA with **LoRA (Low-Rank Adaptation)** and Few-Shot Prompting.

## 📊 Key Findings (Cross-Variety Evaluation)
Our cross-variety experimentation revealed critical insights into dialect-agnostic learning:
* **Sentiment Detection:** Contextual embeddings (RoBERTa) generalized strongly across all varieties (F1 scores ranging from 0.76 to 0.94), showing that opinion-bearing language is largely variety-agnostic.
* **Sarcasm Detection:** Transfer was significantly harder due to class imbalances and localized cultural cues. Models trained on `en-AU` generalized better due to a richer baseline of sarcastic examples.
* **Explainability:** We utilized **LIME** and **SHAP** to inspect failure cases, visualizing exactly which tokens led to cross-dialect misclassifications.

## 📂 Repository Structure

```text
├── notebooks/
│   ├── 01_tfidf_roberta_baseline.ipynb     # TF-IDF & RoBERTa initial models
│   ├── 02_cross_variety_evaluation.ipynb   # Dialect transfer experiments & LIME/SHAP
│   └── 03_llama_lora_few_shot.ipynb        # Parameter-Efficient Fine-Tuning (PEFT) on LLaMA
├── app/
│   └── app.py                              # Streamlit UI for the BESSTIE Classifier
├── data/                                   # Processed datasets (excluded from version control)
├── requirements.txt                        # Python dependencies
└── README.md
