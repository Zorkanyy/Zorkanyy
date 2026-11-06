# skills-library

On-demand skills. Not loaded at startup; the `skill-library` skill in `.claude/skills/` finds them via `INDEX.md`.

- Always-on skills: `.claude/skills/`
- Promote a skill to always-on: move its folder into `.claude/skills/`.
- After adding/removing skills here, rebuild the index: `python3 gen_index.py .` (run from this folder).
