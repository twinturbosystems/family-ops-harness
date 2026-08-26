---
name: grocery-list
description: Build the shopping list for the newest meal plan in plans/, minus what family/pantry.md already has, grouped by store section with quantities and a rough cost. Use when the user asks for a grocery list, a shopping list, or what to buy.
allowed-tools: Read(/family/profile.md) Read(/family/pantry.md) Read(/plans/**) Edit(/plans/**)
---

# Grocery list

Turn the latest meal plan into a list the family can shop from.

## Input

$ARGUMENTS: optional. A specific plan file, budget, store, exclusions, or extra items. Current-run instructions here are authoritative unless they conflict with the allergy or safety rules, and they do not change the profile. If empty, use the newest file in `plans/` whose name contains `meal-plan`. If there is none, say so and offer to run `/meal-plan` first. Do not invent a plan.

## Process

1. Read `family/profile.md` (household size, stores, allergies), `family/pantry.md`, and the plan file.
2. List every ingredient for every dinner in the plan, with a quantity that fits the household size. Count the people in the profile.
3. Remove anything under "Always stocked" or "Have right now" in the pantry, unless the plan needs more than the family plausibly has on hand. Add everything under "Running low".
4. Apply the arguments: add requested extras and use any current-run budget, store, or exclusion instead of the matching profile value.
5. Group by store section: Produce; Meat and fish; Dairy and eggs; Bakery; Dry goods and canned; Frozen; Spices and condiments; Household. Skip empty sections.
6. If the profile lists more than one store, mark items for a secondary store with the store name in parentheses. Everything else goes to the primary store.
7. Put a rough price next to each item and a rough total. Say "roughly". Compare it in one line to the current-run budget from the arguments, or the weekly budget from the profile when no budget was supplied.
8. Allergy screen: compare every named item with the profile's Allergies and the pantry's "Never buy" section. Remove and flag any match. Then state: "Allergy screen: I did not find [listed allergens] in the named items. This is not a guarantee. Check the full package label every time, including the ingredients, Contains statement, and any voluntary may contain or facility warning. If cross-contact is a concern and the label is unclear, leave it out or contact the manufacturer."
9. Save to `plans/YYYY-MM-DD-grocery-list.md` using today's date and tell the user the path in the last line.

## Output format

- One line: which plan this list is for.
- Sections with checkbox lines, for example `- [ ] 2 lb chicken thighs (Costco), roughly $9`.
- Rough total, the budget line, the allergy screen and label warning, the saved file path.

## Rules

- Quantities are estimates for the household size; round to what stores sell (a bunch, a bag, 1 lb, a dozen).
- Do not add items that are not in the plan, the running-low list, or the arguments.
- Do not deliberately add an allergen or a "Never buy" item, even if the plan file contains one by mistake; flag it instead.
- Never describe the list or a packaged product as allergen-free. Advisory cross-contact statements are voluntary, so a missing warning is not proof of safety.
- One screen when possible.
