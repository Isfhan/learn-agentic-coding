# Step 16 · Build Your Own Agent From Scratch

> **⏱️ Time:** ~4 hours · **Prereq:** Step 15

You've been *using* agents for 15 steps. Now you're going to build one — the full loop — in about **200 lines of code**. After this, agents stop feeling magical and start feeling like software.

---

## 🎯 What you'll learn

- The real mechanics: tool-calling + loops.
- How to implement **read_file, list_files, run_shell, edit_file**.
- How to add safety (approvals, timeouts).
- How to turn your agent into a CLI you can actually use.

---

## 1. The recipe (one more time, with feeling)

```python
while not done:
    response = llm.chat(
        messages=history,
        tools=tools,
    )
    history.append(response)

    if response.wants_tool():
        result = run_tool(response.tool_name, response.args)
        history.append({"role": "tool", "content": result})
    else:
        done = True
        print(response.text)
```

That's it. Ready to write it for real?

---

## 2. Minimal agent in Python (~150 LOC)

We'll use the **Anthropic SDK** for clarity (swap for OpenAI SDK with 5 renames if you prefer).

### Setup

```bash
mkdir mini-agent && cd mini-agent
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install anthropic
```

### `agent.py`

```python
import os, subprocess, json, sys
from pathlib import Path
from anthropic import Anthropic

client = Anthropic()

# --- Tool implementations -------------------------------------------------

def list_files(path: str = ".") -> str:
    root = Path(path).resolve()
    out = []
    for p in root.rglob("*"):
        if any(part.startswith(".") for part in p.parts):
            continue
        out.append(str(p.relative_to(root)))
        if len(out) > 500:
            out.append("... (truncated)")
            break
    return "\n".join(out)

def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return f"ERROR: {path} does not exist"
    if p.stat().st_size > 200_000:
        return f"ERROR: {path} is too large"
    return p.read_text(encoding="utf-8", errors="replace")

def edit_file(path: str, content: str) -> str:
    p = Path(path)
    confirm = input(f"Agent wants to write {p}. Allow? [y/N] ")
    if confirm.lower() != "y":
        return "USER: write canceled"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"Wrote {p} ({len(content)} bytes)"

def run_shell(command: str) -> str:
    confirm = input(f"Run: {command!r}? [y/N] ")
    if confirm.lower() != "y":
        return "USER: command canceled"
    try:
        out = subprocess.run(
            command, shell=True, capture_output=True,
            text=True, timeout=30,
        )
        return f"exit={out.returncode}\nstdout:\n{out.stdout}\nstderr:\n{out.stderr}"
    except subprocess.TimeoutExpired:
        return "ERROR: command timed out after 30s"

TOOLS = {
    "list_files": list_files,
    "read_file": read_file,
    "edit_file": edit_file,
    "run_shell": run_shell,
}

TOOL_SCHEMAS = [
    {
        "name": "list_files",
        "description": "Recursively list files under a directory (defaults to cwd). Skips hidden dirs.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string", "default": "."}},
        },
    },
    {
        "name": "read_file",
        "description": "Read a text file.",
        "input_schema": {
            "type": "object",
            "required": ["path"],
            "properties": {"path": {"type": "string"}},
        },
    },
    {
        "name": "edit_file",
        "description": "Create or overwrite a file with the given content. Prompts user for approval.",
        "input_schema": {
            "type": "object",
            "required": ["path", "content"],
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
        },
    },
    {
        "name": "run_shell",
        "description": "Run a shell command in the cwd. Prompts user for approval.",
        "input_schema": {
            "type": "object",
            "required": ["command"],
            "properties": {"command": {"type": "string"}},
        },
    },
]

SYSTEM = """You are Mini-Agent, a minimal coding agent.
You have tools: list_files, read_file, edit_file, run_shell.
Always think step-by-step. Prefer read_file before editing.
For edits and shell commands, the user will be asked to approve each call.
When the user's task is done, stop calling tools and give a short summary."""


def run(user_msg: str):
    messages = [{"role": "user", "content": user_msg}]
    while True:
        resp = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=4096,
            system=SYSTEM,
            tools=TOOL_SCHEMAS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": resp.content})

        if resp.stop_reason == "end_turn":
            for block in resp.content:
                if block.type == "text":
                    print("\n🤖", block.text)
            return

        tool_results = []
        for block in resp.content:
            if block.type == "tool_use":
                name, args = block.name, block.input
                print(f"\n🔧 {name}({json.dumps(args)[:120]})")
                result = TOOLS[name](**args)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result[:8000],  # cap tool output
                })
        messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
    run(" ".join(sys.argv[1:]) or "Summarize this repo.")
```

