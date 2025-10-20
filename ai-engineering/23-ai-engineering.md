# 🧠 Lesson 23 — Retrieval-Augmented Generation (RAG)

### *AI Engineer Roadmap 2025 — Skill #23*

---

## 🎯 Objective

Learn how to **combine external knowledge retrieval with large language model (LLM) generation** to create accurate, up-to-date, and context-aware AI systems — the foundation of modern enterprise chatbots and knowledge assistants.

---

## 🧩 Definition

**Retrieval-Augmented Generation (RAG)** is a hybrid AI framework that improves LLM performance by first **retrieving relevant information** from a knowledge base (e.g., vector database) and then **generating a response** based on that context.
It bridges the gap between **static model knowledge** and **dynamic real-world data**.

---

## 🧠 Core Concepts

| Concept                | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **Retriever**          | Searches for relevant context (using embeddings & similarity search). |
| **Generator**          | The LLM that produces a final response using the retrieved context.   |
| **Knowledge Base**     | Source of truth — documents, PDFs, or structured data.                |
| **Context Window**     | The amount of information an LLM can handle per query.                |
| **Chunking**           | Splitting documents into manageable text segments for embedding.      |
| **Reranking**          | Reordering retrieved chunks based on semantic importance.             |
| **Grounded Responses** | Answers that directly cite or rely on source data.                    |
| **Evaluation**         | Assessing factual accuracy and relevance.                             |

---

## ⚙️ Example — Simple RAG Pipeline (Python)

```python
from openai import OpenAI
import faiss, numpy as np

client = OpenAI(api_key="YOUR_API_KEY")
index = faiss.IndexFlatL2(1536)

# 1️⃣ Create embeddings for stored text
texts = ["AI connects data.", "RAG improves accuracy."]
embeds = [client.embeddings.create(model="text-embedding-3-small", input=t).data[0].embedding for t in texts]
index.add(np.array(embeds).astype('float32'))

# 2️⃣ Query + retrieve
query = "How does RAG help LLMs?"
q_embed = client.embeddings.create(model="text-embedding-3-small", input=query).data[0].embedding
distances, ids = index.search(np.array([q_embed]).astype('float32'), 1)

# 3️⃣ Generate answer with context
context = texts[ids[0][0]]
prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
response = client.chat.completions.create(model="gpt-4-turbo", messages=[{"role": "user", "content": prompt}])
print(response.choices[0].message.content)
```

---

## 🧱 Architecture Overview

1. **Input → Embedding → Retrieval (Vector DB)**
2. **Top-k Contexts → LLM Prompt → Output**
3. **Optional Post-Processing → Logging / Storage**

---

## 🧱 Tools & Frameworks

| Category          | Tools                                   |
| ----------------- | --------------------------------------- |
| **Retrievers**    | FAISS, Pinecone, Weaviate, Chroma       |
| **Frameworks**    | LangChain, LlamaIndex, Haystack         |
| **LLM APIs**      | OpenAI, Anthropic, Gemini, Hugging Face |
| **Orchestration** | FastAPI, Streamlit, CrewAI Agents       |

---

## 📘 Mini Project

**Goal:** Build a **Local RAG Q&A App**
**Steps:**

1. Store 20–50 short text documents.
2. Generate embeddings and store them in FAISS.
3. Accept user questions via an input box.
4. Retrieve top 3 matches and pass to the LLM for a grounded answer.

**Expected Outcome:**
An interactive, context-aware assistant that accurately answers based on local documents — no hallucinations.

---

## 🧠 Example Prompt

> “Explain how Retrieval-Augmented Generation improves factual accuracy in large language models.”

---

## 🔍 Key Takeaway

RAG is the **brain + memory fusion** of modern AI — combining **LLM reasoning** with **retrieved facts** to produce trustworthy, contextual, and verifiable outputs.

---

## 📚 Further Reading

* [OpenAI RAG Guide](https://platform.openai.com/docs/guides/retrieval)
* [LangChain RAG Documentation](https://python.langchain.com/docs/use_cases/question_answering/)
* [LlamaIndex Tutorials](https://gpt-index.readthedocs.io/)
* [Pinecone RAG Examples](https://docs.pinecone.io/docs/retrieval-augmented-generation)