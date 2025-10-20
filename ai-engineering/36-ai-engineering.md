# 🧹 Lesson 36 — Data Cleaning & Preprocessing

### *AI Engineer Roadmap 2025 — Skill #36*

---

## 🎯 Objective

Learn how to **prepare raw data for AI and ML pipelines** through cleaning, handling missing values, outlier removal, and normalization — ensuring your models train on **accurate, consistent, and unbiased** datasets.

---

## 🧩 Definition

**Data Cleaning** (or **Data Preprocessing**) is the process of detecting and correcting errors, inconsistencies, and formatting problems in datasets.
It’s the **first and most critical step** in any machine learning workflow — garbage in, garbage out.

---

## 🧠 Core Concepts

| Concept                     | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| **Missing Values**          | Handle nulls using imputation or removal.             |
| **Outliers**                | Identify extreme values using IQR or Z-score methods. |
| **Duplicate Entries**       | Remove repeated data to avoid bias.                   |
| **Normalization & Scaling** | Bring all numeric features to a common scale.         |
| **Encoding**                | Convert categorical data into numeric form.           |
| **Date Parsing**            | Convert string timestamps into datetime objects.      |
| **Data Consistency**        | Ensure unified units, labels, and data types.         |
| **Data Leakage Prevention** | Avoid including future information in training data.  |

---

## ⚙️ Example — Cleaning a Dataset with Pandas

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data.csv")

# Remove duplicates and handle missing values
df = df.drop_duplicates()
df["age"] = df["age"].fillna(df["age"].median())

# Remove outliers using IQR
Q1, Q3 = df["income"].quantile([0.25, 0.75])
IQR = Q3 - Q1
df = df[(df["income"] >= Q1 - 1.5 * IQR) & (df["income"] <= Q3 + 1.5 * IQR)]

# Normalize numeric columns
scaler = MinMaxScaler()
df[["age", "income"]] = scaler.fit_transform(df[["age", "income"]])
print(df.head())
```

---

## ⚙️ Example — Encoding Categorical Features

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df["gender_encoded"] = encoder.fit_transform(df["gender"])
```

---

## 🧱 Advanced Techniques

| Task                        | Tools / Methods                           |
| --------------------------- | ----------------------------------------- |
| **Missing Data Imputation** | KNNImputer, SimpleImputer                 |
| **Outlier Detection**       | Isolation Forest, DBSCAN                  |
| **Text Cleaning**           | Regex, lowercasing, tokenization          |
| **Data Validation**         | Great Expectations, Pydantic              |
| **Schema Enforcement**      | Pandera, Cerberus                         |
| **Automated Pipelines**     | Scikit-learn `Pipeline`, Prefect, Airflow |

---

## 📘 Mini Project

**Goal:** Build a **Data Cleaning Pipeline for a Housing Dataset**
**Steps:**

1. Load dataset with missing and inconsistent entries.
2. Handle missing values, remove outliers, and normalize numeric features.
3. Encode categorical variables (e.g., “location”, “type”).
4. Save cleaned dataset as `clean_data.parquet`.

**Expected Outcome:**
A reproducible preprocessing pipeline ready for model training — with quality-checked, consistent data.

---

## 🧠 Example Prompt

> “Why is it risky to impute missing target values and how can that affect model bias?”

---

## 🔍 Key Takeaway

Clean data is **the foundation of trustworthy AI** — models can’t fix messy inputs.
Preprocessing transforms chaos into clarity, making learning efficient and reliable.

---

## 📚 Further Reading

* [Pandas Data Cleaning Guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
* [Scikit-Learn Preprocessing Docs](https://scikit-learn.org/stable/modules/preprocessing.html)
* [Great Expectations Framework](https://greatexpectations.io/)
* [Automated Data Cleaning with PyCaret](https://pycaret.gitbook.io/docs/)
* [Data Validation with Pandera](https://pandera.readthedocs.io/)