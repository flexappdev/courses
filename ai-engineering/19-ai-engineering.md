# 🧭 Lesson 19 — Reinforcement Learning (RL)

### *AI Engineer Roadmap 2025 — Skill #19*

---

## 🎯 Objective

Understand how **Reinforcement Learning (RL)** enables AI agents to learn by interacting with an environment — optimizing behavior through trial, error, and rewards.

---

## 🧩 Definition

**Reinforcement Learning** is a type of machine learning where an agent learns by performing actions and receiving feedback in the form of **rewards** or **penalties**.
Unlike supervised learning (which learns from labeled data), RL learns by **experience** — making it key for **autonomous systems**, **games**, and **robotics**.

---

## 🧠 Core Concepts

| Concept                         | Description                                            |
| ------------------------------- | ------------------------------------------------------ |
| **Agent**                       | The learner or decision-maker.                         |
| **Environment**                 | The world the agent interacts with.                    |
| **State (S)**                   | A snapshot of the environment.                         |
| **Action (A)**                  | Choices available to the agent.                        |
| **Reward (R)**                  | Feedback signal for good or bad actions.               |
| **Policy (π)**                  | Strategy defining which actions to take.               |
| **Value Function**              | Estimates expected future rewards.                     |
| **Exploration vs Exploitation** | Balancing trying new actions vs using known best ones. |

---

## ⚙️ Example — Q-Learning in Python

```python
import numpy as np

Q = np.zeros((5, 2))  # states x actions
alpha, gamma = 0.8, 0.95  # learning rate & discount factor
rewards = [1, 0, -1, 2, 0]

for episode in range(10):
    state = np.random.randint(0, 5)
    action = np.random.randint(0, 2)
    next_state = (state + 1) % 5
    Q[state, action] = Q[state, action] + alpha * (rewards[next_state] + gamma * np.max(Q[next_state]) - Q[state, action])

print("Learned Q-table:\n", Q)
```

---

## 🧱 RL Algorithms Overview

| Type             | Algorithms                                      |
| ---------------- | ----------------------------------------------- |
| **Value-Based**  | Q-Learning, Deep Q-Networks (DQN)               |
| **Policy-Based** | REINFORCE, PPO, A2C, SAC                        |
| **Model-Based**  | Dyna-Q, Monte Carlo Tree Search                 |
| **Hybrid**       | Actor-Critic (combines value + policy learning) |

---

## 📘 Mini Project

**Goal:** Build a **Self-Learning Game Agent**
**Steps:**

1. Install OpenAI Gymnasium (`pip install gymnasium`).
2. Create an environment (e.g., CartPole).
3. Train a simple agent using Q-Learning or PPO.
4. Visualize performance over episodes.

**Expected Outcome:**
An agent that learns to balance a pole or navigate an environment autonomously through rewards.

---

## 🧠 Example Prompt

> “Explain how reinforcement learning differs from supervised learning and give one real-world example.”

---

## 🔍 Key Takeaway

Reinforcement Learning is how AI **learns to act** — mastering complex behaviors through feedback and adaptation rather than fixed instructions.

---

## 📚 Further Reading

* [OpenAI Spinning Up — RL Fundamentals](https://spinningup.openai.com/en/latest/)
* [DeepMind RL Course](https://deepmind.com/learning-resources)
* [Gymnasium Environments (OpenAI Gym successor)](https://gymnasium.farama.org/)
* [Stable Baselines3 (Python Library)](https://stable-baselines3.readthedocs.io/)