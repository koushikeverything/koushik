---
name: compound
description: "Preserve reusable learnings from building, reviewing, debugging, or operating a durable agent so the next loop starts smarter: solution notes in docs/solutions/ with an enforcement mechanism, vocabulary in CONCEPTS.md, and a promotion ladder for recurring lessons. Also maintains the solution corpus itself (refresh mode). Use after a non-trivial problem is solved or a durable pattern emerges. Never for trivia."
argument-hint: "[resolved problem or learning | refresh]"
---

# Compound the learning

Read `${CLAUDE_PLUGIN_ROOT}/references/artifacts.md` (solution-note contract
and promotion ladder) and inspect existing `docs/solutions/` BEFORE writing
anything — updating or consolidating an existing note beats creating a
duplicate.

If Every's `ce-compound` is available it may handle generic solution-note
mechanics; koushik still enforces the enforcement question and promotion
ladder below.

## 0. Ground rules

- **One learning per run.** A session that produced several gets several
  sequential runs — batching muddies root causes and produces junk-drawer
  notes.
- **Judge preconditions from the session, never interrogate.** The problem
  must be solved, verified working, and non-trivial — decide that from the
  evidence at hand. When the session plainly holds no such problem, write
  nothing and report why.
- **Write boundary.** Any research subagents write to scratch only; the
  orchestrator alone writes the learning, `CONCEPTS.md`, and (with consent)
  a discoverability line in an existing project instruction file — instruction
  files are edited, never created. Nothing else in the tree is touched.

## 1. Separate signal from noise

What actually happened; what caused it; what was incidental; is it already
documented; is it genuinely reusable beyond this instance? Trivia, one-off
typos, transient logs, and unverified conclusions are deliberately NOT
documented. Review reports' recurring-finding sections are standing input.

## 2. Write (or update) the note

Per artifacts.md: category/tags frontmatter; problem, symptoms, root cause,
evidence, failed approaches when instructive, working solution, prevention/
generalization, where future planners should apply it. Findable by the plan
stage's learnings research — that return arrow is the point of this skill.

## 3. The enforcement question (required, blocking)

*"What mechanism now catches this automatically — an eval, a rule, or a
checklist?"* If none: encode it in the strongest appropriate layer (a
regression eval, a code guard, an AGENTS.md rule) before closing. A learning
that exists only as prose is incomplete.

## 4. Promotion ladder on recurrence

When the same lesson keeps recurring: promote it — solution note →
`AGENTS.md` rule → reference checklist item → eval template → (only with
explicit user approval, per lifecycle.md's human gates) a new reviewer lens.
Patterns become tools. Agents are never auto-created.

## 5. Vocabulary

New precise terms go to `CONCEPTS.md` so future sessions don't invent five
names for one thing.

## Refresh mode (`refresh` argument)

Maintain the corpus itself: walk `docs/solutions/` and decide per note —
keep / update / consolidate / replace / delete — so organizational memory
never becomes a junk drawer. Deletions are proposed to the user, not silent.

## Close

Report: state `compounded`, the note path(s), the enforcement mechanism now
in place, any promotions made or proposed.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
