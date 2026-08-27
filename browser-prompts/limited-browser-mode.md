# Limited browser mode

This is ChatGPT, Claude in a browser, or any other chat window on a website.

## What it cannot do

A chat window on a website cannot reach your computer. That is a limit of the browser, not a setting anyone can change. In limited browser mode this kit cannot:

- operate the folder you downloaded, so it cannot read your profile or your pantry unless you attach those files by hand
- save your progress locally, so no plan is written into `plans/` and nothing carries over into the next chat
- build a finished package of files for you

What it can do is real: advice, analysis, drafts, and copy-ready checklists, including a meal plan and a grocery list you copy out yourself. Nothing typed into a browser chat runs this kit. To actually run it, use Claude Code or the Codex CLI on a computer.

## How to set it up

1. Unzip the downloaded folder.
2. Start a new chat.
3. Before attaching anything, decide what you are willing to send to the assistant's provider. Every attached file and message leaves this folder as part of the chat. The safest first run uses the fictional example files that ship with the kit. For your own household, remove anything the plan does not need. Do not attach Social Security numbers, account numbers, insurance IDs, medical record numbers, or other secrets.
4. Attach these three visible files from the folder:
   - `browser-prompts/family-ops-browser-bundle.md`
   - `family/profile.md`, either the fictional example or the copy you chose to share
   - `family/pantry.md`, either the fictional example or the copy you chose to share

   For `grocery-list`, also attach the meal plan you want turned into a list. You do not need to show hidden files or attach anything from `.claude`.
5. Paste this:

```
Read family-ops-browser-bundle.md first and follow it for this conversation. Use the attached family profile and pantry as the household facts. You are in limited browser mode, so do not claim to read or change any file that I did not attach, and do not claim to save anything on my computer. Give me text I can copy. Start by telling me in one line which jobs the bundle provides, then wait for me.
```

## Two plain notes

Browser chats may not keep attached files available in a later conversation, so attach them again when needed.

For allergies, treat the output as a screen of named ingredients, not a guarantee. Check the full package label every time, including the ingredients, Contains statement, and any voluntary may contain or facility warning. If cross-contact is a concern and the label is unclear, leave it out or contact the manufacturer.
