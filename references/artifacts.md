# Durable artifact contracts

Koushik prefers durable, inspectable files over transient chat context — but a
file must be **earned**: by a decision a downstream consumer needs in ID'd
form, or by the user asking for one. Small, well-bounded, low-ambiguity work
ends in chat with no artifact ceremony; when the tier is uncertain, take the
heavier one. All paths are repo-relative defaults; keep CE-compatible paths
(`STRATEGY.md`, `docs/plans/`, `docs/solutions/`) so both knowledge corpora
interoperate when Every's Compound Engineering plugin is also installed.

Rules for every artifact write: date artifacts from the system clock, never
from model memory. If `.koushik/config.yaml` sets `docs_root`, validate it —
a repo-relative directory whose resolved path stays inside the repo and is
neither the repo root nor under `.git/`; an invalid value is an error naming
the key and value, never a silent fallback.

```text
STRATEGY.md
CONCEPTS.md
.koushik/config.yaml          # project choices incl. agent-native level; never secrets
docs/
  plans/                      # requirements → implementation-ready (one readiness-tracked file)
  agent-architecture/
  agent-reviews/
  eval-reports/
  test-drives/
  deployments/
  runbooks/
  pulse-reports/
  scale-plans/
  solutions/                  # compound learnings (agents/ subfolder for agent-specific)
agent/                        # Eve runtime surface (see eve-runtime.md)
evals/                        # executable Eve behavioral evals
```

## `STRATEGY.md`

Purpose; primary/secondary users; problem and promised outcome; why an agent
rather than deterministic software alone; differentiators; non-goals and
prohibited behavior; **agent invariants** (evidence rules, always-gated actions,
tenancy); **autonomy posture** (advise / draft / act-with-approval /
act-within-policy); success/quality/cost metrics; major tracks.

## Requirements plan (`docs/plans/`, `artifact_readiness: requirements-only`)

User journeys; stable **R-IDs** (requirements), **A-IDs** (acceptance
expectations), **F-IDs** (failure/edge behavior); actor/agent/system boundaries;
entry channels; data sources and outputs; actions and approval expectations;
session-state vs long-term-memory expectations; tenancy assumptions;
privacy/security constraints; latency/cost expectations; explicit exclusions.
The readiness stamp is a gate: requirements-only forbids implementation.

## Agent architecture (`docs/agent-architecture/`)

Root agent role; requirement → smallest-justified-primitive map (see
primitive-placement.md); instructions vs skills vs tools split; each declared
subagent and why isolation pays for it; channels and identity model;
connections with auth principal, scopes, approval policy; sandbox trust
boundary; **three memories kept distinct** (engineering `docs/solutions/` ≠ Eve
session state ≠ external principal-scoped product memory); schedules/triggers;
**the eval taxonomy, defined here before code exists**; observability/audit;
deployment topology; threat/failure model; cost/concurrency assumptions.
Decisions and boundaries — never pre-written implementation.

## Implementation-ready plan (same file, flipped)

Stable **U-IDs**, each with: objective/end state; source R/A/F IDs; likely
files; dependencies; conventional tests; Eve eval scenarios;
security/approval implications; durability/idempotency implications;
migration/config/deploy implications; rollback constraints. WHAT must be true,
never exact code choreography.

**Self-validation before the flip** (blocking): every R-ID maps to ≥1 unit;
unit dependency graph is acyclic; every STRATEGY invariant has an eval unit.

**Progress lives here:** work ticks units off in this file as they complete,
and records any deviation from the plan next to the unit it changed.

## Review artifact (`docs/agent-reviews/`)

Scope; risk lenses selected and why; findings with severity (P0–P3), concrete
evidence, user/runtime impact; disposition per finding (fix / accept / defer);
unresolved risks; and a closing **recurring-finding candidates** section — the
mechanical handoff to compound.

## Eval artifact (`docs/eval-reports/`)

Design notes and run summaries; executable evals live in the repo's real eval
location. Record model/runtime config and thresholds. A blocking threshold is
never lowered silently — that is a product decision, made explicitly.

## Test-drive report (`docs/test-drives/`)

Journeys driven; parking/approval/resume experience; refusal quality; evidence
honesty; small safe fixes applied; product judgments escalated; polish-loop
outcomes.

## Deployment record (`docs/deployments/`) and runbook (`docs/runbooks/`)

Version/commit; environment; config/migration changes; checks and evals run;
rollout and rollback mechanism; success/abort thresholds; known limitations;
owner/on-call path. Runbook stays executable and current.

## Solution note (`docs/solutions/<category>/…​.md`)

Frontmatter: category, tags. Body: problem/symptoms; root cause; evidence;
failed approaches when instructive; working solution; prevention/
generalization; where future planners should apply it.

**Required closing field — the enforcement question:** *"What mechanism now
catches this automatically — an eval, a rule, or a checklist?"* If the answer
is none, the learning is incomplete: encode it in the strongest appropriate
layer before closing.

**Promotion ladder** (applied by compound on recurrence): solution note →
`AGENTS.md` rule → reference checklist item → eval template → (only with
explicit user approval) a new reviewer lens. Patterns become tools; agents are
never auto-created. Only compound non-trivial, reusable knowledge.
