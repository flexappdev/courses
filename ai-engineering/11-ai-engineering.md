# 🌐 Lesson 11 — Working with APIs

### *AI Engineer Roadmap 2025 — Skill #11*

---

## 🎯 Objective

Learn how to **connect AI systems to the outside world** using APIs — to send data, retrieve information, and integrate machine learning models into real products.

---

## 🧩 Definition

An **API (Application Programming Interface)** allows two software systems to communicate.
For AI engineers, APIs are used to **deploy models**, **fetch data**, or **consume external AI services** like OpenAI, Anthropic, or Hugging Face.

---

## 🧠 Core Concepts

| Concept                      | Description                                           |
| ---------------------------- | ----------------------------------------------------- |
| **Endpoint**                 | A specific URL where an API resource can be accessed. |
| **HTTP Methods**             | `GET`, `POST`, `PUT`, `DELETE` — define action types. |
| **Request / Response**       | Client sends data → Server returns data (JSON).       |
| **Headers & Authentication** | API keys or OAuth tokens for secure access.           |
| **Rate Limiting**            | Restricting number of API calls to avoid overuse.     |
| **Error Handling**           | Managing status codes (200, 404, 500).                |
| **Webhooks**                 | Server-side triggers that notify your system.         |

---

## ⚙️ Python Example

```python
import requests

url = "https://api.openai.com/v1/chat/completions"
headers = {"Authorization": "Bearer YOUR_API_KEY"}
data = {
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Explain AI in one sentence."}]
}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])
```

---

## 🧱 Use Cases in AI Engineering

| Area                   | Example                                             |
| ---------------------- | --------------------------------------------------- |
| **Model Deployment**   | Host your own FastAPI endpoint for predictions.     |
| **Third-Party Models** | Access GPT, Claude, Gemini APIs.                    |
| **Data Gathering**     | Pull datasets from APIs (Reddit, YouTube, Twitter). |
| **Integration**        | Connect backends, dashboards, and AI agents.        |
| **Automation**         | Trigger workflows with API calls or webhooks.       |

---

## 📘 Mini Project

**Goal:** Create a **Text Summarizer API**
**Steps:**

1. Build a FastAPI endpoint `/summarize`.
2. Send text input via POST request.
3. Use OpenAI or Hugging Face model to summarize.
4. Return summarized text as JSON.

**Expected Outcome:**
A working local API that takes user input and responds with a generated summary.

---

## 🧠 Example Prompt

> “Explain how REST APIs enable integration between an AI backend and a web frontend.”

---

## 🔍 Key Takeaway

APIs are the **connective tissue of AI** — linking your models, databases, and frontends into cohesive, automated ecosystems.

---

## 📚 Further Reading

* [FastAPI Official Docs](https://fastapi.tiangolo.com/)
* [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
* [Postman API Testing Tool](https://www.postman.com/)
* [RESTful API Design Guidelines](https://restfulapi.net/)