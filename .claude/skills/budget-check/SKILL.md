---
name: budget-check
description: Categorize last month's expenses pasted as plain lines, compare them to the monthly plan in family/profile.md, and name the three biggest levers. No bank access; it only sees what is pasted. Use when the user asks to check the budget, review spending, or see where the money went.
user-invocable: true
allowed-tools: Read(/family/profile.md) Edit(/plans/**)
argument-hint: [paste expenses, plus any current-run budget or category target]
---

# Budget check

Sort last month's spending and compare it to the plan. Arithmetic, not advice.

## Input

$ARGUMENTS: expense lines pasted by the user, in any format, plus any current-run category targets or total budget. A date, a name, and an amount per line is enough. A bank or card export pasted as text is fine. If empty, ask for the paste in one question and stop. A budget or category target supplied here is authoritative for this run and does not change the profile.

## Process

1. Read the Budget section of `family/profile.md` for the monthly plan lines and their category names. Apply any budget or category targets in the arguments for this run instead.
2. Parse each line into date, description, amount. Lines you cannot read go into a "Not counted" list at the end so nothing is dropped silently.
3. Categorize using the same category names as the profile. Anything that does not fit goes to "Other" with the description kept. When a merchant is ambiguous (Costco, Amazon, Target), pick the most likely category and mark it with a question mark so the user can move it.
4. Add up each category. Do the arithmetic carefully and show the per-category totals and the grand total so the user can spot-check.
5. Compare each category to the plan: spent, plan, difference, over or under.
6. Name the three biggest levers: the three places where a change would move next month's total the most, in plain words, with a rough number each. Levers are observations about the pasted numbers, not instructions about what the family should do with money.
7. Save to `plans/YYYY-MM-DD-budget-check.md` when the user asks. Tell them the path.

## Output format

- Table: Category | Spent | Plan | Difference
- Grand total against the planned total, one line.
- "Three biggest levers": three lines.
- "Marked with ?" and "Not counted" lists, if any.

## Rules

- No bank connections, no logins, no links. Only the pasted text.
- Never repeat card numbers or account numbers in the output or the saved file, even if the paste contains them.
- This is arithmetic and sorting, not financial advice. Do not recommend products, investments, or debt moves. If asked, suggest a professional.
- Say "roughly" when rounding.
