# Upstream sources and verification

Koushik vendors neither upstream project. When current behavior matters, verify
against authoritative sources in this order of preference.

## Eve (runtime)

1. The repository's installed package: `node_modules/eve/docs/` (ships full
   docs matching the installed version) and installed types/exports.
2. `eve info --json` for the resolved application surface.
3. https://github.com/vercel/eve and https://eve.dev/ — for latest/upgrade
   questions. Templates: https://eve.dev/templates · Integrations:
   https://eve.dev/integrations

Eve is beta; APIs may change before general availability. Never write imports,
config keys, or route names from model memory when verification is possible.

## Compound Engineering (optional interop)

- https://github.com/EveryInc/compound-engineering-plugin — each skill's
  authoritative runtime spec is `skills/<skill>/SKILL.md`.
- Guide: https://every.to/guides/compound-engineering
- Discover installed CE skills and their modes at runtime; never freeze an
  inventory here (see ce-interop.md).

## Claude Code plugin platform

- Plugins: https://code.claude.com/docs/en/plugins
- Reference: https://code.claude.com/docs/en/plugins-reference
- Skills: https://code.claude.com/docs/en/skills
- Subagents: https://code.claude.com/docs/en/sub-agents
