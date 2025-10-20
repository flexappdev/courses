# 🪶 Lesson 26 — Anthropic API (Claude)

### *AI Engineer Roadmap 2025 — Skill #26*

---

## 🎯 Objective

Learn how to use **Anthropic’s Claude API** to build intelligent applications powered by the **Claude 3** and **Claude 3.5** model family — optimized for reasoning, summarization, and natural conversation.

---

## 🧩 Definition

**Claude** is Anthropic’s family of large language models designed to be **helpful, honest, and harmless**.
The **Anthropic API** provides structured access to these models for chat, document analysis, RAG, and tool-using agents.
Claude models are particularly strong in **long-context reasoning (up to 200K tokens)** and **document comprehension**.

---

## 🧠 Core Concepts

| Concept             | Description                                                        |
| ------------------- | ------------------------------------------------------------------ |
| **Model Families**  | Claude 3 Opus (most powerful), Sonnet (balanced), Haiku (fastest). |
| **Messages API**    | Primary endpoint for chat interactions.                            |
| **System Prompt**   | Defines the assistant’s behavior (“You are a financial analyst…”). |
| **Temperature**     | Controls randomness of outputs.                                    |
| **Context Window**  | Maximum input length — Claude 3.5 supports up to 200K tokens.      |
| **JSON Mode**       | Forces structured responses for API integrations.                  |
| **Tool Use (beta)** | Lets Claude call functions and external APIs.                      |

---

## ⚙️ Example — Chat Completion with Claude

```python
import anthropic

client = anthropic.Anthropic(api_key="YOUR_ANTHROPIC_KEY")

message = client.messages.create(
    model="claude-3-sonnet-20240229",
    system="You are an AI research assistant.",
    messages=[
        {"role": "user", "content": "Explain the difference between GPT and Claude models."}
    ],
    temperature=0.3,
)

print(message.content[0].text)
```

---

## ⚙️ Example — JSON Output Mode

```python
message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    system="You output structured JSON with key facts only.",
    messages=[{"role": "user", "content": "Summarize Tesla's AI strategy."}],
    temperature=0,
    response_format={"type": "json_object"}
)
print(message.content[0].text)
```

---

## 🧱 Use Cases in AI Engineering

| Category                      | Example                                            |
| ----------------------------- | -------------------------------------------------- |
| **Enterprise Chatbots**       | Build document-aware assistants with long context. |
| **Document Summarization**    | Process 100+ page PDFs in one request.             |
| **Tool-Augmented Agents**     | Use Claude’s API for reasoning + tool execution.   |
| **RAG Systems**               | Integrate with vector DBs for factual retrieval.   |
| **Compliance / Legal Review** | Parse large policy documents safely.               |

---

## 📘 Mini Project

**Goal:** Build a **Long-Context Research Assistant**
**Steps:**

1. Choose Claude 3.5 Sonnet (200K context).
2. Upload a 50-page research PDF.
3. Chunk and embed the document.
4. Query using Anthropic’s API with relevant context.

**Expected Outcome:**
A robust long-context assistant that summarizes or answers questions about large documents.

---

## 🧠 Example Prompt

> “Compare Claude 3.5 Sonnet and GPT-4 Turbo in terms of speed, context length, and output quality.”

---

## 🔍 Key Takeaway

Claude is the **AI for reasoning at scale** — ideal for document-heavy tasks, long-context analysis, and structured enterprise workflows.

---

## 📚 Further Reading

* [Anthropic API Documentation](https://docs.anthropic.com/)
* [Claude 3 Model Overview](https://www.anthropic.com/news/claude-3-family)
* [Function Calling (Tool Use) Guide](https://docs.anthropic.com/en/docs/tool-use/overview)
* [Anthropic Safety & Constitutional AI](https://www.anthropic.com/research)