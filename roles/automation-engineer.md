# ⚙️ Automation Engineer Track

> **⏱️ Time:** ~25 hours across the shared steps · **Track:** Tier 1 · **Start:** Step 00

Turns business processes into agent-powered workflows. The RPA (robotic process automation: scripted bots that click through screens) era is over — 2026 automation means **agentic systems** that reason, plan, and self-correct inside guardrails. This is the "AI that executes" role: invoice processing, support ticketing, data entry, approvals.

---

## 💼 What this role actually does

- Maps a business process (e.g., "new customer onboarding") into an automated workflow.
- Connects systems together: CRM, email, spreadsheets, databases, internal APIs — increasingly via MCP.
- Builds agents that do the judgment parts of the process, with human approval at risky steps.
- Maintains exception handling: what happens when the input is weird? (It always is.)
- Monitors runs, measures savings, and reports to business stakeholders.

**You become:** the person who removes whole categories of boring work from the team.

---

## 📊 Market snapshot (2026–2027)

| Signal | Number |
|---|---|
| Market shift | RPA → agentic platforms (UiPath renamed itself "Platform for Agentic Automation") |
| Enterprise adoption | 60% of new enterprise software projects include an agentic component |
| US salary | $150K–$250K (agentic automation specialists) |
| 2027 outlook | McKinsey: agents automate ~30% of knowledge-work tasks by end of 2027 |
| Entry path | DevOps/backend engineers can pivot in ~2–4 months of targeted upskilling |

Sources: Futurum Group, Automation Atlas (2026), Stanford AI Index, published salary surveys (Aug 2026).

---

## 🗺️ Your step order (shared 21 steps, no new lessons)

| Priority | Steps |
|---|---|
| ● Core | 00, 01, 02, 03, 09, 10, 11, 12, 15, 16 |
| ◐ Optional | 07 (rules for workflow repos), 08 (skills for repeatable automations), 13 (context: keep workflows focused), 14 (prove it works) |
| ○ Skim | 04, 05, 06 (one tool), 13.5, 17, 18, 19 |

Rationale: automation is 70% connectors (09–10), event triggers (11), orchestration (12), and safety (15). You build a *minimal* agent (16) because most business automation is small agents on big workflows — not one mega-agent.

---

## 🧰 Tools of the trade

- **Orchestration platforms:** n8n (self-hosted, developer-friendly), Zapier/Make (no-code), UiPath (enterprise RPA heritage).
- **Connectors:** MCP servers are the modern way to give agents access to your systems ([Step 10](../steps/10-mcp-building-servers.md)).
- **Triggers & hooks:** webhooks, schedules, and event hooks ([Step 11](../steps/11-hooks-automation.md)).
- **Guardrails:** human approval for writes, rate limits, alerting ([Step 15](../steps/15-security-safety.md)).

---

## ➕ Role-only additions (what the steps don't cover)

### 1. Workflow design patterns

- **Start narrow, prove value, expand** — the single most reliable playbook. A two-step classification-and-route workflow succeeds where end-to-end process automation fails.
- **Structured handoffs:** every step passes typed, validated data to the next (JSON schemas beat free text).
- **Design for exceptions:** the happy path is 60% of the work; the other 40% is "what if the PDF is a scan?".
- **Human-in-the-loop placement:** put approval gates at *irreversible or expensive* steps, not trivial ones.

### 2. MCP-as-connector patterns

- Wrap each legacy system in a small, read-only-first MCP server.
- Expose *few, focused* tools (see [Step 10](../steps/10-mcp-building-servers.md) tool design) — a connector with 3 good tools beats one with 30 sloppy ones.
- Never give a workflow write access it doesn't need (least privilege).

### 3. Measuring automation value

- Track: time saved, error rate before/after, and exception rate (how often the human had to jump in).
- Report in business terms: *"the workflow processes 200 invoices/week; humans review 15% of them instead of 100%."*

---

## 🚀 Track capstone

1. Build the [public agent capstone](../capstone/public-agent/README.md) core (agent + MCP + evals).
2. Then build **one real business workflow** for a process you actually have access to:
   - Pick something narrow (e.g., "email → CRM entry + Slack notification").
   - Wire it with n8n or a small agent + MCP server.
   - Add one human approval gate at the risky step.
   - Measure the before/after and write it up publicly.

---

## 📚 Resources

- [Step 10 · Building MCP Servers](../steps/10-mcp-building-servers.md) — your core skill.
- [Step 11 · Hooks & Automation](../steps/11-hooks-automation.md) — event-driven thinking.
- [Step 15 · Security & Safety](../steps/15-security-safety.md) — guardrails for unattended runs.
- [Practice projects](../projects/practice-projects.md).

---

## ✅ Self-check

1. Can you design a workflow that starts narrow and expands?
2. Have you built one connector (MCP server or API wrapper) that a real workflow uses?
3. Can you explain your last automation in business terms with a before/after number?
