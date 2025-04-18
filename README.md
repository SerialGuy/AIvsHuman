---
title: AI vs Human Text Classifier
emoji: 🚀
colorFrom: indigo
colorTo: pink
sdk: streamlit
sdk_version: 5.25.2
app_file: app.py
pinned: false
---
# 🧠 AI vs Human Text Detector

This project is a machine learning-based system designed to distinguish between text written by a **human** and that generated by an **AI language model** (e.g., ChatGPT). It uses deep learning and text embeddings to analyze writing patterns and classify them accurately.

---

## 📌 Features

- ✅ Binary classification: AI-generated vs Human-written text
- 📈 Achieved **92% accuracy** and **0.89 F1-Score**
- 🔍 Embedding + Deep Learning model
- 📊 Evaluation on real-world prompts and datasets
- 🧪 Trained and tested using clean, balanced samples

---

## 🚀 Live Demo (Optional)

🔗 **[Try it on Hugging Face Spaces](https://huggingface.co/spaces/SerialGuy/ai-vs-human)**  
(*Coming Soon — stay tuned!*)  
> Enter a piece of text and the model will predict whether it's written by an AI or a human.

---

## 📂 Repository Structure

```bash
.
├── train_model.ipynb      # Notebook to preprocess and train the model
├── requirements.txt       # (Optional) Dependencies
└── README.md              # Project overview and instructions
---
title: AI vs Human Text Classifier
emoji: 🧠
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: "4.20.0"
app_file: app.py
pinned: false
---