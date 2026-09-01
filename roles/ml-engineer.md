# 🤖 ML Engineer (Applied) — Adjacent Track

> **⏱️ Time:** ~20 hours of this roadmap · **Track:** Tier 2 (adjacent) · **Start:** Step 00

The WEF projects AI/ML specialists as the **fastest-growing job by 2027** (~1M new jobs, +40%). This roadmap teaches the *applied, deployment-side* of that role: running models and agents in production. It deliberately does **not** teach model training, deep math, or statistics — those need additional learning (flagged below).

---

## 💼 What this role actually does

- Trains or fine-tunes models (traditional ML path — outside this roadmap).
- Ships models to production: serving, versioning, monitoring (the MLOps path — partially here).
- Builds LLM/agent systems on top of foundation models (the applied path — **this roadmap's sweet spot**).

If your target is pure model training, use this page as a *supplement*, not the main course.

---

## 📊 Market snapshot (2026–2027)

| Signal | Number |
|---|---|
| Growth | Fastest-growing job category by 2027 (WEF), +40% (~1M jobs) |
| Mid-level US salary | $140K–$170K |
| Senior | $200K+ at well-funded companies |
| Entry path | Strong Python + ML fundamentals; applied/agent skills are the differentiator |

Sources: WEF Future of Jobs, LinkedIn/Indeed salary data (Sep 2026).

---

## 🗺️ Your step order (shared 21 steps)

| Priority | Steps |
|---|---|
| ● Core | 00, 01, 02, 03, 13, 14, 16, 17, 19 |
| ◐ Optional | 09, 10 (MCP for serving/connectors), 11 (hooks), 15 (guardrails) |
| ○ Skim | 04, 05, 06, 07, 08, 12, 13.5, 18 |

---

## ⚠️ What this roadmap does NOT cover (add these)

- **ML fundamentals:** statistics, model training, PyTorch/TensorFlow, loss functions. Start with fast.ai or Andrew Ng's ML course, then the [books in resources](../resources/books-papers.md).
- **MLOps tooling:** model registries, feature stores, serving (vLLM, TGI), drift monitoring.
- **Evaluation science:** benchmark design, statistical significance of eval deltas.

---

## 🚀 Track capstone

1. Do the [main capstone](../capstone/public-agent/README.md).
2. Add the MLOps layer: containerize the agent, add tracing, write a monitoring runbook.
3. Optional stretch: serve a small open-weight model (Qwen3-Coder via Ollama/vLLM — see [Step 06](../steps/06-open-source-tools.md)) and route the agent to it for cheap tasks. Post the architecture publicly.

---

## ✅ Self-check

1. Do you know exactly which parts of "ML Engineer" this roadmap covers and which it doesn't?
2. Have you shipped one model-backed system with monitoring, not just a notebook?
