---
name: lifecycle
description: "Orchestrate the koushik durable-agent lifecycle end to end: detect the repo's earliest incomplete state and resume from there — accepting anything from a vague one-line idea (routed into strategy and brainstorm, one question at a time) to a half-built Eve app — then chain architect, plan, work, simplify, review, eval gate, test-drive, and ship to a READY-TO-MERGE PR. Never merges, never deploys. Use for an end-to-end build rather than a single stage."
argument-hint: "[durable-agent idea, feature, or blank to resume]"
disable-model-invocation: true
---

# Run the lifecycle

Read `${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md` — the state machine,
routing table, and human gates there are authoritative. Treat `$ARGUMENTS`
as the goal; blank means "resume whatever this repo is mid-way through."

## 1. Detect state, never restart

Infer the earliest incomplete lifecycle state from the durable artifacts
(STRATEGY.md, `docs/plans/` readiness stamps, `docs/agent-architecture/`,
plan-file unit ticks, review/eval/test-drive reports, PR status) — not from
conversation memory. Completed stages are not redone; a half-done work stage
resumes at the next unticked unit.

## 2. Route vague ideas; refuse only premature implementation

A vague idea is accepted and routed: no strategy → `/koushik:strategy`; no
requirements → `/koushik:brainstorm` (one consequential question at a time —
these stages are interactive by design and are where the human shapes the
product). The rule is precise: **refuse premature implementation, never
vague starting ideas.** Code is never written from an unresolved idea.

## 3. Chain the stages through their gates

From the detected state, run in order, each per its own skill:
architect → plan (self-validation gate) → work (per-unit loop, durable
ticks) → simplify → review (apply eligible fixes) → **eval — a hard gate:
the blocking suite must pass; red routes to debug/work, and thresholds are
never lowered to pass** → test-drive (escalating taste to the human) →
ship → READY-TO-MERGE PR.

**Every stage boundary is a GATE, checked on evidence:** advance only on a
valid completion result from the stage's artifacts; a blocked, malformed, or
missing result stops the pipeline with the blocker reported — a blocked
status outranks the mere presence of an artifact, and a stopped pipeline is
never silently retried past its blocker. One narrow skip exists: simplify's
*invocation* may be skipped for docs-only or trivial (≈under 10 changed
lines) diffs — the skip is recorded, and no other stage is ever skipped.

At each stage boundary, summarize: state reached, artifact produced,
unresolved risk, next stage. Resolve repository facts yourself; stop only
for genuinely consequential product ambiguity, an invalidated settled
decision (surface it, never re-decide silently), or a human gate from
lifecycle.md.

**Residuals become durable before done.** Unapplied judgment-needed findings,
recorded deviations, and accepted risks are written into the review artifact
and the PR body (or a PR comment) before READY TO MERGE is declared — nothing
divergent lives only in this conversation.

## 4. Hard stops

- Stops at `pr-ready`. **Never merges. Never deploys** — merging is the
  human's act; deployment is `/koushik:deploy`, user-invoked only.
- Honors every human gate in lifecycle.md (write capabilities, approval
  changes, autonomy/spend increases…).
- No remote configured → stops at local clean commits and says so.
- CE interop: within stages, delegation follows
  `${CLAUDE_PLUGIN_ROOT}/references/ce-interop.md` (notably: `ce-work` only
  in return-to-caller mode).
- Never claims a stage complete until its gate is actually satisfied.

## Close

Report: journey summary (states traversed), PR URL and its evidence, what
remains human (merge, then `/koushik:deploy`), and any learnings worth
`/koushik:compound`.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
