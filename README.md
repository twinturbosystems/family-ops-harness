# Family Ops Harness

A Claude Code project folder for parents and households. Open it, fill in one profile, and you have a helper that plans dinners, writes the grocery list, sorts out the week, splits the chores, and checks the budget. No build step, no dependencies, no bank connections, and no account beyond the Claude account you already use for Claude Code. Your family's details live in plain text files in this folder and nowhere else.

## Who this is for

This is for whoever in the house does the planning: the one who knows the practice schedule, what the six-year-old will not eat, which store has the cheaper chicken, and how much of the grocery budget is left by Thursday. You keep all of that knowledge. This folder gives you a helper that reads it once and does the tedious part. You do not need to know how to code. If you can fill in a form and type one word into a terminal, you can use it.

## What it does

Six skills. Each one is a command you type inside Claude Code.

- `/meal-plan`: seven dinners from your profile, one leftovers night, prep-ahead notes, a kid-friendly swap where it helps, a rough total under your weekly budget, no allergens.
- `/grocery-list`: the shopping list for the latest plan minus what your pantry file says you have, grouped by store section, with quantities.
- `/week-plan`: paste the week's commitments and get the day-by-day, the conflicts, who drives, and what to prep the night before.
- `/budget-check`: paste last month's expenses as plain lines and get them categorized, compared to your plan, with the three biggest levers named.
- `/chores`: an age-appropriate rotation for the people in your profile, as a table you can print.
- `/school-forms`: paste a form or a school email and get every field listed, what each one needs, the deadlines, and a filled draft from your profile.

## Start in 60 seconds

1. Install Claude Code: https://docs.anthropic.com/en/docs/claude-code
2. Download this folder. On GitHub, click the green Code button, then Download ZIP, and unzip it anywhere. Or run `git clone https://github.com/twinturbosystems/family-ops-harness.git`.
3. Open `family/profile.md` in any text editor and replace the example family with yours. Do the allergies section first. If you want a blank sheet, copy `family/profile.template.md` over it.
4. Open a terminal in the folder. On Windows, right-click the folder and choose Open in Terminal. On a Mac, open Terminal and type `cd ` followed by a space, drag the folder into the window, and press Enter.
5. Type `claude` and press Enter.
6. Type `/meal-plan` and press Enter.

The plan shows on screen and is saved into `plans/` with the date in the filename. Then type `/grocery-list`. Fill in `family/pantry.md` whenever you like; the list gets shorter once it knows what you already have.

## What is in the folder

```
family-ops-harness/
  README.md                 this file
  CLAUDE.md                 the standing instructions the helper follows
  AGENTS.md                 the same, for Codex users
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
    settings.json           pre-approves saving into plans/ so you are not asked every time
```

## Privacy

- Your profile, pantry, and plans are plain text files in this folder. This harness does not sync, upload, or back up anything on its own.
- When you run a skill, Claude Code sends the model what you type plus the files that skill reads: the profile, the pantry, and the latest plan when one is relevant. That is how it knows your allergies and your budget. It also reads `CLAUDE.md` and the skill file, which are instructions, not your data.
- There is no bank connection and no login to anything. The budget check only sees the lines you paste.
- School forms can carry sensitive details. Paste what you are comfortable sending to the model and leave out things like Social Security numbers. The skill will not ask you for them.
- The `plans/` folder is ignored by git by default. If you push this folder to your own GitHub, the `family/` folder goes with it, so keep that repo private or add `family/` to `.gitignore` first.
- `.claude/settings.json` lets the helper write into `plans/` without asking each time. Delete that file if you would rather approve every save.

## Not medical or financial advice

This is a planning helper. It does not know your health situation or your finances beyond the text you give it. Confirm allergens on the label, and talk to a professional for medical, nutrition, or money decisions.

## Why I made this

I build practical things with AI agents, in public, and I wanted a kit a busy household could open and use on day one, with no build step and no jargon. Ibrahim

## More

- Links: https://ibrahim.build/links
- Sibling kits: https://github.com/twinturbosystems/ai-starter-harness and https://github.com/twinturbosystems/security-starter-harness
- Codex users: see `AGENTS.md`

## License

MIT. See `LICENSE`.

Ibrahim Builds is a creator brand from Beit Systems LLC. https://beitsystems.com
