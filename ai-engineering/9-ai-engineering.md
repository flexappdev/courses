# 🧩 Lesson 9 — Object-Oriented Programming (OOP)

### *AI Engineer Roadmap 2025 — Skill #9*

---

## 🎯 Objective

Learn how **Object-Oriented Programming (OOP)** helps structure complex AI systems — making your models, data pipelines, and APIs reusable, maintainable, and scalable.

---

## 🧩 Definition

**OOP** is a programming paradigm that organizes code into **objects** — bundles of data (attributes) and behavior (methods).
In AI engineering, OOP allows you to design modular systems — like model classes, dataset handlers, and training pipelines — that can easily extend or scale.

---

## 🧠 Core Concepts

| Concept               | Description                                                        |
| --------------------- | ------------------------------------------------------------------ |
| **Class**             | A blueprint for creating objects.                                  |
| **Object (Instance)** | A specific implementation of a class.                              |
| **Attributes**        | Variables that belong to a class or object.                        |
| **Methods**           | Functions defined inside a class.                                  |
| **Encapsulation**     | Hides internal state to protect data integrity.                    |
| **Inheritance**       | Lets classes inherit attributes and methods.                       |
| **Polymorphism**      | Allows the same method to behave differently in different classes. |
| **Abstraction**       | Focuses on essential behavior, ignoring complexity.                |

---

## ⚙️ Python Example

```python
class Model:
    def __init__(self, name):
        self.name = name
        self.trained = False

    def train(self, data):
        print(f"Training {self.name} on {len(data)} samples...")
        self.trained = True

    def predict(self, x):
        if not self.trained:
            raise Exception("Model not trained yet!")
        return f"Predicted result for {x}"

model = Model("Linear Regression")
model.train([1, 2, 3])
print(model.predict(5))
```

---

## 🧱 Real-World Uses in AI

| Component             | Example                                             |
| --------------------- | --------------------------------------------------- |
| **Model Abstraction** | Base `Model` class for TensorFlow/PyTorch           |
| **Data Loaders**      | `Dataset` and `DataLoader` classes                  |
| **Pipelines**         | OOP structure for preprocessing & postprocessing    |
| **APIs**              | Classes for FastAPI routes and business logic       |
| **Agents**            | Object-based autonomous systems with memory & tools |

---

## 📘 Mini Project

**Goal:** Create a **Reusable ML Model Class**
**Steps:**

1. Define a `BaseModel` class with `.train()` and `.predict()` methods.
2. Extend it to build a `LinearRegressionModel` subclass.
3. Load data from CSV, train, and make predictions.
4. Save the model as a `.pkl` file for reuse.

**Expected Outcome:**
A modular class-based ML workflow — reusable across multiple datasets or tasks.

---

## 🧠 Example Prompt

> “Explain how inheritance can simplify the design of multiple AI model types in Python.”

---

## 🔍 Key Takeaway

OOP helps AI Engineers **think in systems**, not scripts — turning isolated experiments into maintainable, production-grade codebases.

---

## 📚 Further Reading

* [Python OOP Tutorial — Real Python](https://realpython.com/python3-object-oriented-programming/)
* [OOP in ML — Towards Data Science](https://towardsdatascience.com/object-oriented-programming-for-machine-learning-7d3f98197f82)
* [Clean Code in Python](https://www.oreilly.com/library/view/clean-code-in-python/9781788835831/)