# 🗺️ The Visual Roadmap

> A one-page big picture. Print it, screenshot it, put it on your desk.

---

## The 4 learning phases

```mermaid
flowchart LR
    subgraph P1["🌱 Phase 1 · Foundations (Steps 00-03)"]
        direction TB
        A1[Understand agents] --> A2[LLM basics] --> A3[Prompting] --> A4[Tool landscape]
    end

    subgraph P2["🛠️ Phase 2 · Operator (Steps 04-08)"]
        direction TB
        B1[Cursor] --> B2[Claude Code] --> B3[OSS CLIs] --> B4[Rules] --> B5[Skills]
    end

    subgraph P3["🔌 Phase 3 · Extender (Steps 09-13.5)"]
        direction TB
        C1[MCP intro] --> C2[Build MCP server] --> C3[Hooks] --> C4[Subagents] --> C5[Context engineering] --> C6[Spec-Driven Dev]
    end

    subgraph P4["🧠 Phase 4 · Architect (Steps 14-18)"]
        direction TB
        D1[Evals] --> D2[Security] --> D3[Build from scratch] --> D4[Advanced patterns] --> D5[Stay current]
    end

    P1 --> P2 --> P3 --> P4

    style P1 fill:#dbeafe,stroke:#3b82f6
    style P2 fill:#dcfce7,stroke:#16a34a
    style P3 fill:#fce7f3,stroke:#db2777
    style P4 fill:#fef3c7,stroke:#d97706
```

---

## Skill progression

| Phase | After this phase you can… |
|-------|----------------------------|
| **🌱 Foundations** | Explain what an agent is, pick a tool, write prompts that don't waste tokens. |
| **🛠️ Operator** | Use Cursor & Claude Code at near-expert level. Configure rules and skills that make you 2-5x faster. |
| **🔌 Extender** | Plug agents into any data source via MCP. Automate pre/post-agent steps with hooks. Run multi-agent workflows. Drive features from specs (GitHub Spec Kit). |
| **🧠 Architect** | Write evals, harden for production, build agents from scratch with the SDK, design multi-agent systems. |

---

## Decision tree: *where should I start?*

```mermaid
flowchart TD
    Q1{Have you ever<br/>used Cursor or<br/>Claude Code?}
    Q1 -->|No| S0[Start at Step 00]
    Q1 -->|Yes| Q2{Do you know<br/>what MCP is?}
    Q2 -->|No| S4[Start at Step 04<br/>but skim 00-03]
    Q2 -->|Yes| Q3{Have you built<br/>an MCP server?}
    Q3 -->|No| S9[Start at Step 09]
    Q3 -->|Yes| Q35{Do you use<br/>Spec-Driven<br/>Development?}
    Q35 -->|No| S135[Start at Step 13.5]
    Q35 -->|Yes| Q4{Do you write<br/>evals for agents?}
    Q4 -->|No| S14[Start at Step 14]
    Q4 -->|Yes| S17[You're ahead!<br/>Go to Step 17]

    style S0 fill:#6366f1,color:#fff
    style S4 fill:#10b981,color:#fff
    style S9 fill:#ef4444,color:#fff
    style S135 fill:#0ea5e9,color:#fff
    style S14 fill:#f59e0b,color:#fff
    style S17 fill:#8b5cf6,color:#fff
```

---

## The 3-week plan

> Work through the roadmap on a sustainable schedule.

### Week 1 — Foundations & Operator
| Day | Steps | Outcome |
|-----|-------|---------|
| Mon | 00, 01 | Know the vocabulary |
| Tue | 02 | Write better prompts immediately |
| Wed | 03, 04 | Cursor configured for your workflow |
| Thu | 05 | Claude Code running in terminal |
| Fri | 06 | Try one OSS CLI (Aider or Cline) |
| Weekend | **Mini project:** refactor an old side-project using an agent end-to-end |

### Week 2 — Extender
| Day | Steps | Outcome |
|-----|-------|---------|
| Mon | 07 | `.cursor/rules/` and `AGENTS.md` set up |
| Tue | 08 | Your first custom skill |
| Wed | 09 | MCP big picture locked in |
| Thu | 10 | **Your own MCP server running** |
| Fri | 11 | Hooks running on every session |
| Weekend | **Mini project:** build an MCP server that connects Claude to a real API you use |

### Week 3 — Architect
| Day | Steps | Outcome |
|-----|-------|---------|
| Mon | 12 | Multi-agent delegation working |
| Tue | 13, 13.5 | Context engineering applied; spec-driven workflow running via GitHub Spec Kit |
| Wed | 14 | You have 10+ evals for your agent |
| Thu | 15 | Threat-modeled your agent setup |
| Fri | 16 | Agent-from-scratch in ~200 lines |
| Weekend | **Capstone:** ship a public agent on GitHub with README + evals + MCP server |

---

## Track your progress

Copy this into a `learning-log.md` in your own repo:

```markdown
- [ ] 00 · Introduction
- [ ] 01 · Foundations
- [ ] 02 · Prompt Engineering
- [ ] 03 · Tool Landscape
- [ ] 04 · Cursor Mastery
- [ ] 05 · Claude Code Mastery
- [ ] 06 · Open-Source Tools
- [ ] 07 · Rules & Memory
- [ ] 08 · Skills
- [ ] 09 · MCP Introduction
- [ ] 10 · Building MCP Servers
- [ ] 11 · Hooks & Automation
- [ ] 12 · Subagents & Orchestration
- [ ] 13 · Context Engineering
- [ ] 13.5 · Spec-Driven Development
- [ ] 14 · Evals & Testing
- [ ] 15 · Security & Safety
- [ ] 16 · Build Your Own Agent
- [ ] 17 · Advanced Patterns
- [ ] 18 · Staying Current
```

Post your completed check-list on Twitter/X with `#AgenticCoding` and tag the repo. 💪
