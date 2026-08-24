# Family Ops Kit

A folder you download that turns Claude Code into a household planner: seven dinners, the grocery list, the week laid out, the chore rotation, a budget check, and school forms sorted.

## What is this?

It is a folder of files you download onto your own computer. Inside it are written instructions in plain text, which you can open and read like any other document. When you open that folder in Claude Code and start typing, the assistant reads those instructions first, and from then on it behaves like a household planner for this one job instead of a general chatbot you have to explain yourself to from scratch. Developers call a folder like this a harness, which is why the repository is named family-ops-harness.

The instructions also save each job as a short command. You type `/meal-plan` instead of writing a paragraph about your family, your budget, and your allergies every single time. Your household details live in two text files inside the folder, `family/profile.md` and `family/pantry.md`. You fill those in, you edit them, and they stay on your computer. The folder does not sync, upload, or back up anything on its own.

If this turns out to be useful to you, a star on the repo helps other people find it.

## How it works

The folder is ordinary text files. Nothing in it is compiled, and nothing runs on its own. `CLAUDE.md` holds the standing instructions the helper follows every time: read the profile first, never suggest a listed allergen, ask at most two questions and then produce. Each folder under `.claude/skills` is one named job, written as plain markdown you can open and read.

When you point an assistant at the folder, it reads those instructions before it answers you. From then on it behaves like a household planner for everything you ask, not just the first question. It is not a program that starts up, and nothing is installed on your computer. It is instructions the assistant chooses to follow.

The saved jobs are why you can type one short word instead of describing your family, your budget, and your allergies again every time. `/meal-plan` gives you seven dinners. `/grocery-list` turns the newest plan into shopping. `/week-plan` lays out the days and finds the conflicts. `/budget-check` sorts last month's spending. `/chores` builds the rotation. `/school-forms` takes a form apart and drafts the answers.

Your household details live in two files you own and edit: `family/profile.md` for the people, ages, allergies, budget, stores, and schedule anchors, and `family/pantry.md` for what is already in the house. Finished plans are saved into `plans/` with the date in the filename. All of it sits on your machine, and the folder does not sync, upload, or back anything up on its own.

One honest limitation. An assistant follows instructions, it does not enforce them the way a locked-down program does, so the guardrails in `CLAUDE.md` are strong defaults rather than a guarantee. The allergy rule is written as the rule that beats everything else, and it is still a written rule. Read the ingredients in a plan before you cook from it, and check the label.

## What you need first

An AI assistant. This kit works with Claude Code, with Codex, or with a browser chat like ChatGPT. Claude Code is the smoothest of the three, because the folder is built for it: it reads your profile and the instructions by itself and the commands work exactly as typed.

Claude Code is Anthropic's assistant that runs in a terminal window on your computer. Install it by following the official guide: https://docs.anthropic.com/en/docs/claude-code

Claude Code signs in with a Claude account. If you do not have one yet, it walks you through creating one the first time you run it.

If you would rather use Codex or a browser chat, download the folder first the same way, then follow `ONE-PROMPT.md` for the exact steps and the prompt to paste.

## Download the kit

The one-click way, straight to the zip file:

https://github.com/twinturbosystems/family-ops-harness/archive/refs/heads/main.zip

Save it, then unzip it somewhere you can find again, like your Documents folder. Unzipping gives you a folder called `family-ops-harness-main`. That folder is the kit.

Two other ways to get the same folder, if you prefer them:

- On this page, click the green Code button near the top, then choose Download ZIP.
- If you already use git: `git clone https://github.com/twinturbosystems/family-ops-harness.git`

## Start in 60 seconds

1. Fill in your family. Open `family/profile.md` in any text editor and replace the example family with yours. Do the allergies section first. If you want a blank sheet instead, copy `family/profile.template.md` over it.
2. Open a terminal in the folder. A terminal is the plain text window where you type commands to your computer. On Windows, right-click the folder and choose Open in Terminal. On a Mac, open Terminal and type `cd ` followed by a space, drag the folder into the window, and press Enter.
3. Type `claude` and press Enter. The first time, it asks you to sign in to your Claude account in a browser.
4. Say yes to the trust prompt. The first time Claude Code opens a folder it has not seen before, it asks whether you trust the files in it. That is normal and it only happens once per folder. This is the folder you just downloaded, so choose yes.
5. Type `/meal-plan` and press Enter. Expect two questions at most, then a table of seven dinners with a leftovers night, prep-ahead notes, and a rough total.

The plan appears on screen and is saved into `plans/` with the date in the filename. Then type `/grocery-list` to turn it into the shopping. Fill in `family/pantry.md` whenever you like; the list gets shorter once it knows what you already have.

## Set it up in your assistant

Downloading the folder above is still the first step. This is how you switch that folder on inside the assistant you already use.

