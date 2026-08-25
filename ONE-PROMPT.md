# Set up the Family Ops Kit in your assistant

Downloading the folder is still the first step. This page is not a way to skip it. It is how you switch the downloaded folder on inside the assistant you already use.

Direct download: https://github.com/twinturbosystems/family-ops-harness/archive/refs/heads/main.zip

Unzip it. You get a folder called `family-ops-harness-main`. Open `family/profile.md` in any text editor and put your household in it before you start, allergies first. Then pick the section below that matches your assistant.

## 1. Claude Code

No prompt at all. Claude Code reads `CLAUDE.md` and the `.claude/skills` folder by itself.

1. Open a terminal in the unzipped folder.
2. Type `claude` and press Enter.
3. Say yes to the one-time trust prompt. It only appears once per folder.
4. Type one of the six commands and press Enter.

The commands:

```
/meal-plan
/grocery-list
/week-plan
/budget-check
/chores
/school-forms
```

Optional. If it answers like a general chatbot instead of a household planner, it did not pick the folder up. Paste this once:

```
Read CLAUDE.md in this folder and every SKILL.md file under .claude/skills, then follow those instructions for the rest of this conversation. Read family/profile.md and family/pantry.md before you plan anything. Treat /meal-plan, /grocery-list, /week-plan, /budget-check, /chores and /school-forms as the six jobs described in the matching SKILL.md files. Tell me in one line which files you read, then wait for me.
```

## 2. Codex CLI

Codex reads `AGENTS.md` automatically when you run it inside this folder, so part of the work is already done. Paste this once at the start of the session to make sure it has the rest:

```
You are working inside the Family Ops Kit folder. Read AGENTS.md and CLAUDE.md in this folder, and every SKILL.md file under .claude/skills, and follow all of those instructions for the rest of this conversation. Read family/profile.md and family/pantry.md before you plan anything, and read them again if I tell you they changed. When I type meal-plan, grocery-list, week-plan, budget-check, chores or school-forms, with or without a slash, treat it as the job described in the SKILL.md file of that name, and follow that file's process and output sections. Never suggest an ingredient listed under Allergies in the profile, in any form. Ask me at most two questions, then produce. Save finished plans into plans/ with the date in the filename. Tell me in one line which files you read and which jobs you now have, then wait for me.
```

## 3. ChatGPT or another browser chat

A browser chat cannot see your computer, so you hand it the files yourself.

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
I have attached the instruction files for a household planning kit. Read all of them before you answer anything. Treat CLAUDE.md as your standing instructions for this whole conversation: follow it exactly, above all the allergy rule, and use its tone, its ask-at-most-two-questions rule, and its output style. Treat each attached SKILL.md as one named job triggered by its command word, so when I type meal-plan you follow the meal-plan SKILL.md, and when I type grocery-list you follow that one. Use the attached family profile and pantry as the facts about my household, and read them before you plan anything. If I ask for something the attached files do not cover, ask me rather than assuming. Start by telling me in one line which jobs you now have, then wait for me.
```

Two plain notes about browser chats. They do not keep files between conversations, so attach them again each time you start a new chat. And anything you type or attach there is sent to that provider, so leave out what you would not want to send, such as a Social Security number on a school form.

## 4. Do not have Claude Code or Codex yet?

Section 1 is the smoothest way to run this kit, and it needs Claude Code on the computer first. Installing a developer tool is not usually on a parent's list of things to sort out on a Sunday, and you do not have to work it out alone.

You are already talking to an assistant, and it can talk you through the install step by step. What it cannot do is perform the install or run this kit, because a browser chat cannot reach your computer, and the folder still has to be downloaded either way. Copy the block that matches the tool you want and paste it into ChatGPT, Claude in a browser, or whatever assistant you already have open.

To install Claude Code, paste this:

```
I want to install Claude Code. I may never have opened a terminal, so explain any technical word in one plain sentence and do not rush me.

Start by asking whether I am on Windows, Mac, or Linux, and whether I have ever used a terminal, then adapt to my answer.

Never give me an install command from memory. Install steps change and yours may be out of date. The official documentation is the only source of commands. Have me open https://docs.anthropic.com/en/docs/claude-code and tell you what I actually see there for my system. If that address has moved, have me search for the official Claude Code documentation instead. If a command is not on that page or in what I pasted, say so and find the real one. Never guess.

Before I run anything, tell me in one plain sentence what it does, and never ask me to paste a command I do not understand. Go one step at a time and wait for me to say what happened, including any error text.

Help me through the usual failures: Node missing or too old, the command not found afterwards because of PATH, permission errors, and the terminal not open in the right folder.

We are done when I can type claude in a terminal, it starts, I have opened my unzipped kit folder in it, and I have accepted the one-time trust prompt.
```

To install the Codex CLI, paste this:

```
I want to install the Codex CLI. I may never have opened a terminal, so explain any technical word in one plain sentence and do not rush me.

Start by asking whether I am on Windows, Mac, or Linux, and whether I have ever used a terminal, then adapt to my answer.

Never give me an install command from memory. Install steps change and yours may be out of date. The official documentation is the only source of commands. Have me open https://developers.openai.com/codex/cli and tell you what I actually see there for my system. If that address has moved, have me search for the official Codex CLI documentation instead. If a command is not on that page or in what I pasted, say so and find the real one. Never guess.

Before I run anything, tell me in one plain sentence what it does, and never ask me to paste a command I do not understand. Go one step at a time and wait for me to say what happened, including any error text.

Help me through the usual failures: Node missing or too old, the command not found afterwards because of PATH, permission errors, and the terminal not open in the right folder.

We are done when I can type codex in a terminal, it starts, I have opened my unzipped kit folder in it, and I have accepted the one-time trust prompt.
```

When the tool starts and you have the kit folder open in it, come back to section 1 or section 2 and run `/meal-plan`.
