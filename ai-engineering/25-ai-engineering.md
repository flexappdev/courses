# 🔑 Lesson 25 — OpenAI API Usage

### *AI Engineer Roadmap 2025 — Skill #25*

---

## 🎯 Objective

Learn how to **integrate OpenAI’s API** into your applications to build intelligent tools — from chatbots and summarizers to image and embedding generators — using models like **GPT-4-Turbo**, **GPT-5**, and **text-embedding-3-large**.

---

## 🧩 Definition

The **OpenAI API** provides access to powerful large language models (LLMs), embedding models, and image generation systems.
It uses a **simple REST interface** (or SDK) that accepts JSON payloads — making it easy to embed advanced AI into any app, backend, or automation pipeline.

---

## 🧠 Core Concepts

| Concept              | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| **Endpoint**         | API route such as `/chat/completions`, `/embeddings`, `/images`.      |
| **Model**            | Defines which capability you’re calling (GPT-4, GPT-5, DALL·E, etc.). |
| **Message Format**   | Structured messages with `role` (system, user, assistant).            |
| **Parameters**       | Control generation (`temperature`, `max_tokens`, etc.).               |
| **Streaming**        | Receive output tokens as they’re generated.                           |
| **Rate Limits**      | API quotas per minute or per day.                                     |
| **API Keys**         | Secret tokens for authentication.                                     |
| **Billing / Quotas** | Pay-as-you-go pricing per token or image.                             |

---

## ⚙️ Example — Chat Completion

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system", "content": "You are an AI coding assistant."},
        {"role": "user", "content": "Write a Python function to reverse a string."}
    ],
    temperature=0.4
)

print(response.choices[0].message.content)
```

---

## ⚙️ Example — Embeddings

```python
embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input="AI connects knowledge across disciplines."
)
vector = embedding.data[0].embedding
print(len(vector))  # e.g. 1536 dimensions
```

---

## 🧱 Common Use Cases

| Category             | Example                                         |
| -------------------- | ----------------------------------------------- |
| **Chatbots**         | Customer support, tutoring, brainstorming bots. |
| **Summarization**    | Reduce long text into concise summaries.        |
| **Code Generation**  | Build AI copilots and auto-refactoring tools.   |
| **Content Creation** | Blog, script, or ad copywriting.                |
| **Embeddings + RAG** | Connect GPT models with your own data.          |
| **Image Generation** | Use DALL·E for creative and branding visuals.   |

---

## 📘 Mini Project

**Goal:** Build a **GPT-Powered FAQ Bot**
**Steps:**

1. Set up an OpenAI API key in `.env`.
2. Create a FastAPI endpoint `/ask`.
3. Send user questions to `chat.completions`.
4. Return and display GPT’s answer in a web interface.

**Expected Outcome:**
A working backend that serves natural-language responses using the OpenAI API.

---

## 🧠 Example Prompt

> “How do temperature and max_tokens affect OpenAI model outputs?”

---

## 🔍 Key Takeaway

The OpenAI API is the **gateway to production-grade intelligence** — giving you direct access to world-class models for text, embeddings, and media generation.

---

## 📚 Further Reading

* [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
* [Chat Completions Guide](https://platform.openai.com/docs/guides/text-generation)
* [Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
* [OpenAI Python SDK](https://github.com/openai/openai-python)
* [OpenAI API Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)