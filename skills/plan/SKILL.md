---
name: plan
description: "Convert accepted requirements plus Eve architecture into an implementation-ready plan: stable U-ID work units with files, dependencies, tests, eval scenarios, risks, and rollout guardrails, validated for coverage before the readiness flip. Use immediately before implementation. Not for runtime design (architect) or execution (work)."
argument-hint: "[requirements/architecture artifact, or blank for latest]"
---

# Plan the implementation

Read `${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md`,
`${CLAUDE_PLUGIN_ROOT}/references/artifacts.md` (plan contract),
`${CLAUDE_PLUGIN_ROOT}/references/eve-runtime.md`, and
`${CLAUDE_PLUGIN_ROOT}/references/ce-interop.md`.

## 0. Output contract — an explicit invocation always produces a plan

Never classify a direct invocation as "not a planning task" and route out
empty-handed. Resolve the tier from bounded inline reads:

- **Direct** — statable, doable, verifiable in one pass with no decision the
  user would weigh: state the change in a few sentences and offer the handoff.
- **Chat brief** — bounded work, at most one weighable decision, no risk
  surface: deliver the brief in chat; no file, and no readiness stamp (a chat
  brief must never be treated as implementation-ready downstream).
- **Durable** — everything else, and always when: there is a risk surface
  (auth, payments, migrations, external writes, tenancy, autonomy), the run
  is orchestrated/non-interactive, or the user asked for a plan file.

Uncertain → heavier tier. The Durable path expects the `requirements-only`
and architecture artifacts; when missing for non-trivial scope, route back to
brainstorm/architect rather than inventing product behavior.

If Every's `ce-plan` is available and the user wants it, it may run as the
guardrail planner; koushik still enforces the Eve-specific sections and the
self-validation gate below.

## 1. Research before writing (parallel where non-trivial)

- **Repo research** — what exists; which conventions to follow, not reinvent.
- **Learnings research** — search `docs/solutions/` for applicable prior
  lessons; cite each one in the unit it constrains. This is the compounding
  return arrow — never skip it.
- **Eve freshness** — run eve-runtime.md's protocol for every version-
  sensitive area the plan touches.
- **Risk lenses** — for diffs that will touch auth/writes/schedules, get
  `agent-safety-reviewer` / `reliability-reviewer` input on which units need
  approval gates, idempotency keys, or migration care.

## 2. Write the work units

Per artifacts.md: stable U-IDs, each with objective/end state, source R/A/F
IDs, likely files, dependencies, conventional tests, **Eve eval scenarios**,
security/approval implications, durability implications, rollback constraints.
Eval units are first-class units, not afterthoughts. Plans specify WHAT must
be true — the builder with real code in front of it owns HOW.

## 3. Self-validation gate (blocking)

Before flipping readiness, verify mechanically and record the result:
- every R-ID maps to at least one unit;
- the unit dependency graph is acyclic;
- every STRATEGY.md invariant has an eval unit.
Any gap: fix the plan or send the gap back to brainstorm/architect. If
research surfaced evidence that *invalidates* a settled decision, stop the
write and surface it explicitly (lifecycle.md's settled-decisions rule) —
never plan around it silently. Only then set
`artifact_readiness: implementation-ready`.

## 4. Close

Report: state now `implementation-ready`, unit count and order, top risks,
cited prior learnings, route to `/koushik:work` (via `/koushik:lifecycle` for
the autonomous path).
