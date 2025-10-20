# 📏 Lesson 38 — Model Evaluation Metrics

### *AI Engineer Roadmap 2025 — Skill #38*

---

## 🎯 Objective

Learn how to **measure and interpret model performance** using the right evaluation metrics for classification, regression, clustering, and generative AI tasks — to ensure models are not just accurate, but meaningful.

---

## 🧩 Definition

**Model evaluation** is the process of quantifying how well a model performs on unseen data.
Different tasks (classification, regression, ranking, generation) require **different metrics** to measure predictive power, balance, and real-world effectiveness.

---

## 🧠 Core Concepts

| Category                     | Key Metrics                              | Description                                             |
| ---------------------------- | ---------------------------------------- | ------------------------------------------------------- |
| **Classification**           | Accuracy, Precision, Recall, F1, ROC-AUC | Evaluate correct vs incorrect predictions.              |
| **Regression**               | MSE, MAE, RMSE, R²                       | Measure how far predictions deviate from actual values. |
| **Clustering**               | Silhouette Score, Davies-Bouldin Index   | Assess compactness and separation of clusters.          |
| **Ranking / Recommendation** | MAP, NDCG, Hit@K                         | Measure ranking quality for recommendations.            |
| **Generative Models**        | BLEU, ROUGE, Perplexity                  | Evaluate text quality and fluency.                      |
| **Calibration**              | Brier Score, Reliability Curve           | Assess confidence vs accuracy.                          |
| **Explainability**           | SHAP, LIME                               | Understand feature impact on predictions.               |

---

## ⚙️ Example — Classification Metrics (Scikit-Learn)

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
print("ROC-AUC:", roc_auc_score(y_true, y_pred))
```

---

## ⚙️ Example — Regression Metrics

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

print("MAE:", mean_absolute_error(y_true, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
print("R²:", r2_score(y_true, y_pred))
```

---

## 🧱 Choosing the Right Metric

| Goal                          | Recommended Metric                    |
| ----------------------------- | ------------------------------------- |
| **Balanced classification**   | F1 Score                              |
| **Imbalanced classification** | ROC-AUC, Precision-Recall AUC         |
| **Continuous prediction**     | RMSE, R²                              |
| **Customer ranking / search** | NDCG, MAP                             |
| **Text generation**           | ROUGE-L, BLEU                         |
| **Confidence calibration**    | Brier Score                           |
| **Fairness auditing**         | Equal Opportunity, Demographic Parity |

---

## 📘 Mini Project

**Goal:** Evaluate a **Customer Churn Prediction Model**
**Steps:**

1. Train a logistic regression model.
2. Compute Accuracy, F1, and ROC-AUC.
3. Plot ROC curve and confusion matrix.
4. Interpret which metric best reflects performance for business risk.

**Expected Outcome:**
A clear understanding of how model metrics differ — and which one best represents success for your use case.

---

## 🧠 Example Prompt

> “Why might a model with 95% accuracy still be a poor choice for fraud detection?”

---

## 🔍 Key Takeaway

Choosing the right metric is **as important as choosing the right model** — it defines how success is measured and whether your AI truly works in practice.

---

## 📚 Further Reading

* [Scikit-Learn Metrics Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)
* [Precision-Recall Curves Explained](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)
* [Interpretable ML Book — Christoph Molnar](https://christophm.github.io/interpretable-ml-book/)
* [Google ML Metrics Cheat Sheet](https://developers.google.com/machine-learning/data-prep/construct/evaluation)
* [AI Explainability Tools (SHAP, LIME)](https://shap.readthedocs.io/)