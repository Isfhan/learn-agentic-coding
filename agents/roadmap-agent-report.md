# Roadmap Agent Run Report

Task: Summarize roadmap

## Observations
```text
Step 1 / read_file
SUCCESS
# 🗺️ The Visual Roadmap

> A one-page big picture. Print it, screenshot it, put it on your desk.
>
> **Last verified: September 2026.** See [README.md](./README.md#-currency) for refresh guidance.

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

    subgraph P4["🧠 Phase 4 · Architect (Steps 14-19)"]
        direction TB
        D1[Evals] --> D2[Security] --> D3[Build from scratch] --> D4[Advanced patterns] --> D5[Agent system engineering] --> D6[Stay current]
    end

    P1 --> P2 --> P3 --> P4

    style P1 fill:#FAFAFA,stroke:#0A0A0A
    style P2 fill:#F5F5F5,stroke:#EF4444
    style P3 fill:#E5E5E5,stroke:#DC2626
    sty
```

## Final Summary
This reference runtime demonstrates the core agent pattern:
1) maintain context state
2) choose a tool
3) execute safely
4) evaluate output
5) iterate until done