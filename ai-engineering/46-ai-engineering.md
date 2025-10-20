# ⚡ Lesson 43 — Transformers & Attention Mechanisms

### *AI Engineer Roadmap 2025 — Skill #43*

---

## 🎯 Objective

Understand the architecture and principles behind **Transformers** — the foundation of modern AI models like GPT, BERT, and Gemini — powered by **attention mechanisms** that replaced RNNs in handling sequential data.

---

## 🧩 Definition

**Transformers** are deep learning architectures introduced in 2017 (“Attention Is All You Need”) that rely entirely on **self-attention** rather than recurrence.
They process input sequences **in parallel**, capturing long-range dependencies efficiently, enabling **scalability, contextual understanding**, and **massive pretraining**.

---

## 🧠 Core Concepts

| Concept                             | Description                                                             |
| ----------------------------------- | ----------------------------------------------------------------------- |
| **Attention Mechanism**             | Weighs the importance of different input tokens relative to each other. |
| **Self-Attention**                  | Computes relationships within the same sequence (e.g., word-to-word).   |
| **Multi-Head Attention**            | Uses multiple attention layers to learn diverse relationships.          |
| **Positional Encoding**             | Adds order information since Transformers are non-sequential.           |
| **Encoder-Decoder Architecture**    | Encoder extracts context; decoder generates output.                     |
| **Feedforward Network**             | Processes each token after attention computation.                       |
| **Layer Normalization & Residuals** | Improve gradient flow and stability.                                    |
| **Scalability**                     | Enables massive parallel processing across GPUs/TPUs.                   |

---

## ⚙️ Example — Attention Formula

For query (Q), key (K), and value (V) matrices:
[
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
]

This computes how much focus each token should give to others.

---

## ⚙️ Example — Minimal Transformer Block (PyTorch)

```python
import torch
from torch import nn

class MiniTransformerBlock(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim, num_heads)
        self.ff = nn.Sequential(
            nn.Linear(embed_dim, 4 * embed_dim),
            nn.ReLU(),
            nn.Linear(4 * embed_dim, embed_dim)
        )
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x):
        attn_out, _ = self.attn(x, x, x)
        x = self.norm1(x + attn_out)
        ff_out = self.ff(x)
        return self.norm2(x + ff_out)
```

---

## 🧱 Key Transformer Architectures

| Model                                 | Type            | Purpose                                          |
| ------------------------------------- | --------------- | ------------------------------------------------ |
| **BERT (2018)**                       | Encoder         | Language understanding (classification, Q&A).    |
| **GPT (2018–2024)**                   | Decoder         | Text generation, reasoning, multimodal AI.       |
| **T5 (2019)**                         | Encoder-Decoder | Text-to-text transformations.                    |
| **ViT (2021)**                        | Encoder         | Vision transformer for images.                   |
| **Gemini / Claude / LLaMA / Mistral** | Decoder         | State-of-the-art LLMs with reinforcement tuning. |

---

## 📘 Mini Project

**Goal:** Build a **Transformer-based Text Summarizer**
**Steps:**

1. Load a pretrained model (`t5-small`) via Hugging Face.
2. Input long text; output concise summary.
3. Measure token length and summarize efficiency.
4. Experiment with temperature and max_length settings.

**Expected Outcome:**
A Transformer-powered summarizer that generates fluent, context-aware summaries from any document.

---

## 🧠 Example Prompt

> “Why did Transformers replace RNNs and LSTMs for most NLP and vision tasks?”

---

## 🔍 Key Takeaway

Transformers introduced **attention as the universal mechanism of understanding**, enabling AI to reason across text, vision, and sound — forming the backbone of all frontier models.

---

## 📚 Further Reading

* [Attention Is All You Need (Vaswani et al., 2017)](https://arxiv.org/abs/1706.03762)
* [Illustrated Transformer — Jay Alammar](https://jalammar.github.io/illustrated-transformer/)
* [Hugging Face Transformers Docs](https://huggingface.co/docs/transformers/)
* [Google’s Transformer Architecture Overview](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
* [The Annotated Transformer (Harvard NLP)](http://nlp.seas.harvard.edu/annotated-transformer/)
