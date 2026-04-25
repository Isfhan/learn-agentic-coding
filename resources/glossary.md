# Agentic Coding Glossary

Use this glossary when a lesson uses a new AI or software term. The roadmap keeps the real industry vocabulary, then explains it in plain English.

## Core AI Terms

- **LLM (large language model):** The AI model that predicts and writes text, code, and structured output.
- **Token:** A small chunk of text. AI models count input and output in tokens, not words or lines.
- **Context window:** Everything the model can see right now: your prompt, files, rules, tool results, and conversation history.
- **Prompt:** The instruction or question you give to the AI.
- **System prompt:** Hidden or tool-provided instructions that shape how the AI behaves.
- **Hallucination:** A confident answer that is wrong or invented.
- **Reasoning model:** A model tuned for harder multi-step thinking, debugging, and planning.
- **Instruct model:** A model tuned to follow direct instructions.

## Agent Terms

- **Agent:** An LLM plus tools plus a loop. It reads context, chooses a tool, observes the result, and keeps going until done.
- **Tool calling:** The model asks to run an external action, such as reading a file, searching the web, or calling an API.
- **Subagent:** A smaller agent started by a parent agent for a focused task, such as code review or repo exploration.
- **HITL (human-in-the-loop):** A person must approve risky actions before the agent continues.
- **Orchestration:** Coordinating several tools or agents so each one handles a clear part of the work.

## Context And Knowledge

- **Context engineering:** Choosing, shaping, and limiting what information the AI sees so it can do the task well.
- **RAG (retrieval-augmented generation):** Fetching relevant documents or data before the AI answers.
- **Embedding:** A numeric representation of text used for similarity search.
- **Vector store:** A database for embeddings, often used to find related documents.
- **Context poisoning:** Wrong or malicious information enters the context and later gets treated as truth.

## Tools And Protocols

- **MCP (Model Context Protocol):** A standard way for AI tools to connect to external tools, data, and prompts.
- **MCP host:** The app you use, such as Cursor, Claude Code, or Copilot.
- **MCP client:** The part of the host that speaks to one MCP server.
- **MCP server:** A separate process that exposes tools, resources, or prompts to an AI host.
- **JSON-RPC:** A simple message format where one program calls a method on another program using JSON.
- **stdio (standard input/output):** A local process talks through text streams instead of a network port.
- **SSE (server-sent events):** A way for a server to push updates to a client over HTTP.

## Quality And Production

- **Eval:** A test for AI behavior. It checks whether an AI output is useful, accurate, or safe enough.
- **Deterministic test:** A normal software test that should return the same pass/fail result every run.
- **CI (continuous integration):** Automatic checks that run before code is merged.
- **Observability:** Logs, traces, and metrics that help you understand what happened in a running system.
- **Trace:** A step-by-step record of a request or agent run.
- **Rollback:** Returning to a previous safe version after a bad change.
- **Least privilege:** Give a tool only the permissions it needs, and no more.

## Common Buzzwords

- **Agentic coding:** Building software by giving goals to an AI agent that can inspect, edit, run, and iterate while you supervise.
- **Vibes:** A subjective feeling. In this roadmap, “evals beat vibes” means tests beat guessing.
- **Production-grade:** Ready for real users because it has tests, security controls, monitoring, rollback plans, and human review where needed.
- **Cloud agent:** An AI agent that works in a remote environment and usually returns a pull request.
- **Greenfield:** A new project with little or no existing code.
- **Brownfield:** An existing project with real users, history, constraints, and old decisions.
