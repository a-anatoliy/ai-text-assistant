# AI Text Assistant

**AI Text Assistant** is a lightweight, interactive web app built with Streamlit that uses state-of-the-art NLP models to analyze any text input. It helps users to:

- 🔍 Detect the **sentiment** of the text (positive, negative, neutral)
- 📚 Generate a **short summary**
- ✉️ Suggest an **automatic reply**

Ideal for handling feedback, emails, customer messages, and more.

---

## 🚀 Features

- **Multilingual Sentiment Analysis** using transformer-based models
- **Text Summarization** powered by pre-trained T5/BART
- **Auto-Response Generation** using GPT-2
- Simple and elegant **Streamlit UI**
- Ready for deployment on Hugging Face Spaces

---

## 🧠 Tech Stack

| Purpose              | Technology                                |
|----------------------|--------------------------------------------|
| NLP Models           | [🤗 Transformers](https://huggingface.co/transformers/) |
| Web Interface        | [Streamlit](https://streamlit.io/)        |
| Deep Learning Backend| PyTorch                                   |
| Deployment           | Hugging Face Spaces / GitHub              |

---

## 📦 Installation

```bash
git clone https://github.com/a-anatoliy/ai-text-assistant.git
cd ai-text-assistant
pip install -r requirements.txt
streamlit run app.py
