# 🚀 Lesson 29 — Model Deployment on Cloud

### *AI Engineer Roadmap 2025 — Skill #29*

---

## 🎯 Objective

Learn how to **deploy machine learning and AI models to the cloud** so they can be accessed through APIs, web apps, or production systems — ensuring scalability, availability, and real-world usability.

---

## 🧩 Definition

**Model deployment** is the process of taking a trained model and making it available for inference in a live environment.
This is done using **cloud platforms** (AWS, GCP, Azure), **containers** (Docker), or **model serving frameworks** (FastAPI, Streamlit, TensorFlow Serving, or TorchServe).
The goal is to move from **“works on my laptop”** to **“serves millions of requests reliably.”**

---

## 🧠 Core Concepts

| Concept                | Description                                              |
| ---------------------- | -------------------------------------------------------- |
| **Inference Endpoint** | A cloud-hosted API for making model predictions.         |
| **Containerization**   | Packaging the model and environment with Docker.         |
| **Autoscaling**        | Automatically adjusts resources to match traffic.        |
| **Load Balancing**     | Distributes requests evenly across servers.              |
| **CI/CD Pipelines**    | Automate testing and redeployment of new model versions. |
| **Monitoring**         | Track latency, uptime, and model drift.                  |
| **A/B Testing**        | Compare two versions of a model live.                    |
| **Model Registry**     | Centralized version tracking for deployed models.        |

---

## ⚙️ Example — FastAPI Model Deployment (Local → Cloud)

```python
from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    X = [[data["feature1"], data["feature2"]]]
    y_pred = model.predict(X)[0]
    return {"prediction": float(y_pred)}
```

**Deploy using Docker:**

```bash
docker build -t mymodel .
docker run -d -p 8000:8000 mymodel
```

Then push to AWS ECS / GCP Cloud Run / Azure Container Apps.

---

## 🧱 Cloud Deployment Options

| Platform                      | Key Service                              |
| ----------------------------- | ---------------------------------------- |
| **AWS**                       | SageMaker, ECS, Lambda                   |
| **GCP**                       | Vertex AI, Cloud Run                     |
| **Azure**                     | Azure ML, App Service                    |
| **Hugging Face**              | Spaces (for demos)                       |
| **Render / Railway / Fly.io** | Simple low-cost options for smaller APIs |

---

## 📘 Mini Project

**Goal:** Deploy a **Scikit-Learn Prediction API** to the Cloud
**Steps:**

1. Containerize the model using Docker.
2. Push image to a registry (Docker Hub or ECR).
3. Deploy using AWS ECS or GCP Cloud Run.
4. Test endpoint using `curl` or Postman.

**Expected Outcome:**
A live API endpoint that takes JSON input and returns predictions — accessible anywhere.

---

## 🧠 Example Prompt

> “Explain the steps required to move a trained model from a Jupyter Notebook to a production-ready cloud API.”

---

## 🔍 Key Takeaway

Cloud deployment turns your AI prototype into a **real-world service** — reliable, scalable, and ready for integration with web or enterprise systems.

---

## 📚 Further Reading

* [AWS SageMaker Deployment Guide](https://docs.aws.amazon.com/sagemaker/)
* [Google Cloud Run Documentation](https://cloud.google.com/run/docs)
* [Azure ML Model Deployment](https://learn.microsoft.com/en-us/azure/machine-learning/)
* [Docker Deployment Best Practices](https://docs.docker.com/get-started/deploy/)
* [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)