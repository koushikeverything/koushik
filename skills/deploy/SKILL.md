---
name: deploy
description: "Deploy a merged durable-agent release to production: verify the merged revision, run the full production-readiness gate, build and smoke-test, obtain explicit human approval in this conversation, deploy, verify live, monitor against abort thresholds, and record the deployment. Manually invoked only — this skill is never triggered by the model."
argument-hint: "[environment or release ref, blank for default]"
disable-model-invocation: true
---

# Deploy to production

This skill is user-invoked only (`disable-model-invocation: true`): the model
cannot decide something "looks ready" and trigger it. Deployment begins with
a human keystroke and proceeds only through a human approval.

Read `${CLAUDE_PLUGIN_ROOT}/references/production.md` (the full gate),
`${CLAUDE_PLUGIN_ROOT}/references/security.md`, and the latest review/eval/
test-drive/deployment artifacts.

## 1. Verify what is being deployed

The merged/release revision on the default branch — never a local or feature
branch. Record the exact commit. Confirm lifecycle history: `pr-ready` was
reached and the PR was merged by a human.

## 2. Production-readiness gate

Walk production.md's checklist item by item; every applicable item gets an
explicit answer ("N/A" only with a stated reason). Verify current build/
deploy commands via the freshness protocol (expect `eve build`, `eve link`,
`eve deploy` for Vercel; self-hosting per installed docs). Run a
production-equivalent build and local smoke test.

## 3. Present the deployment plan, then the gate

Show: environment, version/commit, config/migration changes, rollout
mechanism, success metrics, abort thresholds, rollback mechanism. Then ask
the unmistakable question — **deploy to production?** — and wait.

Approval must be explicit, in this conversation, for this deployment.
Silence, prior planning enthusiasm, or "it should be fine" are not approval.
Declined or unanswered → stop, leaving everything recorded and ready.

## 4. Deploy, verify, monitor

After approval: execute only the agreed scope. Immediately smoke-test the
critical paths on the deployed version. Hold a short monitoring window
against the abort thresholds; breach → execute the rollback mechanism and
report honestly.

## 5. Record

Write `docs/deployments/<date>-<name>.md` and create/update the runbook
(disable path, rollback, kill switch, owner) per artifacts.md.

## Close

Report: state `deployed` (or rolled back, with evidence), deployment record
path, route to `/koushik:pulse` after real usage accumulates. Never claim
production success without post-deploy verification.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
