# 🧩 Lesson 60 — MLOps & Model Monitoring (Drift, Retraining, Pipelines)

### *AI Engineer Roadmap 2025 — Skill #60*

---

## 🎯 Objective

Learn how to manage **Machine Learning Operations (MLOps)** — the discipline of automating, monitoring, and maintaining models in production — ensuring reliability, scalability, and continuous improvement.

---

## 🧩 Definition

**MLOps** extends DevOps principles to machine learning systems, integrating data, model, and deployment workflows.
It ensures that **models stay accurate, explainable, and up-to-date** as data changes over time — through continuous monitoring, retraining, and versioned pipelines.

---

## 🧠 Core Concepts

| Concept                 | Description                                                            |
| ----------------------- | ---------------------------------------------------------------------- |
| **Model Drift**         | Gradual performance degradation due to data or concept change.         |
| **Data Drift**          | Input distribution changes (e.g., new user behavior, market shifts).   |
| **Concept Drift**       | Target relationships evolve (e.g., old patterns no longer apply).      |
| **Pipeline Automation** | End-to-end automation from data ingestion → training → deployment.     |
| **Model Registry**      | Stores model versions, metadata, and lineage.                          |
| **Retraining Strategy** | Scheduled, triggered, or continuous retraining based on drift metrics. |
| **Monitoring Metrics**  | Track latency, accuracy, feature drift, prediction bias.               |
| **CI/CD for ML**        | Automates testing and redeployment when data or models change.         |

---

## ⚙️ Example — Detecting Data Drift

```python
import pandas as pd
from evidently.report import Report
from evidently.metrics import DataDriftPreset

ref = pd.read_csv("data_reference.csv")
cur = pd.read_csv("data_current.csv")

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=cur)
report.save_html("drift_report.html")
```

➡️ Generates a visual drift dashboard showing feature shifts and their statistical significance.

---

## ⚙️ Example — Scheduled Retraining Workflow (Airflow DAG)

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from retrain import train_model, evaluate_model, deploy_model

with DAG("retrain_model", start_date=datetime(2025,1,1), schedule="@weekly") as dag:
    t1 = PythonOperator(task_id="train", python_callable=train_model)
    t2 = PythonOperator(task_id="evaluate", python_callable=evaluate_model)
    t3 = PythonOperator(task_id="deploy", python_callable=deploy_model)
    t1 >> t2 >> t3
```

---

## 🧱 Core MLOps Tools & Frameworks (2025 Overview)

| Category                         | Tools                                          |
| -------------------------------- | ---------------------------------------------- |
| **Workflow Orchestration**       | Airflow, Kubeflow, Prefect, Dagster            |
| **Experiment Tracking**          | MLflow, W&B, Neptune.ai                        |
| **Model Registry**               | MLflow, SageMaker Model Registry, Tecton       |
| **Monitoring & Drift Detection** | Evidently, Arize AI, Fiddler AI, WhyLabs       |
| **Pipeline Management**          | Kubeflow Pipelines, Vertex AI Pipelines, ZenML |
| **CI/CD Integration**            | GitHub Actions, Jenkins, GitLab CI             |
| **Cloud Platforms**              | AWS SageMaker, Azure ML, GCP Vertex AI         |

---

## 📘 Mini Project

**Goal:** Create a **Model Drift Monitoring & Auto-Retraining Pipeline**
**Steps:**

1. Train a model and save baseline metrics.
2. Monitor live predictions vs new data weekly.
3. Trigger retraining automatically if drift > 10%.
4. Log results to MLflow and redeploy latest model version.

**Expected Outcome:**
A self-healing AI pipeline that monitors model health and retrains automatically when performance declines.

---

## 🧠 Example Prompt

> “How do you distinguish between data drift and concept drift, and how should your MLOps pipeline respond to each?”

---

## 🔍 Key Takeaway

MLOps keeps your AI **alive and adaptive** — blending software reliability with machine learning agility to sustain production-grade intelligence.

---

## 📚 Further Reading

* [Evidently AI Drift Detection Docs](https://docs.evidentlyai.com/)
* [Google Cloud Vertex AI MLOps Guide](https://cloud.google.com/vertex-ai/docs/mlops)
* [AWS SageMaker Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
* [Kubeflow Pipelines Overview](https://www.kubeflow.org/docs/components/pipelines/)
* [Full Stack Deep Learning — MLOps](https://fullstackdeeplearning.com/)