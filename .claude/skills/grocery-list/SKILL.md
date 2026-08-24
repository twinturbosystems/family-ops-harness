---
name: grocery-list
description: Build the shopping list for the newest meal plan in plans/, minus what family/pantry.md already has, grouped by store section with quantities and a rough cost. Use when the user asks for a grocery list, a shopping list, or what to buy.
user-invocable: true
allowed-tools: Read, Write, Glob
argument-hint: [optional: a plan file path, or extra items like "add dish soap and bananas"]
---

# Grocery list

Turn the latest meal plan into a list the family can shop from.

## Input

$ARGUMENTS: optional. A specific plan file, or extra items to add. If empty, use the newest file in `plans/` whose name contains `meal-plan`. If there is none, say so and offer to run `/meal-plan` first. Do not invent a plan.

## Process

1. Read `family/profile.md` (household size, stores, allergies), `family/pantry.md`, and the plan file.
2. List every ingredient for every dinner in the plan, with a quantity that fits the household size. Count the people in the profile.
3. Remove anything under "Always stocked" or "Have right now" in the pantry, unless the plan needs more than the family plausibly has on hand. Add everything under "Running low".
4. Add any extras from the arguments.
5. Group by store section: Produce; Meat and fish; Dairy and eggs; Bakery; Dry goods and canned; Frozen; Spices and condiments; Household. Skip empty sections.
6. If the profile lists more than one store, mark items for a secondary store with the store name in parentheses. Everything else goes to the primary store.
7. Put a rough price next to each item and a rough total. Say "roughly". Compare to the weekly budget from the profile in one line.
8. Allergen check: confirm nothing on the list appears under the profile's Allergies or the pantry's "Never buy" section. State it in one line.
9. Save to `plans/YYYY-MM-DD-grocery-list.md` using today's date and tell the user the path in the last line.

## Output format

- One line: which plan this list is for.
- Sections with checkbox lines, for example `- [ ] 2 lb chicken thighs (Costco), roughly $9`.
- Rough total, the budget line, the allergen check line, the saved file path.

## Rules

- Quantities are estimates for the household size; round to what stores sell (a bunch, a bag, 1 lb, a dozen).
- Do not add items that are not in the plan, the running-low list, or the arguments.
- Never add an allergen or a "Never buy" item, even if the plan file contains one by mistake; flag it instead.
- One screen when possible.
