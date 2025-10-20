# 🌐 Lesson 27 — Google Vertex AI / Gemini API

### *AI Engineer Roadmap 2025 — Skill #27*

---

## 🎯 Objective

Learn how to build, deploy, and scale AI systems using **Google Cloud’s Vertex AI platform** and **Gemini API**, Google’s ecosystem for advanced machine learning and multimodal large language models.

---

## 🧩 Definition

**Vertex AI** is Google Cloud’s unified platform for developing, training, deploying, and monitoring ML models.
**Gemini**, Google’s family of LLMs, integrates directly with Vertex AI and offers **multimodal capabilities** (text, image, audio, and video).
Together, they provide a full-stack AI environment for both developers and enterprises.

---

## 🧠 Core Concepts

| Concept                     | Description                                                       |
| --------------------------- | ----------------------------------------------------------------- |
| **Vertex AI Studio**        | Interactive console for testing and fine-tuning models.           |
| **Gemini Models**           | Google’s flagship multimodal LLMs (Gemini 1.5 Pro, Flash).        |
| **Model Garden**            | Repository of pre-trained and open-source models.                 |
| **Custom Training**         | Train custom ML models on your data using managed infrastructure. |
| **Endpoints**               | Deploy models as APIs with auto-scaling.                          |
| **Pipelines**               | Automate ML workflows and retraining cycles.                      |
| **BigQuery ML Integration** | Run ML models directly on structured datasets.                    |
| **Responsible AI Toolkit**  | Evaluate fairness, explainability, and privacy compliance.        |

---

## ⚙️ Example — Calling Gemini via Vertex AI

```python
from vertexai.preview.language_models import TextGenerationModel

model = TextGenerationModel.from_pretrained("gemini-1.5-pro")

response = model.predict(
    "Summarize how Gemini differs from GPT-4 in two paragraphs.",
    temperature=0.4,
    max_output_tokens=300,
)

print(response.text)
```

---

## ⚙️ Example — Using Vertex AI SDK for Custom Models

```python
from google.cloud import aiplatform

aiplatform.init(project="my-ai-project", location="us-central1")

model = aiplatform.Model.upload(
    display_name="custom-ml-model",
    artifact_uri="gs://my_bucket/model/",
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"
)

endpoint = model.deploy(machine_type="n1-standard-4")
print(f"Model deployed at: {endpoint.resource_name}")
```

---

## 🧱 Use Cases in AI Engineering

| Category                     | Example                                             |
| ---------------------------- | --------------------------------------------------- |
| **Enterprise AI Assistants** | Build chat and workflow assistants with Gemini 1.5. |
| **Multimodal Analysis**      | Combine image + text for visual reasoning.          |
| **Data Intelligence**        | Connect LLMs to BigQuery for real-time insights.    |
| **Model Deployment**         | Serve models at scale using managed endpoints.      |
| **Compliance-Ready AI**      | Use Google’s Responsible AI tools for auditing.     |

---

## 📘 Mini Project

**Goal:** Build a **Multimodal Document Analyzer**
**Steps:**

1. Use Gemini 1.5 Pro for text + image input.
2. Upload a research paper (PDF) with graphs.
3. Extract insights and generate summaries with visual context.
4. Deploy as a Vertex AI endpoint.

**Expected Outcome:**
A multimodal AI app that understands both visual and textual content for enterprise use cases.

---

## 🧠 Example Prompt

> “Explain how Gemini 1.5 differs from GPT-5 in terms of multimodal understanding and latency.”

---

## 🔍 Key Takeaway

Vertex AI and Gemini together form a **production-grade AI ecosystem** — combining Google’s infrastructure, multimodal power, and cloud-scale deployment tools.

---

## 📚 Further Reading

* [Google Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
* [Gemini API Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
* [Vertex AI SDK Reference](https://cloud.google.com/python/docs/reference/aiplatform/latest)
* [Responsible AI Toolkit](https://cloud.google.com/responsible-ai)
* [BigQuery ML](https://cloud.google.com/bigquery-ml/docs)