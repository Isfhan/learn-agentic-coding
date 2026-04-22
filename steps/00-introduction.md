# Step 00 · Introduction to Agentic Coding

> **⏱️ Time:** 30 minutes · **Prereq:** You've used Cursor / Claude Code / Copilot at least once

---

## 🎯 What you'll learn

By the end of this step you'll be able to:

- Define **agentic coding** in one sentence.
- Explain the difference between *autocomplete*, *chat*, and *agents*.
- Draw the big picture of an agent loop on a napkin.
- Know the vocabulary for the rest of this roadmap.

---

## 🤔 What is "agentic coding"?

> **Agentic coding** is the practice of writing software by giving goals (not keystrokes) to an AI agent that can read your repo, run commands, edit files, and iterate on feedback — all while you supervise.

A regular coding assistant *suggests* code. An agent *takes actions*: opens files, runs your test suite, reads the errors, edits the code, re-runs, commits. **You become the director, not the typist.**

### Three generations of AI coding

| Generation | Example | You do | AI does |
|-----------|---------|--------|---------|
| **1. Autocomplete** (2021) | GitHub Copilot tab-complete | Drive every keystroke | Guess next ~20 tokens |
| **2. Chat** (2023) | ChatGPT, Cursor Chat | Copy-paste code in/out | Answer questions, rewrite snippets |
| **3. Agents** (2024-2026) | Cursor Agent, Claude Code, Aider | Give a goal, review the PR | Plan → read → edit → test → loop |

You are here → **Gen 3.**

---

## 🧠 The big picture that unlocks everything

Under the hood, **every agent is just this**:

```text
┌─────────────────────────────────────────────────┐
│  Goal: "Fix the failing auth test"              │
└────────────────────┬────────────────────────────┘
                     │
         ┌───────────▼──────────┐
         │  LLM reads context   │◄────────┐
         │  (code + goal +      │         │
         │   previous results)  │         │
         └───────────┬──────────┘         │
                     │                    │
                     ▼                    │
         ┌──────────────────────┐         │
         │  LLM picks a TOOL    │         │
         │  (read_file,         │         │
         │   run_shell,         │         │
         │   edit_file, …)      │         │
         └───────────┬──────────┘         │
                     │                    │
                     ▼                    │
         ┌──────────────────────┐         │
         │  Tool runs, returns  │         │
         │  result (file        │         │
         │  contents, stdout,   │         │
         │  errors)             │         │
         └───────────┬──────────┘         │
                     │                    │
                     ▼                    │
         ┌──────────────────────┐   done? │
         │  Result fed back     │─────────┘
         │  into LLM context    │   no
         └──────────────────────┘
                     │ yes
                     ▼
                ✅ Finish
```

**That's it.** An agent = a loop of *"pick a tool → run it → think about the result"*. Everything else in this roadmap (MCP, Skills, Hooks, Subagents) is about making this loop *smarter, safer, or reusable*.

---

## 📖 Vocabulary — the 12 words you need

| Term | In plain English |
|------|------------------|
| **LLM** | The brain. GPT-5, Claude Opus, Gemini, Qwen, Llama, etc. |
| **Context window** | Everything the LLM can "see" right now (code + chat + tool results). Measured in tokens. |
| **Token** | A chunk of text (≈¾ of an English word). "hello" = 1 token, "unbelievable" = 3. |
| **Prompt** | What you type. The question or instruction. |
| **System prompt** | The hidden instructions the tool gives the LLM on your behalf ("You are a coding agent…"). |
| **Tool / Function calling** | The LLM's ability to *request* an action (read this file, run this command). |
| **Agent** | An LLM + tools + a loop. |
| **MCP (Model Context Protocol)** | A standard so any agent can talk to any tool/data source. The "USB-C of AI." |
| **Skill** | A reusable, version-controlled package of instructions (+ optional scripts) that extends what an agent can do well. |
| **Rule** | Persistent, always-on instructions for an agent in a specific project. |
| **Hook** | A custom script that runs before/after agent events (e.g., "format code after every edit"). |
| **Subagent** | A child agent spun up by a parent agent to handle a scoped task in its own context window. |

🎓 **Memorize these now.** The rest of the roadmap uses them casually.

---

## 🎥 Watch (pick ONE, ~15 min)

- **[Andrej Karpathy — Intro to LLMs (1h)](https://www.youtube.com/watch?v=zjkBMFhNj_g)** — skip to 30:00 for the "LLM OS" idea; this is the foundation of modern agents.
- **[What is Agentic AI? (IBM Technology, 7 min)](https://www.youtube.com/watch?v=kJLiOGle3Lw)** — crisp, vendor-neutral overview.
- **[Anthropic — Building effective agents (blog + video)](https://www.anthropic.com/research/building-effective-agents)** — the definitive "what is an agent" essay from the people who build Claude.

## 📚 Read (10 min)

- 📄 [**Anthropic: Building effective agents**](https://www.anthropic.com/research/building-effective-agents) — *start here*.
- 📄 [**Simon Willison: What are AI agents, really?**](https://simonwillison.net/2025/May/22/tools-in-a-loop/) — the clearest one-paragraph definition on the internet.

---

## ✍️ Exercise (20 min)

1. Open your favorite agent tool (Cursor Agent, Claude Code, etc.).
2. Give it this prompt: *"List every file in this repo and summarize what each one does in one sentence."*
3. **Watch carefully.** Note down:
   - What tools did it invoke? (e.g., `list_files`, `read_file`)
   - How many steps did it take?
   - Did it ever get confused or ask you a question?
4. Write 3 sentences in your `learning-log.md`:
   - *"I saw the agent use these tools:…"*
   - *"The loop ran X times before finishing."*
   - *"One surprising thing was…"*

You just directly observed the agent loop. 🎉

---

## ✅ Self-check

Can you answer these without looking back?

1. What are the three generations of AI coding?
2. Draw the agent loop.
3. What's the difference between a **rule**, a **skill**, and an **MCP server**? (One-sentence answers are fine — we'll go deep later.)

---

## 🧭 Next

→ [Step 01 · Foundations of LLMs](./01-foundations.md) — *understand the brain before you drive the body.*
