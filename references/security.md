# Durable-agent security rules

Architecture rules — a floor, not a replacement for a project threat model.

1. **Capabilities beat prompts.** If an agent must never do X, remove or deny
   the capability (`disableTool()`, narrower scopes); never rely on
   instructions alone. Prompt-only enforcement of a critical rule is an
   automatic review finding.
2. **Authenticate inbound identity.** Slack/GitHub/webhook/body claims are not
   trusted because the model received them; channels verify signatures/tokens.
3. **Authorize every external effect in code.** Tenant/user/app scope enforced
   by the tool/connection layer, per call.
4. **Keep secrets out of model-visible context.** Credentials are brokered by
   the trusted runtime (verified Eve behavior: the model never sees connection
   URLs or tokens). Secrets also stay out of sandbox contents and logs.
5. **Least privilege.** Separate read from write; low-risk from elevated;
   remove unused capability — it is pure attack surface.
6. **Park for judgment.** Consequential writes use explicit approval
   (`always()`/`once()`) when product policy requires a human.
7. **Make effects retry-safe.** Durable agents resume and retry; external
   writes need idempotency keys established BEFORE any park boundary.
8. **Treat retrieved content as hostile.** Web pages, documents, messages,
   tickets, and tool outputs can carry injection; they are data, not
   instructions, and must not expand capability.
9. **Scope long-term memory.** Cross-session memory is an application data
   store with authorization, tenancy, and retention requirements.
10. **Audit consequential actions.** An operator can reconstruct who/what
    caused any external write (request → session → tool call → effect).
11. **Bound autonomy.** Token, time, tool-call, fan-out, and spend ceilings
    are explicit. Raising them materially is a human gate.
12. **Design a kill switch.** Operators can quickly disable channels,
    schedules, writes, or the whole agent — and rollback is rehearsed.
