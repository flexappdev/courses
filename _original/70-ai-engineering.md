Excellent — continuing your **AI Engineer 2025 roadmap**, here’s the next one 👇

---

# 🔍 Lesson 70 — AI Explainability & Interpretability (SHAP, LIME, Attention Maps)

### *AI Engineer Roadmap 2025 — Skill #70*

---

## 🎯 Objective

Learn how to **explain and visualize how models make predictions**, ensuring AI systems are transparent, trustworthy, and debuggable — especially in regulated or high-stakes domains.

---

## 🧩 Definition

**Explainability** refers to understanding *how* a model arrives at a decision,
while **interpretability** is about making those insights understandable to humans.
Together, they build trust, enable debugging, and ensure compliance with laws like the **EU AI Act**.

---

## 🧠 Core Concepts

| Concept                                                    | Description                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------------- |
| **Global Explainability**                                  | Understanding how the model works overall.                          |
| **Local Explainability**                                   | Understanding why a model made a specific prediction.               |
| **Feature Importance**                                     | Measuring how each input variable contributes to outcomes.          |
| **SHAP (SHapley Additive exPlanations)**                   | Game-theoretic method for local/global importance.                  |
| **LIME (Local Interpretable Model-agnostic Explanations)** | Approximates model behavior near one instance.                      |
| **Attention Maps**                                         | Visualizing where neural networks “focus” (esp. transformers/CNNs). |
| **Saliency Maps**                                          | Highlight input regions most influencing predictions (images/text). |
| **Counterfactual Explanations**                            | Showing how input changes alter model outcomes.                     |

---

## ⚙️ Example — SHAP for Feature Importance

```python
import shap
import xgboost as xgb
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
model = xgb.XGBClassifier().fit(X, y)

explainer = shap.Explainer(model, X)
shap_values = explainer(X)

shap.summary_plot(shap_values, X)
```

➡️ Generates a **feature importance plot** showing which features most affect predictions.

---

## ⚙️ Example — LIME for Local Explanation

```python
from lime.lime_tabular import LimeTabularExplainer
explainer = LimeTabularExplainer(X, feature_names=feature_names, class_names=["Benign", "Malignant"], discretize_continuous=True)

exp = explainer.explain_instance(X[0], model.predict_proba)
exp.show_in_notebook(show_table=True)
```

➡️ Explains a **single prediction** in a human-readable format.

---

## ⚙️ Example — Attention Visualization for Transformers

```python
from transformers import BertTokenizer, BertModel
import torch
import matplotlib.pyplot as plt

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased", output_attentions=True)

inputs = tokenizer("AI explainability builds trust.", return_tensors="pt")
outputs = model(**inputs)

attn = outputs.attentions[-1][0][0].detach().numpy()
plt.imshow(attn, cmap="hot", interpolation="nearest")
plt.title("Attention Map (Last Layer)")
plt.show()
```

➡️ Visualizes which words the model attends to when generating context.

---

## 🧱 Popular Explainability Tools (2025 Landscape)

| Category                 | Tools                                        |
| ------------------------ | -------------------------------------------- |
| **Model-Agnostic**       | SHAP, LIME, ELI5, Captum                     |
| **Deep Learning**        | Grad-CAM, Integrated Gradients, AttentionViz |
| **Enterprise Platforms** | Fiddler AI, Arize, WhyLabs                   |
| **Governance Docs**      | Model Cards, Explainability Dashboards       |

---

## 📘 Mini Project

**Goal:** Build an **Explainability Dashboard for a Loan Approval Model**
**Steps:**

1. Train an XGBoost or Transformer model.
2. Use SHAP for global + local insights.
3. Visualize results via Plotly or Streamlit dashboard.
4. Export summary as a Model Card (docs + visuals).

**Expected Outcome:**
An explainable ML pipeline with visual feature importance and traceable decision logic — suitable for audit or compliance review.

---

## 🧠 Example Prompt

> “Explain how SHAP differs from LIME in the way they approximate model behavior.”

---

## 🔍 Key Takeaway

Explainability transforms AI from a **black box** into a **glass box** — essential for trust, ethics, and regulatory compliance in 2025 and beyond.

---

## 📚 Further Reading

* [SHAP Documentation](https://shap.readthedocs.io/en/latest/)
* [LIME GitHub Repository](https://github.com/marcotcr/lime)
* [Captum (PyTorch Explainability)](https://captum.ai/)
* [Google’s What-If Tool](https://pair-code.github.io/what-if-tool/)
* [EU AI Act Transparency Requirements](https://artificialintelligenceact.eu/)
* [Explainable AI Playbook (Google Cloud)](https://cloud.google.com/explainable-ai)

---

Would you like me to continue with **Lesson 71 — Causal Inference & Counterfactual Reasoning** next (same 1-page markdown format)?
