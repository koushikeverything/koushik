# Koushik lifecycle — single source of truth

This file is the ONLY authoritative definition of the lifecycle states, the skill
catalog, and the human gates. Skills reference this file; they must not restate
the state machine (restated copies drift).

## Global execution rules (apply to every skill)

- **Fail closed on references.** If a required reference file cannot be read,
  stop before the action it governs and report the blocker and recovery path —
  never reconstruct the missing mechanism from memory.
- **Gates are satisfied by evidence, not announcement.** A stage advances only
  on valid completion evidence from the artifacts; a blocked or malformed
  result outranks the mere presence of an artifact. Announcing a route or
  rendering a plan is not completing it.
- **Report outcomes, not machinery.** User-facing text names what the user
  recognizes — a PR, a finding, an eval, a state — never internal dispatch
  bookkeeping, subagent plumbing, or setup narration.
- **Settled decisions stay settled.** Never re-ask a decision the conversation
  or an accepted artifact already carries. When new evidence *invalidates* a
  settled decision (infeasible, wrong-thing, destructive), stop and surface it
  to the user explicitly — never silently re-decide either way.

## State machine

Use these states to decide what is ready and what should happen next. Never treat
a later state as reached while an earlier gate is unresolved, and never restart a
completed state unnecessarily — detect, then resume.

| # | State | Meaning | Reached via |
|---|-------|---------|-------------|
| 1 | `idea` | rough agent/product idea only | — |
| 2 | `strategy-ready` | users, problem, promise, boundaries, metrics, autonomy posture explicit in `STRATEGY.md` | strategy |
| 3 | `requirements-only` | flows, behaviors, acceptance, failures, exclusions explicit; `artifact_readiness: requirements-only` | brainstorm |
| 4 | `architecture-ready` | Eve runtime surface, trust boundaries, memory split, eval taxonomy, deployment target explicit | architect |
| 5 | `implementation-ready` | U-ID work units with files, deps, tests, evals, risks; `artifact_readiness: implementation-ready` | plan |
| 6 | `implemented` | code + evals exist; per-unit local checks pass; units ticked in the plan file | work |
| 7 | `simplified` | reuse/context-economy/surface-minimization pass done, behavior preserved | simplify |
| 8 | `reviewed` | risk-selected review complete; criticals fixed or explicitly accepted | review |
| 9 | `eval-green` | blocking behavioral evals and conventional checks pass | eval |
| 10 | `experienced` | real end-to-end test drive done; product judgment applied | test-drive |
| 11 | `pr-ready` | PR open, CI green, review feedback resolved — READY TO MERGE | ship |
| 12 | `merged` | human merged the PR (no skill owns this boundary) | human |
| 13 | `deployed` | production-readiness gates passed, human approved in-conversation, deploy verified | deploy (manual-only) |
| 14 | `observed` | production behavior measured against strategy | pulse |
| 15 | `compounded` | reusable learnings preserved and enforced by a mechanism | compound |

`scaled` is a property, not a sequential state: scale plans/executions run through
the normal loop (plan → work → … → deploy) when they change code or infrastructure.

## Core loop

```text
strategy -> brainstorm -> architect -> plan -> work -> simplify -> review -> eval -> test-drive -> ship
    ^                                                                                              |
    |                                                                                       HUMAN MERGE
    |                                                                                              |
    +----- compound <- debug/maintain/scale <- pulse <- production <- deploy (manual) <------------+
```

## Skill catalog and routing

Every skill ends by printing: current lifecycle state, the durable artifact it
produced/updated, unresolved risk, and the next recommended command.

| Skill | Advances | Routes next |
|-------|----------|-------------|
| `/koushik:setup` | environment + artifact tree ready | strategy (or wherever state detection points) |
| `/koushik:strategy` | 1→2 | brainstorm |
| `/koushik:brainstorm` | 2→3 | architect |
| `/koushik:architect` | 3→4 | plan |
| `/koushik:plan` | 4→5 | work |
| `/koushik:work` | 5→6 | simplify |
| `/koushik:simplify` | 6→7 | review |
| `/koushik:review` | 7→8 | eval (or work for fixes) |
| `/koushik:eval` | 8→9 | test-drive (or debug/work if red) |
| `/koushik:test-drive` | 9→10 | ship |
| `/koushik:ship` | 10→11, stops at READY TO MERGE | human merge, then deploy |
| `/koushik:deploy` | 12→13 (manual-only; `disable-model-invocation: true`) | pulse |
| `/koushik:pulse` | 13→14 | debug / maintain / compound / scale by finding |
| `/koushik:debug` | fixes a failure via causal chain | compound when lesson is reusable |
| `/koushik:maintain` | manages drift (framework/model/permissions/evals) | normal loop for code changes |
| `/koushik:compound` | →15 | next loop's brainstorm/plan |
| `/koushik:scale` | plans/executes deliberate growth | normal loop for implementation |
| `/koushik:lifecycle` | orchestrates 1→11 autonomously | stops at pr-ready; never merges/deploys |

`/koushik:lifecycle` accepts anything from a vague one-line idea to a half-built
app: it detects the earliest incomplete state and routes there. The safety rule is
precise — **refuse premature implementation, never vague starting ideas.** A vague
idea routes into strategy/brainstorm (one consequential question at a time); it is
never coded from directly, and never rejected.

## Human gates

Require explicit human judgment — given in the current conversation, never
inferred from earlier enthusiasm — before:

- selecting a materially different product direction;
- granting new external write capabilities;
- lowering or removing an approval gate;
- widening authentication/authorization scope;
- production data migrations with destructive potential;
- merging a PR (belongs to no skill);
- production deployment, rollout, or rollback;
- materially raising spend, concurrency, or autonomy ceilings;
- creating a new reviewer agent from a compound promotion.

## Agent-native levels

`.koushik/config.yaml` records the repo's detected level. Skills CHECK the level
instead of assuming access; on a missing capability they say what is missing and
what it unlocks, rather than failing confusingly.

| Level | Access | Unlocks |
|-------|--------|---------|
| 1 | files, tests, git | build loop through review/eval |
| 2 | browser, local logs, PRs | test-drive, ship |
| 3 | read-only production logs/monitoring | pulse, debug on production |
| 4 | tickets, deploy, external integrations | deploy, full operations |

## Artifact precedence

When sources disagree, prefer, in order: (1) explicit current user decision;
(2) production/security policy and repository rules; (3) current accepted
strategy/requirements/architecture artifacts; (4) current code/tests/evals;
(5) prior solution notes; (6) old plans or conversation history. Record
meaningful reversals in the durable artifact, not chat memory.
