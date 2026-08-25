# Limited browser mode

This is ChatGPT, Claude in a browser, or any other chat window on a website.

## What it cannot do

A chat window on a website cannot reach your computer. That is a limit of the browser, not a setting anyone can change. In limited browser mode this kit cannot:

- operate the folder you downloaded, so it cannot read your profile or your pantry unless you attach those files by hand
- save your progress locally, so no plan is written into `plans/` and nothing carries over into the next chat
- build a finished package of files for you

What it can do is real: advice, analysis, drafts, and copy-ready checklists, including a meal plan and a grocery list you copy out yourself. Nothing typed into a browser chat runs this kit. To actually run it, use Claude Code or the Codex CLI on a computer.

## How to set it up

1. Unzip the downloaded folder.
2. Start a new chat.
3. Attach these files from the folder:
   - `CLAUDE.md`
   - `family/profile.md`, the one you filled in with your household
   - `family/pantry.md`
   - `.claude/skills/meal-plan/SKILL.md`
   - `.claude/skills/grocery-list/SKILL.md`

   Attach the other four SKILL.md files as well if you want those jobs in the same chat.
4. Paste this:

```
I have attached the instruction files for a household planning kit. Read all of them before you answer anything. Treat CLAUDE.md as your standing instructions for this whole conversation: follow it exactly, above all the allergy rule, and use its tone, its ask-at-most-two-questions rule, and its output style. Treat each attached SKILL.md as one named job triggered by its command word, so when I type meal-plan you follow the meal-plan SKILL.md, and when I type grocery-list you follow that one. Use the attached family profile and pantry as the facts about my household, and read them before you plan anything. You are running in limited browser mode, so you cannot see or change the folder on my computer: do not claim to have read, written, or saved any file, and give me text I can copy instead. If I ask for something the attached files do not cover, ask me rather than assuming. Start by telling me in one line which jobs you now have, then wait for me.
```

## Two plain notes

Browser chats do not keep files between conversations, so attach them again each time you start a new chat.

Anything you type or attach there is sent to that provider, so leave out what you would not want to send, such as a Social Security number on a school form.
