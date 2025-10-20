# 🐳 Lesson 13 — Docker & Containerization

### *AI Engineer Roadmap 2025 — Skill #13*

---

## 🎯 Objective

Learn how to **package and run AI applications in containers** using Docker — ensuring consistency, portability, and scalability across environments.

---

## 🧩 Definition

**Docker** is a containerization platform that allows you to bundle code, dependencies, and environment settings into lightweight, portable containers.
For AI engineers, Docker guarantees that your model will **run identically** on your laptop, server, or cloud — solving the classic *“it works on my machine”* problem.

---

## 🧠 Core Concepts

| Concept            | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| **Image**          | Blueprint for a container (e.g., Python + dependencies).    |
| **Container**      | A running instance of an image.                             |
| **Dockerfile**     | Script defining how an image is built.                      |
| **Volume**         | Persistent data storage outside containers.                 |
| **Port Mapping**   | Exposing container ports to host machine (e.g., `8080:80`). |
| **Docker Compose** | Manage multi-container apps (e.g., backend + DB).           |
| **Registry**       | A place to store images (Docker Hub, ECR, GHCR).            |

---

## ⚙️ Example Dockerfile

```dockerfile
# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose API port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ⚙️ Build & Run Commands

```bash
# Build the image
docker build -t ai-api .

# Run the container
docker run -d -p 8000:8000 ai-api
```

---

## 🧱 AI Engineering Use Cases

| Area                        | Example                                                      |
| --------------------------- | ------------------------------------------------------------ |
| **Model Deployment**        | Run ML models in isolated environments.                      |
| **Reproducibility**         | Share the same setup with collaborators.                     |
| **Local → Cloud Migration** | Deploy on AWS ECS, Azure Container Apps, or GCP Cloud Run.   |
| **MLOps Pipelines**         | Standardize environments for training, testing, and serving. |
| **Experiment Tracking**     | Version different containerized model builds.                |

---

## 📘 Mini Project

**Goal:** Dockerize a **FastAPI ML App**
**Steps:**

1. Create a FastAPI prediction API (`main.py`).
2. Write a `Dockerfile` for the app.
3. Build and run it locally.
4. Push your image to Docker Hub.

**Expected Outcome:**
A working containerized AI API accessible at `localhost:8000/predict`.

---

## 🧠 Example Prompt

> “Explain how Docker helps deploy machine learning models consistently across different environments.”

---

## 🔍 Key Takeaway

Docker turns your AI project into a **self-contained unit** — portable, consistent, and production-ready from local dev to global deployment.

---

## 📚 Further Reading

* [Docker Official Documentation](https://docs.docker.com/get-started/)
* [FastAPI + Docker Tutorial](https://fastapi.tiangolo.com/deployment/docker/)
* [Docker Compose Guide](https://docs.docker.com/compose/)
* [AWS ECS + Docker Integration](https://aws.amazon.com/ecs/)