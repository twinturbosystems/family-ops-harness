---
name: chores
description: Build an age-appropriate chore rotation for the household members in family/profile.md, as a weekly table the family can print. Use when the user asks for chores, a chore chart, or who does what around the house.
user-invocable: true
allowed-tools: Read, Write
argument-hint: [optional: "two weeks", "add walk the dog", "Leila has exams this week"]
---

# Chores

Split the housework so everyone knows what is theirs this week.

## Input

$ARGUMENTS: optional. Length of the rotation, chores to add or remove, or a temporary change ("one kid is away Tuesday").

## Process

1. Read `family/profile.md`: members with ages, and the Chores section (what each person can do, how adults split things, what is off-limits).
2. Build the chore list from the profile. If the profile has no Chores section, use the age bands below and say that the family should adjust them.
3. Assign. Daily chores rotate by day; weekly chores rotate by week. Kids get chores that match their age band and the profile's notes. Adults split the rest evenly unless the profile says otherwise. Nothing off-limits goes to a kid.
4. Keep the kids' load light and visible: two or three daily items each and one weekly item.
5. Output the table for the week (or the length asked) and two lines on running it: where to hang it and what happens when a chore is missed. No lecture.
6. Save to `plans/YYYY-MM-DD-chores.md` when the user asks.

## Age bands (general starting points; the parents decide)

- 3 to 5: put toys away, put clothes in the hamper, put napkins on the table, wipe up small spills.
- 6 to 8: set and clear the table, feed pets with help, sort laundry, water plants, make the bed.
- 9 to 12: load and unload the dishwasher, take out trash and recycling, fold and put away own laundry, simple food prep without the stove, vacuum a room.
- 13 and up: cook a simple dinner with an adult nearby, laundry start to finish, clean a bathroom, yard work, short stretches of watching a younger sibling when the parents agree.

## Output format

- Table: Chore | Mon | Tue | Wed | Thu | Fri | Sat | Sun, with a name in each cell, or "-" for none that day.
- Weekly chores as a second short table: Chore | Who | When
- Two lines on running it.

## Rules

- The profile beats the age bands.
- Never assign a chore the profile lists as off-limits.
- No rewards, points, or allowance advice unless asked.
- Short lines, printable.
