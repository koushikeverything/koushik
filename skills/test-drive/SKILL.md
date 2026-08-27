---
name: test-drive
description: "Drive the real durable agent end-to-end as its target user persona — via eve dev, eve invoke, or the browser when a web channel exists — checking what evals cannot: approval-card clarity, parked-session feel, resume-after-approval seamlessness, refusal helpfulness, evidence honesty; then run the human polish loop. Use after evals are green and before ship. Not automated assertion testing (eval)."
argument-hint: "[journey, channel, or blank for critical journeys]"
---

# Test-drive the product

Read `STRATEGY.md` (the persona and promise) and the requirements artifact's
user journeys. Check `.koushik/config.yaml` `agent_native_level` — driving a
web channel needs level ≥2 (browser); without it, drive via `eve dev`/`eve
invoke` and say what could not be exercised rather than pretending.

## 1. Drive as the persona

Exercise the critical journeys end-to-end as the target user, not as the
builder: first-run/onboarding, the core ask-and-answer loop, an
approval-gated action, a parked-and-resumed session, a refusal path, an
insufficient-evidence path. Schedules: trigger via the dev dispatch route
(`POST /eve/v1/dev/schedules/<name>` — `eve dev` never fires cron cadences).

Judge experience, not correctness (evals already did correctness):
- does parking feel like progress or a crash?
- is the approval card self-explanatory — action, evidence, consequences?
- does resume-after-approval continue seamlessly?
- are refusals helpful next steps or dead ends?
- is uncertainty honest rather than evasive; is evidence inspectable?

The `product-experience-reviewer` agent may take an independent pass on the
same journeys.

## 2. Fix small, escalate taste

Apply only small, clearly-safe, low-risk fixes (copy, an empty state, a
loading flash) — re-running evals after each. Product judgment calls go to
the human, which opens:

## 3. The polish loop (human-led)

The user experiences the product and gives taste feedback ("too dense",
"citations feel like footnotes"); apply, reload, repeat until "this feels
right." Taste comes from the human; iteration speed from the machine. This
loop is deliberately not autonomous.

## Close

Save the report to `docs/test-drives/` per artifacts.md: journeys driven,
findings, fixes applied, escalations and their resolutions, what could not be
exercised. Report: state `experienced`, route to `/koushik:ship`.
