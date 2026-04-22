# Mini Refactor Project (Week 1)

This artifact records the week-1 requirement: run an end-to-end mini refactor with an agent workflow.

## Scenario

- Legacy helper had duplicated normalization logic and weak naming.
- Goal: simplify logic, reduce branching, improve readability.

## Before

```python
def f(x):
    if x is None:
        return ""
    if type(x) == str:
        return x.strip().lower()
    if type(x) == int:
        return str(x).strip().lower()
    return str(x).strip().lower()
```

## After

```python
def normalize_value(value):
    if value is None:
        return ""
    return str(value).strip().lower()
```

## Agentic workflow used

1. Research existing function usage.
2. Produce refactor plan.
3. Apply change in one focused patch.
4. Re-check downstream call sites.
5. Summarize risk and rollback path.

## Why this matters

- Demonstrates "goal -> plan -> edit -> verify" loop, not one-shot prompting.
- Creates a small but shippable example for portfolio evidence.
