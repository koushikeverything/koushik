#!/usr/bin/env python3
"""Structural validator for the koushik plugin.

Checks manifest, skill/agent frontmatter, required references, and that every
${CLAUDE_PLUGIN_ROOT} path mentioned in a skill or agent actually exists.
Run: python3 scripts/validate-plugin.py [plugin-root]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
errors: list[str] = []
warnings: list[str] = []

KEBAB = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')

manifest = root / '.claude-plugin' / 'plugin.json'
data: dict = {}
try:
    data = json.loads(manifest.read_text(encoding='utf-8'))
    name = data.get('name')
    if not isinstance(name, str) or not KEBAB.fullmatch(name):
        errors.append('plugin name must be kebab-case')
except Exception as exc:  # noqa: BLE001
    errors.append(f'invalid plugin.json: {exc}')

mkt = root / '.claude-plugin' / 'marketplace.json'
if mkt.is_file():
    try:
        m = json.loads(mkt.read_text(encoding='utf-8'))
        for key in ('name', 'owner', 'plugins'):
            if key not in m:
                errors.append(f'marketplace.json missing {key}')
        for entry in m.get('plugins', []):
            if entry.get('version') and data.get('version') and entry['version'] != data['version']:
                errors.append('marketplace.json plugin version != plugin.json version')
    except Exception as exc:  # noqa: BLE001
        errors.append(f'invalid marketplace.json: {exc}')


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        errors.append(f'{path.relative_to(root)}: missing YAML frontmatter')
        return {}
    end = text.find('\n---\n', 4)
    if end < 0:
        errors.append(f'{path.relative_to(root)}: unterminated YAML frontmatter')
        return {}
    out: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith((' ', '- ')):
            continue
        if ':' in line:
            k, v = line.split(':', 1)
            out[k.strip()] = v.strip().strip('"\'')
    return out


def check_plugin_root_refs(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    for ref in re.findall(r'\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)', text):
        ref = ref.rstrip('.')
        target = root / ref
        if not (target.is_file() or target.is_dir()):
            errors.append(f'{path.relative_to(root)}: references missing {ref}')


EXPECTED_SKILLS = {
    'setup', 'strategy', 'brainstorm', 'architect', 'plan', 'work', 'simplify',
    'review', 'eval', 'test-drive', 'ship', 'deploy', 'lifecycle', 'pulse',
    'debug', 'maintain', 'compound', 'scale', 'tracker',
}
MANUAL_ONLY = {'deploy'}

skill_names: set[str] = set()
for path in sorted((root / 'skills').glob('*/SKILL.md')):
    fm = frontmatter(path)
    sname = fm.get('name', '')
    desc = fm.get('description', '')
    if not KEBAB.fullmatch(sname):
        errors.append(f'{path.relative_to(root)}: invalid skill name {sname!r}')
    if sname != path.parent.name:
        errors.append(f'{path.relative_to(root)}: frontmatter name {sname!r} != folder {path.parent.name!r}')
    if sname in skill_names:
        errors.append(f'{path.relative_to(root)}: duplicate skill name {sname}')
    skill_names.add(sname)
    if len(desc) < 60:
        errors.append(f'{path.relative_to(root)}: description too short (<60 chars)')
    if len(desc) > 1536:
        errors.append(f'{path.relative_to(root)}: description exceeds 1536-char limit')
    if sname in MANUAL_ONLY and fm.get('disable-model-invocation') != 'true':
        errors.append(f'{path.relative_to(root)}: {sname} must set disable-model-invocation: true')
    check_plugin_root_refs(path)

missing_skills = EXPECTED_SKILLS - skill_names
if missing_skills:
    warnings.append(f'skills not yet authored: {", ".join(sorted(missing_skills))}')
unexpected = skill_names - EXPECTED_SKILLS
if unexpected:
    warnings.append(f'skills outside expected catalog: {", ".join(sorted(unexpected))}')

EXPECTED_AGENTS = {
    'requirements-critic', 'eve-architect', 'agent-behavior-reviewer',
    'agent-safety-reviewer', 'reliability-reviewer',
    'product-experience-reviewer', 'scale-reviewer',
}
agent_names: set[str] = set()
for path in sorted((root / 'agents').glob('*.md')):
    fm = frontmatter(path)
    aname = fm.get('name', '')
    desc = fm.get('description', '')
    if not KEBAB.fullmatch(aname):
        errors.append(f'{path.relative_to(root)}: invalid agent name {aname!r}')
    if aname in agent_names:
        errors.append(f'{path.relative_to(root)}: duplicate agent name {aname}')
    agent_names.add(aname)
    if len(desc) < 40:
        errors.append(f'{path.relative_to(root)}: description too short (<40 chars)')
    if 'disallowedTools' not in fm:
        warnings.append(f'{path.relative_to(root)}: reviewer has no disallowedTools (expected read-only)')
    check_plugin_root_refs(path)

if agent_names and agent_names != EXPECTED_AGENTS:
    warnings.append(f'agent roster differs from expected: {sorted(agent_names ^ EXPECTED_AGENTS)}')

REQUIRED_REFS = [
    'references/lifecycle.md',
    'references/artifacts.md',
    'references/eve-runtime.md',
    'references/primitive-placement.md',
    'references/review-rubric.md',
    'references/eval-rubric.md',
    'references/security.md',
    'references/production.md',
    'references/maintenance.md',
    'references/scale.md',
    'references/ce-interop.md',
    'references/upstream.md',
    'references/frontstage.md',
]
for rel in REQUIRED_REFS:
    if not (root / rel).is_file():
        errors.append(f'missing {rel}')

for w in warnings:
    print(f'WARN:  {w}')
if errors:
    for err in errors:
        print(f'ERROR: {err}')
    sys.exit(1)
print(f'OK: {data.get("name")} with {len(skill_names)} skills and {len(agent_names)} agents')
