# 🌍 Cross-Variety NLP Classifier — BESSTIE

> COMM061 NLP Group Coursework | Group 26  
> Sarcasm & Sentiment Detection across British, Australian, and Indian English

---

## 📖 Overview

This project investigates cross-variety sarcasm and sentiment classification across three English dialects — **British (en-UK)**, **Australian (en-AU)**, and **Indian (en-IN)** — using the [BESSTIE dataset](https://huggingface.co/datasets/surrey-nlp/BESSTIE-CW-26).

Three experimental setups are explored:
- Classical ML baseline (TF-IDF + Logistic Regression) vs. fine-tuned **RoBERTa**
- **Cross-variety transfer** evaluation (zero-shot generalisation across dialects)
- **LoRA fine-tuning** of Llama 3.2 1B with few-shot prompting for sarcasm explanation

---

## 👥 Team

| Name | 
|------|
| Bong Jun Kim |
| Piyush Gupta |
| Akash Chohan |
| Parth Singh Jhala |
| Turab Ghumman |

---

## 📁 Repository Structure

```
├── [1.] TD-IDF_Logistic_regression__RoBERTa.ipynb   # Baseline vs RoBERTa experiments
├── [2.] Cross_Variety_Evaluation.ipynb              # Cross-variety transfer experiments
├── [3.] Llama_LoRA__Few_Shot_prompt.ipynb           # LoRA fine-tuning & few-shot prompting
├── [4.] app.py                                       # Streamlit deployment app
├── Report_PG-26.pdf                                  # Full coursework report
└── requirements.txt                                  # Python dependencies
```

---

## 🧪 Experiments

### 1. Baseline vs RoBERTa
Compares TF-IDF + Logistic Regression against fine-tuned RoBERTa-base for sentiment and sarcasm classification.

| Task | Model | Macro-F1 |
|------|-------|----------|
| Sentiment | TF-IDF + LR | 0.8241 |
| Sentiment | RoBERTa | 0.8940 |
| Sarcasm | TF-IDF + LR | 0.6249 |
| Sarcasm | RoBERTa | 0.6814 |

### 2. Cross-Variety Transfer
Models trained on one English variety and tested on the others (zero-shot setting). Sentiment transfers well; sarcasm shows significant degradation across dialects.

### 3. Llama 3.2 1B + LoRA
Dialect-specific LoRA adapters trained for en-UK and en-IN sarcasm detection. Threshold tuning used to optimise Macro-F1. Few-shot prompting corrects 5/6 false positive errors.

---

## 🚀 Deployment

A **Streamlit** web app allows users to input text, select an English variety, and receive dialect-aware sentiment and sarcasm predictions.

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Key Findings

- **Sentiment** classification transfers robustly across all English varieties
- **Sarcasm** detection is inherently dialect-sensitive and struggles under cross-variety transfer
- Models rely on shallow lexical cues rather than deeper pragmatic signals (confirmed via LIME & SHAP)
- LoRA adapters offer parameter-efficient dialect-specific fine-tuning (~4–6M trainable params vs ~1B)
- **Macro-F1** is used as the primary metric throughout due to significant class imbalance in sarcasm labels

---

## ⚠️ Note on API Tokens

This repository does not contain any API keys or access tokens. If running the Llama LoRA notebook, store your Hugging Face token securely using Colab Secrets or a `.env` file — never hardcode it in the notebook.

---

## 📄 License

This project was developed for academic purposes as part of the COMM061 NLP module.
