#!/usr/bin/env node
"use strict";

/**
 * beforeShellExecution hook — blocks known-dangerous shell commands.
 * Reads JSON from stdin; writes permission JSON to stdout.
 */

const BLOCKED = [
  "rm -rf",
  "rm -fr",
  "git push --force",
  "git push -f",
  "git reset --hard",
  "drop table",
  "truncate table",
  "curl | sh",
  "curl | bash",
  "wget | sh",
  "del /f",
  "rd /s",
  "remove-item",
  "format c:",
  "mkfs",
  "shutdown",
  ":(){ :|:& };:",
];

function readStdinSync() {
  try {
    if (process.stdin.isTTY) return "";
    const fs = require("node:fs");
    return fs.readFileSync(0, "utf8");
  } catch {
    return "";
  }
}

function extractCommand(input) {
  if (!input || !input.trim()) {
    return process.env.CURSOR_SHELL_COMMAND || "";
  }
  try {
    const parsed = JSON.parse(input);
    if (typeof parsed.command === "string") return parsed.command;
    if (parsed.command && typeof parsed.command.command === "string") {
      return parsed.command.command;
    }
  } catch {
    const match = input.match(/"command"\s*:\s*"([^"]*)"/);
    if (match) return match[1];
  }
  return "";
}

function allow() {
  process.stdout.write(JSON.stringify({ permission: "allow" }));
  process.exit(0);
}

function deny(reason) {
  process.stdout.write(
    JSON.stringify({
      permission: "deny",
      user_message: reason,
      agent_message: reason,
    })
  );
  process.exit(0);
}

function main() {
  const input = readStdinSync();
  const command = extractCommand(input).toLowerCase().replace(/\s+/g, " ").trim();

  if (!command) {
    allow();
    return;
  }

  for (const pattern of BLOCKED) {
    if (command.includes(pattern)) {
      deny(`Blocked dangerous shell command matching: ${pattern}`);
      return;
    }
  }

  allow();
}

try {
  main();
} catch {
  process.stdout.write(JSON.stringify({ permission: "allow" }));
  process.exit(0);
}
