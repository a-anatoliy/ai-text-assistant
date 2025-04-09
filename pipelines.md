# 🤖 NLP Pipelines Overview (Hugging Face Transformers)

This file contains a practical reference for common NLP pipeline tasks supported by Hugging Face `transformers`. Use this table to quickly match a real-world task with the correct `pipeline` and model.

---

## 🧭 Step-by-step Guide

1. **Classify your task**
   What do you want to do with the text? (e.g., summarize, classify, answer questions)

2. **Choose the appropriate pipeline**
   Each task has a matching `pipeline()` function in Hugging Face.

3. **Select a model**
   Either use the default model (automatically selected), or specify one manually for better control (e.g., language, accuracy, size).

---

## 🔧 Popular Pipelines Table

| Pipeline Task             | Purpose                                         | Example Call                                  | Common Models                                            |
|--------------------------|--------------------------------------------------|------------------------------------------------|----------------------------------------------------------|
| `sentiment-analysis`     | Detect emotion (positive/negative)              | `pipeline("sentiment-analysis")`              | `distilbert-base-uncased-finetuned-sst-2-english`        |
| `text-classification`    | General classification (e.g., topic, spam)      | `pipeline("text-classification")`             | `bert-base-uncased`, `roberta-base`                      |
| `summarization`          | Summarize large texts                           | `pipeline("summarization")`                   | `facebook/bart-large-cnn`, `t5-small`                    |
| `translation`            | Translate between languages                     | `pipeline("translation_en_to_fr")`            | `Helsinki-NLP/opus-mt-en-fr`, `t5-small`                 |
| `text-generation`        | Generate continuations or replies               | `pipeline("text-generation")`                 | `gpt2`, `mistralai/Mistral-7B-Instruct-v0.1`             |
| `question-answering`     | Extract answers from context                    | `pipeline("question-answering")`              | `distilbert-base-cased-distilled-squad`                  |
| `ner`                    | Named Entity Recognition                        | `pipeline("ner")`                              | `dbmdz/bert-large-cased-finetuned-conll03-english`       |
| `zero-shot-classification`| Classify without training data                  | `pipeline("zero-shot-classification")`         | `facebook/bart-large-mnli`                              |

---

## 🔗 Resources

- 📘 [Transformers pipeline documentation](https://huggingface.co/docs/transformers/main_classes/pipelines)
- 🧠 [Hugging Face Models Hub](https://huggingface.co/models)
- ⚙️ [List of available tasks](https://huggingface.co/tasks)

---

Feel free to expand this file as your assistant grows 🤍
