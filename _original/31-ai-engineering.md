# 🖥️ Lesson 31 — Streamlit / Gradio Apps

### *AI Engineer Roadmap 2025 — Skill #31*

---

## 🎯 Objective

Learn how to **build interactive AI web apps** using **Streamlit** and **Gradio** — lightweight frameworks that make it simple to demo, visualize, and share machine learning models with a user-friendly UI.

---

## 🧩 Definition

**Streamlit** and **Gradio** are Python libraries for quickly turning data science and AI scripts into web applications — **without frontend code**.
They’re ideal for creating dashboards, model demos, and proof-of-concept tools that anyone can use in a browser.

---

## 🧠 Core Concepts

| Concept              | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| **Reactive UI**      | Automatic updates when user input changes.                      |
| **Widgets**          | Interactive inputs like sliders, text boxes, and dropdowns.     |
| **Caching**          | Store model/data to avoid reloading each time.                  |
| **Layout**           | Control page sections and columns easily.                       |
| **Deployment**       | Share apps online using Streamlit Cloud or Hugging Face Spaces. |
| **State Management** | Keep track of user input across sessions.                       |
| **Integration**      | Combine with APIs, OpenAI, or local ML models.                  |

---

## ⚙️ Example — Streamlit App for Sentiment Analysis

```python
import streamlit as st
from transformers import pipeline

st.title("💬 Sentiment Analysis App")

analyzer = pipeline("sentiment-analysis")
text = st.text_area("Enter your text:")

if st.button("Analyze"):
    result = analyzer(text)[0]
    st.write(f"**Label:** {result['label']} | **Score:** {result['score']:.2f}")
```

Run it:

```bash
streamlit run app.py
```

---

## ⚙️ Example — Gradio Interface for Image Classification

```python
import gradio as gr
from transformers import pipeline

classifier = pipeline("image-classification")

def classify_image(img):
    return classifier(img)

app = gr.Interface(fn=classify_image, inputs="image", outputs="label")
app.launch()
```

---

## 🧱 Use Cases in AI Engineering

| Category              | Example                                   |
| --------------------- | ----------------------------------------- |
| **Model Demos**       | Share interactive versions of ML models.  |
| **Data Dashboards**   | Visualize training metrics or embeddings. |
| **AI Assistants**     | Build GPT-powered chat UIs.               |
| **Internal Tools**    | Create quick utilities for teams.         |
| **Hackathons / MVPs** | Prototype ideas rapidly.                  |

---

## 📘 Mini Project

**Goal:** Build a **Text-to-Image Generator App**
**Steps:**

1. Use the OpenAI or Stability API for image generation.
2. Create a text input field for prompts.
3. Display generated images in real time.
4. Deploy on Hugging Face Spaces.

**Expected Outcome:**
A sharable app that turns text prompts into images within seconds.

---

## 🧠 Example Prompt

> “Compare Streamlit and Gradio for AI app prototyping — which is better for interactive model demos?”

---

## 🔍 Key Takeaway

Streamlit and Gradio make **AI accessible and visual** — bridging the gap between data scientists and end users through instant, interactive interfaces.

---

## 📚 Further Reading

* [Streamlit Official Docs](https://docs.streamlit.io/)
* [Gradio Documentation](https://gradio.app/docs/)
* [Streamlit Cloud Deployment](https://streamlit.io/cloud)
* [Hugging Face Spaces Guide](https://huggingface.co/docs/hub/spaces-overview)
* [Building Streamlit + OpenAI Apps](https://platform.openai.com/docs/guides/streamlit)