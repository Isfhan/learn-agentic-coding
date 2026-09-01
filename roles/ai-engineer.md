# 👨‍💻 AI Engineer / AI Agent Developer Track

> **⏱️ Time:** ~30 hours across the shared steps · **Track:** Tier 1 · **Start:** Step 00

Builds the agent systems themselves: LLM apps, RAG, tool use, orchestration, evals. The role LinkedIn ranks #1 fastest-growing in 2026 (+143% postings) — and it's exactly what this roadmap's core was built to teach.

---

## 💼 What this role actually does

- Wires LLM APIs into products (chat, copilots, automation).
- Builds agents that use tools: read files, call APIs, run code, decide next steps.
- Designs RAG (retrieval pipelines) so the model answers from *your* data, not guesswork.
- Sets up evals so you can prove the agent got better, not just feel it.
- Ships to production: prompts, models, context, cost, and failure modes are all your problem.

**You become:** the person who turns "can we make AI do X?" into a working system.

---

## 📊 Market snapshot (2026–2027)

| Signal | Number |
|---|---|
| Posting growth | +143% YoY (LinkedIn, 2026); 13x role growth in 2 years |
| Mid-level US salary | $130K–$160K (median ~$154K, Levels.fyi) |
| Senior / frontier labs | $180K–$300K+ |
| Remote share | ~85% of AI agent developer postings (2026) |
| 2027 outlook | Strongest growth continues; agent-specific roles are the fastest subcategory |

Sources: LinkedIn Jobs on the Rise 2026, Indeed Hiring Lab, Stanford AI Index 2026, Levels.fyi (Sep 2026).

---

## 🗺️ Your step order (shared 21 steps, no new lessons)

| Priority | Steps |
|---|---|
| ● Core | 00, 01, 02, 03, 07, 08, 09, 10, 12, 13, 13.5, 14, 16, 17, 19 |
| ◐ Optional | 11 (hooks — useful for CI agents), 05 (pick your daily CLI) |
| ○ Skim | 04, 06 (one tool deep is enough), 15 (read the threat model once), 18 |

Suggested order: 00→03 (foundations), 07→08 (rules/skills), 09→10 (MCP), 12→13→13.5 (orchestration + specs), 14 (evals), 16→17→19 (build, patterns, engineering).

---

## 🧰 Tools of the trade

- **Frameworks:** LangGraph, OpenAI Agents SDK, PydanticAI, CrewAI, smolagents (see [Step 16](../steps/16-build-your-own-agent.md#frameworks) for the full table).
- **Evals:** promptfoo, LangSmith, Braintrust (see [Step 14](../steps/14-evals-testing.md)).
- **MCP:** build your own servers ([Step 10](../steps/10-mcp-building-servers.md)) — this is a differentiator on resumes.
- **Specs:** GitHub Spec Kit or OpenSpec for larger features ([Step 13.5](../steps/13.5-spec-driven-development.md)).

---

## ➕ Role-only additions (what the steps don't cover)

### 1. Framework selection cheat sheet

| Situation | Pick |
|---|---|
| Production-grade graph workflows (loops, branches, human-in-the-loop) | **LangGraph** |
| Quick single-agent tool-calling app | **OpenAI Agents SDK** or **PydanticAI** |
| Type-safe Python, minimal ceremony | **PydanticAI** |
| Multi-agent role-play teams (research/write/review) | **CrewAI** |
| Lightweight, runs anywhere | **smolagents** |

Rule of thumb: for your portfolio, build one agent *without* a framework (Step 16 style) so you understand the loop, then one *with* a framework so you can answer interview questions about both.

### 2. RAG essentials

- Chunk well, embed well, retrieve top-k, and always cite sources in the answer.
- Start without a vector DB: a simple keyword/BM25 search over your docs is often enough.
- Evaluate retrieval + generation separately (see [Step 14](../steps/14-evals-testing.md)).

### 3. Interview prep

- Be ready to draw the agent loop ([Step 00](../steps/00-introduction.md)) on a whiteboard.
- Have 3 evals that prove your portfolio agent works (a hiring manager asks for these in 2026).
- Practice "context engineering" answers: what do you put in the context window and why ([Step 13](../steps/13-context-engineering.md)).

---

## 🚀 Track capstone

Ship one public agent repo (this also satisfies the [main capstone](../capstone/public-agent/README.md)):

1. An agent with at least 3 tools (read/search/shell or an MCP server).
2. A `AGENTS.md` with rules, plus one custom skill.
3. An eval suite with 10+ cases, `promptfoo eval` passing or documented as skipped.
4. A README that explains the loop, the context strategy, and the threat model.
5. Post it publicly with `#AgenticCoding`.

**Hiring tip:** 3 small shipped things (agent + MCP server + eval suite) beat one unfinished monorepo.

---

## 📚 Resources

- [Step 16: Build Your Own Agent](../steps/16-build-your-own-agent.md) — the core exercise for this role.
- [Step 17: Advanced Patterns](../steps/17-advanced-patterns.md) — the patterns interviewers name-drop.
- [Resources index](../resources/README.md) — books, papers, communities.
- [Practice projects](../projects/practice-projects.md) — pick 2–3 to fill your portfolio.

---

## ✅ Self-check

1. Can you draw the agent loop from memory?
2. Can you explain why evals matter more than "it felt better"?
3. Do you have 3 shipped, public artifacts an interviewer could open?
