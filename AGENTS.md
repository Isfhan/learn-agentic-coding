# Agentic Coding Roadmap Workspace

## Stack
- Markdown docs
- Mermaid diagrams
- Node.js (for MCP example server)
- Python (for build-your-own-agent example)

## Structure
- `steps/`: 20 step files (00-18, including 13.5)
- `resources/`: external references and cheatsheets
- `.cursor/rules/`: persistent project guidance
- `.cursor/skills/`: reusable agent capabilities
- `.cursor/hooks.json`: event-driven guardrails
- `mcp/`: MCP sample servers
- `evals/`: quality checks
- `agents/`: custom agent examples
- `capstone/`: public-facing final artifact

## Conventions
- Keep examples production-minded and security-aware.
- Prefer small, testable artifacts over large monolithic demos.
- Explain industry terms with plain-English meaning in parentheses on first use, especially for non-native English readers.
- Prefer clear words over slang. If a common AI phrase is useful, keep it and add the plain meaning.

## Commands
- `node mcp/hn-context-server/server.js`
- `python agents/roadmap_agent.py --task "Summarize roadmap"`
- `python -m py_compile agents/roadmap_agent.py`

## Before done
- Verify docs are linked and runnable snippets are consistent.
- Ensure hooks, evals, and threat model are present.

## Don'ts
- Do not put secrets in tracked files.
- Do not expose destructive tools without HITL approval.
- Do not ship "vibe-only" (guesswork-only) changes without eval evidence.
