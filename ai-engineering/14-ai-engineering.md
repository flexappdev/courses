# ⚡ Lesson 14 — FastAPI / Flask Basics

### *AI Engineer Roadmap 2025 — Skill #14*

---

## 🎯 Objective

Learn how to **turn your machine learning models into APIs** using lightweight Python frameworks like **FastAPI** and **Flask** — to serve predictions and integrate with other systems.

---

## 🧩 Definition

**FastAPI** and **Flask** are Python web frameworks for building APIs quickly.

* **Flask** is simple, flexible, and minimal — great for quick prototypes.
* **FastAPI** is modern, asynchronous, and built for high performance — ideal for production-grade AI apps.

---

## 🧠 Core Concepts

| Concept                  | Description                                                     |
| ------------------------ | --------------------------------------------------------------- |
| **Route / Endpoint**     | URL path where a function is exposed (`/predict`).              |
| **Request / Response**   | Client sends data → Server returns a prediction.                |
| **HTTP Methods**         | `GET`, `POST`, `PUT`, `DELETE`.                                 |
| **JSON Payloads**        | Common data format for APIs.                                    |
| **Dependency Injection** | FastAPI method for managing model or DB loading.                |
| **Async Functions**      | Non-blocking endpoints for performance.                         |
| **Middleware**           | Code that runs before/after each request (e.g., logging, auth). |

---

## ⚙️ Example (FastAPI)

```python
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    prediction = model.predict([[data["x1"], data["x2"]]])[0]
    return {"prediction": float(prediction)}
```

Run with:

```bash
uvicorn main:app --reload
```

---

## ⚙️ Example (Flask)

```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    pred = model.predict([[data['x1'], data['x2']]])[0]
    return jsonify({"prediction": float(pred)})

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🧱 Use Cases in AI Engineering

| Use Case                | Example                                            |
| ----------------------- | -------------------------------------------------- |
| **Model Serving**       | Expose trained ML models via `/predict` endpoint.  |
| **Dashboard Backends**  | Serve AI data to frontends (React, Streamlit).     |
| **MLOps Integration**   | Deploy APIs inside Docker for reproducibility.     |
| **Agent Communication** | Let AI agents call backend routes.                 |
| **Microservices**       | Break large AI systems into smaller scalable APIs. |

---

## 📘 Mini Project

**Goal:** Build a **Prediction API with FastAPI**
**Steps:**

1. Train a simple regression model in Python.
2. Save it as `model.pkl` using `joblib`.
3. Build `/predict` route in FastAPI.
4. Test with `curl` or Postman.

**Expected Outcome:**
A fully working API returning predictions from a trained model.

---

## 🧠 Example Prompt

> “Explain the difference between FastAPI and Flask for deploying machine learning models.”

---

## 🔍 Key Takeaway

FastAPI and Flask are the **bridges between your models and the world** — turning offline notebooks into real, interactive AI applications.

---

## 📚 Further Reading

* [FastAPI Official Docs](https://fastapi.tiangolo.com/)
* [Flask Documentation](https://flask.palletsprojects.com/)
* [Uvicorn ASGI Server](https://www.uvicorn.org/)
* [FastAPI + Docker Tutorial](https://testdriven.io/blog/fastapi-docker/)