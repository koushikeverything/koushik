---
name: simplify
description: "Reduce accidental complexity in freshly built durable-agent code before formal review, preserving behavior: instruction bloat moved to skills, tool-surface minimization, duplicate procedures merged, needless subagents inlined, unused capability removed. Use between work and review. Not a bug hunt (review) and not a refactor license."
argument-hint: "[branch, diff, or blank for current changes]"
---

# Simplify what was just built

Read `${CLAUDE_PLUGIN_ROOT}/references/primitive-placement.md` (placement
smells) and `${CLAUDE_PLUGIN_ROOT}/references/eve-runtime.md` (separation
rules). Scope: the current change set, not the whole repository.

If Every's `ce-simplify-code` is available it may run the generic reuse/
quality/efficiency pass; koushik still applies the agent-specific passes
below and the behavior-preservation rule.

## The three passes

1. **Reuse** — did this change reinvent something the repo already had
   (helpers, abstractions, existing tools)? Merge into the existing form.
2. **Context economy** — is anything permanently in `instructions.md` that
   should load on demand as a skill? Every always-on line costs every future
   turn. Target: instructions stay compact (~150 lines is the smell line).
3. **Surface minimization** — fewest tools with the narrowest scopes;
   overlapping tool descriptions merged or sharpened (misrouting risk);
   subagents with no isolation rationale inlined; unused capability removed
   (it is pure attack surface); forbidden actions disabled by capability.

## The rule that makes this safe

Behavior is preserved, provably: re-run the relevant tests AND evals after
each simplification. An eval that changes result means the "simplification"
changed behavior — revert it or escalate it as a real change through the
normal gates. Never touch accepted product behavior, approval gates, or
thresholds here.

## Close

Report: state now `simplified`, what was removed/merged/moved with line
counts, eval re-run evidence, route to `/koushik:review`.
