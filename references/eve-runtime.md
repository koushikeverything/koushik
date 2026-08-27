# Eve runtime reference

Eve is the production runtime for the durable agent. The filesystem is the
authoring contract. Facts below were verified against the live vercel/eve repo
(2026-08); Eve is **beta** and moving — always run the freshness protocol
before writing version-sensitive code.

## Freshness protocol (mandatory, in this order)

1. `package.json` + lockfile — the installed Eve version is the truth.
2. Existing `agent/` conventions in this repository.
3. **Installed docs: `node_modules/eve/docs/`** — the package ships its full
   documentation, matching the installed version. Prefer this over the web.
4. Installed types/exports in `node_modules/eve`.
5. `eve info --json` — the resolved application surface.
6. Current official web docs (eve.dev / github.com/vercel/eve) — for
   latest/upgrade questions only.
7. Model memory — last, never for imports, config keys, or route names.

## Project layout (verified)

```text
agent/
  instructions.md | instructions.ts   # authoring both at root = build error
  instructions/                        # extra modules, read non-recursively
  agent.ts                             # optional defineAgent (model, limits…)
  skills/<name>/SKILL.md
  tools/<slug>.ts                      # file path = tool identity
  connections/<slug>.ts
  subagents/<name>/                    # own agent.ts/instructions/tools…
  sandbox/                             # incl. workspace/ seed files
  channels/<slug>.ts
  schedules/<name>.ts|.md              # path derives schedule name
  hooks/
  lib/
  instrumentation.ts
evals/                                 # APP ROOT, not under agent/
  evals.config.ts                      # exactly one; judge model, reporters…
  *.eval.ts                            # file path = eval identity
```

Scaffold: `npx eve@latest init <target|.>`. Node.js **24+**. Local loop:
`eve dev` (TUI) · `eve invoke` (headless) · `eve info --json` (diagnosis).
Deploy: `eve link` then `eve deploy` (Vercel), or self-host (documented).

## Built-in tools (verified list)

`bash`, `read_file`, `write_file`, `web_fetch`, `web_search`, `todo`,
`ask_question`, `agent` (root session only), `load_skill` (when skills exist),
`connection_search` (when connections exist).

- **Disable** by capability: export the `disableTool()` sentinel from
  `agent/tools/<slug>.ts`. Never rely on prompt politeness.
- **Override**: author a tool at the same slug (may wrap the original).

## Delegation — two different kinds

- **Root copies** (built-in `agent` tool): fresh copies of the root — same
  instructions/connections/auth/sandbox, fresh history and state. Use for
  "same work, independently, possibly parallel."
- **Declared subagents** (`agent/subagents/<name>/`): inherit **nothing** from
  the root's authored slots. The parent must pass everything relevant in the
  delegation message. Use for genuinely different specialists — and for
  independent review (the reviewer never sees the delegator's reasoning).
- **Workflow orchestration**: opt-in experimental — `agent/tools/workflow.ts`
  exporting `experimental_workflow()` from `eve/tools/workflow`. Isolated JS
  orchestration of subagents; not a host escape hatch. Verify current status
  before use.

## Connections and approval

- App-scoped auth: one shared credential across sessions. User-scoped: each
  end user authorizes their own account; requires an authenticated session
  (schedules/no-principal contexts fail with `principal_required`).
- Approval helpers from `eve/tools/approval`: `never()`, `once()` (first time
  per session), `always()`.
- **Credential brokering**: the model never sees a connection's URL or
  credentials; tokens never enter conversation history.

## Durability, sessions, HITL

- The agent emits `input.requested`; the session parks (`session.waiting`);
  compute can stop. Resume by POSTing responses keyed by the pending
  `requestId` to the session's messages endpoint.
- Everything is keyed by the durable **`sessionId`**. Continuation tokens are
  **channel-local identities only** — never accepted or returned by the Eve
  HTTP session API. (Older notes describing a two-token API are stale.)
- **Idempotency-on-resume rule**: any external side effect that survives a
  park/resume boundary must establish its identity (operation key) BEFORE the
  park, never inside the resumed step — or retries/resumes duplicate it.

## State vs memory

- `defineState("ns.name", () => initial)` at module scope → `get()`/
  `update(fn)`. Survives crashes/redeploys/days-long sessions, but is
  **conversation-scoped** — it dies with the session.
- Cross-session memory belongs in an application-owned, principal-scoped
  external store (see `docs/patterns/multi-tenant-memory.md` in the installed
  docs). Never abuse `defineState` for it.

## Evals (verified API)

Run: `eve eval [dir|name] [--url https://<app>]`; exit 0 = gates passed.
Assertions: `t.succeeded()`, `t.parked()`, `t.messageIncludes()`,
`t.calledTool(name, opts?)`, `t.notCalledTool()`, `t.toolOrder([...])`,
`t.usedNoTools()`, `t.maxToolCalls(n)`, `t.noFailedActions()`,
`t.loadedSkill()`, `t.calledSubagent()`, `t.event()/t.notEvent()/
t.eventOrder()/t.eventsSatisfy()`, `turn.outputEquals()/outputMatches(schema)`,
`t.check(...)` value assertions (`includes/equals/matches/similarity/
satisfies`). Severity modifiers: `.gate()` (blocking) / `.soft()` /
`.atLeast()` / `.label()`. An LLM judge is available for open-ended quality.

## Schedules

`agent/schedules/<name>.ts|.md`; `defineSchedule` takes `cron` plus exactly one
of `markdown` (fire-and-forget prompt) or `run` (handler with `to()`,
`waitUntil()`, `appAuth`). `eve dev` never fires cron cadences — test via the
dev-only dispatch route `POST /eve/v1/dev/schedules/<name>`. Production
(`eve start` / deployed) fires them. Design for overlap/re-entry safety.

## Separation rules

- Product identity and always-on invariants → instructions (kept compact).
- Lengthy situational procedure → skills (loaded on demand via `load_skill`).
- Effects → typed tools/connections, never prompt prose.
- Specialists → least capability needed; challenge every subagent that exists
  for conceptual neatness.
- Secrets stay out of model-visible context and sandbox contents.
- Inbound channel identity is untrusted until the channel/auth layer verifies
  it (signatures/tokens, never body claims).
- Consequential external writes: idempotent, authorized in code, and
  approval-gated when product policy requires it.
