# Maintaining a production durable agent

Maintenance keeps a deployed agent safe, compatible, observable, and
understandable as dependencies, models, data, and user behavior drift. It is
never permission to rewrite a working agent or chase the newest dependency
without evidence. Code/runtime changes go through the normal
plan → work → review → eval → ship gates.

## Maintenance surfaces

### Eve/framework upgrades
- Inspect the pinned version, changelog/release notes, and installed types
  BEFORE proposing changes (freshness protocol — the installed
  `node_modules/eve/docs` after upgrade is the new truth).
- Upgrade in a branch/worktree; run blocking tests/evals before and after.
- Explicitly review behavior changes in defaults, tools, connections,
  approvals, sessions, sandboxes, channels, and schedules.

### Model changes — the canary discipline
Never "new model looks good → change production default." Always:
1. Benchmark the candidate against the stable blocking eval suite.
2. Compare: quality, tool routing, refusal behavior, approval behavior,
   latency, cost — per category, not one blended score.
3. Fix or explicitly accept any regression (a threshold is never lowered
   silently to make a candidate pass).
4. Canary a bounded slice of traffic/workspaces with abort thresholds.
5. Promote only after the canary window; keep rollback one step away.

### Instructions and skills
- Keep always-on instructions compact; remove stale/contradictory procedure.
- Consolidate overlapping skills; sharpen colliding tool descriptions.
- Turn repeated production failures into executable evals or code guards
  (the compound promotion ladder), not more prose.

### Tools, connections, auth — permission drift
- Remove unused permissions and tools; re-audit scopes when provider APIs
  change; rotate credentials through the trusted connection layer.
- Confirm approval policies still match product policy. Widening any write
  scope or lowering any approval requirement is a human gate, always.

### Memory and data
- Review retention/deletion behavior and principal scoping; test restores
  where required; prune knowledge only through deliberate policy.

### Evals
- Keep a stable release-blocking core; grow the regression category; remove
  redundant/flaky evals only with evidence; never normalize degraded quality.

### Operations
- Verify alerts, traces, dashboards, budgets, kill switches actually work;
  keep runbooks executable; review top failure/cost drivers from recent
  pulse reports.

## Maintenance record

For substantial maintenance record: why now; versions/config before/after;
compatibility changes; eval comparison; canary/rollout; rollback; learnings
routed to compound.
