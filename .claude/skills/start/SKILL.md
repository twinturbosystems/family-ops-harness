---
name: start
description: The first thing to run in this folder. Confirms from the files which kit this is, names the assistant running it, says in one line what the kit does, gives the exact next thing to type, and offers a worked example built on the fictional example family that ships in the folder. Asks for no personal information. Use when the person types "Start the kit", "/start", "start", or asks what this folder is, how to begin, or where to start.
user-invocable: true
allowed-tools: Read(/README.md) Read(/.claude/skills/**) Read(/family/profile.md) Read(/family/pantry.md) Read(/examples/sample-meal-plan.md) Read(/docs/STUCK.md)
argument-hint: [nothing needed, just type: Start the kit]
---

# Start the kit

The person has downloaded a folder, opened it, and typed three words. They are a busy parent, not a developer, and they may not know what a skill, a command, or a hidden folder is. Your job is to get them from nothing to a first result without asking them for anything about their household.

## Never, in this skill

- Never ask for a name, an age, an allergy, an address, a school, a budget, a store, or any other household detail. Not one question. This skill exists to be usable before any of that.
- Never ask them to fill in `family/profile.md` before they can see anything.
- Never explain what a skill, an agent, markdown, or a hidden directory is. None of that is needed to succeed here.
- Never guess what is in the folder. Read it.

## Step 1. Confirm which kit this is, from the files

Read `README.md` in this folder, and list the folders under `.claude/skills/`. Do not decide from the folder name alone.

This folder is the Family Ops Kit. Its repository is named `family-ops-harness`, so the unzipped folder is usually called `family-ops-harness-main`. If what you actually read does not match that, say so plainly in one line and stop rather than pretending. Point the person at `docs/STUCK.md` and let them tell you what they see.

## Step 2. Say these five things, in this order, in about ten lines

1. Which kit this is, by name, and that you read that from the files in the folder rather than assuming it.
2. Which assistant is running it. Name yourself, for example "You are running this in Claude Code." If you are not certain which product you are, say which one you believe you are and add that the kit works the same either way.
3. What this kit does, in one line: it plans the household week, meaning seven dinners, the grocery list, the days laid out, the chores, a budget check, and school forms.
4. The very next thing to type, on its own line, exactly as it should be typed:

   ```
   /meal-plan
   ```

   Then one line on what it will do: ask at most two questions, then give back seven dinners with a leftovers night, prep-ahead notes, and a rough total.
5. The offer, as one question: "Want to see a week planned for the example family first? The folder ships with a fictional family already filled in, so nothing about your household is involved."

Then stop and wait for their answer. Do not run ahead into the plan, and do not start asking meal-plan questions yourself.

Do say, in one short line, that they can put their own household in later by editing `family/profile.md`, or by asking you to do it for them. Do not make it a step they have to complete first.

## Step 3. If they want the example

Read `family/profile.md` and confirm it is still the fictional example family. Then either run the meal-plan job for that example family, following `.claude/skills/meal-plan/SKILL.md`, or read `examples/sample-meal-plan.md` and show them that. Either way, say in one line up front that the family is invented and the plan is an illustration. Finish by pointing them back at `/meal-plan` as the thing to type once their own household is in the profile.

## Step 4. If they ask for something else

Answer briefly and follow the standing instructions in `CLAUDE.md`, including the allergy rule. If what they are asking for is one of the other jobs in this folder, name the command and offer it. If they say something is broken or they cannot get started, point them at `docs/STUCK.md` and give one next action rather than a list.

## Tone

Short sentences. Plain words. No exclamation marks, no emojis, no hype. Do not congratulate them for downloading a folder. Say what is here, say what to type, and get out of the way.
