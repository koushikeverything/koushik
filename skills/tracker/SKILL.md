---
name: tracker
description: "Create or refresh the live HTML project tracker — a plain-language, continuously updated view of where the build stands: stage rail, what each stage produced and why, decisions waiting on the user, what the system has learned, recommended next action, and distance to a usable product. Use to answer 'where are we?', after any stage completes, or when starting a project. Not a build stage — a window onto them."
argument-hint: "[blank to create/refresh, or a question about status]"
---

# The live project tracker

Read `${CLAUDE_PLUGIN_ROOT}/references/frontstage.md` (the contract this
page embodies) and `${CLAUDE_PLUGIN_ROOT}/references/lifecycle.md` (the
state machine the rail renders). The tracker translates the durable
artifacts into product progress — it never invents state: everything on the
page derives from STRATEGY.md, the plan file's readiness stamp and unit
ticks, the architecture/review/eval/test-drive/deployment artifacts, and
git/PR status.

## 1. Locate or create

Check `.koushik/config.yaml` for a `tracker` entry (path and, when
published, its stable URL). Exists → refresh that same page in place; the
URL/location never changes for a project. Absent → create it now and record
the entry.

**Where it lives:** if the host can publish an updateable web page
(an artifact/preview capability), publish there — one stable link the user
can keep open. Otherwise write `docs/tracker.html` and tell the user, in
plain words, to open it in their browser (and that it refreshes on every
stage). Either way the file itself lives in the repo so it survives hosts.

## 2. What the page must show

Self-contained HTML, light+dark safe, phone-friendly, no external assets.
Sections, in order:

1. **Header** — project name, one-line promise (from STRATEGY.md), current
   status word (Planning / Building / Checking / Waiting on you / Blocked /
   Shipping / Live), and the rough progress estimate per frontstage.md.
2. **Stage rail** — the 15 lifecycle states as a visual rail: done /
   current / blocked / not yet. The current stage says what is happening
   right now and which skill/agent is doing it.
3. **Waiting on you** — pending decisions rendered per the decision-support
   contract (meaning, why now, impact, recommendation, reversibility, what
   happens after). Empty state: "Nothing needs you right now."
4. **What's been built** — per completed stage: what was produced in plain
   language, why it was needed, which part of the product it serves, action
   type (🗂🔨✅🚀🧠), who did it (skill/specialist), with a small
   expandable "technical detail" line naming the actual files/commands for
   readers who want it.
5. **🧠 What the system learned** — accumulated compound learnings in the
   frontstage.md shape. Empty state explains that learnings will appear as
   the system improves itself.
6. **Next** — the recommended next action; whether it needs the user; the
   remaining path to a usable, deployed product in a few plain steps.
7. **Footer** — last-updated timestamp (system clock) and links to the
   deep artifacts (strategy, plan, reports) for technical readers.

## 3. Update discipline

- Refresh = edit the existing page in place; keep its structure and any
  stable URL. Never fork a second tracker for the same project.
- Derive, don't remember: re-read the artifacts each refresh; the page must
  match the repo even if the conversation is stale or a new session picks
  the project up cold.
- Never let the page run ahead of reality: a stage renders done only when
  its gate evidence exists (lifecycle.md's evidence rule applies here too).
- Every other skill's close step already says to update the tracker when
  one exists — this skill is also directly invocable whenever the user asks
  "where are we?" (answer in chat per the reporting contract AND refresh
  the page).

## Close

Report per frontstage.md: where the project stands, what changed on the
page, the link/location, and the recommended next action.
