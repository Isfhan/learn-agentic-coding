#!/usr/bin/env bash
set -u

payload="$(cat || true)"
command="$(printf "%s" "$payload" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')"

deny_pattern='(rm -rf|git push --force|git reset --hard|DROP TABLE|curl .*\\|\\s*sh)'

if [[ -n "${command:-}" && "$command" =~ $deny_pattern ]]; then
  printf '%s\n' '{"permission":"deny","user_message":"Blocked by hook: potentially destructive shell command.","agent_message":"Use a safer alternative or request explicit approval."}'
  exit 0
fi

printf '%s\n' '{"permission":"allow"}'
