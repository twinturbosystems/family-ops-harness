# Codex CLI

Install or update Codex from the official guide at https://learn.chatgpt.com/docs/codex/cli. Codex reads `AGENTS.md` automatically when you run it inside this folder, so part of the work is already done. Paste this once at the start of the session to make sure it has the rest:

```
You are working inside the Family Ops Kit folder. Read AGENTS.md and CLAUDE.md in this folder, and every SKILL.md file under .claude/skills, and follow all of those instructions for the rest of this conversation. Read family/profile.md and family/pantry.md before you plan anything, and read them again if I tell you they changed. When I type start, meal-plan, grocery-list, week-plan, budget-check, chores or school-forms, with or without a slash, treat it as the job described in the SKILL.md file of that name, and follow that file's process and output sections. Treat the words "Start the kit" as the start job, which asks me for nothing about my household. Never suggest an ingredient listed under Allergies in the profile, in any form. Ask me at most two questions, then produce. Save finished plans into plans/ with the date in the filename. Tell me in one line which files you read and which jobs you now have, then wait for me.
```

Then type `Start the kit`.
