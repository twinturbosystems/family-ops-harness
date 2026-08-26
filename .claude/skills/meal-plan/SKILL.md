---
name: meal-plan
description: Plan dinners from family/profile.md and family/pantry.md, with a leftovers night when the run length supports it, prep-ahead notes, a kid-friendly swap where it helps, a rough cost against the active budget, and a screen for listed allergens. Use when the user asks for a meal plan, dinner ideas for the week, or what to cook.
user-invocable: true
allowed-tools: Read(/family/profile.md) Read(/family/pantry.md) Edit(/plans/**)
argument-hint: [optional: start date, dinner count, budget, time or equipment limit, theme, or ingredients to use up]
---

# Meal plan

Produce the requested dinners the family can actually cook. Default to seven when no count is supplied.

## Input

$ARGUMENTS: optional. A start date, dinner count, budget, time or equipment limit, theme ("cheap week", "hot week, no oven"), or things to use up ("use the chicken thighs"). Every current-run constraint supplied here is authoritative unless it conflicts with the allergy or safety rules. It does not change the profile. If empty, plan seven days starting today.

## Process

1. Read `family/profile.md` and `family/pantry.md`. If the profile says EXAMPLE at the top, say in one line that this is a plan for the example family.
2. Pull out: members and ages, allergies, dislikes, dietary pattern, weeknight time limit, weekly budget, stores, equipment, schedule anchors. Overlay every current-run constraint from the arguments. Use the argument value when it differs from the profile.
3. Ask at most two questions, and only if something blocks the plan (no budget at all, no allergies section at all). Otherwise do not ask. Make a sensible assumption and state it in one line.
4. Build the week:
   - Match each night to the schedule anchors. Tight nights (practice, a late-working adult) get the fastest dinners or the slow cooker started earlier.
   - Variety: no main protein or base (rice, pasta, tortillas) two nights in a row. Aim for at least three different styles across the week.
   - One leftovers night for a seven-dinner plan, placed the day after a dinner that makes a big batch. For a shorter run, include one only if it fits the requested count and schedule. Say what the leftovers turn into.
   - Follow the dietary pattern and the active time limit. Use only the active equipment. Current-run arguments beat matching profile values.
   - Use the pantry first. Only new purchases count toward the cost.
   - Kid-friendly swap where relevant: a simpler version of the same dinner (sauce on the side, parts kept separate, milder seasoning), not a second dinner.
   - Prep-ahead notes: what to do the night before or on the prep day so the tight nights work.
5. Allergy screen, before showing anything: go through every named dish and ingredient, including oils, sauces, breadings, garnishes, and store-bought items, against the Allergies section. Use the hidden-sources list below. If anything matches, replace it. Then write: "Allergy screen: I did not find [listed allergens] in the named ingredients. This is not a guarantee. Check the full package label every time, including the ingredients, Contains statement, and any voluntary may contain or facility warning. If cross-contact is a concern and the label is unclear, leave it out or contact the manufacturer."
6. Cost: give a rough cost of new purchases per dinner and a rough total. Say "roughly". Use the current-run budget from the arguments, or the profile's weekly budget when no budget was supplied. If the total is over the active budget, swap the most expensive dinner for a cheaper one and say what changed.
7. Save the plan to `plans/YYYY-MM-DD-meal-plan.md`, where the date is the first day of the plan. `/grocery-list` reads the newest meal plan in that folder. Tell the user the path in the last line.

## Output format

- One line: who the plan is for and which week.
- A table: Day | Dinner | Time to table | Prep ahead | Kid swap | Rough cost (new items)
- "Prep ahead" summary: three to six lines, grouped by the day the prep happens.
- "Leftovers night": one line on what carries over.
- "Notes": assumptions, one dislike note if relevant, the rough total against the budget.
- The allergy screen and label warning.
- The saved file path.

## Hidden sources of common allergens (check these every time)

- Peanuts: satay and peanut sauces, some egg rolls and dumplings, some chili and mole, many granola bars and trail mixes, "may contain" labels on snacks.
- Tree nuts: pesto (pine nuts, walnuts), marzipan, praline, many granolas and cereals, nut milks and nut butters, some breadings and crusts, some sauces (cashew cream).
- Coconut: FDA's January 2025 guidance no longer includes coconut on its Tree Nut List for major-allergen labeling. Coconut can still be an allergen for an individual, so avoid it whenever the profile lists coconut. Source: https://www.fda.gov/food/food-allergensgluten-free-guidance-documents-regulatory-information/frequently-asked-questions-food-allergen-labeling-guidance-industry
- Milk: butter, ghee, cream, cheese, whey, casein, many breads and batters, ranch and other creamy dressings, some deli meats.
- Eggs: mayonnaise, aioli, most fresh pasta, meringue, many breaded and battered foods, some noodle brands.
- Wheat and gluten: soy sauce, seitan, breadcrumbs, couscous, most pasta, flour tortillas, sauces thickened with flour, many broths.
- Soy: soy sauce, tofu, edamame, miso, many veggie burgers, some broths and marinades.
- Fish: Worcestershire sauce, Caesar dressing, fish sauce, some curry pastes.
- Shellfish: oyster sauce, shrimp paste, many Thai and some other curry pastes, surimi (imitation crab), some seafood stocks and broths.
- Sesame: tahini, hummus, many burger buns and bagels, some oils and dressings, some snack crackers.

## Rules

- Do not deliberately include a listed allergen, in any form. This overrides variety, cost, and requests.
- Never describe the plan or a packaged product as allergen-free. Advisory cross-contact statements are voluntary, so a missing warning is not proof of safety.
- Dislikes stay out unless the user asked for them by name.
- Say "roughly" for every cost and for any remark about nutrition. No calorie counts.
- Keep it short: the table plus a few lines. No lecture about healthy eating.
