# 📊 Lesson 5 — Data Science Fundamentals

### *AI Engineer Roadmap 2025 — Skill #5*

---

## 🎯 Objective

Learn how to **collect, clean, analyze, and visualize data** — the essential foundation for every AI and ML project.

---

## 🧩 Definition

**Data Science** combines statistics, mathematics, and programming to extract insights and patterns from structured or unstructured data.
For an AI Engineer, it’s the process that transforms raw data into meaningful inputs for machine learning models.

---

## 🧠 Core Concepts

| Concept                             | Description                                              |
| ----------------------------------- | -------------------------------------------------------- |
| **Data Collection**                 | Gathering data from APIs, databases, or sensors.         |
| **Data Cleaning**                   | Handling missing, duplicate, or inconsistent values.     |
| **Exploratory Data Analysis (EDA)** | Understanding distributions, correlations, and outliers. |
| **Feature Selection**               | Identifying key variables that drive model performance.  |
| **Data Visualization**              | Communicating insights with charts and dashboards.       |
| **Statistical Testing**             | Using t-tests, chi-square, ANOVA for data validation.    |
| **Data Ethics**                     | Ensuring privacy, consent, and fairness in datasets.     |

---

## 🧱 Common Tools & Libraries

| Purpose               | Tools                        |
| --------------------- | ---------------------------- |
| **Data Manipulation** | Pandas, NumPy                |
| **Visualization**     | Matplotlib, Seaborn, Plotly  |
| **Analysis**          | Scipy, Statsmodels           |
| **Notebooks**         | Jupyter, Google Colab        |
| **Big Data**          | Spark, Dask                  |
| **Dashboards**        | Streamlit, Power BI, Tableau |

---

## ⚙️ Code Example — Quick EDA

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
print(df.info())
print(df.describe())

sns.pairplot(df)
plt.show()
```

---

## 📘 Mini Project

**Goal:** Build a **Data Insights Dashboard**.
**Steps:**

1. Load a real dataset (e.g., Titanic, Iris, or Kaggle dataset).
2. Perform EDA — find missing data, correlations, and key trends.
3. Visualize results using Seaborn or Plotly.
4. Create a simple Streamlit dashboard to display findings.

**Expected Outcome:**
An interactive dashboard summarizing the dataset with clear visuals and metrics.

---

## 🧠 Example Prompt

> “Describe how data cleaning affects machine learning performance in under 100 words.”

---

## 🔍 Key Takeaway

Data Science gives AI its **eyes and ears** — transforming raw noise into structured information that models can understand and learn from.

---

## 📚 Further Reading

* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Kaggle Learn: Data Science Micro-Courses](https://www.kaggle.com/learn)
* [Data Visualization with Seaborn](https://seaborn.pydata.org/tutorial.html)