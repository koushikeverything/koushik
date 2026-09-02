---
name: eval
description: "Design, implement, run, and interpret behavioral evaluations for an Eve durable agent across the 13-category taxonomy: grounding, routing, correct non-action, approval parking, tenant isolation, retry/resume idempotency, adversarial input, cost, and production regressions. Use as the release gate after review, for model comparisons, or to turn a failure into a permanent regression case. Not for experiencing the product (test-drive)."
argument-hint: "[behavior, release, failure, or eval scope]"
---

# Evaluate the agent's behavior

Read `${CLAUDE_PLUGIN_ROOT}/references/eval-rubric.md` and
`${CLAUDE_PLUGIN_ROOT}/references/eve-runtime.md` (verified assertion API),
plus the architecture artifact's eval taxonomy.

## 1. Verify the eval surface first

Freshness protocol: inspect the installed Eve eval API and existing `evals/`
conventions before generating code. Evals live at the app root `evals/`
(`*.eval.ts`, one `evals.config.ts`); run via `eve eval` — exit 0 is the gate.

## 2. Build or extend the matrix

From the taxonomy defined at architect time and the risks that emerged since:
- every STRATEGY.md invariant → a named eval file;
- per critical behavior: one positive and one negative/adversarial case;
- deterministic assertions for decisions (`t.calledTool`, `t.notCalledTool`,
  `t.toolOrder`, `t.parked`, `t.usedNoTools`, `t.calledSubagent`,
  `t.loadedSkill`, `t.maxToolCalls`); judge/rubric scoring only for
  open-ended quality;
- `.gate()` for the blocking release set, `.soft()` for exploratory;
- the regression category grows monotonically — debug adds a case for every
  real failure BEFORE its fix lands.

## 3. Run and interpret

Run the blocking set plus the project's conventional tests. Record model and
runtime configuration with the results — these runs double as benchmarks for
maintain-stage model comparisons. Red gates → route to `/koushik:debug`
(behavioral root cause) or `/koushik:work` (implementation gap). Flaky evals
are fixed or explicitly demoted with evidence, never ignored.

## 4. The threshold rule

Never lower a blocking threshold or demote a `.gate()` to make a change pass.
That is a product/reliability decision: it requires the user's explicit
approval and is recorded in the eval report with the reason.

## Close

Save the design/summary to `docs/eval-reports/` per artifacts.md. Report:
state `eval-green` (or exactly which gates are red and why), config recorded,
route to `/koushik:test-drive` when green.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
