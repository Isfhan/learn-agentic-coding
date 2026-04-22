# Roadmap Implementation Journal

## Week 1 (Foundations + Operator)

- Completed steps 00-06 in sequence.
- Cursor setup documented via `AGENTS.md` and `.cursor/rules/agentic-roadmap.mdc`.
- Claude Code and one OSS CLI represented in workflow notes and command references.
- Mini refactor project logged in `projects/mini-refactor-project.md`.

## Week 2 (Extender)

- Added first custom skill: `.cursor/skills/roadmap-execution/SKILL.md`.
- Built MCP server connected to live Hacker News API: `mcp/hn-context-server/server.js`.
- Added hooks automation and shell safety gate: `.cursor/hooks.json`, `.cursor/hooks/block-dangerous-shell.sh`.

## Week 3 (Architect)

- Added eval suite with 12 tests: `evals/promptfooconfig.yaml`.
- Added threat model: `security/threat-model.md`.
- Added build-your-own-agent implementation (~200 lines): `agents/roadmap_agent.py`.
