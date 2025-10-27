Perfect — continuing your **AI Engineer 2025 roadmap**, here’s the next one 👇

---

# 🤖 Lesson 47 — Agents, Tools & Function Calling

### *AI Engineer Roadmap 2025 — Skill #47*

---

## 🎯 Objective

Learn how to create **AI agents** that can **think, decide, and act** by calling external **functions, APIs, or tools** — turning static LLMs into dynamic, goal-driven systems that interact with the real world.

---

## 🧩 Definition

**AI Agents** combine reasoning (via LLMs) with action (via functions or APIs).
They decide *what* to do next, *how* to do it, and sometimes *when* to stop.
This paradigm powers applications like **ChatGPT with tools**, **AutoGPT**, and **LangChain Agents**, where the model moves from “text generator” to “autonomous problem-solver.”

---

## 🧠 Core Concepts

| Concept                  | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| **Tool Use**             | The model can call external functions like “search()” or “get_weather()”. |
| **Function Calling**     | Structured API calls triggered by model reasoning.                        |
| **Planning & Reasoning** | Step-by-step breakdown of multi-action tasks.                             |
| **Memory**               | Keeps track of previous steps or context across sessions.                 |
| **Looping / Iteration**  | Agents run multiple steps until a goal is achieved.                       |
| **Tool Registry**        | List of available functions and descriptions for the model.               |
| **Delegation**           | Agents call sub-agents for specialized tasks (e.g., code, search, image). |
| **Safety & Boundaries**  | Controlled execution to prevent unwanted actions.                         |

---

## ⚙️ Example — OpenAI Function Calling

```python
from openai import OpenAI
client = OpenAI()

functions = [
    {
        "name": "get_weather",
        "description": "Retrieve current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"]
        }
    }
]

response = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": "What’s the weather in London?"}],
    functions=functions
)

print(response.choices[0].message)
```

---

## ⚙️ Example — LangChain Agent with Tools

```python
from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(model="gpt-4-turbo")
tools = load_tools(["serpapi", "llm-math"])
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")

agent.run("Search the capital of Poland and calculate its name length.")
```

---

## 🧱 Common Agent Frameworks (2025)

| Framework                                    | Strength                                             |
| -------------------------------------------- | ---------------------------------------------------- |
| **LangChain**                                | Modular agents + toolchains + memory.                |
| **LlamaIndex**                               | Data-centric RAG + tool-augmented agents.            |
| **OpenAI Function Calling / Assistants API** | Built-in tool use and persistent threads.            |
| **CrewAI / AutoGen**                         | Multi-agent collaboration and task delegation.       |
| **Microsoft Semantic Kernel**                | .NET & Python SDK for building agentic apps.         |
| **Haystack Agents**                          | RAG + reasoning orchestration for enterprise search. |

---

## 📘 Mini Project

**Goal:** Build a **Personal AI Assistant with Tools**
**Steps:**

1. Define 3–5 tools (search, weather, notes, calculator).
2. Register them via OpenAI function calling or LangChain.
3. Create an event loop that allows step-by-step reasoning.
4. Add short-term memory (JSON) for multi-turn interactions.

**Expected Outcome:**
An AI assistant capable of retrieving info, performing calculations, and maintaining short conversations — all autonomously.

---

## 🧠 Example Prompt

> “What’s the difference between tool-using agents and end-to-end LLM pipelines?”

---

## 🔍 Key Takeaway

Agents turn LLMs from **passive responders into active doers** — they can search, code, fetch, and plan, enabling automation across workflows, data, and APIs.

---

## 📚 Further Reading

* [OpenAI Function Calling Docs](https://platform.openai.com/docs/guides/function-calling)
* [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/)
* [Microsoft Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
* [AutoGen (Microsoft Research)](https://microsoft.github.io/autogen/)
* [CrewAI Multi-Agent Framework](https://github.com/joaomdmoura/crewai)

---

Would you like me to continue with **Lesson 48: Memory & Long-Context Architectures** next — same 1-page markdown format?
