# 🚀 Forward Deployed Engineer (FDE) Track

> **⏱️ Time:** ~30 hours across the shared steps · **Track:** Tier 1 · **Start:** Step 00

The hottest enterprise-AI role of 2026: postings up **800%+ year-over-year**, 42x role growth in two years. An FDE embeds inside customer environments, builds working agent systems on their messy legacy infrastructure, and owns the outcome end-to-end. Part engineer, part consultant.

---

## 💼 What this role actually does

- Sits inside (or beside) a customer's team, not in your own office.
- Takes a demo'd AI capability and makes it work in *their* environment: their data, their security, their legacy systems.
- Writes production code on-site: Python, full-stack, agent workflows, MCP connectors.
- Measures and defends the outcome: "did the customer's workflow actually get faster?"
- Translates technical trade-offs into decisions for non-technical executives.

**You become:** the person who turns "AI that works in a demo" into "AI that works in production."

---

## 📊 Market snapshot (2026–2027)

| Signal | Number |
|---|---|
| Posting growth | +800% YoY (187 → 450+ US listings across scans) |
| Role growth | 42x over 2 years (fastest-growing technical title) |
| US salary | $150K–$325K disclosed bands; $500K+ at frontier labs |
| Employers | OpenAI, Anthropic, Palantir, Scale AI, Salesforce, Snowflake, TCS (8,900 FDE roles), Tredence (200 FDEs) |
| 2027 outlook | Enterprise AI's biggest bottleneck — demand keeps outpacing supply |

Sources: Dexity JD scan (2026), jobsbyculture/Stanford AI Index (2026), AEI analysis (May 2026).

---

## 🗺️ Your step order (shared 21 steps, no new lessons)

| Priority | Steps |
|---|---|
| ● Core | 00, 01, 02, 03, 05, 09, 10, 13.5, 14, 15, 16, 19 |
| ◐ Optional | 11 (hooks for safety), 12 (multi-agent in customer stacks), 17 (patterns) |
| ○ Skim | 04, 06, 08, 18 |

Rationale: FDEs live in terminals and deploys (05), ship MCP connectors into customer systems (09–10), run spec-driven work under delivery pressure (13.5), prove quality with evals (14), and must threat-model what they build (15). Step 19's loop/graph/harness engineering is your production-level crown.

---

## 🧰 Tools of the trade

- **Daily driver:** Claude Code or Codex CLI (terminal-first, works over SSH into customer environments).
- **Stack:** Python + full-stack basics (JS/TS), cloud (AWS/GCP), Docker.
- **Connectors:** MCP servers for customer APIs, databases, and internal tools ([Step 10](../steps/10-mcp-building-servers.md)).
- **Specs:** GitHub Spec Kit — customers need to approve *what* before you build it ([Step 13.5](../steps/13.5-spec-driven-development.md)).
- **Evals + observability:** promptfoo, LangSmith/Langfuse — you must show improvement, not claim it ([Step 14](../steps/14-evals-testing.md)).

---

## ➕ Role-only additions (what the steps don't cover)

### 1. Client-facing communication

- Practice the **1-minute executive brief**: problem → what we built → measured result → next step.
- Keep a decision log: every technical choice you make for a customer, plus why.
- Learn to say "no" with an alternative: *"We can't ship that this week; here's the 80% version that ships today."*

### 2. Deploying into legacy environments

- Assume constraints: air-gapped networks, old Python/Node versions, no Docker, strict change windows.
- Design for **fallback**: if the agent fails, the old manual process must still work (see [Step 15](../steps/15-security-safety.md) threat modeling).
- Document exactly what runs where, with which credentials, and how to roll back.

### 3. Outcome ownership

- Agree on **one success metric** with the customer before you start (time saved, error rate, tickets resolved).
- Instrument it from day one — "we improved X by 30%" needs a before/after number.
- Write the handover: the customer's own team must run the system after you leave.

---

## 🚀 Track capstone

1. Build the [public agent capstone](../capstone/public-agent/README.md) (it proves the full loop).
2. Then simulate an FDE deployment:
   - Pick a *small real business process* you can observe (e.g., a friend's shop, a club, a local org).
   - Deploy one agent that automates a narrow piece of it, *in their environment*.
   - Measure before/after with a number.
   - Write a one-page handover document a non-technical person can read.
3. Post the story publicly — FDE hiring managers look for exactly this kind of evidence: *"owned a deployment inside a real environment."*

---

## 📚 Resources

- [Step 19 · Agent System Engineering](../steps/19-agent-engineering.md) — includes the roadmap-to-FDE skill map.
- [Step 15 · Security & Safety](../steps/15-security-safety.md) — non-negotiable for customer work.
- [Step 05 · Claude Code Mastery](../steps/05-claude-code-mastery.md) — the FDE daily driver.
- [Resources index](../resources/README.md).

---

## ✅ Self-check

1. Can you explain to a non-technical person what your agent does and why it's trustworthy?
2. Have you shipped (not just built) one agent into a real environment with a measured outcome?
3. Do you have a one-page handover document example in your portfolio?
