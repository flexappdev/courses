# 🧭 Lesson 53 — Vector Databases & Semantic Search (FAISS, Pinecone, Weaviate, Chroma)

### *AI Engineer Roadmap 2025 — Skill #53*

---

## 🎯 Objective

Learn how to use **vector databases** and **semantic search** to store, query, and retrieve information based on **meaning** rather than keywords — the foundation for RAG, memory, and context-aware AI systems.

---

## 🧩 Definition

A **vector database** stores data as **embeddings** — numerical representations of meaning — and allows fast **similarity search** to find the most relevant items to a user query.
This is how modern AI systems perform semantic search, document retrieval, recommendation, and memory recall.

---

## 🧠 Core Concepts

| Concept                | Description                                                                     |
| ---------------------- | ------------------------------------------------------------------------------- |
| **Embedding**          | A dense vector representation of text, images, or audio in n-dimensional space. |
| **Vector Index**       | Data structure for fast nearest-neighbor lookups.                               |
| **Similarity Metrics** | Methods like cosine similarity or dot product to measure vector closeness.      |
| **Semantic Search**    | Retrieves items that *mean* the same, not just *sound* the same.                |
| **Chunking**           | Breaking documents into embedding-friendly segments.                            |
| **Upsert**             | Insert or update existing embeddings.                                           |
| **Metadata Filtering** | Filter search results based on tags, source, or author.                         |
| **Scalability**        | Vector DBs are optimized for billions of embeddings across clusters.            |

---

## ⚙️ Example — FAISS Semantic Search

```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

sentences = [
    "AI is transforming education.",
    "Neural networks are powerful.",
    "Reinforcement learning improves agents."
]

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(sentences)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

query = model.encode(["How does AI impact schools?"])
_, I = index.search(np.array(query), k=1)
print("Most similar sentence:", sentences[I[0][0]])
```

---

## ⚙️ Example — Pinecone Cloud Integration

```python
import pinecone
from openai import OpenAI
client = OpenAI()

pinecone.init(api_key="YOUR_API_KEY", environment="us-west1-gcp")
index = pinecone.Index("semantic-search")

query_embedding = client.embeddings.create(input="AI education trends", model="text-embedding-3-large").data[0].embedding
results = index.query(vector=query_embedding, top_k=3, include_metadata=True)
print(results)
```

---

## 🧱 Popular Vector Databases

| Database         | Strength                                                         |
| ---------------- | ---------------------------------------------------------------- |
| **FAISS (Meta)** | Local, open-source, ultra-fast search engine.                    |
| **Pinecone**     | Fully managed cloud vector service with APIs and filtering.      |
| **Weaviate**     | Graph-aware vector DB with hybrid search and schema support.     |
| **Chroma**       | Developer-friendly local vector store integrated with LangChain. |
| **Milvus**       | Scalable open-source alternative used in enterprise RAG systems. |

---

## 📘 Mini Project

**Goal:** Build a **Semantic Knowledge Search App**
**Steps:**

1. Split PDFs or text files into 500-token chunks.
2. Generate embeddings via OpenAI or SentenceTransformers.
3. Store them in FAISS or Pinecone.
4. Implement a semantic search API that retrieves top results by meaning.

**Expected Outcome:**
An intelligent search engine that understands context, not just keywords — perfect for RAG, chatbots, or enterprise document search.

---

## 🧠 Example Prompt

> “Why does cosine similarity work better than Euclidean distance for semantic retrieval?”

---

## 🔍 Key Takeaway

Vector databases give AI **memory and context** — they make knowledge searchable, meaningful, and instantly retrievable at scale.

---

## 📚 Further Reading

* [FAISS Documentation (Meta AI)](https://faiss.ai/)
* [Pinecone Developer Guide](https://docs.pinecone.io/)
* [Weaviate Vector Search](https://weaviate.io/developers/weaviate)
* [Chroma Docs (LangChain)](https://docs.trychroma.com/)
* [Milvus Open Source DB](https://milvus.io/docs)
* [OpenAI Embeddings Overview](https://platform.openai.com/docs/guides/embeddings)