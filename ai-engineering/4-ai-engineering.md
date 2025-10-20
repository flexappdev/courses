# 🐍 Lesson 4 — Python Programming

### *AI Engineer Roadmap 2025 — Skill #4*

---

## 🎯 Objective

Master **Python** as the core programming language for AI development — used in data science, ML/DL, automation, and backend systems.

---

## 🧩 Definition

**Python** is an interpreted, high-level programming language known for readability and massive ecosystem support in AI (e.g., NumPy, Pandas, TensorFlow, PyTorch).
It’s the lingua franca of AI engineering — simple syntax, huge library base, and perfect for experimentation.

---

## 🧠 Core Concepts

| Concept                    | Description                                     |
| -------------------------- | ----------------------------------------------- |
| **Variables & Data Types** | Strings, Integers, Lists, Tuples, Dicts         |
| **Control Flow**           | `if`, `for`, `while`, `break`, `continue`       |
| **Functions**              | Modular, reusable code blocks (`def`, `lambda`) |
| **Modules & Packages**     | Importing and structuring reusable code         |
| **File Handling**          | Reading/writing data files (CSV, JSON)          |
| **Error Handling**         | Using `try`, `except`, `finally`                |
| **List Comprehensions**    | One-line loops for efficient data ops           |
| **Virtual Environments**   | Isolating dependencies using `venv` or `conda`  |

---

## 🧱 Key AI Libraries

| Purpose           | Libraries                               |
| ----------------- | --------------------------------------- |
| **Math & Arrays** | `NumPy`, `SciPy`                        |
| **Data Handling** | `Pandas`, `Dask`                        |
| **Visualization** | `Matplotlib`, `Seaborn`, `Plotly`       |
| **ML/DL**         | `Scikit-Learn`, `PyTorch`, `TensorFlow` |
| **Deployment**    | `FastAPI`, `Flask`, `Docker`            |
| **Automation**    | `OS`, `Subprocess`, `Schedule`          |

---

## ⚙️ Code Snippet Example

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[5]])

print(f"Prediction for x=5: {prediction[0]}")
```

---

## 📘 Mini Project

**Goal:** Build a simple **AI Calculator CLI**.
**Steps:**

1. Create a Python script `aicalc.py`.
2. Ask user for input numbers and operation.
3. Use basic functions for add, subtract, multiply, divide.
4. Add an option to “predict next number” using `LinearRegression`.

**Expected Outcome:**
A lightweight, command-line calculator that integrates Python logic + ML.

---

## 🧠 Example Prompt

> “Write a Python function that reads a CSV file and prints the average of a numeric column.”

---

## 🔍 Key Takeaway

Python is the **AI engineer’s toolbox language** — everything from model training to deployment flows through Python-based frameworks.

---

## 📚 Further Reading

* [Python.org Tutorial](https://docs.python.org/3/tutorial/)
* [Real Python — Python for AI Developers](https://realpython.com/)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)