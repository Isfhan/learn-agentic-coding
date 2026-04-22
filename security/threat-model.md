# Threat Model for Agentic Coding Setup

## Scope

- Local coding agent with shell/file tools
- MCP servers (local stdio)
- Git workflow and repository artifacts

## Assets

- Source code integrity
- Secrets/tokens
- Build/release pipeline trust
- Developer workstation state

## Trust boundaries

1. User intent -> agent execution
2. Agent -> shell commands
3. Agent -> MCP server -> external APIs
4. Repository -> CI/CD

## Top threats and controls

| Threat | Risk | Control |
|---|---|---|
| Secret leakage into git | High | `.env` ignore rules, redaction checks, least-privilege tokens |
| Destructive shell command | High | `beforeShellExecution` deny hook + HITL approval |
| Prompt injection via docs/web | Medium | trusted-source policy, explicit tool constraints |
| Over-permissioned MCP server | High | expose minimal tool surface, read-only default |
| Hallucinated file/tool action | Medium | require verify step + eval checks + guarded commands |
| Supply chain risk in dependencies | Medium | pin dependencies, use trusted registries |

## Abuse cases

1. Agent is tricked into `git push --force`.
2. Agent reads secret file and prints token in output.
3. MCP tool with write access modifies production data accidentally.

## Mitigations checklist

- [x] Hook blocks dangerous shell patterns
- [x] Least privilege principle documented
- [x] Evals added for reliability checks
- [x] Human approval required for irreversible actions
- [x] Threat model reviewed before capstone publish
