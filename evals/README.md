# Evals

This folder contains Promptfoo checks for roadmap answer quality.

## Prerequisites

- Install Promptfoo: `npm install -g promptfoo` or use `npx promptfoo`.
- Set provider API keys for the models in `promptfooconfig.yaml`, such as `ANTHROPIC_API_KEY` and `OPENAI_API_KEY`.
- Review the provider IDs before running. Model names and provider slugs change over time, so `anthropic:claude-sonnet-4.5` or `openai:gpt-5.1` may need to be replaced with the current IDs from Promptfoo and vendor docs.

## Run

```bash
promptfoo eval -c evals/promptfooconfig.yaml
```

If API keys or model access are unavailable, record the eval as skipped and include the reason in your capstone evidence.
