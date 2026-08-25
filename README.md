# Family Ops Kit

This kit helps you get the week off your plate: seven dinners, the grocery list, the days laid out, the chore rotation, a budget check, and school forms sorted. You download a folder, open it in an AI assistant, and the assistant becomes a household planner instead of a general chatbot.

## What you need first

- A Mac, Windows, or Linux computer.
- An account with an AI assistant. Claude Code is the smoothest, because this folder is built for it. Install it from the official guide at https://docs.anthropic.com/en/docs/claude-code and it walks you through creating a Claude account the first time you run it.

Choose a kit now, then finish setup on a Mac, Windows, or Linux computer. On your phone? Save this page and come back to it there.

## Download the kit

https://github.com/twinturbosystems/family-ops-harness/archive/refs/heads/main.zip

## Three steps to set it up

1. Unzip the file you just downloaded. You get a folder called `family-ops-harness-main`.
2. Open a terminal in that folder and type `claude`, then press Enter. A terminal is the plain text window where you type commands to your computer.
3. Say yes when it asks whether you trust the files in this folder. It asks once per folder.

## Type this first

Type these three words and press Enter.

```
Start the kit
```

That is the whole first instruction. It is the same three words in every one of these kits.

## What a good result looks like

Within a few seconds the assistant tells you which kit it is reading, names itself, says in one line what this kit does, and gives you the exact next thing to type. It then offers to plan a week of dinners for the fictional example family that already ships in the folder, so you can see a finished plan before you type a single thing about your own household. It does not ask you for personal information to get started.

If that is not what you see, [docs/STUCK.md](docs/STUCK.md) gives one next action for each of the common stumbles.

## Privacy and safety

The kit has no account, no server, and no telemetry, and it does not upload, sync, or back up anything on its own. The files the assistant reads, and everything you type, are sent to that assistant's provider as part of the conversation, the same as any other chat with it. Your household details are stored only as plain text files inside this folder on your computer, in `family/profile.md` and `family/pantry.md`, where you can read, edit, or delete them. School forms can carry sensitive details, so leave out things like Social Security numbers; the kit will not ask for them.

---

Everything below is detail. You do not need it to begin.

## What is this?

It is a folder of files you download onto your own computer. Inside it are written instructions in plain text, which you can open and read like any other document. When you open that folder in Claude Code and start typing, the assistant reads those instructions first, and from then on it behaves like a household planner for this one job instead of a general chatbot you have to explain yourself to from scratch. Developers call a folder like this a harness, which is why the repository is named family-ops-harness.

The instructions also save each job as a short command. You type `/meal-plan` instead of writing a paragraph about your family, your budget, and your allergies every single time. Your household details live in two text files inside the folder, `family/profile.md` and `family/pantry.md`. You fill those in, you edit them, and they stay on your computer.

If this turns out to be useful to you, a star on the repo helps other people find it.

## How it works

The folder is ordinary text files. Nothing in it is compiled, and nothing runs on its own. `CLAUDE.md` holds the standing instructions the helper follows every time: read the profile first, never suggest a listed allergen, ask at most two questions and then produce. Each folder under `.claude/skills` is one named job, written as plain markdown you can open and read.

When you point an assistant at the folder, it reads those instructions before it answers you. From then on it behaves like a household planner for everything you ask, not just the first question. It is not a program that starts up, and nothing is installed on your computer. It is instructions the assistant chooses to follow.

The saved jobs are why you can type one short word instead of describing your family, your budget, and your allergies again every time. `Start the kit` orients you and offers the example. `/meal-plan` gives you seven dinners. `/grocery-list` turns the newest plan into shopping. `/week-plan` lays out the days and finds the conflicts. `/budget-check` sorts last month's spending. `/chores` builds the rotation. `/school-forms` takes a form apart and drafts the answers.

Your household details live in two files you own and edit: `family/profile.md` for the people, ages, allergies, budget, stores, and schedule anchors, and `family/pantry.md` for what is already in the house. The folder ships with a fictional example family filled in, so every job works before you have entered anything of your own. Finished plans are saved into `plans/` with the date in the filename.

One honest limitation. An assistant follows instructions, it does not enforce them the way a locked-down program does, so the guardrails in `CLAUDE.md` are strong defaults rather than a guarantee. The allergy rule is written as the rule that beats everything else, and it is still a written rule. Read the ingredients in a plan before you cook from it, and check the label.

