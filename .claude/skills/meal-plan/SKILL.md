---
name: meal-plan
description: Plan seven dinners for the week from family/profile.md and family/pantry.md, with one leftovers night, prep-ahead notes, a kid-friendly swap where it helps, a rough cost under the weekly budget, and no allergens. Use when the user asks for a meal plan, dinner ideas for the week, or what to cook.
user-invocable: true
allowed-tools: Read, Write
argument-hint: [optional: start date, a theme like "cheap week" or "no oven", or things to use up]
---

# Meal plan

Produce seven dinners the family can actually cook this week.

## Input

$ARGUMENTS: optional. A start date, a theme ("cheap week", "hot week, no oven"), or things to use up ("use the chicken thighs"). If empty, plan seven days starting today.

## Process

1. Read `family/profile.md` and `family/pantry.md`. If the profile says EXAMPLE at the top, say in one line that this is a plan for the example family.
2. Pull out: members and ages, allergies, dislikes, dietary pattern, weeknight time limit, weekly budget, stores, equipment, schedule anchors.
3. Ask at most two questions, and only if something blocks the plan (no budget at all, no allergies section at all). Otherwise do not ask. Make a sensible assumption and state it in one line.
4. Build the week:
   - Match each night to the schedule anchors. Tight nights (practice, a late-working adult) get the fastest dinners or the slow cooker started earlier.
   - Variety: no main protein or base (rice, pasta, tortillas) two nights in a row. Aim for at least three different styles across the week.
   - One leftovers night, placed the day after a dinner that makes a big batch. Say what the leftovers turn into.
   - Follow the dietary pattern and the weeknight time limit. Use only the equipment in the profile.
   - Use the pantry first. Only new purchases count toward the cost.
   - Kid-friendly swap where relevant: a simpler version of the same dinner (sauce on the side, parts kept separate, milder seasoning), not a second dinner.
   - Prep-ahead notes: what to do the night before or on the prep day so the tight nights work.
5. Allergen check, before showing anything: go through every dish and every ingredient, including oils, sauces, breadings, garnishes, and store-bought items, against the Allergies section. Use the hidden-sources list below. If anything matches, replace it. Then write one line at the bottom: "Allergen check: no [allergens] in this plan."
6. Cost: give a rough cost of new purchases per dinner and a rough weekly total. Say "roughly". If the total is over the weekly budget, swap the most expensive dinner for a cheaper one and say what changed.
7. Save the plan to `plans/YYYY-MM-DD-meal-plan.md`, where the date is the first day of the plan. `/grocery-list` reads the newest meal plan in that folder. Tell the user the path in the last line.

## Output format

- One line: who the plan is for and which week.
- A table: Day | Dinner | Time to table | Prep ahead | Kid swap | Rough cost (new items)
- "Prep ahead" summary: three to six lines, grouped by the day the prep happens.
- "Leftovers night": one line on what carries over.
- "Notes": assumptions, one dislike note if relevant, the rough total against the budget.
- The allergen check line.
- The saved file path.

## Hidden sources of common allergens (check these every time)

- Peanuts: satay and peanut sauces, some egg rolls and dumplings, some chili and mole, many granola bars and trail mixes, "may contain" labels on snacks.
- Tree nuts: pesto (pine nuts, walnuts), marzipan, praline, many granolas and cereals, nut milks and nut butters, some breadings and crusts, some sauces (cashew cream). The FDA lists coconut as a tree nut for labeling; treat it as one unless the profile says otherwise.
- Milk: butter, ghee, cream, cheese, whey, casein, many breads and batters, ranch and other creamy dressings, some deli meats.
- Eggs: mayonnaise, aioli, most fresh pasta, meringue, many breaded and battered foods, some noodle brands.
- Wheat and gluten: soy sauce, seitan, breadcrumbs, couscous, most pasta, flour tortillas, sauces thickened with flour, many broths.
- Soy: soy sauce, tofu, edamame, miso, many veggie burgers, some broths and marinades.
- Fish: Worcestershire sauce, Caesar dressing, fish sauce, some curry pastes.
- Shellfish: oyster sauce, shrimp paste, many Thai and some other curry pastes, surimi (imitation crab), some seafood stocks and broths.
- Sesame: tahini, hummus, many burger buns and bagels, some oils and dressings, some snack crackers.

## Rules

- Never include an allergen, in any form. This overrides variety, cost, and requests.
- Dislikes stay out unless the user asked for them by name.
- Say "roughly" for every cost and for any remark about nutrition. No calorie counts.
- Keep it short: the table plus a few lines. No lecture about healthy eating.
