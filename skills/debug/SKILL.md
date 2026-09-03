---
name: debug
description: "Root-cause a durable-agent failure by causal chain, not speculative patching: wrong answers, misrouted tools or subagents, auth/tenant leaks, duplicate side effects after resume, approval and parking failures, schedule overlaps, connection errors, eval regressions, production incidents. Captures the reproduction as a permanent eval before fixing. Use when something is broken. Not for production overview (pulse)."
argument-hint: "[symptom, trace, incident, or failing eval]"
---

# Debug by causal chain

Read `${CLAUDE_PLUGIN_ROOT}/references/eve-runtime.md` (durability and
delegation semantics — most agent bugs live there),
`${CLAUDE_PLUGIN_ROOT}/references/security.md`, and search
`docs/solutions/` for this failure class before investigating from scratch.

The flow is: symptom → candidate causes → evidence → causal chain →
predictions → verify predictions → root cause → fix. Never symptom →
plausible patch → pray.

## 1. Reproduce concretely

A specific failing session/trace/eval — from `eve logs`, `eve traces`, or a
new failing eval case. No concrete trajectory → gather one before theorizing.

**Production forensics — when the logs are gone, manufacture evidence.**
Runtime log retention is short and traces may be local-only; do not stall on
missing history. Instead: (a) treat the app's own durable store as ground
truth — what did and didn't get written tells you exactly how far a run got;
(b) drive targeted **probe turns** against the deployed agent (`eve invoke
--url`), one subsystem per probe, wall-clocking every one — a probe that
forces just the fetch path, just a subagent delegation, just the file
workspace, or a deliberately long turn will convict or clear each subsystem
in minutes; (c) start any live log tail BEFORE re-triggering, never after.
Eliminate suspects by experiment, not plausibility.

## 2. Classify the failure layer

Requirement ambiguity · instructions/skill routing · model reasoning ·
custom tool logic · connection/auth/approval · subagent delegation · sandbox
· durable session/state/resume · long-term memory · channel identity/delivery
· schedule/concurrency · external dependency · observability gap ·
**duplicate actor** (a second session/process working the same repo under
the same identity — unexplained commits, PRs, or state changes; check for
concurrent sessions before assuming the runtime did it). The layer
determines which evidence matters. (Signature class: side-effect identity
created inside a resumable step — one approval, two effects.)

## 3. Hypotheses with predictions

A small set, each with a testable prediction ("if X, duplicates appear only
when reconnect follows approval within the retry window"). Inspect exactly
the traces/code/state that falsify them. Root cause is claimed only when the
predictions verify.

## 4. Regression eval BEFORE the fix

Capture the reproduction as a permanent eval case (category 13) — it must
fail on current code and pass on the fix. This is how a bug fix eliminates a
category, not an instance.

**When a faithful eval is impractical** (the failure needs production scale,
real cron context, or a 10-minute run no blocking suite can afford), do NOT
silently skip. Install the guard at another layer and record which one: a
budget-headroom assertion (eval-rubric category 12), a config/schema-level
check that removes the failing capability outright, or — last resort — a
documented manual verification protocol in the runbook. A skipped eval with
no named substitute guard means the debug is not done.

## 5. Fix through the gates

Implement; run review + eval gates on the fix like any change (production
pressure never skips gates). If the fix is urgent-and-tiny, gates shrink but
never disappear.

## Close

Report: root cause with the verified causal chain, the fix, the regression
eval added, and — when the lesson generalizes — route to `/koushik:compound`.
If Every's `ce-debug` is available and the incident is purely code-shaped, it
may run the generic investigation; the layer classification above stays with
koushik.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
