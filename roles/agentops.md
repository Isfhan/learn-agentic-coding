# 🛡️ AgentOps / AI Reliability Engineer Track

> **⏱️ Time:** ~25 hours across the shared steps · **Track:** Tier 1 · **Start:** Step 07

The newest ops discipline: **running agents in production**. Agents fail differently than software — they hallucinate, loop forever, degrade silently after a model update, and can take unexpected actions. AgentOps engineers deploy, monitor, guardrail, and debug them. DevOps engineers can pivot here in 2–4 months; the pay premium is real.

---

## 💼 What this role actually does

- Deploys agents and their tooling to production (CI/CD for prompts, models, and tool configs).
- Builds **eval pipelines** so every change is tested before it ships (see [Step 14](../steps/14-evals-testing.md)).
- Instruments observability: traces every LLM call, tool call, token, and cost ([Step 19](../steps/19-agent-engineering.md)).
- Sets guardrails: approvals, sandboxes, rate limits, and refusal rules ([Step 15](../steps/15-security-safety.md)).
- Runs incident response for agent failures — the 2 AM "why did the agent email the wrong client?" role.

**You become:** the person who makes agents safe enough to leave unattended.

---

## 📊 Market snapshot (2026–2027)

| Signal | Number |
|---|---|
| Posting growth | Agentic AI postings +280% YoY (~90,000 US listings) |
| US salary | $185K–$320K base (+$40K–$120K equity at growth-stage) |
| Premium vs ML engineers | 15–20%+ |
| Entry path | SRE/DevOps/backend engineers pivot in ~2–3 months |
| 2027 outlook | AgentOps becomes a standard enterprise function; converges with MLOps/LLMOps |

Sources: The AI Career Lab 2026 guide, Futurum Group, Stanford AI Index (Sep 2026).

---

## 🗺️ Your step order (shared 21 steps, no new lessons)

| Priority | Steps |
|---|---|
| ● Core | 07, 11, 14, 15, 17, 19 |
| ◐ Optional | 08 (skills as reusable runbooks), 12 (multi-agent observability), 16 (understand the loop you're monitoring), 13 (context bloat = cost + drift) |
| ○ Skim | 00–06 (vocabulary only), 09, 10 (enough MCP to audit servers), 13.5, 18 |

Rationale: everything this role does is *governance of the agent loop* — rules/memory (07), hooks as enforcement (11), evals as tests (14), security (15), production patterns (17), and loop/graph/harness engineering (19). You audit the MCP servers more than you build them (09–10 skim is enough).

---

## 🧰 Tools of the trade

- **Evals:** promptfoo ([Step 14](../steps/14-evals-testing.md)) — your CI gate.
- **Observability:** LangSmith, Langfuse, Helicone, or OpenTelemetry traces (agentic spans are standardized now via W3C trace context).
- **Guardrails:** hooks ([Step 11](../steps/11-hooks-automation.md)), approval policies, shell allowlists ([Step 15](../steps/15-security-safety.md)).
- **Cost control:** token accounting per agent, per user, per run — context engineering ([Step 13](../steps/13-context-engineering.md)) is a cost lever, not just a quality lever.

---

## ➕ Role-only additions (what the steps don't cover)

### 1. Agent failure modes (the ops cheat sheet)

| Symptom | Likely cause | First check |
|---|---|---|
| Loops forever | Missing stop rule; tool keeps returning "success" without progress | Step 19 loop design; add max-iterations |
| Silent quality drop | Model updated, or prompt/tool changed without an eval | Eval suite diff; pin model versions |
| Hallucinated tool call | Vague tool descriptions; prompt injection | Tighten schemas; trusted-source policy |
| Cost spike | Context bloat; retry storms | Token telemetry; compaction ([Step 13](../steps/13-context-engineering.md)) |
| Unexpected action | Over-permissioned tools | Least privilege; HITL gates ([Step 15](../steps/15-security-safety.md)) |

### 2. The eval-first rollout

1. Every change to prompt, model, tool, or rules ships **only** through an eval-gated pipeline.
2. Keep a golden set of 20–50 cases ([Step 14](../steps/14-evals-testing.md) corpus) that never changes without review.
3. Record the failure rate before/after every release — trend it in a chart.

### 3. Incident response for agents

- Write an incident template: what the agent did, what it was supposed to do, the inputs, the tool calls, the model version.
- Reproduce first: the trace (every LLM/tool call) is your log. If you can't trace it, you can't debug it.
- Roll back the **config**, not just the code: prompts and rules are versioned artifacts too (git).

---

## 🚀 Track capstone

1. Build the [public agent capstone](../capstone/public-agent/README.md) core.
2. Then harden it like production:
   - Add an eval pipeline that runs in CI (this repo's [quality workflow](../.github/workflows/quality.yml) is your template).
   - Add trace logging to the [MCP server](../mcp/hn-context-server/server.js) (or your own agent).
   - Write 3 incident runbooks: loop, cost spike, tool misuse.
   - Post the write-up: *"I took an agent from demo to monitored production."*

---

## 📚 Resources

- [Step 14 · Evals & Testing](../steps/14-evals-testing.md) — your core skill.
- [Step 19 · Agent System Engineering](../steps/19-agent-engineering.md) — loop/graph/harness engineering.
- [Step 15 · Security & Safety](../steps/15-security-safety.md) — guardrails.
- [Evals in this repo](../evals/README.md) — a working promptfoo setup to copy.

---

## ✅ Self-check

1. Can you list 4 agent-specific failure modes and their first checks?
2. Do you have an eval pipeline that runs automatically, not "when I remember"?
3. Could you trace a failed agent run from a log today?
