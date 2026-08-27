# Compound Engineering interoperability (optional, discovered, never required)

Koushik is self-contained. When Every's `compound-engineering` plugin is
installed, koushik MAY delegate generic engineering mechanics to it — but every
delegation follows the rules below. When CE is absent, execute the koushik
stage directly with the same principles.

## Discovery, not assumption

Detect CE availability at runtime (available skills in the current session, or
the doctor's detection). Never assume a fixed CE inventory or flag set — CE
versions move. Before using a mode flag, confirm it exists in the installed
CE's skill (its `argument-hint`/description states its modes).

## Delegation map

| Koushik stage | CE skill (when available + confirmed) | Koushik still owns |
|---|---|---|
| strategy | `ce-strategy` | autonomy posture, agent invariants |
| brainstorm | `ce-brainstorm` | agent lenses: channels, approvals, memory, tenancy, refusal behavior |
| plan | `ce-plan` | Eve architecture constraints, eval units, self-validation gate |
| work | `ce-work` **`mode:return-to-caller` ONLY** | freshness protocol, runtime invariants, canonical commits |
| simplify | `ce-simplify-code` | behavior-preservation via eval re-run |
| review | `ce-code-review` (`mode:agent`, optionally `apply:local`) | Eve-specific reviewer routing on top |
| debug | `ce-debug` when the incident is code-shaped | agent/session/HITL causal layers |
| compound | `ce-compound` | agent-specific discoverability + enforcement question |
| pulse | `ce-product-pulse` when suitable | agent metrics (approvals, parks, token cost, eval drift) |

## The critical rule: never plain `ce-work` from an orchestrated flow

Standalone `ce-work` runs its own shipping tail (simplify, review, PR, CI
babysitting) — calling it plainly from koushik's lifecycle duplicates koushik's
remaining stages and breaks gate ownership.

Verified interop surface (CE ≥3.x): `ce-work` accepts
`mode:return-to-caller [implementation_engine:<compact-json>]
[implementation_run:<safe-id>] <plan path>` — implementation + local
verification only, returning a structured envelope (`status`, `changed_files`,
`u_ids_completed`, `verification_results`, `unit_receipts`, `blockers`,
`standalone_shipping_skipped: true`; schema in CE's
`references/implementation-result-schema.json`). The caller (koushik) owns
authoritative verification, canonical commits, and all downstream gates.

`ce-code-review` verified modes: `mode:agent` (concurrent reviewer dispatch,
no changes applied), `apply:local` (apply findings to working tree),
`base:<ref>`. Default reviews the current branch without mutations.

## Delegation conduct

- Pass accepted koushik artifacts as context; preserve their scope decisions.
- Do not let a delegate change artifact semantics (`artifact_readiness` values
  are shared vocabulary: `requirements-only` / `implementation-ready`).
- Shared artifact paths (`STRATEGY.md`, `docs/plans/`, `docs/solutions/`) are
  intentionally CE-compatible — both corpora form one organizational memory.
- A delegation that fails or returns a blocker → fall back to executing the
  koushik stage directly; never leave the lifecycle half-delegated.
