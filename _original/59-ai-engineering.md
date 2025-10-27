# 🚀 Lesson 59 — Model Deployment & Serving (FastAPI, Docker, CI/CD)

### *AI Engineer Roadmap 2025 — Skill #59*

---

## 🎯 Objective

Learn how to **deploy machine learning models into production** using **FastAPI**, **Docker**, and **CI/CD pipelines**, ensuring scalability, version control, and reliable inference for end-users or applications.

---

## 🧩 Definition

**Model Deployment** is the process of taking a trained model and making it accessible via an API or web service.
**Serving** refers to running that model in a production environment where users, apps, or other systems can query it in real time.
By combining **FastAPI** (for endpoints), **Docker** (for packaging), and **CI/CD** (for automation), you create a fully reproducible AI service pipeline.

---

## 🧠 Core Concepts

| Concept              | Description                                                           |
| -------------------- | --------------------------------------------------------------------- |
| **Inference**        | Running the trained model to generate predictions.                    |
| **FastAPI**          | Lightweight Python web framework for serving ML models via REST APIs. |
| **Containerization** | Packaging code + dependencies into an isolated environment (Docker).  |
| **CI/CD**            | Automating testing, building, and deployment to production.           |
| **Model Registry**   | Central storage for versioned models (MLflow, S3, Hugging Face Hub).  |
| **Load Balancing**   | Distributing requests across multiple replicas for scale.             |
| **Monitoring**       | Tracking latency, errors, and data drift in production.               |
| **Rollback**         | Restoring to a previous model version if an update fails.             |

---

## ⚙️ Example — Serving a Model with FastAPI

```python
from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return {"prediction": str(prediction)}
```

Run with:

```bash
uvicorn main:app --reload
```

---

## ⚙️ Example — Dockerfile for Model Deployment

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t ai-model-api .
docker run -p 8000:8000 ai-model-api
```

---

## ⚙️ Example — GitHub Actions CI/CD Workflow

```yaml
name: Deploy Model API
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker image
        run: docker build -t model-api .
      - name: Push to Registry
        run: docker push user/model-api:latest
      - name: Deploy to Server
        run: ssh ubuntu@server "docker pull user/model-api && docker restart model-api"
```

---

## 🧱 Deployment Stacks (2025 Overview)

| Tool                                     | Purpose                           |
| ---------------------------------------- | --------------------------------- |
| **FastAPI / Flask**                      | Python APIs for model serving.    |
| **Docker / Podman**                      | Containerization for portability. |
| **Kubernetes**                           | Scaling and orchestration.        |
| **GitHub Actions / GitLab CI / Jenkins** | CI/CD automation.                 |
| **AWS EC2 / Lambda / SageMaker**         | Cloud deployment.                 |
| **Hugging Face Inference API**           | Hosted model deployment.          |
| **Vercel / Render / Fly.io**             | Quick edge deployments.           |

---

## 📘 Mini Project

**Goal:** Deploy a **Customer Churn Prediction Model**
**Steps:**

1. Export a trained `model.pkl`.
2. Create FastAPI endpoint `/predict`.
3. Containerize with Docker.
4. Automate deployment using GitHub Actions to an EC2 instance.

**Expected Outcome:**
A live REST API that takes JSON input, runs inference, and returns predictions in real time — automatically redeploying on new pushes.

---

## 🧠 Example Prompt

> “What’s the difference between batch inference and real-time inference, and when would you use each?”

---

## 🔍 Key Takeaway

Deployment turns your model from a **notebook experiment** into a **real-world AI product** — CI/CD keeps it alive, consistent, and scalable.

---

## 📚 Further Reading

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Docker Official Guide](https://docs.docker.com/get-started/)
* [MLflow Model Serving](https://mlflow.org/docs/latest/models.html)
* [GitHub Actions CI/CD](https://docs.github.com/en/actions)
* [AWS SageMaker Deployment Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms.html)
* [Full Stack Deep Learning: Deployment Chapter](https://fullstackdeeplearning.com/)