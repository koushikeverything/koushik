---
name: strategy
description: "Define or update the durable-agent product strategy in STRATEGY.md before any requirements or code: users, problem, promise, boundaries, agent invariants, autonomy posture, and success metrics. Use for a new agent idea, repositioning, or deciding what the agent must never do. Not for feature requirements (brainstorm) or runtime design (architect)."
argument-hint: "[agent idea or strategy question]"
---

# Define the strategy

Read `${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md` and
`${CLAUDE_PLUGIN_ROOT}/references/artifacts.md` (STRATEGY.md contract).

If Every's `ce-strategy` is available and the user wants it, it may run the
generic product-strategy interview (per
`${CLAUDE_PLUGIN_ROOT}/references/ce-interop.md`); koushik then adds the
agent-specific sections below. Otherwise execute directly.

## 1. Evidence before questions

Read what the repo already knows — README, docs, existing STRATEGY.md, code,
git history. Never ask a question the repository can answer.

## 2. Interview — one consequential question at a time

Ask about the business, not the buttons. Cover, in whatever order the
conversation earns:

- target user and operating context; the painful job;
- promised outcome, and what the user stops doing once it exists;
- why an agent at all, instead of deterministic software alone;
- primary interaction channels;
- **autonomy posture**: advise / draft / act-with-approval / act-within-policy
  — per action class, not one global setting;
- **agent invariants**: actions explicitly prohibited or always human-gated;
  evidence rules for claims; tenancy/data-sensitivity boundaries;
- success, quality, and cost metrics; non-goals; major tracks.

Challenge weak answers once ("is this an analytics product or an assistant?");
accept the user's decision after that.

## 3. Write the artifact

Create or update `STRATEGY.md` per the artifacts.md contract. The invariants
section matters most: every invariant written here will later become an eval
file (eval stage) and an enforcement mechanism (architect stage) — write them
as testable statements, not aspirations.

## 4. Close

Report: state now `strategy-ready` (or what still blocks it), the artifact
path, unresolved product risks, and route to `/koushik:brainstorm` when a
direction is ready.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
