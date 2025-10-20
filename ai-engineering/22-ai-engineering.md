# 🧮 Lesson 22 — Vector Databases (Pinecone, FAISS)

### *AI Engineer Roadmap 2025 — Skill #22*

---

## 🎯 Objective

Learn how to **store, search, and retrieve embeddings efficiently** using specialized **vector databases** — essential for Retrieval-Augmented Generation (RAG), semantic search, and AI memory systems.

---

## 🧩 Definition

A **Vector Database** stores high-dimensional embedding vectors and enables **similarity search** (finding items with meaning closest to a query).
Unlike SQL or NoSQL databases, vector DBs are optimized for **cosine similarity, dot product, or Euclidean distance**, making them ideal for AI-driven search and reasoning.

---

## 🧠 Core Concepts

| Concept                                | Description                                                       |
| -------------------------------------- | ----------------------------------------------------------------- |
| **Vector Index**                       | Data structure optimized for fast similarity search.              |
| **Similarity Metrics**                 | Cosine, dot product, or Euclidean distance.                       |
| **Dimensionality Reduction**           | Techniques like PCA to optimize space.                            |
| **Approximate Nearest Neighbor (ANN)** | Balances accuracy and speed for large datasets.                   |
| **Metadata Storage**                   | Combine embeddings with descriptive info.                         |
| **Batch Upserts**                      | Add or update multiple vectors efficiently.                       |
| **Index Refresh / Rebuild**            | Recreate the index when model or data updates.                    |
| **Scalability**                        | Distribute vector indexes across nodes for large-scale retrieval. |

---

## ⚙️ Example — Using **Pinecone**

```python
import pinecone
from openai import OpenAI

# Init
pinecone.init(api_key="YOUR_PINECONE_KEY")
index = pinecone.Index("ai-knowledge")

# Create embedding
client = OpenAI(api_key="YOUR_OPENAI_KEY")
embed = client.embeddings.create(model="text-embedding-3-small", input="AI connects ideas.")

# Upsert
index.upsert([("doc1", embed.data[0].embedding)])

# Query
results = index.query(vector=embed.data[0].embedding, top_k=3, include_metadata=True)
print(results)
```

---

## ⚙️ Example — Using **FAISS (Local)**

```python
import faiss
import numpy as np

vectors = np.random.rand(1000, 1536).astype('float32')
index = faiss.IndexFlatL2(1536)
index.add(vectors)

query = np.random.rand(1, 1536).astype('float32')
distances, ids = index.search(query, 5)
print(ids)
```

---

## 🧱 Common Vector Databases

| Database         | Key Features                                     |
| ---------------- | ------------------------------------------------ |
| **Pinecone**     | Managed, serverless, scalable vector DB for RAG. |
| **FAISS (Meta)** | Local, GPU-optimized similarity search.          |
| **Weaviate**     | Open-source, schema-based semantic search.       |
| **Milvus**       | Enterprise-grade, cloud-friendly vector engine.  |
| **Chroma**       | Developer-friendly local DB for LangChain apps.  |

---

## 📘 Mini Project

**Goal:** Build a **Local Vector Search Demo**
**Steps:**

1. Generate embeddings for 50 text snippets.
2. Store them in FAISS or Chroma.
3. Input a query and return top 3 most similar snippets.
4. Display similarity scores and metadata.

**Expected Outcome:**
A simple semantic search system using a vector index — the foundation of RAG pipelines.

---

## 🧠 Example Prompt

> “Explain why vector databases are more suitable than SQL databases for semantic search.”

---

## 🔍 Key Takeaway

Vector databases are the **memory banks of AI systems** — enabling semantic retrieval, contextual recall, and the intelligent grounding of LLMs.

---

## 📚 Further Reading

* [Pinecone Docs](https://docs.pinecone.io/)
* [FAISS GitHub Repository](https://github.com/facebookresearch/faiss)
* [Weaviate Documentation](https://weaviate.io/developers/weaviate)
* [Chroma DB Guide](https://docs.trychroma.com/)
* [Milvus Vector Database](https://milvus.io/)