- Claude Code: no prompt needed. Open a terminal in the folder, run `claude`, accept the one-time trust prompt, and type a command. That is the five steps above.
- Codex CLI: run it inside the folder. It reads `AGENTS.md` by itself, and one short paste-in prompt covers the rest.
- ChatGPT or another browser chat: there is no folder there, so you attach the instruction files, including your filled-in profile, and paste one setup prompt.

The exact steps and copy-ready prompts for all three are in [ONE-PROMPT.md](ONE-PROMPT.md).

## What you can type

Six commands. Each one is a conversation, not a form.

- `/meal-plan` gives you seven dinners from your profile, one leftovers night, prep-ahead notes, a kid-friendly swap where it helps, a rough total under your weekly budget, and no allergens.
- `/grocery-list` turns the latest plan into a shopping list, minus what your pantry file says you already have, grouped by store section, with quantities.
- `/week-plan` takes the week's commitments you paste in and gives back the day-by-day, the conflicts, who drives, and what to prep the night before.
- `/budget-check` takes last month's expenses as plain lines and gives back categories, a comparison to your plan, and the three biggest levers named.
- `/chores` builds an age-appropriate rotation for the people in your profile, as a table you can print.
- `/school-forms` takes a form or a school email and lists every field, what each one needs, the deadlines, and a filled draft from your profile.

## Who this is for

Whoever in the house does the planning: the one who knows the practice schedule, what the six-year-old will not eat, which store has the cheaper chicken, and how much of the grocery budget is left by Thursday. You keep all of that knowledge. This kit gives you a helper that reads it once and does the tedious part. You do not need to know how to code. If you can fill in a form and type one word into a terminal, you can use it.

## What is in the folder

```
family-ops-harness-main/
  README.md                 this file
  CLAUDE.md                 the standing instructions the helper follows
  AGENTS.md                 the same, for Codex users
  ONE-PROMPT.md             how to set the kit up in Claude Code, Codex, or a browser chat
  family/
    profile.md              your household (ships filled with a fictional example family)
    profile.template.md     a blank copy of the profile
    pantry.md               what you have on hand (ships with an example)
    pantry.template.md      a blank copy of the pantry
  plans/                    where plans, lists, and checks are saved (kept out of git by default)
  examples/
    sample-meal-plan.md     what a finished plan looks like, for the example family
  .claude/
    skills/                 the six commands
    settings.json           pre-approves saving into plans/ once you have trusted the folder
```

## Privacy

- Your profile, pantry, and plans are plain text files in this folder. This kit does not sync, upload, or back up anything on its own.
- When you run a command, Claude Code sends the model what you type plus the files that command reads: the profile, the pantry, and the latest plan when one is relevant. That is how it knows your allergies and your budget. It also reads `CLAUDE.md` and the command file, which are instructions, not your data.
- There is no bank connection and no login to anything. The budget check only sees the lines you paste.
- School forms can carry sensitive details. Paste what you are comfortable sending to the model and leave out things like Social Security numbers. The command will not ask you for them.
- The `plans/` folder is ignored by git by default. If you push this folder to your own GitHub, the `family/` folder goes with it, so keep that repo private or add `family/` to `.gitignore` first.
- `.claude/settings.json` lets the helper write into `plans/` without asking each time, once you have opened the folder in Claude Code and accepted the trust prompt. Before that first trust it asks before every save, which is the safe direction. Delete that file if you would rather approve every save.

## Not medical or financial advice

This is a planning helper. It does not know your health situation or your finances beyond the text you give it. Confirm allergens on the label, and talk to a professional for medical, nutrition, or money decisions.

## Why I made this

I build practical things with AI agents, in public, and I wanted something a busy household could open and use on day one, with no build step and no jargon. Ibrahim

## The other three kits

Same idea, different job. Each is a separate folder you download the same way.

AI Starter Kit, for people who are new to AI tools and want to build one small real thing today.
Download: https://github.com/twinturbosystems/ai-starter-harness/archive/refs/heads/main.zip
Read first: https://github.com/twinturbosystems/ai-starter-harness

Security Starter Kit, for people who are new to security and want their own accounts, devices, and small business locked down.
Download: https://github.com/twinturbosystems/security-starter-harness/archive/refs/heads/main.zip
Read first: https://github.com/twinturbosystems/security-starter-harness

GovCon Starter Kit, for a solo government contractor who wins prime contracts and delivers through subcontractors and teaming partners.
Download: https://github.com/twinturbosystems/govcon-starter-harness/archive/refs/heads/main.zip
Read first: https://github.com/twinturbosystems/govcon-starter-harness

## More

- Everything I make, in one place: https://ibrahim.build/links
- Codex users: see `AGENTS.md`

## License

MIT. See `LICENSE`.

Ibrahim Builds is a creator brand from Beit Systems LLC. https://beitsystems.com
