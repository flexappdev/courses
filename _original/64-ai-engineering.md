Perfect — continuing your **AI Engineer 2025 roadmap**, here’s the next one 👇

---

# 🎓 Lesson 64 — Knowledge Distillation & Student–Teacher Training

### *AI Engineer Roadmap 2025 — Skill #64*

---

## 🎯 Objective

Learn how to **transfer intelligence from large models (teachers)** to **smaller, faster models (students)** through **knowledge distillation** — a core technique for making high-performance AI efficient and deployable.

---

## 🧩 Definition

**Knowledge Distillation (KD)** is a compression technique where a small **student model** is trained to mimic the outputs (soft probabilities, embeddings, or hidden states) of a larger, more accurate **teacher model**.
It allows retaining most of the teacher’s intelligence while dramatically reducing computational cost and model size.

---

## 🧠 Core Concepts

| Concept                             | Description                                                                |
| ----------------------------------- | -------------------------------------------------------------------------- |
| **Teacher Model**                   | Large, pretrained model (e.g., BERT-large, GPT-5).                         |
| **Student Model**                   | Smaller, efficient model trained to replicate teacher outputs.             |
| **Soft Targets**                    | Teacher’s output probabilities (not hard labels) — richer learning signal. |
| **Temperature (T)**                 | Controls how smooth or sharp the teacher’s output probabilities are.       |
| **Loss Function**                   | Usually a weighted mix of KD loss + standard task loss.                    |
| **Intermediate Layer Distillation** | Aligning hidden states, not just outputs.                                  |
| **Task-Specific KD**                | Fine-tuning the student for specific domains (QA, summarization, etc.).    |
| **Progressive Distillation**        | Multi-stage shrinking (teacher → mid → tiny student).                      |

---

## ⚙️ Example — Soft Target Distillation (PyTorch)

```python
import torch, torch.nn.functional as F

def distillation_loss(student_logits, teacher_logits, labels, T=2.0, alpha=0.5):
    soft_loss = F.kl_div(
        F.log_softmax(student_logits / T, dim=1),
        F.softmax(teacher_logits / T, dim=1),
        reduction="batchmean"
    ) * (T * T * alpha)
    
    hard_loss = F.cross_entropy(student_logits, labels) * (1 - alpha)
    return soft_loss + hard_loss
```

➡️ Combines **soft loss (teacher mimicry)** and **hard loss (ground truth)** for balanced learning.

---

## ⚙️ Example — Distilling BERT → DistilBERT

```python
from transformers import DistilBertForSequenceClassification, BertForSequenceClassification

teacher = BertForSequenceClassification.from_pretrained("bert-base-uncased")
student = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")

# Fine-tune the student using teacher predictions as soft labels
# (Hugging Face Trainer API can handle KD via custom loss functions)
```

---

## 🧱 Variants of Knowledge Distillation

| Method                         | Description                                            |
| ------------------------------ | ------------------------------------------------------ |
| **Logit Matching (Hinton)**    | Match teacher and student softmax outputs.             |
| **Feature Matching (FitNets)** | Align intermediate hidden states.                      |
| **Attention Transfer**         | Student mimics teacher’s attention maps.               |
| **TinyBERT / MiniLM**          | Distilled BERT variants with layer-level distillation. |
| **Self-Distillation**          | Model teaches itself across epochs or checkpoints.     |
| **Ensemble Distillation**      | Combine multiple teachers into one student.            |

---

## 📘 Mini Project

**Goal:** Distill a **BERT sentiment classifier** into a smaller model
**Steps:**

1. Train or load a `bert-base` model as the teacher.
2. Initialize a `distilbert` or `bert-mini` as the student.
3. Train with KD loss combining teacher logits + true labels.
4. Compare performance and latency between teacher and student.

**Expected Outcome:**
A student model with ~60–70% fewer parameters but only ~2–3% accuracy drop — ideal for mobile or API deployment.

---

## 🧠 Example Prompt

> “Why does soft label training in knowledge distillation improve generalization over hard label training?”

---

## 🔍 Key Takeaway

Knowledge distillation allows engineers to **scale down intelligence without dumbing it down** — capturing the wisdom of giant models in lightweight, deployable ones.

---

## 📚 Further Reading

* [Distilling the Knowledge in a Neural Network (Hinton et al., 2015)](https://arxiv.org/abs/1503.02531)
* [TinyBERT Paper (Huawei)](https://arxiv.org/abs/1909.10351)
* [MiniLM Paper (Microsoft)](https://arxiv.org/abs/2002.10957)
* [Self-Distillation Techniques Overview](https://arxiv.org/abs/2106.05237)
* [Hugging Face Distillation Example Scripts](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation)

---

Would you like me to continue with **Lesson 65: Model Optimization for Inference (ONNX, TensorRT, OpenVINO)** next — same 1-page markdown format?
