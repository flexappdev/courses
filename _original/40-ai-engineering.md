# 🧠 Lesson 40 — Deep Learning Fundamentals

### *AI Engineer Roadmap 2025 — Skill #40*

---

## 🎯 Objective

Understand the **core principles of deep learning**, including how neural networks learn, the role of activation functions, and the importance of backpropagation — the foundation for modern AI architectures.

---

## 🧩 Definition

**Deep Learning (DL)** is a subset of machine learning where **neural networks** with multiple layers learn complex representations of data.
It powers applications like **computer vision, natural language processing, and speech recognition**, learning directly from raw data instead of hand-crafted features.

---

## 🧠 Core Concepts

| Concept                          | Description                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------- |
| **Neuron**                       | Basic unit that computes a weighted sum of inputs and applies an activation. |
| **Layer**                        | A group of neurons (input, hidden, output).                                  |
| **Activation Function**          | Introduces non-linearity (ReLU, Sigmoid, Tanh).                              |
| **Forward Propagation**          | Passing inputs through the network to generate outputs.                      |
| **Loss Function**                | Measures how far predictions are from targets.                               |
| **Backpropagation**              | Algorithm that adjusts weights using gradients.                              |
| **Gradient Descent**             | Optimization method to minimize loss.                                        |
| **Epoch / Batch Size**           | Defines how much data is seen and how often weights update.                  |
| **Overfitting / Regularization** | Preventing models from memorizing data (Dropout, L2).                        |

---

## ⚙️ Example — Simple Neural Network with Keras

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, batch_size=32)
```

---

## ⚙️ Example — Visualizing Model Architecture

```python
from tensorflow.keras.utils import plot_model
plot_model(model, show_shapes=True, to_file="model.png")
```

---

## 🧱 Key Building Blocks

| Component          | Example                            |
| ------------------ | ---------------------------------- |
| **Optimizers**     | Adam, SGD, RMSprop                 |
| **Loss Functions** | Cross-Entropy, MSE, Huber          |
| **Regularization** | Dropout, Early Stopping, BatchNorm |
| **Initialization** | Xavier, He, Uniform                |
| **Frameworks**     | TensorFlow, PyTorch, JAX           |

---

## 📘 Mini Project

**Goal:** Build a **Deep Neural Network for Digit Recognition (MNIST)**
**Steps:**

1. Load MNIST dataset (28x28 grayscale images).
2. Normalize pixel values (0–1).
3. Build a multi-layer neural network.
4. Train and evaluate accuracy.

**Expected Outcome:**
A deep learning model achieving >95% accuracy on handwritten digit classification.

---

## 🧠 Example Prompt

> “Explain how backpropagation works and why activation functions are necessary in deep networks.”

---

## 🔍 Key Takeaway

Deep learning mimics the human brain’s ability to learn from experience — **stacking layers of abstraction** to solve problems traditional ML cannot.

---

## 📚 Further Reading

* [Deep Learning Book — Ian Goodfellow](https://www.deeplearningbook.org/)
* [TensorFlow Keras Guide](https://www.tensorflow.org/guide/keras)
* [PyTorch Tutorials](https://pytorch.org/tutorials/)
* [CS231n: Convolutional Neural Networks for Visual Recognition](https://cs231n.stanford.edu/)
* [Andrej Karpathy — Neural Networks: Zero to Hero (YouTube)](https://www.youtube.com/@AndrejKarpathy)