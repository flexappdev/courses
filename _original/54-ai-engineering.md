# 🕸️ Lesson 54 — Knowledge Graphs & Hybrid Search

### *AI Engineer Roadmap 2025 — Skill #54*

---

## 🎯 Objective

Learn how to **combine structured and unstructured data** using **Knowledge Graphs (KGs)** and **Hybrid Search** — enabling AI systems to reason with both *semantic meaning* and *explicit relationships* for smarter, context-aware retrieval.

---

## 🧩 Definition

A **Knowledge Graph** is a network of **entities (nodes)** and **relationships (edges)** that encodes facts about the world — e.g., *“Einstein → discovered → Theory of Relativity.”*
**Hybrid Search** merges **symbolic (graph/keyword)** and **neural (vector)** retrieval to improve precision, recall, and explainability.

---

## 🧠 Core Concepts

| Concept                 | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| **Entity**              | A real-world object, concept, or person (e.g., “Einstein”). |
| **Relationship (Edge)** | How two entities are connected (e.g., “discovered”).        |
| **Triple**              | A (Subject, Predicate, Object) unit in RDF/OWL format.      |
| **Ontology**            | Schema defining allowed entity and relationship types.      |
| **Graph Embeddings**    | Vectorizing graph nodes for semantic similarity.            |
| **Hybrid Retrieval**    | Combines vector similarity + symbolic constraints.          |
| **SPARQL**              | Query language for graph databases.                         |
| **Semantic Reasoning**  | Inferring new facts from existing graph structures.         |

---

## ⚙️ Example — Create & Query a Simple Knowledge Graph

```python
import networkx as nx

G = nx.DiGraph()
G.add_edge("Einstein", "Theory of Relativity", relation="discovered")
G.add_edge("Theory of Relativity", "Physics", relation="belongs_to")

for u, v, data in G.edges(data=True):
    print(f"{u} -> {data['relation']} -> {v}")
```

---

## ⚙️ Example — Hybrid Search (Graph + Embeddings)

```python
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
entities = ["Einstein", "Newton", "Quantum Mechanics", "Theory of Relativity"]

query = "Who worked on relativity?"
query_emb = model.encode(query, convert_to_tensor=True)
entity_embs = model.encode(entities, convert_to_tensor=True)

scores = util.pytorch_cos_sim(query_emb, entity_embs)
best_match = entities[scores.argmax()]
print("Best match:", best_match)
```

Then combine with **graph traversal** to infer related knowledge (e.g., `Einstein → Theory of Relativity → Physics`).

---

## 🧱 Knowledge Graph Tools

| Tool                         | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| **Neo4j**                    | Leading graph database with Cypher query language. |
| **RDFLib**                   | Python library for RDF triples and SPARQL queries. |
| **TigerGraph**               | Enterprise-grade graph engine for large-scale KGs. |
| **GraphDB (Ontotext)**       | Semantic web-focused triple store.                 |
| **Weaviate Hybrid Search**   | Combines vector + graph + keyword search natively. |
| **LangChain GraphRetriever** | Integrates graph reasoning into LLM workflows.     |

---

## 📘 Mini Project

**Goal:** Build a **Hybrid Knowledge Graph for Company Data**
**Steps:**

1. Define entities (employees, projects, clients).
2. Add edges (e.g., “works_on”, “reports_to”).
3. Embed entity descriptions for semantic search.
4. Implement hybrid search combining text embeddings + graph traversal.

**Expected Outcome:**
A system that can answer queries like *“Who manages AI projects for European clients?”* by combining structured graph facts with semantic similarity.

---

## 🧠 Example Prompt

> “Why are hybrid retrieval systems more accurate than pure vector search in enterprise AI applications?”

---

## 🔍 Key Takeaway

Knowledge graphs bring **structure and reasoning**, while vector search adds **context and meaning** — hybrid systems merge both to create truly intelligent retrieval engines.

---

## 📚 Further Reading

* [Neo4j Graph Database Docs](https://neo4j.com/docs/)
* [Weaviate Hybrid Search Overview](https://weaviate.io/blog/hybrid-search)
* [RDFLib Python Library](https://rdflib.readthedocs.io/)
* [Stanford Knowledge Graphs Course](https://web.stanford.edu/class/cs520/)
* [LangChain GraphRetriever Docs](https://python.langchain.com/docs/integrations/retrievers/graph)