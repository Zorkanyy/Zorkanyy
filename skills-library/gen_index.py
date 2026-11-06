import os, re, sys
root = sys.argv[1]
out = ["# Skill library index", "", "Skills here are NOT auto-loaded. To use one: Read its SKILL.md and follow it. Relative paths inside a skill resolve against that skill's own folder.", "References like `superpowers:<name>` mean `skills-library/superpowers/<name>/SKILL.md`; `thinking-skills:thinking-<slug>` means `skills-library/thinking/thinking-<slug>/SKILL.md`.", ""]
for group in sorted(os.listdir(root)):
    g = os.path.join(root, group)
    if not os.path.isdir(g): continue
    out.append(f"## {group}")
    for name in sorted(os.listdir(g)):
        p = os.path.join(g, name, "SKILL.md")
        if not os.path.isfile(p): continue
        txt = open(p, encoding="utf-8").read()
        m = re.search(r"^description:\s*(.*?)(?=^\w[\w-]*:|^---)", txt, re.S | re.M)
        desc = " ".join(m.group(1).split()).strip("\"'>| ") if m else ""
        if len(desc) > 180: desc = desc[:177].rstrip() + "..."
        out.append(f"- **{name}** — `skills-library/{group}/{name}/SKILL.md` — {desc}")
    out.append("")
out.append("## ads agents\nSubagent definitions for the ads skills live in `skills-library/ads/_agents/`. To use one, copy it into `.claude/agents/` (takes effect next session), or pass its file contents as the prompt to a general-purpose agent.")
open(os.path.join(root, "INDEX.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
