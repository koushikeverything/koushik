# Scaling durable agents — seven dimensions, treated separately

Scale only the dimension actually under pressure, with evidence. "More users"
and "more autonomy" are different problems; conflating them is how agents get
dangerous quietly.

## The seven dimensions

### 1. Tenant scale (100 → 10,000 companies)
Principal-scoped state/memory partitioning; authorization on every boundary;
tenant-aware rate and spend limits; noisy-neighbor isolation.

### 2. Traffic scale (10 → 10,000 concurrent workflows)
Durable workflow/store capacity; queueing/backpressure; sandbox provisioning
limits; schedule fan-out (stagger stampedes — 1,000 workspaces × Monday 8am);
external API rate limits.

### 3. Knowledge scale (10 docs → millions of records)
Always-on instructions stay compact; procedures in skills; retrieve rather
than inject; version knowledge and its migration rules.

### 4. Agent scale (1 root → specialist delegation)
Delegate only when isolation, expertise, or parallelism pays for cost/latency;
cap fan-out and recursion; keep reviewer independence intentional; measure
per-subagent contribution.

### 5. Autonomy scale (advise → draft → approved action → bounded autonomous action)
**A security and product change, not an infrastructure optimization.** Moving
up this ladder requires: strategy review, new approval design, new evals for
the newly-autonomous behavior, explicit human approval — the full loop, never
a config tweak. Also: read/write tool separation, capability tiers, audit on
every consequential effect.

### 6. Cost scale ($100/mo → $100k/mo)
Quality/cost model tiers; session/token/tool budgets; cache deterministic
work; cheaper paths for low-value volume; compare models through evals before
changing defaults; cost per outcome, not per request.

### 7. Operations scale (one engineer → platform)
Idempotency keys; retry policy by failure class; timeouts/cancellation;
terminal/dead-letter states; graceful degradation when dependencies fail;
canary + rollback for instruction/model/tool changes; runbooks that scale past
their author.

## Scale plan contract (`docs/scale-plans/`)

Current bottleneck + evidence · target load/autonomy · architecture changes ·
safety changes · cost model · load/eval test plan · rollout/rollback ·
success and abort thresholds.

Execution goes through the normal loop. Never raise production
spend/concurrency/autonomy ceilings materially without explicit approval;
infrastructure-mutating scale execution is user-invoked, not model-initiated.
