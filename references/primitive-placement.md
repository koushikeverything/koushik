# Primitive placement — the smallest justified Eve capability

The central architecture question, asked once per accepted requirement:

> What is the SMALLEST Eve primitive that satisfies this requirement?

Work down this table; stop at the first row that fits. Escalating a row without
a stated reason is the classic failure ("we have an agent framework, therefore
everything becomes an agent").

| Need | Primitive | Design question | Escalate only if |
|------|-----------|-----------------|------------------|
| Always-true identity/invariant | `agent/instructions.md` | Must this be true on nearly every turn? | It's situational → skill |
| Situational procedure | `agent/skills/` | Loaded only when relevant? | It must *act* → tool |
| Executable local action | `agent/tools/` (typed) | What exact typed capability? | It's an external service → connection |
| External service | `agent/connections/` | Auth principal (app vs user)? Scopes? Approval policy? | — |
| Independent perspective | `agent/subagents/` | Does isolation, expertise, or parallelism pay for the cost? | Never "for neatness" |
| Same work, in parallel | built-in `agent` tool (root copies) | Fresh context enough, no capability change needed? | Different capability set → declared subagent |
| Heavy file/code work | `agent/sandbox/` | Should this run outside trusted app runtime? Seed workspace files? | — |
| User/event entry point | `agent/channels/` | How is inbound identity verified? | — |
| Recurring work | `agent/schedules/` | Overlap/re-entry safe? Needs a principal? | — |
| This-conversation memory | `defineState` | Dies with the session — is that correct? | Must survive sessions → external store |
| Cross-session memory | external principal-scoped store + safe tools | Tenant+user scoping enforced in code? Retention policy? | — |
| Human judgment | approval gate (`never()/once()/always()`) + HITL | Which actions park until a person decides? | — |
| Behavioral guarantee | eval (`evals/*.eval.ts`) | What decision/outcome must remain true forever? | — |
| Operational visibility | hooks / `instrumentation.ts` | What must an operator reconstruct? | — |

## The three memories — never conflated

| Memory | Lives in | Owner | Example |
|--------|----------|-------|---------|
| Engineering learnings | `docs/solutions/` | builders | "side effects need identity before parking" |
| Session state | Eve `defineState` | the running conversation | "current filter: Enterprise" |
| Product memory | external tenant+user-scoped store | product & its users | "Jane's default segment is Enterprise" |

## Defense in depth for critical invariants

A rule the product must never break is enforced in EVERY applicable layer, not
one: `STRATEGY.md` (written invariant) → `instructions.md` (always-on rule) →
skill (procedure) → independent reviewer subagent → connection approval gate →
backend authorization + idempotency → eval (regression) → human approval click.
Prompt-only enforcement of a critical rule is an automatic review finding.

## Placement smells

- instructions.md growing past ~150 lines → procedures belong in skills.
- A subagent invoked from exactly one place with no isolation rationale → inline.
- Two tools whose descriptions overlap → the model will misroute; merge or sharpen.
- A tool the agent never uses → remove; unused capability is pure attack surface.
- `defineState` holding user preferences → move to the external memory store.
- A prompt sentence saying "never do X" with the X capability still enabled →
  disable the capability (`disableTool()` / narrower scopes).
- A run-claim/overlap marker released only on success → a crashed run's
  marker blocks honest retries for the whole staleness window (it bit twice
  in one incident). Release the claim on terminal failure too, or size the
  staleness window to the retry cadence — never to the schedule cadence.
