---
name: scale
description: "Plan deliberate growth of a durable agent across the seven scale dimensions — tenants, traffic, knowledge, agent fan-out, autonomy, cost, operations — from an evidenced bottleneck to a scale plan with success and abort thresholds. Autonomy increases are treated as security/product changes, never capacity tweaks. Use when load or autonomy is growing. Infrastructure-mutating execution is user-directed, not model-initiated."
argument-hint: "[target load, bottleneck, autonomy change, or scale goal]"
---

# Scale deliberately

Read `${CLAUDE_PLUGIN_ROOT}/references/scale.md` (the seven dimensions and
plan contract), `${CLAUDE_PLUGIN_ROOT}/references/security.md`,
`${CLAUDE_PLUGIN_ROOT}/references/production.md`, recent pulse reports, and
relevant solution notes.

## 1. Evidence first

Identify the actual constraint with evidence (pulse data, traces, cost
reports). "We might need to scale" without a measured bottleneck → challenge
premature complexity; often the right plan is "not yet, revisit when X".

## 2. Decompose by dimension

A goal like "1,000 workspaces at 10× volume" is several different problems —
treat each of scale.md's dimensions separately: tenant isolation/partitioning,
traffic/queues/schedule-stampedes, knowledge retrieval, agent fan-out caps,
autonomy, cost tiers/budgets, operations. Delegate an independent pass to the
`scale-reviewer` agent for significant plans.

## 3. The autonomy rule

If the plan expands what the agent may do without a human (moving up
advise → draft → approved action → bounded autonomous action), that portion
is a **security/product change**: it requires strategy review, approval
redesign, new evals for the newly-autonomous behavior, and explicit human
approval — the full loop, never a config tweak.

## 4. Write the plan

`docs/scale-plans/` per scale.md's contract: bottleneck + evidence, target,
architecture changes, safety changes, cost model, load/eval test plan,
rollout order, rollback, success and abort thresholds.

## 5. Execute through the normal loop

Implementation goes through `plan → work → review → eval → ship →
deploy`. Never raise production spend/concurrency/autonomy ceilings
materially without explicit approval; infrastructure-mutating execution
starts on the user's word, not the model's initiative.

## Close

Report: the bottleneck, the plan path, which dimensions it touches, any
human gates it will hit, the first implementation step.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
