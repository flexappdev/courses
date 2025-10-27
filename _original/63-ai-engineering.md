Perfect — continuing your **AI Engineer 2025 roadmap**, here’s the next one 👇

---

# 🧱 Lesson 63 — Quantization, Pruning & Model Compression

### *AI Engineer Roadmap 2025 — Skill #63*

---

## 🎯 Objective

Learn how to **compress large models** through **quantization**, **pruning**, and **knowledge distillation**, reducing size and latency while maintaining accuracy — critical for deploying LLMs and edge AI models efficiently.

---

## 🧩 Definition

**Model compression** encompasses techniques that make neural networks faster, smaller, and cheaper to run without retraining from scratch.
These methods enable models like GPT, LLaMA, and Stable Diffusion to run efficiently on laptops, phones, and embedded devices.

---

## 🧠 Core Concepts

| Concept                                | Description                                                          |
| -------------------------------------- | -------------------------------------------------------------------- |
| **Quantization**                       | Reducing precision of weights (e.g., FP32 → INT8 or FP16).           |
| **Pruning**                            | Removing redundant weights or neurons with little impact on output.  |
| **Knowledge Distillation**             | Training a smaller “student” model to mimic a large “teacher” model. |
| **Dynamic Quantization**               | Quantizes model weights during inference only.                       |
| **Static Quantization**                | Calibrates quantization parameters ahead of inference.               |
| **Structured vs Unstructured Pruning** | Removing entire neurons/layers vs individual weights.                |
| **Latency vs Accuracy Tradeoff**       | Balancing model speed and performance degradation.                   |
| **Edge AI Deployment**                 | Running models on constrained devices (Jetson, mobile CPUs).         |

---

## ⚙️ Example — Dynamic Quantization in PyTorch

```python
import torch
from transformers import BertModel

model = BertModel.from_pretrained("bert-base-uncased")
quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

torch.save(quantized_model.state_dict(), "bert_quantized.pt")
print("Model quantized and saved!")
```

➡️ Reduces model size by ~4× and speeds up CPU inference.

---

## ⚙️ Example — Pruning Weights in PyTorch

```python
import torch.nn.utils.prune as prune

for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        prune.l1_unstructured(module, name="weight", amount=0.3)
```

➡️ Removes 30% of weights with the smallest L1 magnitude.

---

## ⚙️ Example — Knowledge Distillation Setup

```python
teacher = BertModel.from_pretrained("bert-base-uncased")
student = BertModel.from_pretrained("prajjwal1/bert-tiny")

# Distillation loss: student learns from teacher outputs
loss = ((student_output - teacher_output.detach()) ** 2).mean()
```

---

## 🧱 Model Optimization Tools (2025 Landscape)

| Tool                            | Purpose                                  | Highlights |
| ------------------------------- | ---------------------------------------- | ---------- |
| **PyTorch FX / ONNX Runtime**   | Graph-level quantization & optimization. |            |
| **Intel Neural Compressor**     | Automated quantization for CPUs.         |            |
| **TensorRT (NVIDIA)**           | GPU inference acceleration.              |            |
| **OpenVINO (Intel)**            | Edge deployment for quantized models.    |            |
| **BitsAndBytes (Hugging Face)** | 4-bit/8-bit quantization for LLMs.       |            |
| **DeepSpeed ZeRO-Offload**      | Memory-efficient training & compression. |            |
| **GGUF / GPTQ / AWQ**           | Lightweight LLM quantization formats.    |            |

---

## 📘 Mini Project

**Goal:** Quantize and deploy a **DistilBERT sentiment model**
**Steps:**

1. Train or download a DistilBERT model.
2. Apply dynamic quantization using PyTorch or BitsAndBytes.
3. Measure accuracy loss and latency improvements.
4. Export as ONNX and deploy via FastAPI on CPU-only hardware.

**Expected Outcome:**
A compact model (~4× smaller, ~2× faster) with negligible accuracy loss — ready for real-time inference on limited devices.

---

## 🧠 Example Prompt

> “What’s the trade-off between 4-bit and 8-bit quantization for large language models?”

---

## 🔍 Key Takeaway

Compression transforms large models into **efficient, deployable intelligence** — making AI accessible across edge, mobile, and enterprise environments.

---

## 📚 Further Reading

* [PyTorch Quantization Tutorial](https://pytorch.org/docs/stable/quantization.html)
* [TensorRT Developer Guide](https://developer.nvidia.com/tensorrt)
* [Intel OpenVINO Toolkit](https://docs.openvino.ai/)
* [BitsAndBytes LLM Quantization](https://huggingface.co/docs/transformers/main_classes/quantization)
* [Distillation Paper (Hinton et al., 2015)](https://arxiv.org/abs/1503.02531)
* [GGUF Format Overview (LLaMA.cpp)](https://github.com/ggerganov/llama.cpp)

---

Would you like me to continue with **Lesson 64: Knowledge Distillation & Student–Teacher Training** next — same 1-page markdown format (more in-depth continuation of compression techniques)?
