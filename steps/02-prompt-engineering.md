# Step 02 · Prompt Engineering for Coders

> **⏱️ Time:** ~2 hours · **Prereq:** Step 01

> *"The difference between a senior and a junior with the same AI tool is entirely in their prompts."*

---

## 🎯 What you'll learn

- A simple **5-part prompt template** for any coding task.
- How to give an agent **just enough** context (not too little, not too much).
- The difference between *asking* and *instructing*.
- Anti-patterns that silently waste your time.

---

## The 5-part prompt template

Great coding prompts almost always have these 5 parts, in order:

```
1. ROLE        → Who should the agent "be"?
2. GOAL        → What outcome do you want?
3. CONTEXT     → What does it need to know?
4. CONSTRAINTS → What should it NOT do?
5. FORMAT      → How should the output look?
```

### 🚫 Bad prompt
> "Add auth to my app."

### ✅ Good prompt
```text
ROLE: You are a TypeScript backend engineer familiar with Fastify.

GOAL: Add email/password authentication with JWT sessions to the /api routes.

CONTEXT: The project uses Fastify v5, Prisma with Postgres, and already has a
`User` model in prisma/schema.prisma. See src/routes/health.ts for the
routing pattern we use.

CONSTRAINTS:
- Do NOT install new dependencies beyond @fastify/jwt and bcrypt.
- Do NOT modify prisma/schema.prisma — I'll add the PasswordHash column myself.
- Passwords must be bcrypted with cost=12.
- Reject emails not matching a basic regex.

FORMAT: Give me a plan first as a numbered list, then wait for me to approve
before editing any files.
```

The second prompt will get you a useful result on the first try. The first prompt will get you a re-prompt loop.

---

## The #1 technique: "show, don't tell"

LLMs are pattern-matchers. **Examples beat explanations.**

### Explanation-only (weaker)
> "Follow our error-handling style."

### With example (stronger)
> "Follow our error-handling style. Example of what we do:
> ```ts
> try {
>   const user = await db.users.findUnique({ where: { id } });
>   if (!user) throw new AppError('user_not_found', 404);
> } catch (e) {
>   logger.error({ err: e, id }, 'failed to fetch user');
>   throw e;
> }
> ```"

Now the agent has a concrete pattern to mimic.

> 🧠 **Insight:** "A project's `AGENTS.md` is just a giant set of examples of how to act here." You'll build one in [Step 07](./07-rules-and-memory.md).

---

## The 7 power techniques

### 1. Chain of thought
> "Think step-by-step before writing code."

Not needed for reasoning models (they already do this internally), but massively helps non-reasoning models on tricky tasks.

### 2. Plan then execute
> "First produce a numbered plan. Do not write code until I reply `go`."

This one habit saves hours. You catch misunderstandings *before* files change.

### 3. Few-shot examples
Paste 2–3 before/after pairs of what you want. Especially powerful for refactors.

### 4. Force verification
> "Before claiming a file exists, use `read_file`. Before claiming a command works, run it with the shell tool."

Prevents hallucinations from compounding.

### 5. Ask for alternatives
> "Propose 3 different approaches with pros/cons. Don't pick one yet."

Turns the agent into a brainstorming partner instead of a code-emitter.

### 6. Constrain output
> "Output a unified diff only. No prose. No code fences."

Agents default to chatty prose. If you just want the patch, say so.

### 7. Ask it to critique itself
> "Now review the code you just wrote as if you were a senior engineer doing a code review. List the 3 biggest risks."

The model often catches its own bugs. Free QA round.

---

## Anti-patterns that waste your time

| 🚫 Anti-pattern | ✅ Do instead |
|----------|----------|
| "Fix the bug." | "The test `test_login_redirects` fails with `TypeError: null is not an object`. Find the root cause before changing anything." |
| Dumping 20 files into context | Point to 2-3 files and let the agent use `read_file` for the rest. |
| "Rewrite this to be better." | "Rewrite this for readability. Constraints: keep the public API; keep performance within 10%; add JSDoc to exported functions." |
| "Make it production-ready." | "Production-ready for *us* means: has unit tests, logs errors with our logger, and handles the 3 edge cases we hit before (empty, auth-expired, network-flaky)." |
| Asking follow-ups in a *huge* chat | Start a new session for a new task — clean context outperforms huge context. |

---

## Prompt recipes (steal these)

### 🔍 Exploration
> "Before I describe the task, explore this repo for me. Use `list_files`, then `read_file` on the 5 most architecturally important files. Summarize the architecture in a tree and a paragraph. Do not edit anything."

### 🐛 Bug hunt
> "Reproduce the bug described in `bug-report.md`. Add failing tests that demonstrate it. Do *not* fix it yet — I want to see the failing tests first."

### 🧪 Refactor
> "Refactor `src/x.ts` for [goal]. Follow these rules: 1) every commit must keep tests green; 2) break it into at most 5 small diffs; 3) pause after each for my review."

### 📖 Docs
> "Read `src/auth/`. Generate a `docs/auth.md` that: explains the flow in one diagram, lists every public function with a one-sentence description, and includes one end-to-end usage example that a new developer could copy."

### 🎯 Feature
> "Goal: [one sentence]. Examples of similar features we already built: [link file A, file B]. Non-goals: [what NOT to build]. Start with a plan, no code yet."

---

## 🎥 Watch

- **[Anthropic — Prompt Engineering Interactive Course](https://github.com/anthropics/prompt-eng-interactive-tutorial)** (self-paced notebooks, free, ~3h) — the single most respected prompt course.
- **[Andrej Karpathy — How I use LLMs (YouTube, 2h)](https://www.youtube.com/watch?v=EWvNQjAaOHw)** — how a legend *actually* prompts.
- **[Elvis Saravia — Prompt Engineering Guide (YouTube playlist)](https://www.youtube.com/@elvissaravia)** — regular, digestible updates.

## 📚 Read

- 📘 [**promptingguide.ai**](https://www.promptingguide.ai/) — the community-built canonical reference. Bookmark it.
- 📄 [**OpenAI Cookbook — Techniques to improve reliability**](https://cookbook.openai.com/articles/techniques_to_improve_reliability)
- 📄 [**Anthropic — Prompt engineering for Claude**](https://docs.anthropic.com/claude/docs/prompt-engineering)
- 📘 [**GitHub: dair-ai/Prompt-Engineering-Guide**](https://github.com/dair-ai/Prompt-Engineering-Guide) — 40k⭐ curated repo.

---

## ✍️ Exercise (45 min)

Take a real task from your own project (or invent one: "Add rate limiting to the login endpoint").

1. Write a **bad prompt** (one sentence, no context). Run it. Save the result as `bad.md`.
2. Rewrite it using the **5-part template**. Run it. Save as `good.md`.
3. Diff the two outputs. Write 3 sentences in your learning log about the difference.

Bonus: post both prompts side-by-side on Twitter/X with `#AgenticCoding`. It's a relatable format that gets engagement.

---

## ✅ Self-check

1. What are the 5 parts of a great coding prompt?
2. Why do examples outperform explanations?
3. When should you start a *new* chat instead of continuing?

---

## 🧭 Next

→ [Step 03 · The AI Coding Tool Landscape](./03-ai-coding-tools.md)
