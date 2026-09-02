---
name: setup
description: "Inspect and prepare a repository for koushik durable-agent development with Eve. Use when starting a new agent project, adding koushik to an existing app or Eve project, diagnosing prerequisites, or asking where the project currently stands in the lifecycle. Not for defining the product (strategy) or building (work)."
argument-hint: "[project goal, or blank to inspect]"
---

# Set up koushik in this repository

Read `${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md` and
`${CLAUDE_PLUGIN_ROOT}/references/artifacts.md` before acting. Setup is
idempotent: running it again repairs and reports; it never duplicates.

## 1. Diagnose

Run `${CLAUDE_PLUGIN_ROOT}/bin/koushik-doctor` and read its output. It checks
versions and compatibility, not mere existence. Then classify the repo:
new/empty · existing app with no Eve agent · existing Eve project · existing
koushik project. Inspect rather than assume: `package.json`, lockfile,
`agent/`, `evals/`, `docs/`, project instruction files.

## 2. Greenfield git

If not a git repository: `git init -b main` and an initial commit. If no
remote exists, offer `gh repo create` — only with the user's explicit
permission, never silently. Do not push anything during setup.

## 3. Create the artifact tree

Create any missing pieces of the durable artifact layout from artifacts.md:
`docs/{plans,agent-architecture,agent-reviews,eval-reports,test-drives,deployments,runbooks,pulse-reports,scale-plans,solutions}/`
(a `.gitkeep` in empty dirs), `CONCEPTS.md` (seed with a one-line purpose if
absent), and extend — never overwrite — `AGENTS.md`/`CLAUDE.md` with a short
koushik section: artifact locations, the freshness protocol pointer, and the
rule that critical invariants are enforced by capability, not prompt prose.

## 4. Record project configuration

Create or update `.koushik/config.yaml` (never secrets):
- `agent_native_level`: the NUMERIC level `1`–`4` per lifecycle.md's table —
  detect what access this environment actually has (browser? gh auth?
  production logs? deploy) and record the number plus the evidence lines
  that support it.
- `ce_interop`: whether Every's compound-engineering plugin is detected
  (doctor reports this). Mark `optional` either way.
- `docs_root` if the user relocates artifacts.

## 5. Do not overreach

Setup never installs Eve (work scaffolds it when the plan calls for it),
never deploys, and never modifies application code.

## 6. Close

Report: doctor summary, repo classification, agent-native level, what was
created vs already present, the current lifecycle state per lifecycle.md's
state machine, and the next recommended command (usually `/koushik:strategy`
for a fresh project, or wherever state detection points).

---

*Frontstage: this stage's close, every decision it puts to the user, and any
error it reports follow `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` —
plain-language outcomes with action types, guided decisions (meaning, why
now, impact, recommendation, reversibility, what happens next), and an
in-place update to the live project tracker when one exists
(`/koushik:tracker`).*
