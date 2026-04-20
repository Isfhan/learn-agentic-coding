# Step 06 · Open-Source Coding Agents

> **⏱️ Time:** ~2 hours · **Prereq:** Step 05

Closed tools are convenient. Open-source tools give you **privacy, portability, and understanding** — you can literally read how the agent loop is implemented.

---

## 🎯 What you'll learn

- The four flagship OSS coding agents: **Aider, Cline, Continue, Qwen Code**.
- When to reach for OSS vs. a commercial tool.
- How to run an agent fully **local** (no cloud) with Ollama + Qwen.
- A mental model of "agent internals" you'll reuse in Step 16.

---

## The contenders at a glance

| Tool | Shape | Stars | Vibe |
|------|-------|-------|------|
| **Aider** | CLI | 40k+ | Unix-philosophy. Git-native. Token-efficient. |
| **Cline** | VS Code extension | 57k+ | Autonomous with step approval. Polished UI. |
| **Continue** | VS Code + JetBrains | 26k+ | Most configurable. Great autocomplete + chat. |
| **Qwen Code** | CLI | Growing fast | Alibaba's open-source agent. Runs massive local models. |

All are **free** — you pay only for LLM tokens (or zero if you self-host).

---

## 1. Aider — the terminal minimalist

```bash
pip install aider-install
aider-install
aider
```

**Why it's special:**
- Auto-commits every change with a clear message.
- "Repo map" summarizes your codebase into a few thousand tokens instead of dumping whole files → ~40% fewer tokens than Cline for multi-file work.
- Works with 75+ model providers.

**Killer workflow:**
```bash
# Use Claude for the plan, GPT-4o for edits
aider --architect --editor-model openai/gpt-4o --model anthropic/claude-sonnet
```
"Architect mode" lets a strong reasoning model plan, while a faster/cheaper model does the mechanical edits.

---

## 2. Cline — the autonomous VS Code extension

- Install from the VS Code marketplace.
- Shows every step (read this file, run this command, edit this) and asks approval.
- Great for regulated environments needing audit trails.
- Supports 75+ providers; also supports **Plan vs. Act modes**.

**Killer feature:** it can control a **real browser** natively, which is gold for frontend work.

---

## 3. Continue — the customizer's dream

- VS Code + JetBrains.
- Config via a YAML file — you define exactly which models handle chat, autocomplete, edits.
- Slash commands, context providers (`@codebase`, `@docs`, `@terminal`), and custom actions.
- Best if you want a **team-shareable AI config** checked into git.

Example `config.yaml`:

```yaml
models:
  - name: Claude Sonnet
    provider: anthropic
    model: claude-sonnet-4.5
    roles: [chat, edit]
  - name: Qwen 2.5 Coder
    provider: ollama
    model: qwen2.5-coder:7b
    roles: [autocomplete]
contextProviders:
  - name: codebase
  - name: docs
```

---

## 4. Qwen Code — open, powerful, self-hostable

Alibaba's answer to Claude Code. Open source under a permissive license; pair with the Qwen3-Coder family (up to 480B params).

```bash
npm i -g @qwen-code/qwen-code
qwen
```

Why it's exciting:
- **Fully self-hostable** — zero cloud calls if you run Qwen locally via vLLM or Ollama.
- **Strong autonomy** — designed for agentic multi-turn planning.
- **Open license** — you can modify the agent loop itself.

---

## 5. Run an agent fully local (privacy mode)

A fun exercise that'll make you popular at work:

### Setup (15 min)

```bash
# 1. Install Ollama: https://ollama.com
# 2. Pull a coding model
ollama pull qwen2.5-coder:7b  # ~4 GB, runs on a M1 Mac with 16GB RAM

# 3. Point Aider at it
aider --model ollama/qwen2.5-coder:7b --no-auto-commits
```

Now you have a coding agent running **completely offline**. No API keys, no data leaving your machine.

> ⚠️ Quality is noticeably below Claude/GPT. Use for privacy-critical tasks or experimentation, not everything.

---

## 6. Mental model: "what's actually inside"

Every OSS agent does roughly this:

```python
def agent(goal, context, tools):
    while True:
        # 1. Assemble the prompt
        prompt = system_prompt + context + goal + tool_schemas

        # 2. Call the LLM
        response = llm.chat(prompt, tools=tools)

        # 3. If the LLM chose a tool, run it
        if response.wants_tool():
            tool_result = run_tool(response.tool_name, response.args)
            context += tool_result
            continue

        # 4. Otherwise, it's done
        return response.message
```

**That is the entire core.** Cursor, Claude Code, Cline, and Aider all build on this — the differences are:

- Which tools are exposed (read_file, shell, browser, MCP…)
- How context gets trimmed/summarized
- UX around approvals, diffs, history

Pick an OSS agent and **read its main loop file**. Aider's is in `aider/coders/base_coder.py`; Cline's is in `src/core/`. You'll never fear agents again.

---

## 7. When to pick what

| Situation | Reach for |
|-----------|-----------|
| Terminal person, token-conscious | **Aider** |
| Need approvals / audit trail | **Cline** |
| Polyglot IDE team (VS Code + JetBrains) | **Continue** |
| Air-gapped / regulated / privacy-critical | **Qwen Code** + Ollama |
| You want to *read* the agent source | Any of the above |

---

## 🎥 Watch

- **[Aider walkthrough](https://www.youtube.com/results?search_query=aider+ai+tutorial+2026)** — search recent videos.
- **[Cline in VS Code — real workflow](https://www.youtube.com/results?search_query=cline+vs+code+tutorial+2026)**
- **[Continue.dev official channel](https://www.youtube.com/@continuedev)**
- **[Running local LLMs with Ollama](https://www.youtube.com/results?search_query=ollama+local+llm+coding+agent)**

## 📚 Read

- 📘 [**Aider** (GitHub)](https://github.com/paul-gauthier/aider)
- 📘 [**Cline** (GitHub)](https://github.com/cline/cline)
- 📘 [**Continue** (GitHub)](https://github.com/continuedev/continue)
- 📘 [**Qwen Code** (GitHub)](https://github.com/QwenLM/qwen-code)
- 📄 [**"Aider vs Cline vs Continue" (vibecodemeta)**](https://vibecodemeta.com/blog/aider-vs-cline-vs-continue/)
- 📄 [**"Best Open-Source AI Coding Agents 2026"**](https://cssauthor.com/best-open-source-ai-coding-agents/)

---

## ✍️ Exercise (45 min)

1. Install **Aider** and give it a real task on one of your projects.
2. Pick one OSS agent repo (Aider, Cline, or Continue). Open its main file on GitHub. Read the agent loop. Can you map it to the pseudocode above?
3. Bonus: install **Ollama**, pull `qwen2.5-coder:7b`, and run Aider fully offline on a toy task.
4. Log:
   - What surprised you about the source code?
   - Which OSS tool would you bring to a privacy-sensitive job?

---

## ✅ Self-check

1. What's the "repo map" and why does it matter?
2. What are the 4 steps of every agent loop?
3. Which OSS tool would you pick for an air-gapped environment?

---

## 🧭 Next

→ [Step 07 · Rules & Memory](./07-rules-and-memory.md)
