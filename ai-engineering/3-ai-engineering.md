# 🧬 Lesson 3 — Deep Learning Basics

### *AI Engineer Roadmap 2025 — Skill #3*

---

## 🎯 Objective

Understand the **fundamentals of Deep Learning (DL)** — how neural networks learn complex data patterns and form the backbone of modern AI systems like ChatGPT, Gemini, and Stable Diffusion.

---

## 🧩 Definition

**Deep Learning** is a subset of Machine Learning that uses **artificial neural networks (ANNs)** with many layers (“deep” layers) to learn from large volumes of data.
It excels at tasks like image recognition, speech understanding, and natural language processing.

---

## 🧠 Core Concepts

| Concept                 | Description                                                                       |
| ----------------------- | --------------------------------------------------------------------------------- |
| **Neuron & Layer**      | A neuron processes input → applies weights → passes activation to the next layer. |
| **Activation Function** | Determines how signals propagate (ReLU, Sigmoid, Tanh).                           |
| **Forward Propagation** | Data flows through the network to make predictions.                               |
| **Backpropagation**     | Adjusts weights using gradient descent to reduce error.                           |
| **Loss Function**       | Measures prediction error (MSE, Cross-Entropy).                                   |
| **Optimizer**           | Improves learning speed (SGD, Adam, RMSProp).                                     |

---

## 🧱 Network Types

| Type                                       | Use Case                             |
| ------------------------------------------ | ------------------------------------ |
| **Feedforward (ANN/MLP)**                  | Tabular & general prediction tasks   |
| **Convolutional Neural Network (CNN)**     | Image and vision tasks               |
| **Recurrent Neural Network (RNN)**         | Sequential data, speech, time series |
| **Transformers**                           | Long-context text & multi-modal data |
| **Autoencoders**                           | Feature compression & denoising      |
| **GANs (Generative Adversarial Networks)** | Synthetic image generation           |

---

## ⚙️ Tech Stack Example

```python
import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 32)
        self.fc2 = nn.Linear(32, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = SimpleNN()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

---

## 📘 Mini Project

**Goal:** Build a **Digit Classifier** using the MNIST dataset.
**Steps:**

1. Load MNIST dataset (images of handwritten digits).
2. Build a small CNN with PyTorch or TensorFlow.
3. Train for 5 epochs and visualize accuracy.
4. Predict random digits and display results.

**Expected Outcome:**
A trained deep learning model achieving >95% accuracy on MNIST.

---

## 🧠 Example Prompt

> “Explain the difference between CNNs and RNNs in 3 sentences, including one key use case for each.”

---

## 🔍 Key Takeaway

Deep Learning teaches machines to **extract features automatically** — shifting from rule-based programming to representation learning.

---

## 📚 Further Reading

* [DeepLearning.AI — Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/)
* [PyTorch Tutorials](https://pytorch.org/tutorials/)
* [Stanford CS231n Notes](http://cs231n.stanford.edu/)