## Other ways to get the same folder

- On this page, click the green Code button near the top, then choose Download ZIP.
- If you already use git: `git clone https://github.com/twinturbosystems/family-ops-harness.git`

## Put your household in

The kit ships with a fictional family so you can see a real plan first. When you are ready for plans that fit your house, open `family/profile.md` in any text editor and replace the example family with yours. Do the allergies section first. If you want a blank sheet instead, copy `family/profile.template.md` over it. `family/pantry.md` is worth filling in whenever you like; the grocery list gets shorter once it knows what you already have.

You do not have to edit either file by hand. You can also say to the assistant, in plain words, "put my family in the profile" and answer its questions.

## Start in 60 seconds

The sixty seconds begins after the assistant is installed and the unzipped folder is open in it. Installing an assistant for the first time takes longer than that, and that is normal.

1. Open a terminal in the folder. On Windows, right-click the folder and choose Open in Terminal. On a Mac, open Terminal and type `cd ` followed by a space, drag the folder into the window, and press Enter.
2. Type `claude` and press Enter. The first time, it asks you to sign in to your Claude account in a browser.
3. Say yes to the trust prompt. The first time Claude Code opens a folder it has not seen before, it asks whether you trust the files in it. That is normal and it only happens once per folder. This is the folder you just downloaded, so choose yes.
4. Type `Start the kit` and press Enter. Expect a short orientation, the exact next thing to type, and an offer to plan a week for the example family so you can see the shape of it.
5. Type `/meal-plan` and press Enter. Expect two questions at most, then a table of seven dinners with a leftovers night, prep-ahead notes, and a rough total.

The plan appears on screen and is saved into `plans/` with the date in the filename. Then type `/grocery-list` to turn it into the shopping.

## Set it up in your assistant

Downloading the folder above is still the first step. This is how you switch that folder on inside the assistant you already use.

- Claude Code: no prompt needed. Open a terminal in the folder, run `claude`, accept the one-time trust prompt, and type `Start the kit`. That is the steps above. Claude Code reads your profile and the instructions by itself and the commands work exactly as typed.
- Codex CLI: run it inside the folder. It reads `AGENTS.md` by itself, and one short paste-in prompt covers the rest.
- Limited browser mode, which means ChatGPT, Claude in a browser, or any other chat window on a website: there is no folder there, so you attach the instruction files, including your filled-in profile, and paste one setup prompt. Read the limits below before you choose this path.

The copy-ready prompts for all three are in the [browser-prompts](browser-prompts/) folder, in plain view rather than inside the hidden `.claude` directory. [ONE-PROMPT.md](ONE-PROMPT.md) is the short guide that points at them.

## Limited browser mode

A chat window on a website cannot reach your computer. That is a hard limit of the browser, not a setting anyone can change. In limited browser mode this kit cannot:

- operate the folder you downloaded, so it cannot read your profile or your pantry unless you attach those files by hand
- save your progress locally, so no plan is written into `plans/` and nothing carries over to the next chat
- build a finished package of files for you

What it can do is real and often enough: give advice, analysis, drafts, and copy-ready checklists, including a meal plan and a grocery list you copy out yourself. Nothing typed into a browser chat runs this kit. To actually run the kit, use Claude Code or the Codex CLI on a computer.

## What you can type

One starting instruction and six commands. Each one is a conversation, not a form.

- `Start the kit`, or `/start`, orients you: which kit this is, what it does, what to type next, and an offer to see a week planned for the example family first.
- `/meal-plan` gives you seven dinners from your profile, one leftovers night, prep-ahead notes, a kid-friendly swap where it helps, a rough total under your weekly budget, and no allergens.
- `/grocery-list` turns the latest plan into a shopping list, minus what your pantry file says you already have, grouped by store section, with quantities.
- `/week-plan` takes the week's commitments you paste in and gives back the day-by-day, the conflicts, who drives, and what to prep the night before.
- `/budget-check` takes last month's expenses as plain lines and gives back categories, a comparison to your plan, and the three biggest levers named.
- `/chores` builds an age-appropriate rotation for the people in your profile, as a table you can print.
- `/school-forms` takes a form or a school email and lists every field, what each one needs, the deadlines, and a filled draft from your profile.

If anything goes wrong at any point, read [docs/STUCK.md](docs/STUCK.md).

