# Worked example: SignalDesk

A compact end-to-end run of koushik. SignalDesk is a durable B2B
product-intelligence agent: it reads approved customer-feedback sources,
answers PM questions with cited evidence, sends a weekly brief, and can
create a Linear issue — only with human approval.

## 1. Start

```text
/koushik:setup
/koushik:lifecycle "Build SignalDesk: a durable product-intelligence agent
that reads approved Slack channels and GitHub issues, produces evidence-backed
weekly briefs, answers PM questions with citations, and can draft/create
Linear issues only with human approval. Tenant-isolated. No DMs. No automatic
roadmap changes."
```

Lifecycle detects `idea`, routes through strategy and brainstorm (one
question at a time: channels? DMs? insufficient-evidence behavior? approval
UX?), then architect maps requirements to primitives:

```text
"claims require cited evidence"     → instructions.md invariant + eval
"analyze a week of feedback"        → skill: analyze-feedback + tool: search_feedback
"challenge conclusions"             → subagent: evidence-reviewer (no write tools)
"create Linear issue on approval"   → connection: linear + always() + op-key idempotency
"Monday brief"                      → schedule: weekly-brief (stagger at scale)
"Jane's default segment"            → external memory store (tenant+user scoped)
```

## 2. Build → ready PR

Plan self-validates (every R-ID → unit, every invariant → eval unit), work
runs the per-unit loop, simplify trims instruction bloat, review routes
safety+reliability+behavior+experience lenses, `eve eval` gates the release
(evidence-required, approval-parks, tenant-isolation, correct-non-action,
retry-resume-idempotency, adversarial-injection…), test-drive checks that
parking feels like progress and the approval card explains itself. Ship opens
a PR carrying eval + test-drive evidence and stops at READY TO MERGE.

## 3. Human merge, then

```text
/koushik:deploy          # manual-only: readiness gate → "DEPLOY TO PRODUCTION?" → verify → monitor
```

## 4. Operate

```text
/koushik:pulse 7d
/koushik:debug "Some approved Linear issues appear twice after reconnect"
/koushik:compound        # → docs/solutions/agents/durable-resume-side-effects.md
/koushik:maintain "evaluate the new model for SignalDesk"
/koushik:scale "Prepare for 1,000 workspaces and 10x brief volume"
```

## 5. The return arrow

A month later, `/koushik:lifecycle "Add Jira as an action target"` — the plan
stage's learnings research finds `durable-resume-side-effects.md`, and the
Jira connection starts with the operation-key pattern. The duplicate-write
incident that cost a production bug on Linear cannot recur on Jira. That is
the compound return: the model didn't get smarter — the repository did.
