---
name: work
description: "Implement an implementation-ready durable-agent plan in the actual repository: scaffold Eve when greenfield, author agent instructions, skills, tools, connections, subagents, channels, schedules, state and memory integration, application code, tests, and evals — one validated unit at a time with durable progress. Use after plan flips to implementation-ready. Not for planning (plan) or cleanup (simplify)."
argument-hint: "[implementation-ready plan path or U-ID range]"
---

# Build the agent

Read `${CLAUDE_PLUGIN_ROOT}/references/eve-runtime.md`,
`${CLAUDE_PLUGIN_ROOT}/references/security.md`, and the accepted
implementation-ready plan. If the plan is `requirements-only`, STOP and route
to `/koushik:plan` — the readiness stamp is a gate, not a suggestion.

If Every's `ce-work` is available and delegation is wanted, use
**`mode:return-to-caller` ONLY** (never plain `ce-work` — it runs its own
shipping tail and duplicates koushik's gates; see
`${CLAUDE_PLUGIN_ROOT}/references/ce-interop.md` for the envelope contract).
Koushik still owns the freshness protocol, runtime invariants, and commits.

## 0a. Branch first — a hard gate

Create the feature branch (or worktree) BEFORE implementing anything.
Refuse to implement units on the default branch: without the branch, the
ship stage has no reviewable PR boundary. (Learned the hard way in loop one.)

## 0b. Scaffold when greenfield

No Eve yet and the plan calls for it: verify the current scaffold command via
the freshness protocol. `eve init .` refuses non-empty directories — and a
koushik-setup-first repo is always non-empty — so scaffold into a temp
directory and merge the generated files in (rename the package, merge
AGENTS.md content rather than overwriting). Never invent imports or config
keys from memory.

**Then check the resolved surface against the architecture:** run
`eve info --json` and diff its tool list against the architecture doc's
intended surface — scaffolds enable more built-ins than most architectures
want (e.g. `agent` fan-out, `web_search`); disable the excess by capability
before writing any unit.

## 1. The per-unit loop — durable, always the same

For each unit in dependency order:

1. **Isolate** — a feature branch; separate worktrees only for genuinely
   independent units with non-overlapping files/interfaces (parallel work).
2. **Implement** — the unit's end state, with HOW decided here against the
   real code. Respect the separation rules: compact instructions, procedures
   in skills, effects behind typed tools, authorization in code, idempotency
   before park boundaries, `disableTool()` for forbidden capability.
3. **Validate** — tests, lint, typecheck, AND the unit's evals. Evals are
   written alongside the unit, never after the feature. Validation evidence
   must be real: never pipe a gating command through a filter that masks its
   exit code (`cmd | tail` reports tail's status, not cmd's) — check the
   command's own status before the commit step may run.
4. **Commit** — one clean, convention-aware commit per unit.
5. **Tick** — mark the unit done in the plan file itself; progress lives in
   the artifact, not the chat, so any future session knows what remains.

## 2. Deviations are recorded, never absorbed

When reality contradicts the plan (a file doesn't exist, a constraint was
wrong), record the deviation next to the affected unit and continue if the
intent is preserved; if the deviation changes accepted product behavior, stop
and route back to plan/architect. When evidence *invalidates* a settled
decision outright (infeasible, wrong-thing, destructive), stop and surface it
per lifecycle.md — proceeding-and-flagging is only for deviations that
preserve the decision's intent. Never weaken an approval, authorization, or
eval threshold to make implementation easier.

## 3. Verify the whole

After the last unit: full test + eval run, `eve dev`-level sanity where
practical. Broken → fix or route to `/koushik:debug`.

## 4. Close

Report: state now `implemented`, units completed/remaining (from the plan
file), deviations recorded, verification evidence, route to
`/koushik:simplify`.