### Run it

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python agent.py "Add a function double(x: int) -> int to a new file math_helpers.py and a matching pytest"
```

**You just wrote your own Claude Code.** Every agent tool does *this*, plus polish.

---

## 3. What to build next (10-line additions each)

1. **Conversation persistence** — dump `messages` to `./.agent-history/<session>.json`.
2. **`/clear`, `/compact`** — a `/clear` resets; `/compact` asks the model to summarize `messages` into a short system note.
3. **A rules file** — read `AGENTS.md` and prepend to `SYSTEM`.
4. **Safer shell** — block `rm -rf`, `curl | sh` before asking for approval.
5. **MCP support** — there's an `mcp` Python SDK; connect to any MCP server and expose its tools to your agent. Congrats, now your agent talks to GitHub/Postgres/etc. for free.
6. **Multi-model routing** — cheap model for simple turns, reasoning model for hard ones.

---

## 4. TypeScript version (short form)

The shape is identical. Use `@anthropic-ai/sdk` or `openai` + `zod`:

```ts
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();

const tools = [/* schemas identical to Python */];

async function run(userMsg: string) {
  const messages: any[] = [{ role: "user", content: userMsg }];
  while (true) {
    const resp = await client.messages.create({
      model: "claude-sonnet-4-5",
      max_tokens: 4096,
      system: "You are Mini-Agent…",
      tools,
      messages,
    });
    messages.push({ role: "assistant", content: resp.content });
    if (resp.stop_reason === "end_turn") return;
    const results: any[] = [];
    for (const b of resp.content) {
      if (b.type === "tool_use") {
        const out = await runTool(b.name, b.input);
        results.push({ type: "tool_result", tool_use_id: b.id, content: out });
      }
    }
    messages.push({ role: "user", content: results });
  }
}
```

---

## 5. Frameworks (for when minimalism isn't enough)

Once you understand the loop, frameworks become valuable. They give you:
- Memory / state
- Multi-agent orchestration
- Graph-like control flow
- Built-in tracing and evals

| Framework | Language | Sweet spot |
|-----------|----------|-----------|
| **LangGraph** | Python, TS | Graph-based multi-agent; prod ready |
| **OpenAI Agents SDK** | Python, TS | Official, minimal, solid |
| **PydanticAI** | Python | Type-safe, Pythonic |
| **CrewAI** | Python | Role-based multi-agent |
| **AutoGen** | Python | Microsoft's; conversational multi-agent |
| **smolagents** (HF) | Python | Minimal, readable |
| **Mastra** | TypeScript | TS-native; full-stack DX |
| **DSPy** | Python | Prompt optimization, not orchestration |

> **Don't pick a framework before you've built the 200-LOC agent above.** If you skip this step, every framework will feel like magic. Once you've done it, frameworks feel like shortcuts you earned.

---

## 🎥 Watch

- **[Andrej Karpathy — "LLM agents are dumb, but also smart"](https://www.youtube.com/results?search_query=karpathy+LLM+agents)**
- **[Every — "Build an agent in Python from scratch"](https://www.youtube.com/results?search_query=build+agent+python+from+scratch)**
- **[Hamel Husain — "What agent frameworks get wrong"](https://www.youtube.com/results?search_query=hamel+husain+agent+frameworks)**

## 📚 Read

- 📘 [**Anthropic SDK tool-use docs**](https://docs.anthropic.com/claude/docs/tool-use)
- 📘 [**OpenAI Agents SDK**](https://github.com/openai/openai-agents-python)
- 📘 [**LangGraph docs**](https://langchain-ai.github.io/langgraph/)
- 📘 [**Hugging Face — smolagents**](https://github.com/huggingface/smolagents) — read this source code; it's *tiny* and teaches you everything.
- 📄 [**Anthropic — Building effective agents**](https://www.anthropic.com/research/building-effective-agents) — still the single best essay.

---

## ✍️ Exercise (2 hours) — **CAPSTONE**

1. Type out the agent above by hand (don't copy-paste). Notice what each line does.
2. Make it work on your laptop. Run it on a toy task.
3. Add **one** extension from the list in §3.
4. Then add **MCP support** — let your agent use any MCP server (even the one you built in Step 10!).
5. Push the repo to GitHub with a clean README and a 30-second demo GIF.
6. Tweet it: *"I built my own Claude Code in 200 lines of Python. Here's how: [repo link]."*

That tweet performs well. Guaranteed hit with dev Twitter.

---

## ✅ Self-check

1. In your agent, who decides when the loop stops?
2. Why does the tool schema matter so much?
3. What would the minimum change be to add a new tool (e.g., `git_diff`)?

---

## 🧭 Next

→ [Step 17 · Advanced Patterns](./17-advanced-patterns.md)
