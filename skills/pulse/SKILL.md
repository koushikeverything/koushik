---
name: pulse
description: "Produce a time-windowed production reading of a deployed durable agent — usage, grounding quality, approval denials, parked-and-abandoned sessions, refusals, tool and subagent failures, latency, token cost per outcome, eval drift, incidents — graded against STRATEGY.md's definition of success. Use after deployment or when deciding what to improve next. Not for diagnosing a specific failure (debug)."
argument-hint: "[24h|7d|30d or custom window]"
---

# Production pulse

Read `STRATEGY.md` (the metrics that define success),
`${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md`, and recent deployment/
runbook artifacts. Check `.koushik/config.yaml` `agent_native_level`: pulse
needs level ≥3 (production logs/monitoring). Below that, produce what local
evidence supports and state plainly which signals are unavailable and what
access would unlock them — never invent metrics.

## 1. Gather what actually exists

`eve logs` / `eve traces`, platform monitoring, app telemetry, error
tracking, user feedback channels. Use only real sources; state gaps.

## 2. Read the agent-shaped signals

Beyond generic product metrics, specifically:
- approval requests, denial rate, time-to-resolution (are we asking for the
  wrong things, or asking badly?);
- refusal and insufficient-evidence rates (honest, or evasive?);
- sessions that parked and were never resumed (abandonment);
- retry/resume anomalies and any duplicate-effect incidents;
- tool/connection/subagent failure rates;
- token/model/tool cost **per outcome**, not per request;
- eval drift candidates: production behavior the blocking suite doesn't cover;
- auth/tenant anomalies; blocking-eval regressions since last pulse.

## 3. Grade against strategy, separate facts from hypotheses

Every number is read against what STRATEGY.md says success means. Facts and
hypotheses are labeled as such.

**Also grade the last deployment's watch-list:** open the most recent
`docs/deployments/` record and explicitly revisit every known-limitation and
watch item it recorded — each one gets a verdict (resolved / still watching /
worsened) in this pulse. Watch items that nobody re-reads are how small
oddities become incidents.

## 4. Route the findings

Smallest next investigation named explicitly. Breakage → `/koushik:debug`.
Drift (model/framework/permissions/evals) → `/koushik:maintain`. Reusable
lesson → `/koushik:compound`. Growth pressure → `/koushik:scale`. New product
scope → `/koushik:brainstorm`.

## Close

Save to `docs/pulse-reports/` per artifacts.md. Report: state `observed`,
the one-paragraph reading, the routed follow-ups.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
