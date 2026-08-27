# Behavioral eval design

Evals run real agent sessions and assert decisions, not implementation trivia.
For every critical invariant: at least one positive and one negative/
adversarial case where practical. Every invariant in `STRATEGY.md` maps to a
named eval file. See eve-runtime.md for the verified assertion API
(`t.parked()`, `t.calledTool()`, `t.toolOrder()`, `.gate()/.soft()` …).

## The 13 categories

1. **Intent quality** — does the agent solve the user's real task?
2. **Evidence / grounding** — cites required evidence; states uncertainty;
   says "insufficient evidence" instead of guessing.
3. **Skill routing** — loads the right skill when the situation calls for it.
4. **Tool routing** — right tool, right arguments, right order.
5. **Correct non-action** — no tool call when none is justified
   (`t.usedNoTools()` / `t.notCalledTool()`).
6. **Human approval** — consequential actions park before execution
   (`t.parked()`); nothing executes from planning enthusiasm.
7. **Authorization / tenancy** — no principal ever reads or writes another
   principal's data; cross-tenant requests are refused.
8. **Durability** — resume/retry preserves intent without repeating external
   effects (one approval = one side effect).
9. **Memory behavior** — session state scoped to the session; long-term memory
   principal-scoped and only written through safe tools.
10. **Failure handling** — partial failure surfaced honestly; recovery sensible.
11. **Adversarial input** — prompt injection in retrieved content, malicious
    tool results, conflicting evidence: capabilities don't expand, secrets
    don't leak, instructions don't get overridden.
12. **Cost / latency** — representative tasks stay within tool-call and token
    budgets (`t.maxToolCalls(n)`).
13. **Known production regressions** — every real production failure becomes a
    permanent executable case (added by debug before its fix lands). This
    category only grows.

## Quality rules

- Deterministic assertions for tool/order/approval/state behavior; rubric or
  LLM-judge scoring only for open-ended quality.
- Separate **blocking release evals** (`.gate()`) from exploratory ones
  (`.soft()`); exit-code 0 is the ship gate.
- Record model/runtime configuration with results — eval runs double as model
  benchmarks for maintain-stage comparisons.
- **Never lower a blocking threshold to make a change pass.** A threshold
  change is a product/reliability decision made explicitly by the user, and it
  is recorded in the eval report.
- Eval design starts at the architect stage (taxonomy before code); eval
  implementation lands alongside each work unit, never after the feature.
