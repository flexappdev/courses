# 📈 Lesson 6 — Statistics & Probability

### *AI Engineer Roadmap 2025 — Skill #6*

---

## 🎯 Objective

Master the **statistical and probabilistic foundations** that power machine learning — understanding data distributions, uncertainty, and model confidence.

---

## 🧩 Definition

**Statistics** helps you summarize and interpret data, while **Probability** helps you reason about uncertainty.
Together, they form the mathematical core of all AI systems — from simple regression to complex generative models.

---

## 🧠 Core Concepts

| Concept                       | Description                                      |                                |
| ----------------------------- | ------------------------------------------------ | ------------------------------ |
| **Descriptive Statistics**    | Mean, Median, Mode, Variance, Standard Deviation |                                |
| **Probability Distributions** | Normal, Binomial, Poisson, Uniform               |                                |
| **Conditional Probability**   | `P(A                                             | B)` — probability of A given B |
| **Bayes’ Theorem**            | Updating beliefs with new evidence               |                                |
| **Sampling Methods**          | Random, Stratified, Bootstrapping                |                                |
| **Hypothesis Testing**        | t-test, ANOVA, Chi-square, p-values              |                                |
| **Confidence Intervals**      | Estimating population metrics with bounds        |                                |
| **Correlation & Covariance**  | Measuring relationships between variables        |                                |

---

## 🧮 Example Formulas

```text
Mean (μ) = Σx / n
Variance (σ²) = Σ(x - μ)² / n
Standard Deviation = √σ²
Bayes’ Theorem: P(A|B) = [P(B|A) * P(A)] / P(B)
```

---

## ⚙️ Python Example

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = np.random.normal(loc=50, scale=10, size=1000)
sns.histplot(data, kde=True)
plt.title(f"Mean={np.mean(data):.2f}, Std={np.std(data):.2f}")
plt.show()

t_stat, p_value = stats.ttest_1samp(data, 50)
print("p-value:", p_value)
```

---

## 📘 Mini Project

**Goal:** Perform **Statistical Analysis on Sales Data**.
**Steps:**

1. Load sales data (CSV).
2. Compute mean, median, variance, and visualize the distribution.
3. Test if average sales differ between two regions using a t-test.
4. Draw conclusions with confidence intervals.

**Expected Outcome:**
An analytical notebook demonstrating real-world statistical reasoning and hypothesis validation.

---

## 🧠 Example Prompt

> “Explain why understanding normal distribution and variance is crucial for machine learning models.”

---

## 🔍 Key Takeaway

Statistics & Probability teach AI Engineers to **trust (or doubt) their data** — turning uncertainty into measurable confidence.

---

## 📚 Further Reading

* [Khan Academy — Statistics & Probability](https://www.khanacademy.org/math/statistics-probability)
* [Think Stats (Free eBook)](https://greenteapress.com/wp/think-stats-2e/)
* [StatQuest YouTube Channel](https://www.youtube.com/user/joshstarmer)