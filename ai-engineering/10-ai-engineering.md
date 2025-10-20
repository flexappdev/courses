# 🗂️ Lesson 10 — Version Control (Git & GitHub)

### *AI Engineer Roadmap 2025 — Skill #10*

---

## 🎯 Objective

Learn how to **track, manage, and collaborate on AI projects** using Git and GitHub — ensuring your models, datasets, and code evolve safely and reproducibly.

---

## 🧩 Definition

**Version Control Systems (VCS)** record changes to code over time, allowing you to revert, branch, or collaborate without losing work.
In AI engineering, Git ensures your experiments, models, and notebooks remain traceable — critical for reproducibility and teamwork.

---

## 🧠 Core Concepts

| Concept               | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| **Repository (Repo)** | A project folder tracked by Git.                           |
| **Commit**            | A saved snapshot of code changes.                          |
| **Branch**            | A parallel version of the project for new features.        |
| **Merge**             | Combine changes from one branch into another.              |
| **Pull Request (PR)** | A review request before merging.                           |
| **Clone / Fork**      | Copying projects for collaboration or contribution.        |
| **.gitignore**        | File specifying what not to track (e.g., datasets, creds). |
| **GitHub Actions**    | Automate CI/CD for ML models and apps.                     |

---

## ⚙️ Command Cheat Sheet

```bash
# Initialize repository
git init

# Track and commit files
git add .
git commit -m "Initial commit"

# Connect to GitHub
git remote add origin https://github.com/username/project.git
git push -u origin main

# Branching
git checkout -b feature/new-model
git merge feature/new-model
```

---

## 🧱 Use Cases for AI Engineers

| Area                    | Example                                          |
| ----------------------- | ------------------------------------------------ |
| **Experiment Tracking** | Commit changes in model configurations.          |
| **Model Versioning**    | Tag checkpoints (v1.0, v1.1, etc.).              |
| **Team Collaboration**  | Review pull requests before merging.             |
| **CI/CD Automation**    | Run training or lint checks with GitHub Actions. |
| **Reproducibility**     | Revert to any version of a pipeline or notebook. |

---

## 📘 Mini Project

**Goal:** Set up **Version Control for an AI Project**
**Steps:**

1. Create a GitHub repo named `ai-project-demo`.
2. Add your `main.py`, `requirements.txt`, and `/data/` folder.
3. Commit changes with meaningful messages.
4. Create a new branch (`feature-new-model`) and merge after testing.

**Expected Outcome:**
A fully versioned project repo with clean commit history and branch management.

---

## 🧠 Example Prompt

> “Why is Git essential for managing AI experiments and reproducibility?”

---

## 🔍 Key Takeaway

Git & GitHub are your **AI memory systems** — every experiment, notebook, and model version is safely stored and shareable.

---

## 📚 Further Reading

* [Git Official Documentation](https://git-scm.com/doc)
* [GitHub Docs — Collaboration Guide](https://docs.github.com/en/get-started/quickstart)
* [DVC + Git Integration](https://dvc.org/doc/start) — for data versioning in ML projects