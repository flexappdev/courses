# 🧪 Lesson 58 — Model Training & Experiment Tracking (MLflow, Weights & Biases)

### *AI Engineer Roadmap 2025 — Skill #58*

---

## 🎯 Objective

Learn how to **train, version, and track** machine learning and AI model experiments using frameworks like **MLflow** and **Weights & Biases (W&B)** — ensuring reproducibility, visibility, and performance optimization.

---

## 🧩 Definition

**Model Training** is the process of teaching a model to minimize error by learning from data.
**Experiment Tracking** records **hyperparameters, metrics, and artifacts** across runs, so engineers can compare versions and identify what works best.
This is essential for collaboration and scaling AI development in teams or production pipelines.

---

## 🧠 Core Concepts

| Concept             | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| **Training Loop**   | Repeated forward/backward passes to optimize model weights.  |
| **Loss Function**   | Measures prediction error (e.g., MSE, Cross-Entropy).        |
| **Optimizer**       | Algorithm adjusting weights (Adam, SGD).                     |
| **Hyperparameters** | Tunable configuration variables (learning rate, batch size). |
| **Experiment Run**  | A single model training execution with recorded metadata.    |
| **Model Artifact**  | Saved model checkpoint, plots, or configs.                   |
| **Versioning**      | Keeping track of dataset, code, and parameter versions.      |
| **Dashboarding**    | Visual performance analysis across multiple runs.            |

---

## ⚙️ Example — Simple Training Loop (PyTorch)

```python
import torch, torch.nn as nn, torch.optim as optim

class Net(nn.Module):
    def __init__(self): super().__init__(); self.fc = nn.Linear(10, 1)
    def forward(self, x): return self.fc(x)

model = Net()
optimizer = optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

for epoch in range(5):
    x, y = torch.randn(32, 10), torch.randn(32, 1)
    pred = model(x)
    loss = loss_fn(pred, y)
    optimizer.zero_grad(); loss.backward(); optimizer.step()
    print(f"Epoch {epoch+1}: Loss={loss.item():.4f}")
```

---

## ⚙️ Example — Tracking Experiments with MLflow

```python
import mlflow

mlflow.set_experiment("user_churn_prediction")

with mlflow.start_run():
    lr = 0.01
    mlflow.log_param("learning_rate", lr)
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_artifact("model.pkl")
```

You can view the run dashboard at `http://localhost:5000`.

---

## ⚙️ Example — Tracking with Weights & Biases (W&B)

```python
import wandb

wandb.init(project="text-classifier", config={"lr": 0.001, "epochs": 10})
for epoch in range(10):
    loss = 0.2 / (epoch + 1)
    wandb.log({"epoch": epoch, "loss": loss})
wandb.finish()
```

---

## 🧱 Key Tools & Frameworks

| Tool                       | Type                                                  | Highlights                                       |
| -------------------------- | ----------------------------------------------------- | ------------------------------------------------ |
| **MLflow**                 | Open-source                                           | End-to-end experiment tracking + model registry. |
| **Weights & Biases (W&B)** | Cloud                                                 | Live dashboards, comparisons, and teams.         |
| **Neptune.ai**             | Experiment tracking                                   | Lightweight alternative with metadata tagging.   |
| **Comet.ml**               | Cloud                                                 | ML experiment tracking and collaboration.        |
| **Optuna / Ray Tune**      | Hyperparameter tuning integrated with tracking tools. |                                                  |

---

## 📘 Mini Project

**Goal:** Build a **Training & Tracking Pipeline for Sentiment Classification**
**Steps:**

1. Train a text classifier using a small dataset (IMDb or Yelp).
2. Track hyperparameters and accuracy in MLflow or W&B.
3. Log model artifacts (weights, plots).
4. Compare multiple experiments visually in the dashboard.

**Expected Outcome:**
A reproducible ML pipeline that saves every run, making performance comparison and deployment seamless.

---

## 🧠 Example Prompt

> “What are the main differences between MLflow and Weights & Biases for tracking and versioning AI experiments?”

---

## 🔍 Key Takeaway

Experiment tracking makes your model development **scientific and scalable** — no more lost results or mystery “magic runs.”

---

## 📚 Further Reading

* [MLflow Docs](https://mlflow.org/docs/latest/index.html)
* [Weights & Biases Tutorials](https://docs.wandb.ai/)
* [Neptune.ai Guide](https://docs.neptune.ai/)
* [Ray Tune for Hyperparameter Tuning](https://docs.ray.io/en/latest/tune/index.html)
* [ML Experiment Management Comparison](https://www.comet.com/site/blog/ml-experiment-tracking-tools/)