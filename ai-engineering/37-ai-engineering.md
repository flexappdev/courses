# 📊 Lesson 37 — Data Visualization & EDA (Exploratory Data Analysis)

### *AI Engineer Roadmap 2025 — Skill #37*

---

## 🎯 Objective

Learn how to **understand, visualize, and explore data** before model training — uncovering hidden patterns, relationships, and anomalies that guide feature engineering and model design.

---

## 🧩 Definition

**Exploratory Data Analysis (EDA)** is the process of **summarizing datasets visually and statistically** to extract insights and detect patterns.
It helps AI engineers make informed decisions about cleaning, transformation, and feature selection **before** training models.

---

## 🧠 Core Concepts

| Concept                               | Description                                                     |
| ------------------------------------- | --------------------------------------------------------------- |
| **Univariate Analysis**               | Study of single variables (histograms, box plots).              |
| **Bivariate / Multivariate Analysis** | Relationship between two or more variables (scatter, heatmaps). |
| **Correlation Matrix**                | Quantifies linear relationships between features.               |
| **Distribution Analysis**             | Checks data spread and skewness.                                |
| **Outlier Detection**                 | Visual methods to spot anomalies.                               |
| **Categorical Analysis**              | Frequency and distribution of categorical features.             |
| **Dimensionality Visualization**      | PCA, t-SNE, or UMAP for high-dimensional data.                  |
| **Feature Relationships**             | How variables interact and affect the target.                   |

---

## ⚙️ Example — EDA with Pandas & Matplotlib

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

# Overview
print(df.info())
print(df.describe())

# Distribution
df["income"].hist(bins=20)
plt.title("Income Distribution")

# Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Matrix")
plt.show()
```

---

## ⚙️ Example — Detecting Outliers with Boxplot

```python
sns.boxplot(x=df["age"])
plt.title("Age Outlier Detection")
plt.show()
```

---

## 🧱 Tools & Libraries

| Category                     | Tools                                       |
| ---------------------------- | ------------------------------------------- |
| **Visualization**            | Matplotlib, Seaborn, Plotly, Altair         |
| **EDA Automation**           | Pandas Profiling, Sweetviz, YData Profiling |
| **Interactive Dashboards**   | Streamlit, Dash, Power BI                   |
| **Dimensionality Reduction** | PCA, t-SNE, UMAP                            |
| **Statistical Analysis**     | SciPy, StatsModels                          |

---

## 📘 Mini Project

**Goal:** Perform **EDA on a Customer Churn Dataset**
**Steps:**

1. Load the dataset and check for missing or skewed data.
2. Visualize distributions of numerical and categorical features.
3. Create correlation heatmaps for key metrics.
4. Summarize findings (e.g., “high tenure = low churn”).

**Expected Outcome:**
A clear EDA report identifying relationships and potential predictors for the model.

---

## 🧠 Example Prompt

> “How can correlation heatmaps help identify redundant or collinear features before model training?”

---

## 🔍 Key Takeaway

EDA is **data storytelling for AI** — it reveals what’s true, what’s broken, and what’s useful before you ever train a model.

---

## 📚 Further Reading

* [Seaborn Visualization Guide](https://seaborn.pydata.org/tutorial.html)
* [Matplotlib User Guide](https://matplotlib.org/stable/users/index.html)
* [Pandas Profiling (YData)](https://pandas-profiling.ydata.ai/docs/master/)
* [EDA Best Practices — Kaggle](https://www.kaggle.com/learn/data-visualization)
* [Plotly Dash for Interactive Apps](https://dash.plotly.com/)