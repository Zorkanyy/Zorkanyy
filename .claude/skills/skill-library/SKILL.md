---
name: skill-library
description: On-demand library of 115+ extra skills (paid ads, Remotion/HyperFrames/video editing, graphify knowledge graphs, 27 thinking models, superpowers dev workflows, extra caveman tools). Use when a task needs a specialist skill not already loaded.
---

# Skill library

Extra skills live in `skills-library/` at the repo root. They are not auto-loaded, to save tokens.

1. Read `skills-library/INDEX.md` (one line per skill, grouped).
2. Pick the one best match (or none). Don't load several "just in case".
3. Read that skill's `SKILL.md` and follow it as if invoked. Relative paths in it resolve against its own folder.
4. If it points to another skill (e.g. `superpowers:x`, `thinking-skills:thinking-x`), find it in the index the same way.

Groups: ads, caveman, graphify, hyperframes, remotion, superpowers, thinking, video.
