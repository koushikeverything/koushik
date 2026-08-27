---
name: maintain
description: "Manage drift in a production durable agent: Eve/framework upgrades, model changes benchmarked through the stable eval suite with canary rollout, instruction and skill staleness, tool and connection permission drift, memory and data upkeep, eval baseline health, budgets and runbooks. Use for upgrades, dependency changes, or scheduled hygiene. Not for new features (brainstorm) or capacity growth (scale)."
argument-hint: "[upgrade, model, dependency, or drift concern]"
---

# Maintain the agent

Read `${CLAUDE_PLUGIN_ROOT}/references/maintenance.md` (the discipline per
surface), `${CLAUDE_PLUGIN_ROOT}/references/eve-runtime.md`, and recent
pulse/solution artifacts. Establish WHY maintenance is needed now — a
version change, observed drift, a security notice, a cost/quality trend, or
scheduled hygiene — before proposing anything.

## The surfaces (see maintenance.md for each discipline)

- **Eve/framework upgrades** — freshness protocol against the NEW installed
  version (its `node_modules/eve/docs` is the new truth); upgrade in a
  branch; blocking tests+evals before and after; explicit review of behavior
  changes in tools, approvals, sessions, schedules.
- **Model changes** — the canary discipline, always: stable eval suite →
  per-category comparison (quality, routing, refusals, approvals, latency,
  cost) → fix or explicitly accept regressions → bounded canary with abort
  thresholds → promote. Never "new model looks good → change the default."
- **Instructions/skills** — compact always-on context; stale procedures
  removed; overlapping skills consolidated; repeated failures promoted to
  evals or code guards, not more prose.
- **Permission drift** — unused tools/scopes removed; approval policies
  re-checked against product policy. Widening any write scope or lowering
  any approval requirement is a human gate, always.
- **Memory/data** — retention, principal scoping, restores.
- **Evals** — stable blocking core; growing regression set; flaky evals
  fixed or demoted with evidence; degraded quality never normalized.
- **Operations** — alerts, budgets, kill switches actually tested; runbooks
  executable.

## The rule

Maintenance is never permission to rewrite a working agent or chase the
newest dependency without evidence. Any code/runtime change goes through the
normal `plan → work → review → eval → ship` gates; production rollout still
requires `/koushik:deploy` with its human approval.

## Close

Record substantial maintenance per maintenance.md (why now, before/after,
eval comparison, canary, rollback). Report what changed, what was deliberately
left alone, learnings routed to `/koushik:compound`.
