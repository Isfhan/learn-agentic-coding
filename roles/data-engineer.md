# 🗄️ Data Engineer — Adjacent Track

> **⏱️ Time:** ~15 hours of this roadmap (light touch) · **Track:** Tier 2 (adjacent) · **Start:** Step 00

The #1 role in recruiter search volume (SignalHire, 2026): every AI system runs on data, and someone must keep that data clean, flowing, and accessible. This roadmap gives you the agentic/AI layer; the pipeline fundamentals (SQL, warehouses, orchestration) are your separate homework (flagged below).

---

## 💼 What this role actually does

- Builds and maintains pipelines: raw data → clean tables → ready for models and agents.
- Owns data quality: dedup, schema, freshness, and access control.
- Increasingly: powers **RAG and agent memory** — the exact data plumbing LLM systems need.

The agentic angle is why you're here: agents eat clean, well-modeled data. Engineers who understand both are rare.

---

## 📊 Market snapshot (2026–2027)

| Signal | Number |
|---|---|
| Demand | #1 in recruiter search volume for AI-adjacent roles |
| Mid-level US salary | $120K–$160K |
| Entry path | The most common pivot for backend/SQL developers |
| 2027 outlook | Pipelines stay foundational; RAG/agent data plumbing is the growth area |

Sources: SignalHire recruiter-search analysis, published salary surveys (Aug 2026).

---

## 🗺️ Your step order (shared 21 steps)

| Priority | Steps |
|---|---|
| ● Core | 00, 01, 02, 03, 09, 10, 13, 14 |
| ◐ Optional | 11 (pipeline triggers), 15 (access control), 16 (agents that consume your data) |
| ○ Skim | 04, 05, 06, 07, 08, 12, 13.5, 17, 18, 19 |

---

## ⚠️ What this roadmap does NOT cover (add these)

- **SQL** and data modeling (star schemas, normalization).
- **Warehouses & lakes:** Snowflake, BigQuery, Databricks.
- **Pipeline orchestration:** Airflow, dbt, Spark.
- **Streaming:** Kafka, Flink.

The [resources index](../resources/README.md) and [practice projects](../projects/practice-projects.md) point to community leads; pair them with a dedicated data-engineering course.

---

## 🚀 Track capstone

1. Do the [main capstone](../capstone/public-agent/README.md).
2. Add the data layer: build a **RAG pipeline** (a small corpus → chunk → embed → retrieve — see [Step 13](../steps/13-context-engineering.md) and [Step 14](../steps/14-evals-testing.md)).
3. Write the schema, the refresh job (hook or cron), and the quality checks. Post the architecture.

---

## ✅ Self-check

1. Do you know exactly which parts of "Data Engineer" this roadmap covers and which it doesn't?
2. Have you shipped one pipeline that feeds an agent, with quality checks?
