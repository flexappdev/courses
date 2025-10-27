# 🧭 Lesson 50 — Reinforcement Learning & RLHF (Human Feedback)

### *AI Engineer Roadmap 2025 — Skill #50*

---

## 🎯 Objective

Understand how **Reinforcement Learning (RL)** teaches agents to make decisions through **trial and reward**, and how **RLHF (Reinforcement Learning from Human Feedback)** aligns large language models (LLMs) with human values and preferences.

---

## 🧩 Definition

**Reinforcement Learning** is a machine learning paradigm where an **agent** interacts with an **environment**, taking actions that maximize cumulative **rewards**.
In the LLM world, **RLHF** refines pretrained models using human-rated responses — combining **supervised fine-tuning (SFT)** and **reward modeling** to guide ethical, coherent, and helpful behavior.

---

## 🧠 Core Concepts

| Concept                         | Description                                                   |
| ------------------------------- | ------------------------------------------------------------- |
| **Agent**                       | Learner that interacts with an environment to achieve a goal. |
| **Environment**                 | Context where the agent acts and receives feedback.           |
| **Policy**                      | Strategy the agent follows to choose actions.                 |
| **Reward Function**             | Numeric feedback signal guiding the agent.                    |
| **Exploration vs Exploitation** | Balancing trying new actions vs using known best ones.        |
| **Q-Learning**                  | Value-based RL where the agent learns state–action values.    |
| **Policy Gradient Methods**     | Directly optimize action probabilities (e.g., PPO).           |
| **RLHF Pipeline**               | (1) SFT → (2) Reward Model → (3) PPO Fine-Tuning.             |

---

## ⚙️ Example — Simple Q-Learning

```python
import numpy as np

# Initialize Q-table
Q = np.zeros((5, 2))  # 5 states, 2 actions
alpha, gamma, episodes = 0.1, 0.9, 100

for _ in range(episodes):
    state = np.random.randint(0, 5)
    action = np.argmax(Q[state] + np.random.randn(1, 2)*(1/_+1))  # exploration
    reward = np.random.choice([1, 0])  # random feedback
    next_state = (state + 1) % 5
    Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])

print("Trained Q-Table:\n", Q)
```

---

## ⚙️ Example — RLHF Simplified Pipeline

```text
1️⃣ Collect human preference data (e.g., "Response A is better than Response B")
2️⃣ Train a Reward Model (predicts quality score for outputs)
3️⃣ Fine-tune the base LLM with PPO to maximize Reward Model scores
```

---

## 🧱 Key Frameworks & Libraries

| Framework                                | Use Case                                        |
| ---------------------------------------- | ----------------------------------------------- |
| **OpenAI PPO / TRL (HF)**                | RLHF for fine-tuning transformer models.        |
| **Stable-Baselines3**                    | Classic RL algorithms (A2C, PPO, DQN).          |
| **Ray RLlib**                            | Scalable distributed reinforcement learning.    |
| **DeepMind Acme / CleanRL**              | Research-friendly RL libraries.                 |
| **DPO (Direct Preference Optimization)** | RLHF alternative without explicit reward model. |

---

## 📘 Mini Project

**Goal:** Implement a **Text Rewriter with Preference Feedback**
**Steps:**

1. Generate two versions of each rewritten text.
2. Ask humans (or heuristics) to rate which is better.
3. Train a reward model on preferences.
4. Fine-tune with TRL’s PPOTrainer to maximize reward.

**Expected Outcome:**
A small RLHF loop that improves model style and alignment based on human preference signals.

---

## 🧠 Example Prompt

> “Why is RLHF preferred over supervised fine-tuning for aligning LLM behavior with human expectations?”

---

## 🔍 Key Takeaway

Reinforcement Learning makes models **goal-oriented**, while RLHF makes them **human-aligned** — balancing intelligence with empathy and control.

---

## 📚 Further Reading

* [OpenAI PPO & RLHF Overview](https://openai.com/research/learning-from-human-feedback)
* [Hugging Face TRL Library](https://huggingface.co/docs/trl/index)
* [DeepMind RL Research](https://www.deepmind.com/research)
* [CleanRL Implementations](https://github.com/vwxyzjn/cleanrl)
* [DPO: Direct Preference Optimization Paper (2023)](https://arxiv.org/abs/2305.18290)