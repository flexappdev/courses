# ☁️ Lesson 12 — Cloud Platforms (AWS / GCP / Azure)

### *AI Engineer Roadmap 2025 — Skill #12*

---

## 🎯 Objective

Learn how to **build, train, and deploy AI models on the cloud** — using managed compute, storage, and ML services from Amazon, Google, and Microsoft.

---

## 🧩 Definition

**Cloud Platforms** provide scalable infrastructure for AI development.
Instead of running models locally, you can use virtual machines (EC2), managed databases (RDS, Firestore), and dedicated AI services (SageMaker, Vertex AI, Azure ML) — all optimized for compute-heavy workloads.

---

## 🧠 Core Concepts

| Concept                                | Description                                            |
| -------------------------------------- | ------------------------------------------------------ |
| **Compute Instances**                  | Virtual servers (AWS EC2, GCP Compute Engine).         |
| **Storage Services**                   | Object and file storage (S3, Cloud Storage, Blob).     |
| **Serverless Computing**               | On-demand functions (Lambda, Cloud Functions).         |
| **Managed ML Services**                | Prebuilt tools for model training and deployment.      |
| **IAM (Identity & Access Management)** | Secure user and key permissions.                       |
| **Networking**                         | VPCs, load balancers, and endpoints for communication. |
| **Monitoring & Logging**               | CloudWatch, Stackdriver, Azure Monitor.                |

---

## 🧱 AI-Specific Services

| Platform  | Core AI Services                                           |
| --------- | ---------------------------------------------------------- |
| **AWS**   | SageMaker, Bedrock, Comprehend, Rekognition                |
| **GCP**   | Vertex AI, AutoML, Gemini API, BigQuery ML                 |
| **Azure** | Azure Machine Learning, Cognitive Services, OpenAI Service |

---

## ⚙️ Example: Deploy a Model on AWS SageMaker

```python
import sagemaker
from sagemaker import get_execution_role

session = sagemaker.Session()
role = get_execution_role()

model = sagemaker.sklearn.model.SKLearnModel(
    model_data='s3://my-bucket/model.tar.gz',
    role=role,
    framework_version='1.2-1'
)
predictor = model.deploy(instance_type='ml.t2.medium', initial_instance_count=1)
```

---

## 📘 Mini Project

**Goal:** Deploy a **Machine Learning Model on the Cloud**
**Steps:**

1. Train a simple model locally (e.g., Scikit-Learn).
2. Upload the model file to S3 (or equivalent).
3. Use SageMaker / Vertex AI to host it as an endpoint.
4. Test the API using `requests.post()`.

**Expected Outcome:**
A live model endpoint accessible via API — scalable, monitored, and ready for production use.

---

## 🧠 Example Prompt

> “Compare AWS SageMaker, Google Vertex AI, and Azure ML — which is best for end-to-end AI development?”

---

## 🔍 Key Takeaway

Cloud platforms are the **AI engineer’s supercomputers** — offering scalable compute, data pipelines, and integrated ML workflows at your fingertips.

---

## 📚 Further Reading

* [AWS SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/)
* [Google Vertex AI Docs](https://cloud.google.com/vertex-ai/docs)
* [Azure Machine Learning Service](https://learn.microsoft.com/en-us/azure/machine-learning/)
* [Cloud Cost Optimization for AI](https://aws.amazon.com/architecture/cost-optimization/)