# 🗄️ Lesson 15 — Working with Databases (SQL & NoSQL)

### *AI Engineer Roadmap 2025 — Skill #15*

---

## 🎯 Objective

Learn how to **store, query, and manage data** efficiently using both **SQL (structured)** and **NoSQL (unstructured)** databases — essential for feeding, logging, and scaling AI systems.

---

## 🧩 Definition

A **database** is a structured way to store and retrieve information.
AI engineers use databases to manage **training data**, **model metadata**, **user logs**, and **app content**.

* **SQL** (e.g., PostgreSQL, MySQL) is best for relational, structured data.
* **NoSQL** (e.g., MongoDB, Firebase) is best for flexible, document-based data (JSON).

---

## 🧠 Core Concepts

| Concept                              | Description                                                      |
| ------------------------------------ | ---------------------------------------------------------------- |
| **Tables / Collections**             | Where data is stored.                                            |
| **Records / Documents**              | Individual rows (SQL) or JSON entries (NoSQL).                   |
| **Queries**                          | Commands to retrieve or update data.                             |
| **Indexes**                          | Speed up searches.                                               |
| **Relationships**                    | Linking tables in SQL (1:1, 1:N, N:M).                           |
| **Transactions**                     | Ensure consistent updates.                                       |
| **ORMs (Object-Relational Mappers)** | Tools like SQLAlchemy or Prisma for easier database interaction. |

---

## ⚙️ SQL Example (PostgreSQL)

```python
import psycopg2

conn = psycopg2.connect(database="ai_db", user="user", password="pass", host="localhost")
cur = conn.cursor()

cur.execute("SELECT * FROM users WHERE active = TRUE;")
rows = cur.fetchall()
for row in rows:
    print(row)
```

---

## ⚙️ NoSQL Example (MongoDB)

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ai_db"]
collection = db["predictions"]

collection.insert_one({"user": "mat", "result": 0.87})
for doc in collection.find():
    print(doc)
```

---

## 🧱 Use Cases in AI Engineering

| Use Case                  | Example                                         |
| ------------------------- | ----------------------------------------------- |
| **Training Data Storage** | Keep labeled datasets in MongoDB or PostgreSQL. |
| **Model Metadata**        | Log model versions and parameters.              |
| **User Interaction Logs** | Save API calls or chatbot messages.             |
| **RAG Pipelines**         | Use vector databases (like Pinecone or FAISS).  |
| **Analytics Dashboards**  | Query results for visualization in dashboards.  |

---

## 📘 Mini Project

**Goal:** Build a **Prediction Log Database**
**Steps:**

1. Create a MongoDB collection called `predictions`.
2. After every API call, log the user input, timestamp, and model result.
3. Build a FastAPI route `/logs` to display the last 10 entries.
4. Test locally and visualize results.

**Expected Outcome:**
A working local or cloud database storing model predictions and user data.

---

## 🧠 Example Prompt

> “When would you use MongoDB instead of PostgreSQL in an AI project?”

---

## 🔍 Key Takeaway

Databases are the **memory layer** of AI systems — storing the data your models learn from and the insights they generate.

---

## 📚 Further Reading

* [PostgreSQL Docs](https://www.postgresql.org/docs/)
* [MongoDB Developer Guide](https://www.mongodb.com/developer/)
* [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
* [Firebase Firestore Overview](https://firebase.google.com/docs/firestore)