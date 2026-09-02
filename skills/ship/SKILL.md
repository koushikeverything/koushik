---
name: ship
description: "Take a reviewed, eval-green, test-driven change to a READY-TO-MERGE pull request: final verification, clean commits, push, a PR carrying its eval and test-drive evidence, then bounded CI and review-feedback shepherding. Stops at ready-to-merge — merging is the human's act, and production deployment is the separate /koushik:deploy skill. Not for deploying (deploy)."
argument-hint: "[branch or blank for current]"
---

# Ship to a ready-to-merge PR

Read `${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md` and the latest review,
eval, and test-drive artifacts.

## 1. Gate check (blocking)

Confirm the lifecycle really is `reviewed`, `eval-green`, and `experienced` —
from the artifacts, not memory. A missing gate: STOP and route to it.
Enthusiasm never skips gates. Requires a git remote and authenticated `gh`
(agent-native level ≥2); if absent, say exactly what is missing.

## 2. Commit and push

Clean, convention-aware commits (work should have left per-unit commits;
tidy only what is safe). Push the feature branch. Never push to the default
branch directly.

## 3. Open the PR — it carries its own proof

PR body assembled from real evidence, not adjectives: what changed (by unit),
eval results (blocking set, config), test-drive report link, review
disposition summary, known limitations, rollback notes. A reviewable
boundary, not a "trust me."

## 4. Shepherd, bounded

Watch CI and review activity for this PR:
- CI failure → diagnose with debug discipline, fix, push; if it exposes a
  real defect, route through `/koushik:debug` properly.
- Review comments → evaluate honestly, fix where justified (re-running
  evals), answer with evidence where not. Never rubber-stamp or dismiss.
Bounded: shepherd this PR's checks and feedback; do not expand scope or
start new features from review commentary — new scope routes to brainstorm.

## 5. Stop at READY TO MERGE

When CI is green and feedback is resolved, declare READY TO MERGE and stop.
**This skill never merges.** Merging is a human decision that belongs to no
skill; production deployment is `/koushik:deploy`, user-invoked only.

## Close

Report: state `pr-ready`, PR URL, evidence summary, anything the human
should weigh before merging, and the reminder that after merging, deployment
is `/koushik:deploy`.

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
