---
name: week-plan
description: Turn pasted commitments (practices, appointments, work travel, school events) plus the schedule anchors in family/profile.md into a day-by-day family week with conflicts flagged, who drives, and what to prep the night before. Use when the user asks to plan the week, sort the schedule, or find conflicts.
user-invocable: true
allowed-tools: Read(/family/profile.md) Read(/plans/**) Edit(/plans/**)
argument-hint: [paste the week's commitments, or a note like "same as usual plus dentist Thursday 4pm"]
---

# Week plan

Lay out the family's week so nobody is in two places at once.

## Input

$ARGUMENTS: the week's commitments in any form (a paste from a group chat, a school email, a list, or "same as usual plus ..."), plus any current-run date range, time limit, or driver change. Current-run instructions are authoritative and do not change the profile. If empty, ask for the commitments in one question and stop.

## Process

1. Read `family/profile.md`: members, schedule anchors, who drives, weeknight time limit. If a meal plan for this week exists in `plans/`, read it so dinners line up with the evenings.
2. Merge the anchors with the pasted commitments. Anchors repeat every week unless the paste says otherwise.
3. Ask at most two questions if something is unclear (which day, which kid, morning or evening). Otherwise assume and say so in one line.
4. Build the day-by-day. For each day: morning, after school, evening; who is where and when; who drives; dinner from the meal plan if one exists, otherwise "quick dinner" on tight nights.
5. Flag conflicts: two people needed in two places with one driver; a pickup that overlaps a start time; an evening with no time to cook; travel that leaves one adult solo for bedtime. Suggest a fix for each (carpool, swap drivers, move dinner earlier, leftovers night).
6. Night-before prep: for each day, the one to three things that make the next morning easier (bags, forms, uniforms, thaw the chicken, charge the tablet).
7. Save to `plans/YYYY-MM-DD-week-plan.md` (the Monday of that week) when the user asks or when the output is longer than one screen. Tell them the path.

## Output format

- Table: Day | Who is where (times) | Driver | Dinner | Night-before prep
- "Conflicts": one line per conflict with the suggested fix. If there are none, say so in one line.
- "This week's one thing": the single item most likely to be forgotten, such as a form deadline or a uniform.

## Rules

- Do not invent commitments. If the paste is unclear, ask (two questions at most) or label the item "unclear".
- Keep times exactly as the user wrote them.
- Short lines. One screen when possible.