## It will not fit you perfectly

This is a starting point, not a finished product. It was written for a general version of a household, and yours is specific. Your week has a shape nobody else's has, and the kit does not know it yet. Some of what it gives you will be wrong for your house.

Everything in the folder is plain text. You can open any file in it with any text editor and read it like a letter. Nothing is compiled, nothing is hidden, and nothing is locked.

The way to change it is to tell the assistant what you want different, and ask it to edit the file for you. You do not have to edit anything by hand. For example, if seven dinners is one too many because Friday is always takeout, type this:

> Plan six dinners, not seven, and leave Friday out. Edit `.claude/skills/meal-plan/SKILL.md` so it does that every week from now on.

The leftovers night works the same way. If nobody in your house will eat leftovers, ask it to take that rule out of the same file. Change the file and the change sticks for every future week, not just this one. Anything that should apply to every job, not just the meal plan, lives in `CLAUDE.md`.

If a change goes wrong, download the folder again and start from the original. Your household details are in separate files, `family/profile.md` and `family/pantry.md`, and your saved plans are in `plans/`. Copy those three somewhere safe first, then put them into the fresh folder.

One honest line. It can be wrong. It can misjudge a cooking time, get a cost wrong, or miss something you wrote in the profile. Read the plan before you shop or cook from it, and check the label yourself on anything where an allergy is involved.

## Who this is for

Whoever in the house does the planning: the one who knows the practice schedule, what the six-year-old will not eat, which store has the cheaper chicken, and how much of the grocery budget is left by Thursday. You keep all of that knowledge. This kit gives you a helper that reads it once and does the tedious part. You do not need to know how to code. If you can fill in a form and type one word into a terminal, you can use it.

## What is in the folder

```
family-ops-harness-main/
  README.md                 this file
  CLAUDE.md                 the standing instructions the helper follows
  AGENTS.md                 the same, for Codex users
  ONE-PROMPT.md             a short guide to setting the kit up in each assistant
  browser-prompts/          the paste-ready prompts, in plain view
  docs/
    STUCK.md                one next action for each of the common stumbles
  family/
    profile.md              your household (ships filled with a fictional example family)
    profile.template.md     a blank copy of the profile
    pantry.md               what you have on hand (ships with an example)
    pantry.template.md      a blank copy of the pantry
  plans/                    where plans, lists, and checks are saved (kept out of git by default)
  examples/
    sample-meal-plan.md     what a finished plan looks like, for the example family
  .claude/
    skills/                 the starting instruction and the six commands
    settings.json           pre-approves saving into plans/ once you have trusted the folder
```

## Privacy, in more detail

- Your profile, pantry, and plans are plain text files in this folder. This kit does not sync, upload, or back up anything on its own.
- When you run a command, Claude Code sends the model what you type plus the files that command reads: the profile, the pantry, and the latest plan when one is relevant. That is how it knows your allergies and your budget. It also reads `CLAUDE.md` and the command file, which are instructions, not your data. Those files go to the assistant's provider as part of the conversation.
- There is no bank connection and no login to anything. The budget check only sees the lines you paste.
- School forms can carry sensitive details. Paste what you are comfortable sending to the model and leave out things like Social Security numbers. The command will not ask you for them.
- The `plans/` folder is ignored by git by default. If you push this folder to your own GitHub, the `family/` folder goes with it, so keep that repo private or add `family/` to `.gitignore` first.
- `.claude/settings.json` lets the helper write into `plans/` without asking each time, once you have opened the folder in Claude Code and accepted the trust prompt. Before that first trust it asks before every save, which is the safe direction. Delete that file if you would rather approve every save.

## Not medical or financial advice

This is a planning helper. It does not know your health situation or your finances beyond the text you give it. Confirm allergens on the label, and talk to a professional for medical, nutrition, or money decisions.

## Why I made this

I build practical things with AI agents, in public, and I wanted something a busy household could open and use on day one, with no build step and no jargon. Ibrahim

## The other three kits

Same idea, different job. Each is a separate folder you download the same way, and each one starts with the same three words.

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
- When something goes wrong: `docs/STUCK.md`
- Paste-ready prompts: `browser-prompts/`
- Codex users: see `AGENTS.md`

## License

MIT. See `LICENSE`.

Ibrahim Builds is a creator brand from Beit Systems LLC. https://beitsystems.com
