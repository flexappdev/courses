# 🧮 Lesson 35 — Feature Engineering for Machine Learning

### *AI Engineer Roadmap 2025 — Skill #35*

---

## 🎯 Objective

Learn how to **transform raw data into meaningful features** that improve model accuracy, interpretability, and generalization — the secret weapon of top AI engineers.

---

## 🧩 Definition

**Feature Engineering** is the process of creating, selecting, and transforming input variables (features) from raw data to improve a model’s predictive power.
It bridges the gap between **data collection** and **model training**, often determining the difference between an average and world-class AI model.

---

## 🧠 Core Concepts

| Concept                    | Description                                                           |
| -------------------------- | --------------------------------------------------------------------- |
| **Feature Creation**       | Deriving new variables (e.g., `price_per_item = revenue / quantity`). |
| **Feature Transformation** | Normalizing, encoding, or scaling inputs.                             |
| **Feature Selection**      | Choosing the most relevant features to reduce noise.                  |
| **Categorical Encoding**   | One-hot, label, or target encoding.                                   |
| **Numerical Scaling**      | Standardization (Z-score), MinMax scaling.                            |
| **Temporal Features**      | Extracting time-based data (hour, weekday, season).                   |
| **Text Features**          | TF-IDF, bag-of-words, embeddings.                                     |
| **Feature Importance**     | Using SHAP or permutation importance to interpret contributions.      |

---

## ⚙️ Example — Basic Feature Engineering in Python

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.read_csv("sales.csv")

# Create new features
df["price_per_item"] = df["revenue"] / (df["quantity"] + 1)

# Scale numerical data
scaler = StandardScaler()
df["revenue_scaled"] = scaler.fit_transform(df[["revenue"]])

# Encode categorical data
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df[["region"]])
df_encoded = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(["region"]))

df_final = pd.concat([df, df_encoded], axis=1)
print(df_final.head())
```

---

## ⚙️ Example — Feature Importance with Random Forest

```python
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

model = RandomForestClassifier().fit(X_train, y_train)
importances = model.feature_importances_

plt.barh(X_train.columns, importances)
plt.title("Feature Importance")
plt.show()
```

---

## 🧱 Advanced Techniques

| Category                            | Example                                                    |
| ----------------------------------- | ---------------------------------------------------------- |
| **Polynomial Features**             | Create non-linear relationships.                           |
| **Binning**                         | Group continuous data into ranges.                         |
| **Feature Interaction**             | Combine columns to expose dependencies.                    |
| **Dimensionality Reduction**        | PCA, t-SNE, or UMAP for visualization and compression.     |
| **Embeddings for Categorical Data** | Represent categories in dense vectors (deep learning).     |
| **Feature Stores**                  | Store reusable features for multiple models (e.g., Feast). |

---

## 📘 Mini Project

**Goal:** Build a **Feature-Rich Dataset for a Churn Prediction Model**
**Steps:**

1. Load customer data (age, tenure, purchases).
2. Create new behavior features (e.g., average spend per month).
3. Scale and encode features.
4. Evaluate which features drive churn most.

**Expected Outcome:**
A clean, feature-enhanced dataset that boosts model accuracy and explains customer behavior.

---

## 🧠 Example Prompt

> “Why does good feature engineering often outperform more complex model architectures?”

---

## 🔍 Key Takeaway

Feature engineering is **creative data science** — where intuition meets math.
Great features often matter more than the model itself.

---

## 📚 Further Reading

* [Feature Engineering for ML — Google Developers](https://developers.google.com/machine-learning/data-prep/construct/transform)
* [Hands-On Feature Engineering — Kaggle](https://www.kaggle.com/learn/feature-engineering)
* [SHAP Explainability Library](https://shap.readthedocs.io/en/latest/)
* [Feature Store Feast Docs](https://docs.feast.dev/)
* [Scikit-Learn Preprocessing Guide](https://scikit-learn.org/stable/modules/preprocessing.html)