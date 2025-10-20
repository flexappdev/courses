# 🤖 Lesson 2 — Machine Learning Basics

### *AI Engineer Roadmap 2025 — Skill #2*

---

## 🎯 Objective

Learn the **core principles of Machine Learning (ML)** — how algorithms learn from data, make predictions, and improve over time.

---

## 🧩 Definition

**Machine Learning** is the science of teaching computers to learn from data instead of being explicitly programmed.
It’s the foundation of most modern AI applications — from spam filters and recommendation engines to autonomous vehicles and LLM pretraining.

---

## 🧠 Core Concepts

| Concept                    | Description                                                                    |
| -------------------------- | ------------------------------------------------------------------------------ |
| **Supervised Learning**    | Model learns from labeled data (input → output mapping).                       |
| **Unsupervised Learning**  | Model finds patterns in unlabeled data (clustering, dimensionality reduction). |
| **Reinforcement Learning** | Model learns through trial and reward (agents, environments).                  |
| **Feature Engineering**    | Selecting and transforming variables to improve learning.                      |
| **Evaluation Metrics**     | Accuracy, Precision, Recall, F1 Score, ROC-AUC.                                |

---

## 🛠️ Common Algorithms

| Type                         | Algorithms                                             |
| ---------------------------- | ------------------------------------------------------ |
| **Regression**               | Linear Regression, Ridge, Lasso                        |
| **Classification**           | Logistic Regression, Decision Tree, Random Forest, SVM |
| **Clustering**               | K-Means, DBSCAN                                        |
| **Dimensionality Reduction** | PCA, t-SNE                                             |
| **Neural Networks**          | MLP, CNN, RNN (bridge to Deep Learning)                |

---

## ⚙️ Tech Stack Example

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('housing.csv')
X = data[['sqft', 'bedrooms']]
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression().fit(X_train, y_train)
print("Model R²:", model.score(X_test, y_test))
```

---

## 📘 Mini Project

**Goal:** Build a simple **House Price Predictor**
**Steps:**

1. Load a CSV dataset (features: sqft, bedrooms, location, price)
2. Train a regression model using Scikit-Learn
3. Predict prices for unseen data
4. Visualize predictions with Matplotlib

**Expected Outcome:**
A baseline ML model predicting numeric values with minimal preprocessing.

---

## 🧠 Example Prompt

> “Summarize the difference between supervised, unsupervised, and reinforcement learning in 100 words.”

---

## 🔍 Key Takeaway

Machine Learning is about **patterns, not rules** — models infer relationships from data and continuously improve through iteration and feedback.

---

## 📚 Further Reading

* [Scikit-Learn User Guide](https://scikit-learn.org/stable/user_guide.html)
* [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course)
* [DeepLearning.AI — Intro to ML](https://www.deeplearning.ai/short-courses/)