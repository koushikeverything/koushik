---
name: architect
description: "Design the Eve runtime architecture for a durable agent after requirements are clear: map every requirement to the smallest justified primitive (instructions, skills, tools, connections, subagents, sandbox, channels, schedules, state, external memory, approvals, evals, instrumentation), define trust boundaries and the eval taxonomy. Use between brainstorm and plan. Not for requirements definition (brainstorm) or work-unit planning (plan)."
argument-hint: "[requirements artifact or architecture focus]"
---

# Architect the Eve agent

Read `${CLAUDE_PLUGIN_ROOT}/references/primitive-placement.md`,
`${CLAUDE_PLUGIN_ROOT}/references/eve-runtime.md`,
`${CLAUDE_PLUGIN_ROOT}/references/security.md`, and
`${CLAUDE_PLUGIN_ROOT}/references/artifacts.md` (architecture contract).
Input: an accepted `requirements-only` artifact. If none exists, route to
`/koushik:brainstorm` — do not architect from a vague idea.

## 1. Verify the runtime surface

Run the freshness protocol from eve-runtime.md before any version-sensitive
claim: installed package → existing `agent/` patterns → installed docs
(`node_modules/eve/docs/`) → types → `eve info --json` → web docs → memory.
On a greenfield repo with no Eve installed, mark every Eve-specific detail
"verify at build" rather than asserting from memory.

## 2. Independent architecture pass

For non-trivial scope, delegate to the `eve-architect` agent (read-only,
separate context) with the requirements artifact and strategy as input.
For complex or high-stakes requirements, also run `requirements-critic` first
and resolve its consequential findings with the user before designing.

## 3. Map every requirement to the smallest justified primitive

Apply primitive-placement.md's table per R-ID. Record the mapping AND the
justification. Enforce its disciplines:

- fewer agents, narrower capabilities; no subagent for conceptual neatness;
- the three memories kept distinct (engineering / session / product);
- connection auth principal chosen deliberately (app vs user);
- every critical invariant assigned its defense-in-depth layers;
- capability restriction over prompt politeness (what gets `disableTool()`?).

## 4. Define the boundaries that sink agent projects later

Identity/auth per channel and connection; side-effect idempotency (operation
identity before any park boundary); failure handling; data boundaries and
retention; cost/concurrency assumptions; rollback/kill-switch needs;
**the eval taxonomy** — which of eval-rubric.md's 13 categories apply and what
the blocking set is. Evals are designed here, before code exists.

## 5. Write the artifact

Save to `docs/agent-architecture/` per artifacts.md. Decisions and boundaries,
never source-code choreography. Link it from the requirements artifact.

## 6. Close

Report: state now `architecture-ready`, artifact path, key decisions and their
alternatives-rejected, unresolved risks, route to `/koushik:plan`.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
