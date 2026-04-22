---
name: roadmap-execution
description: Execute the Agentic Coding Roadmap end-to-end with weekly deliverables, including decision-tree start selection, learning-log updates, MCP integration, hooks, evals, threat modeling, and capstone packaging. Use when the user asks to implement or operationalize this roadmap in a repository.
---

# Roadmap Execution

## Goal
Turn roadmap learning steps into concrete repository artifacts that demonstrate operator, extender, and architect-level capability.

## Workflow
1. Pick start step using the decision tree in `ROADMAP.md`.
2. Initialize `learning-log.md` and track completed steps.
3. Build week 1 outputs (tooling setup notes, mini project evidence).
4. Build week 2 outputs (rules, skill, MCP server, hooks).
5. Build week 3 outputs (eval suite, threat model, custom agent).
6. Package capstone with runbook and public-sharing draft.
7. Add staying-current cadence and review checklist.

## Required Outputs
- Learning log with checked progress.
- At least one project rule and one custom skill.
- One MCP server connected to a real API.
- Hooks configuration with safety gating.
- Eval config with 10+ tests.
- Threat model document.
- Build-your-own-agent implementation (~200 lines).
- Capstone README with test plan.

## Quality Gates
- No secrets in source control.
- Clear instructions to run each artifact.
- Explicit industry terms followed by plain-language meaning.
