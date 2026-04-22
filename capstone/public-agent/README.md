# Public Agent Capstone

This capstone packages a complete agentic engineering artifact with:

- custom agent runtime (`agents/roadmap_agent.py`)
- MCP server with real API integration (`mcp/hn-context-server/server.js`)
- eval suite (`evals/promptfooconfig.yaml`)
- safety model (`security/threat-model.md`)
- persistent project context (`AGENTS.md`, `.cursor/rules/`, `.cursor/skills/`, hooks)

## Capstone goals

1. Demonstrate end-to-end agent loop design.
2. Demonstrate MCP interoperability with a live API.
3. Demonstrate quality gates using evals.
4. Demonstrate security controls (least privilege + blocked dangerous shell patterns).

## Runbook

### 1) Run custom agent

```bash
python agents/roadmap_agent.py --task "Summarize roadmap" --max-steps 4
```

### 2) Run MCP server

```bash
node mcp/hn-context-server/server.js
```

### 3) Execute evals

```bash
promptfoo eval -c evals/promptfooconfig.yaml
```

## Test plan

- [ ] Agent report file is generated.
- [ ] MCP server responds to `initialize`, `tools/list`, and `tools/call`.
- [ ] Eval suite runs with 10+ tests and reports pass/fail.
- [ ] Threat model reviewed and controls mapped to implementation.

## Deliverable checklist

- [x] README with usage + test plan
- [x] Evals config
- [x] MCP server
- [x] Security/threat model
- [x] Learning log

## Share template (X / Twitter)

Use the draft in `capstone/public-agent/x-post-draft.md`.
