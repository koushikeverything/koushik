---
name: review
description: "Risk-selected multi-agent review of a durable agent change: correctness always, plus behavior, safety, reliability, experience, and scale lenses routed by what the diff touches; P0–P3 findings with evidence, auto-fix of eligible findings, and a --triage mode for judgment calls. Also reviews requirements/architecture documents (doc-review). Use after simplify, or on any diff/branch/PR/document. Not for running evals (eval) or experiencing the product (test-drive)."
argument-hint: "[diff|branch|PR|document path] [--triage]"
---

# Review the change

Read `${CLAUDE_PLUGIN_ROOT}/references/review-rubric.md` and the accepted
requirements/architecture/plan artifacts (findings are judged against accepted
intent, not taste). For document targets (a requirements or architecture
file), run doc-review: route to `requirements-critic` (requirements) or
`eve-architect` (architecture) and report findings without rewriting the
document.

If Every's `ce-code-review` is available it may run the general code review
(`mode:agent`; `apply:local` only when fixes are authorized — see
`${CLAUDE_PLUGIN_ROOT}/references/ce-interop.md`); koushik always adds its
Eve-specific lenses on top.

## 1. Route lenses by risk

Use review-rubric.md's selection table against what the diff actually
contains. Correctness always; each other lens only when warranted. Never all
seven for a small diff; never skip safety when auth/writes/tenant data moved.
Dispatch selected reviewer agents concurrently — they run read-only, in
separate contexts, seeing the code but never the builder's reasoning.

## 2. Merge and prioritize

One deduplicated list, P0→P3, each finding with concrete evidence, impact,
and a disposition proposal. Mark each **auto-fixable** (mechanical, behavior-
preserving, clearly correct) or **judgment-needed**.

## 3. Resolve

- Auto-fixable: apply P0/P1 first, then P2; re-run tests and evals after
  fixes — a fix that changes eval results is not a safe fix.
- Judgment-needed: with `--triage`, walk findings one at a time — approve
  (status: ready) / skip / adjust priority. Without it, present the list and
  wait for direction. Never auto-fix judgment-heavy findings.

## 4. Record

Save substantial reviews to `docs/agent-reviews/` per the artifacts.md
contract — including the closing **recurring-finding candidates** section,
the mechanical handoff that feeds `/koushik:compound`.

## Close

Report: state now `reviewed` (criticals fixed or explicitly accepted),
findings summary by severity and disposition, route behavioral-coverage gaps
to `/koushik:eval`, root causes to `/koushik:debug`, then onward to
`/koushik:eval`.
