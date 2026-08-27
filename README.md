# Koushik

Koushik is a Claude Code plugin for taking a **durable AI agent** from a rough
idea to production — and then maintaining and scaling it. It fuses two ideas:

- **Compound Engineering** (Every) as the development method: durable
  artifacts, requirements gating, risk-routed review, and learnings that make
  each loop start smarter than the last.
- **Eve** (Vercel) as the production runtime: the filesystem-first `agent/`
  contract, human-approval parking, durable sessions, and behavioral evals.

Koushik vendors neither project. It can optionally delegate to Every's
compound-engineering plugin when installed (discovered at runtime, never
required), and it verifies Eve against the project's *installed* package and
docs before writing version-sensitive code. General software development
beyond agent products is deliberately deferred to a later version.

## Install

Development / local:

```bash
claude --plugin-dir ./koushik
```

Or as a marketplace:

```text
/plugin marketplace add <path-or-git-repo>
/plugin install koushik
```

Then:

```text
/koushik:setup
/koushik:lifecycle "Build an evidence-backed product research agent"
```

## The lifecycle

```text
idea → strategy → brainstorm → architect → plan → work → simplify
     → review → eval → test-drive → ship → READY-TO-MERGE PR
     → HUMAN MERGE → deploy (manual-only) → production
     → pulse → debug / maintain / scale → compound → next loop
```

Fifteen lifecycle states with explicit gates (see
`references/lifecycle.md`, the single source of truth). Every skill ends by
printing the current state and the next recommended command — you never have
to memorize the catalog.

## The 18 skills

| Command | Purpose |
|---|---|
| `/koushik:setup` | Inspect/prepare the repo: doctor, artifact tree, agent-native level |
| `/koushik:strategy` | `STRATEGY.md`: users, promise, invariants, autonomy posture |
| `/koushik:brainstorm` | Idea → requirements, one consequential question at a time |
| `/koushik:architect` | Requirements → smallest justified Eve primitives + eval taxonomy |
| `/koushik:plan` | Architecture → U-ID work units, self-validated, implementation-ready |
| `/koushik:work` | Build: per-unit isolate→implement→validate→commit→tick loop |
| `/koushik:simplify` | Remove accidental complexity before review, behavior preserved |
| `/koushik:review` | Risk-routed multi-agent review, P0–P3, `--triage` mode |
| `/koushik:eval` | Behavioral evals across 13 categories; the release gate |
| `/koushik:test-drive` | Drive the real agent as its user; human polish loop |
| `/koushik:ship` | Verification → PR with evidence → CI shepherding → READY TO MERGE |
| `/koushik:deploy` | Production gate + human approval + deploy + monitor. **Manual-only** |
| `/koushik:lifecycle` | Orchestrate everything to a ready PR; never merges or deploys |
| `/koushik:pulse` | Time-windowed production reading graded against strategy |
| `/koushik:debug` | Causal-chain root cause; reproduction becomes a permanent eval |
| `/koushik:maintain` | Framework/model/permission drift; canary discipline |
| `/koushik:compound` | Learnings → `docs/solutions/` with an enforcement mechanism |
| `/koushik:scale` | Seven scale dimensions; autonomy treated as a security change |

Seven read-only specialist agents back the review/architecture stages:
requirements-critic, eve-architect, agent-behavior-reviewer,
agent-safety-reviewer, reliability-reviewer, product-experience-reviewer,
scale-reviewer — risk-routed, never all at once.

## Durable artifacts

```text
STRATEGY.md · CONCEPTS.md · .koushik/config.yaml
docs/{plans, agent-architecture, agent-reviews, eval-reports, test-drives,
      deployments, runbooks, pulse-reports, scale-plans, solutions}/
agent/   (Eve runtime surface)          evals/   (behavioral evals)
```

Paths are CE-compatible on purpose: if Every's plugin is installed later,
both share one organizational memory.

## Safety model

Explicit human gates: production deployment (`/koushik:deploy` is
`disable-model-invocation: true`), merging a PR (belongs to no skill),
destructive external actions, widening tool/connection scopes, lowering
approval requirements, and material autonomy/spend increases. Critical agent
invariants are enforced by capability and eval, never prompt prose alone.

## Development

```bash
python3 scripts/validate-plugin.py .
claude plugin validate . --strict
./bin/koushik-doctor
```

## Roadmap (v0.2)

Dogfood by building 2–3 real agents (research, approval-gated operational,
multi-tenant); eval benchmark history; canary/release helpers; **cross-model
adversarial review** (an independent peer review by a different model vendor,
as CE's Stage 3d and Eve's Foreman both do — deferred until the dispatch
plumbing earns its keep); optional enforcement hooks.

## Acknowledgements

Inspired by Every's Compound Engineering methodology; builds applications on
Vercel's Eve framework (beta — koushik's freshness protocol re-verifies Eve
facts against the installed version at use time). Koushik is not an official
Every or Vercel product.
