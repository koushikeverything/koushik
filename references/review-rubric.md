# Risk-selected review rubric

Always review correctness. Add lenses (and their reviewer agents) only when the
change warrants them — never all seven for a 15-line diff. Severity: **P0**
(ship-blocking, must fix now) · **P1** (must fix before merge) · **P2** (should
fix) · **P3** (nice to fix). Every finding: severity, concrete evidence from
the actual code/architecture, user/runtime impact, disposition (fix / accept /
defer). No style-only noise unless it materially harms behavior or maintenance.

## Lens selection

| Diff contains | Route to |
|---|---|
| any code | correctness (always) |
| instructions/skills/tool descriptions/routing | agent-behavior-reviewer |
| auth, tenancy, external writes, connections, secrets, injection surface | agent-safety-reviewer |
| retries, schedules, park/resume, side effects, migrations | reliability-reviewer |
| user-facing surfaces, approval UX, errors, waiting states | product-experience-reviewer |
| capacity, fan-out, budgets, autonomy changes | scale-reviewer |
| requirements/architecture documents (doc-review mode) | requirements-critic |

Reviewers run in separate contexts with read-only tools and never see the
builder's reasoning — independence is the point.

## Lenses

**Correctness** — behavior matches requirements and accepted architecture;
edge/failure states explicit; retries/resumes cannot produce duplicate effects.

**Agent behavior** — instructions clear without bloating always-on context;
procedures in skills, not permanently injected; no overlapping tool/subagent
descriptions the model can misroute; insufficient-evidence and ask-a-human
conditions defined; every behavioral finding gets a recommended eval case.

**Security & authorization** — every external action scoped to the
authenticated principal; secrets out of prompts/logs/sandbox; consequential
writes approval-gated per policy; channel identities verified by signature, not
body claims; prompt injection cannot expand capability or exfiltrate; any
critical rule enforced only by prompt text is an automatic finding.

**Data & privacy** — retention/deletion/residency known; long-term memory
principal-scoped and intentionally writable; session state not abused as user
memory.

**Reliability & durability** — side effects idempotent across retry and durable
resume (operation identity established before parking); timeout/retry/terminal
states defined; schedules cannot overlap or re-enter unsafely; partial
completion visible.

**Tools & connections** — tool capability no wider than instructions imply;
read vs write separated where useful; scopes and approval modes minimal;
unused capability removed.

**Subagents** — each specialist justifies its context/capability boundary;
delegation input complete without leaking unnecessary history; reviewer
independence preserved where it matters.

**Eval coverage** — evals test choices and outcomes, not helper functions;
negative/refusal, auth/tenant, approval, retry/resume, and adversarial cases
present; regressions detectable before deploy.

**Operations** — an operator can correlate request → session → tool calls →
external side effect; cost/token/tool limits bounded; failures alertable.

**Experience** — uncertainty, evidence, actions, approvals, waiting, partial
failure, and recovery are understandable to the target user.

## Process

1. Route lenses by the table; run selected reviewers concurrently.
2. Merge findings into one prioritized list; mark each **auto-fixable** or
   **judgment-needed**.
3. Apply auto-fixable findings P0/P1-first; re-run evals after fixes.
4. `--triage` mode: present judgment-needed findings one at a time — approve
   (status: ready) / skip / adjust priority — for the user to decide.
5. Save substantial reviews to `docs/agent-reviews/` per artifacts.md,
   including the closing **recurring-finding candidates** section for compound.
