---
name: brainstorm
description: "Turn a durable-agent idea into explicit requirements before architecture or code: user journeys, agent responsibilities, evidence and refusal rules, approval boundaries, memory expectations, tenancy, failure behavior, and an MVP boundary. Use after strategy exists, or when a feature idea needs definition. Not for mapping onto Eve primitives (architect) or implementation planning (plan)."
argument-hint: "[feature or durable-agent idea]"
---

# Brainstorm the requirements

Read `${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md`,
`${CLAUDE_PLUGIN_ROOT}/references/artifacts.md` (requirements contract), and
`${CLAUDE_PLUGIN_ROOT}/references/security.md`. Ground yourself in
`STRATEGY.md`; if it is missing and the idea is a whole product, route to
`/koushik:strategy` first — a feature on an established product may proceed.

If Every's `ce-brainstorm` is available and suitable, it may run the generic
requirements engine (per `${CLAUDE_PLUGIN_ROOT}/references/ce-interop.md`);
koushik then deepens the result with the agent lenses below.

## 0. Right-size before any ceremony

Classify the request from bounded inline reads before dispatching anything.
**Lightweight** — small, well-bounded, low ambiguity — ends in a chat
paragraph: the decisions stated, no file, no research fan-out. A file is
earned only by a decision a downstream consumer needs in ID'd (R/A/F) form,
or by the user asking for one. When the tier is uncertain, take the heavier
one; a risk surface (auth, payments, external writes, tenant data, autonomy)
always forces the full path.

## 1. Light repo research first

Read the existing code, plans, and `docs/solutions/` touching this area.
Never ask the user a factual question the repository answers, and never
re-ask a decision the conversation or an accepted artifact already settled
(lifecycle.md's settled-decisions rule).

## 2. One consequential question at a time

Never a form. Each question should settle a real product decision. Work
through the agent-specific dimensions ordinary specs skip:

- entry channels and user journeys;
- what the agent may decide vs what stays deterministic application logic;
- evidence/grounding required for claims; when it must refuse or say
  "insufficient evidence" instead of guessing;
- external actions and their approval expectations;
- session-state vs cross-session-memory expectations;
- multi-user/tenant assumptions; privacy constraints;
- schedule/event-driven behavior; failure and partial-completion behavior;
- latency/cost expectations; auditability; explicit scope exclusions.

Propose 2–4 candidate directions when the shape is genuinely open (ideation
mode), then converge with the user.

## 3. Prototype to reduce uncertainty (optional)

When a behavior or interaction is genuinely uncertain and arguing won't settle
it, offer a throwaway prototype: a disposable `eve dev` agent or mock the user
can experience. Conclusions flow back into the requirements; the prototype is
never the foundation of production code.

## 4. Write the artifact

Create or update one requirements file under `docs/plans/` per artifacts.md:
stable R-/A-/F- IDs, and frontmatter `artifact_readiness: requirements-only`.
That stamp is a gate — it means "we know WHAT it must do" and forbids
implementation. Do not choose Eve primitives, imports, or code here.

## 5. Close

Report: state now `requirements-only`, artifact path, the decisions made, open
questions if any, and route to `/koushik:architect`.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
