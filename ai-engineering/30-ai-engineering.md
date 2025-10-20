# ⚡ Lesson 30 — FastAPI Endpoints for AI

### *AI Engineer Roadmap 2025 — Skill #30*

---

## 🎯 Objective

Learn how to **serve AI and ML models via FastAPI endpoints**, turning your trained models into scalable APIs that deliver real-time predictions, insights, and automation.

---

## 🧩 Definition

**FastAPI** is a modern, high-performance web framework for building REST APIs with Python.
It’s asynchronous, type-safe, and perfect for deploying AI models as web services — providing millisecond-level latency and auto-generated documentation (Swagger UI).

---

## 🧠 Core Concepts

| Concept              | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| **Endpoint**         | A specific route (e.g., `/predict`) where requests are processed. |
| **Request Body**     | The input JSON data sent by the client.                           |
| **Response Model**   | Defines the structured output returned by the API.                |
| **Pydantic Models**  | Ensure input/output validation with typed schemas.                |
| **CORS Middleware**  | Allows frontend apps (React, Vue, etc.) to call your API.         |
| **Swagger UI**       | Interactive auto-docs at `/docs`.                                 |
| **Background Tasks** | Run async operations like model loading or logging.               |

---

## ⚙️ Example — AI Prediction Endpoint

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI(title="AI Prediction API")

class InputData(BaseModel):
    x1: float
    x2: float

model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: InputData):
    result = model.predict([[data.x1, data.x2]])[0]
    return {"prediction": float(result)}
```

Run locally:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Visit: **[http://localhost:8000/docs](http://localhost:8000/docs)** for interactive API testing.

---

## ⚙️ Async Example (Streaming AI)

```python
from fastapi.responses import StreamingResponse
import openai

@app.get("/stream")
async def stream_response(prompt: str):
    stream = openai.chat.completions.create(
        model="gpt-4-turbo", messages=[{"role": "user", "content": prompt}], stream=True)
    return StreamingResponse((chunk.choices[0].delta.get("content", "") for chunk in stream))
```

---

## 🧱 Use Cases in AI Engineering

| Category           | Example                                                    |
| ------------------ | ---------------------------------------------------------- |
| **Model Serving**  | Host models for real-time predictions.                     |
| **Chatbots**       | Serve AI conversations through `/chat`.                    |
| **Data Pipelines** | Connect preprocessing, inference, and analytics endpoints. |
| **Agent Backends** | Power tool-calling and decision-making APIs.               |
| **Dashboard APIs** | Serve analytics and insights to web apps.                  |

---

## 📘 Mini Project

**Goal:** Build a **FastAPI Service for Text Summarization**
**Steps:**

1. Use the OpenAI API for summarization.
2. Create a POST route `/summarize` that takes `{"text": "... "}`.
3. Return the summarized text in JSON.
4. Test locally and containerize with Docker.

**Expected Outcome:**
A local AI microservice that takes long text and returns short summaries instantly.

---

## 🧠 Example Prompt

> “How does FastAPI differ from Flask for AI model deployment, and why is it preferred for production APIs?”

---

## 🔍 Key Takeaway

FastAPI turns your AI code into **scalable, production-grade microservices** — fast, async, and ready for deployment in the cloud or on Docker.

---

## 📚 Further Reading

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Models Reference](https://docs.pydantic.dev/latest/)
* [Uvicorn ASGI Server](https://www.uvicorn.org/)
* [FastAPI + Docker Deployment](https://testdriven.io/blog/fastapi-docker/)
* [Building Async APIs for AI](https://fastapi.tiangolo.com/async/)