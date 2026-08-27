# Production-readiness gate

Run by `/koushik:deploy` (and previewed by ship). An agent is not
production-ready until every applicable item has an explicit answer. "Not
applicable" is an acceptable answer only with a stated reason.

## Identity and access
- Channel/API authentication verified (signatures, not body claims).
- Tenant/user/app principals explicit everywhere data or tools are touched.
- Tool and connection authorization enforced outside prompt text.
- Write capabilities and their approval gates documented.

## Durability and side effects
- External writes idempotent / retry-safe (operation identity before parking).
- Resume after HITL cannot duplicate actions.
- Schedule overlap/re-entry behavior safe (staggering where fan-out is large).
- Terminal failures visible to operators and, where relevant, users.

## Data
- Sensitive data paths known; secrets absent from prompts/sandbox/logs.
- Retention/deletion and long-term memory policy explicit and principal-scoped.
- Backup/recovery exists for durable application state where required.

## Quality
- Blocking conventional tests pass.
- Blocking Eve evals pass (`eve eval` exit 0) — thresholds not lowered to pass.
- Known critical failure modes have regression coverage.
- Representative user journeys test-driven (docs/test-drives/ evidence).

## Operations
- Logs/traces/metrics cover model calls, tools, subagents, approvals, failures.
- Cost/token/concurrency ceilings set.
- Alerting/escalation path for critical failure classes.
- Runbook current: disable, rollback, kill switch — all executable.

## Deployment
- Deploying the merged/release revision, never a local branch.
- Build reproducible; env/connections provisioned without credential leaks.
- Version/commit recorded in docs/deployments/.
- Rollout and rollback mechanisms explicit, with success/abort thresholds.
- **Production deployment requires the user's explicit approval in the current
  conversation.** `/koushik:deploy` is user-invoked only
  (`disable-model-invocation: true`); approval is never inferred.

## After deploy
- Immediate smoke test of critical paths on the deployed version.
- Short monitoring window against the abort thresholds; rollback if breached.
- Deployment record + runbook updated; route to pulse.
