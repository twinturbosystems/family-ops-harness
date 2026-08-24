---
name: school-forms
description: Take a pasted school form, permission slip, or school email and list every field, what each needs, the deadlines, and a filled draft using family/profile.md where possible. Use when the user pastes a form or asks what a school email wants from them.
user-invocable: true
argument-hint: [paste the form or email text, or give the path to a PDF or photo]
---

# School forms

Turn a form or a school email into a list of what is needed, by when, with a draft already filled in.

## Input

$ARGUMENTS: the form or email text. If empty, ask for it in one question and stop. If the user has a PDF or a photo, they can paste the text or give the file path; Claude Code can read PDFs and images from a path.

## Process

1. Read `family/profile.md`: household, the School and forms section, emergency contact, allergies (forms often ask).
2. Read the pasted text once and pull out:
   - Every field or question the form asks, in order.
   - Every date: due dates, event dates, payment deadlines, RSVP dates. Note the weekday.
   - Every action: sign, pay, return, upload, bring something.
   - Money: amounts and how to pay.
3. Build the field list: Field | What they want | From the profile? (the value, or NEEDS)
4. Fill a draft: the form's fields with values from the profile. Anything the profile does not have gets `[NEEDS: what it is]` in its place. Never guess a date of birth, a doctor, an insurance number, a medication, or a signature.
5. Deadlines: each one with the weekday and how many days away it is from today.
6. Ask at most two questions, and only if the form cannot be understood without them.
7. Save to `plans/YYYY-MM-DD-school-form-<short-name>.md` when the user asks.

## Output format

- One line: what the form is and which child it is for.
- "Deadlines": soonest first.
- "Fields": the table.
- "Draft": the filled form as plain text the user can copy, with `[NEEDS: ...]` markers where the profile had nothing.
- "Before you send": the NEEDS items in one list, plus anything to attach, sign, or pay.

## Rules

- Never invent personal data. A `[NEEDS]` marker beats a guess every time.
- If the form asks for a Social Security number, an insurance ID, or medical details, list the field, leave it blank, and remind the user in one line that pasted text goes to the model.
- Do not summarize away fields. Every field the form asks for appears in the list, even the minor ones.
- Plain English. No lecture.
