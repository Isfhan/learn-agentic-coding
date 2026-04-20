# Step 01 · Foundations of LLMs

> **⏱️ Time:** ~2 hours · **Prereq:** Step 00

You don't need a PhD. But you need *intuition* for how LLMs think, because **every weird agent behavior ultimately traces back to these fundamentals.**

---

## 🎯 What you'll learn

- What a **token** is and why it costs you money.
- What a **context window** is and why "just make it bigger" isn't the answer.
- What **temperature, top-p, and sampling** are — and when they matter for coding.
- Why LLMs **hallucinate**, and how that manifests in agents.
- The difference between a **base model**, **instruct model**, and **reasoning model**.

---

## 1. Tokens: the atomic unit of LLMs

LLMs don't see characters or words. They see **tokens** — chunks of ~¾ of an English word.

- `"hello"` → 1 token
- `"unbelievable"` → 3 tokens (`un`, `believe`, `able`)
- `"fn calculate_total(items: &Vec<Item>) -> u64"` → ~15 tokens

### Why it matters

- **You pay per token** (input + output).
- **The context window is measured in tokens**, not lines.
- **Code is token-dense** — JSON, minified code, and stack traces eat context fast.

### 🔧 Try it now

1. Go to [tiktokenizer.vercel.app](https://tiktokenizer.vercel.app/) or [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer).
2. Paste a random file from your project.
3. See how many tokens it is. Surprised?

---

## 2. The context window

The **context window** is the LLM's short-term memory. Everything the model sees for the next response goes in here:

```
┌────────────────────────────────────┐
│  SYSTEM PROMPT    ~2-10k tokens    │  ← set by the tool (Cursor, Claude)
├────────────────────────────────────┤
│  RULES / AGENTS.md   ~1-5k tokens  │  ← your project's persistent rules
├────────────────────────────────────┤
│  FILES READ BY AGENT  0-100k       │  ← read_file tool results
├────────────────────────────────────┤
│  CONVERSATION HISTORY  0-?         │  ← your prompts + its answers so far
├────────────────────────────────────┤
│  TOOL RESULTS  0-?                 │  ← shell output, test output, etc.
├────────────────────────────────────┤
│  CURRENT USER MESSAGE              │
└────────────────────────────────────┘
                 ↓
           LLM RESPONDS
```

Typical limits in 2026:

| Model family | Context window |
|--------------|----------------|
| GPT-5 / Codex | 200K–400K tokens |
| Claude Opus / Sonnet | 200K–1M tokens |
| Gemini 2.5 | 1M–2M tokens |
| Open-source (Qwen, Llama) | 128K–256K tokens |

### ⚠️ The cliff

Even if a model supports 1M tokens, **quality degrades sharply past ~32K–64K tokens**. This is called the "lost in the middle" problem. You'll hear about it again in [Step 13 · Context Engineering](./13-context-engineering.md).

> **Rule of thumb:** A focused 20K-token context beats a bloated 200K-token context on almost every task.

---

## 3. Sampling: temperature & top-p

When an LLM generates a response, it picks the next token from a probability distribution.

- **Temperature = 0** → always picks the most likely token. Deterministic. Best for code.
- **Temperature = 0.7** → more creative, more varied.
- **Temperature = 1.0+** → gets weird.

Most coding agents set temperature low (0–0.3) by default. You usually don't need to touch it.

**Top-p** (nucleus sampling) is a different lever: only sample from the top X% of probability mass. Use `top_p = 0.95` and temperature together — tweaking both is overkill for most coding tasks.

---

## 4. Why LLMs hallucinate (and what it means for agents)

An LLM is a **next-token prediction** engine trained on probabilities. It does not "know" things — it knows *what text usually follows what text*. When it's uncertain, it produces plausible-sounding nonsense. This is a **hallucination**.

In an agent loop, hallucinations compound:

1. Agent hallucinates that a file named `src/config.ts` exists.
2. Agent "edits" it (or fails, confused).
3. Failure gets written into context.
4. Next turn, agent might *still* act as if the file exists ← **context poisoning.**

**Mitigations you'll learn:**
- Force tool use for facts (*"verify by reading the file first"*). → Step 02
- Use rules to ground it in project truth. → Step 07
- Keep context clean. → Step 13

---

## 5. Base vs. Instruct vs. Reasoning models

| Type | What it is | Example | When coders use it |
|------|-----------|---------|---------------------|
| **Base model** | Raw next-token predictor, never RLHF'd | Llama 3 base | Almost never directly |
| **Instruct model** | Fine-tuned to follow instructions | GPT-4o, Claude Sonnet, Qwen Coder | Default for most agent work |
| **Reasoning model** | Generates a hidden "thinking" pass before answering | GPT-5, Claude Opus with extended thinking, DeepSeek R1 | Hard debugging, architecture, multi-step planning |

**Rule of thumb for coding:**

- Fast tasks (rename variable, add types) → **fast instruct model** (cheaper, faster)
- Hard tasks (unfamiliar bug, new architecture) → **reasoning model** (more expensive, slower, but fewer loops)

---

## 🎥 Watch

- **[Andrej Karpathy — Let's build GPT (2h)](https://www.youtube.com/watch?v=kCc8FmEb1nY)** — the single best "LLM from scratch" intro. Watch at 1.5x.
- **[3Blue1Brown — But what is a GPT? (27 min)](https://www.youtube.com/watch?v=wjZofJX0v4M)** — the prettiest visual explanation.
- **[Jay Alammar — The Illustrated Transformer (read, 20 min)](https://jalammar.github.io/illustrated-transformer/)** — legendary diagrams.

## 📚 Read

- 📄 [**Anthropic: Prompt engineering overview**](https://docs.anthropic.com/claude/docs/prompt-engineering) — short + practical.
- 📄 [**Lilian Weng: Prompt Engineering**](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) — comprehensive reference.
- 📄 [**Simon Willison — Hallucinations in code are the least dangerous form**](https://simonwillison.net/2025/Mar/2/hallucinations-in-code/) — beautiful short read.

---

## ✍️ Exercise (30 min)

Open [chat.openai.com](https://chat.openai.com) or [claude.ai](https://claude.ai) in a regular browser (*not* inside Cursor).

1. **Hallucination hunt:** Ask: *"What's the exact signature of `os.path.splitroot` in Python 3.9?"* (Hint: it was added in 3.12.) Observe whether the model admits ignorance or makes something up.
2. **Context limit:** Paste a **really long** file (>5000 lines). Ask for the first and last function. See what it remembers.
3. **Temperature feel:** If your tool lets you, run the same prompt at `temperature=0` and `temperature=1.0` three times each. Note the differences.

Log your observations.

---

## ✅ Self-check

1. You have a 2000-line TypeScript file. Roughly how many tokens is it?
2. Why might an agent "forget" a fact from earlier in the session?
3. When would you pick a reasoning model over an instruct model?

---

## 🧭 Next

→ [Step 02 · Prompt Engineering for Coders](./02-prompt-engineering.md)
