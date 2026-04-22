#!/usr/bin/env python3
"""
roadmap_agent.py

Reference implementation for "Build Your Own Agent" step.
This is a small supervised agent runtime with:
- explicit context state
- pluggable tools
- safety checks for shell usage
- looped plan/act/evaluate behavior
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List


ToolFn = Callable[[Dict[str, Any]], Dict[str, Any]]


@dataclass
class Message:
    role: str
    content: str


@dataclass
class AgentState:
    task: str
    messages: List[Message] = field(default_factory=list)
    observations: List[str] = field(default_factory=list)
    max_steps: int = 6
    cwd: Path = field(default_factory=lambda: Path.cwd())

    def add_observation(self, text: str) -> None:
        self.observations.append(text)
        self.messages.append(Message(role="tool", content=text))

    def summarize(self) -> str:
        joined = "\n".join(f"- {x}" for x in self.observations[-6:])
        return f"Task: {self.task}\nRecent observations:\n{joined or '- none'}"


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: Dict[str, ToolFn] = {}

    def register(self, name: str, fn: ToolFn) -> None:
        self._tools[name] = fn

    def list_tools(self) -> List[str]:
        return sorted(self._tools.keys())

    def call(self, name: str, args: Dict[str, Any]) -> Dict[str, Any]:
        if name not in self._tools:
            return {"ok": False, "error": f"Unknown tool: {name}"}
        return self._tools[name](args)


def tool_read_file(args: Dict[str, Any]) -> Dict[str, Any]:
    path = Path(args.get("path", "")).expanduser()
    if not path.exists():
        return {"ok": False, "error": f"File not found: {path}"}
    try:
        data = path.read_text(encoding="utf-8")
        return {"ok": True, "data": data[:4000]}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}


def tool_write_file(args: Dict[str, Any]) -> Dict[str, Any]:
    path = Path(args.get("path", "")).expanduser()
    content = args.get("content", "")
    if not path:
        return {"ok": False, "error": "Missing path"}
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(str(content), encoding="utf-8")
        return {"ok": True, "data": f"Wrote {path}"}
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}


def is_shell_safe(command: str) -> bool:
    blocked = ["rm -rf", "git reset --hard", "git push --force", "DROP TABLE", "curl | sh"]
    normalized = " ".join(command.strip().split()).lower()
    return not any(token.lower() in normalized for token in blocked)


def tool_shell(args: Dict[str, Any]) -> Dict[str, Any]:
    command = str(args.get("command", ""))
    cwd = str(args.get("cwd", "."))
    if not command:
        return {"ok": False, "error": "Missing command"}
    if not is_shell_safe(command):
        return {"ok": False, "error": f"Blocked unsafe command: {command}"}

    try:
        proc = subprocess.run(  # noqa: S603
            command,
            shell=True,  # noqa: S602
            cwd=cwd,
            check=False,
            text=True,
            capture_output=True,
            timeout=20,
        )
        return {
            "ok": proc.returncode == 0,
            "data": {
                "stdout": proc.stdout[-3000:],
                "stderr": proc.stderr[-3000:],
                "returncode": proc.returncode,
            },
        }
    except Exception as exc:  # noqa: BLE001
        return {"ok": False, "error": str(exc)}


def naive_planner(state: AgentState, tools: ToolRegistry) -> Dict[str, Any]:
    """
    A deterministic "planner" placeholder.
    In production this would be an LLM call with tool-selection.
    """
    task = state.task.lower()
    if "summarize" in task and "roadmap" in task:
        return {"tool": "read_file", "args": {"path": "README.md"}}
    if "create file" in task:
        return {"tool": "write_file", "args": {"path": "output.txt", "content": "created by roadmap_agent"}}
    if "list files" in task:
        return {"tool": "shell", "args": {"command": "ls", "cwd": str(state.cwd)}}

    # Fallback: ask shell for pwd as a harmless proof-of-work.
    return {"tool": "shell", "args": {"command": "pwd", "cwd": str(state.cwd)}}


def evaluate_step(result: Dict[str, Any]) -> str:
    if result.get("ok"):
        data = result.get("data")
        if isinstance(data, dict):
            text = json.dumps(data, indent=2)
        else:
            text = str(data)
        return f"SUCCESS\n{text[:1200]}"
    return f"FAILURE\n{result.get('error', 'unknown error')}"


def run_agent(task: str, max_steps: int) -> AgentState:
    state = AgentState(task=task, max_steps=max_steps)
    tools = ToolRegistry()
    tools.register("read_file", tool_read_file)
    tools.register("write_file", tool_write_file)
    tools.register("shell", tool_shell)

    state.messages.append(
        Message(
            role="system",
            content=(
                "You are a supervised coding agent runtime. "
                "Use small safe actions, observe result, and stop when enough evidence exists."
            ),
        )
    )
    state.messages.append(Message(role="user", content=task))

    for step in range(1, state.max_steps + 1):
        decision = naive_planner(state, tools)
        tool = decision["tool"]
        args = decision["args"]

        state.messages.append(
            Message(
                role="assistant",
                content=f"Step {step}: choose tool `{tool}` with args {json.dumps(args)}",
            )
        )

        result = tools.call(tool, args)
        observation = evaluate_step(result)
        state.add_observation(f"Step {step} / {tool}\n{observation}")

        # Early stop conditions
        if result.get("ok") and tool == "read_file":
            break
        if result.get("ok") and "returncode" in str(result.get("data", "")):
            break

    return state


def render_report(state: AgentState) -> str:
    lines = [
        "# Roadmap Agent Run Report",
        "",
        f"Task: {state.task}",
        "",
        "## Observations",
    ]
    for item in state.observations:
        lines.append("```text")
        lines.append(item)
        lines.append("```")

    lines.extend(
        [
            "",
            "## Final Summary",
            textwrap.dedent(
                """\
                This reference runtime demonstrates the core agent pattern:
                1) maintain context state
                2) choose a tool
                3) execute safely
                4) evaluate output
                5) iterate until done
                """
            ).strip(),
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a minimal supervised coding agent.")
    parser.add_argument("--task", required=True, help="Goal for the agent to execute.")
    parser.add_argument("--max-steps", type=int, default=6, help="Maximum loop iterations.")
    parser.add_argument("--report", default="agents/roadmap-agent-report.md", help="Path to write run report.")
    args = parser.parse_args()

    state = run_agent(task=args.task, max_steps=args.max_steps)
    report = render_report(state)

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")

    print(f"Run complete. Report written to {report_path}")
    print()
    print(state.summarize())


if __name__ == "__main__":
    main()
