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

## 2. Classify the failure layer

Requirement ambiguity · instructions/skill routing · model reasoning ·
custom tool logic · connection/auth/approval · subagent delegation · sandbox
· durable session/state/resume · long-term memory · channel identity/delivery
· schedule/concurrency · external dependency · observability gap. The layer
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
