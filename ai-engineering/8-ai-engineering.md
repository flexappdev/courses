# 🔺 Lesson 8 — Calculus for Optimization

### *AI Engineer Roadmap 2025 — Skill #8*

---

## 🎯 Objective

Learn how **calculus** powers optimization in machine learning — helping models minimize error and improve performance through gradient-based learning.

---

## 🧩 Definition

**Calculus** is the study of change. In AI, it’s used to adjust model parameters (weights and biases) using gradients — the rate of change of the loss function with respect to each parameter.
Without calculus, neural networks couldn’t learn.

---

## 🧠 Core Concepts

| Concept                     | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| **Functions & Derivatives** | Measure how outputs change with inputs.               |
| **Partial Derivatives**     | Gradients for multivariable functions.                |
| **Gradient Descent**        | Iterative method to minimize loss.                    |
| **Chain Rule**              | Links multiple derivatives (core of backpropagation). |
| **Loss Function**           | Quantifies model error (e.g., MSE, Cross-Entropy).    |
| **Learning Rate**           | Controls how fast weights update.                     |
| **Local vs Global Minima**  | Where optimization can get stuck.                     |
| **Regularization**          | Prevents overfitting by adding penalty terms.         |

---

## 🧮 Example Formulas

```text
Derivative: f'(x) = lim(Δx→0) [f(x+Δx) - f(x)] / Δx
Gradient Descent: w = w - η * ∇L(w)
Chain Rule: dL/dx = (dL/dy) * (dy/dx)
```

---

## ⚙️ Python Example

```python
import numpy as np

# Simple gradient descent for y = x^2
x = 10  # initial guess
lr = 0.1

for i in range(20):
    grad = 2 * x         # derivative of x^2 is 2x
    x -= lr * grad
    print(f"Step {i+1}: x={x:.4f}, grad={grad:.4f}")
```

---

## 📘 Mini Project

**Goal:** Implement **Gradient Descent on a Custom Loss Function**
**Steps:**

1. Define a quadratic or logistic loss function.
2. Compute its gradient manually and visualize convergence.
3. Experiment with different learning rates.
4. Plot the loss curve over iterations.

**Expected Outcome:**
A visualization of how optimization finds the minimum — the same process used in training deep neural networks.

---

## 🧠 Example Prompt

> “Explain how gradient descent uses derivatives to optimize neural network weights.”

---

## 🔍 Key Takeaway

Calculus is the **mathematical heartbeat of learning** — it teaches AI models *how to improve themselves* by moving toward lower loss values.

---

## 📚 Further Reading

* [3Blue1Brown — Gradient Descent Explained](https://www.youtube.com/watch?v=IHZwWFHWa-w)
* [Khan Academy — Calculus for ML](https://www.khanacademy.org/math/calculus-1)
* [Deep Learning Book — Optimization for Learning](https://www.deeplearningbook.org/contents/optimization.html)