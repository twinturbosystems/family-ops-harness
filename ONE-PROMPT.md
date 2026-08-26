# Set up the Family Ops Kit in your assistant

Downloading the folder is still the first step. This page is not a way to skip it. It is how you switch the downloaded folder on inside the assistant you already use.

Direct download: https://github.com/twinturbosystems/family-ops-harness/archive/refs/heads/main.zip

Unzip it. You get a folder called `family-ops-harness-main`.

Choose your assistant before typing a command. If you have Claude Code or the Codex CLI on your computer, open a terminal in that folder, start the assistant, and type `Start the kit`. The folder ships with a fictional example family already filled in, so you can see a finished plan before you put your own household in `family/profile.md`. If you use a browser chat, read the privacy warning in section 3 before attaching household files.

The prompts themselves now live in the [browser-prompts](browser-prompts/) folder, in plain view rather than inside the hidden `.claude` directory. This page points at them so there is one copy of each rather than two.

## 1. Claude Code

No prompt at all. Claude Code reads `CLAUDE.md` and the `.claude/skills` folder by itself. Claude Code requires an eligible account; use Anthropic's [official native installation guide](https://code.claude.com/docs/en/installation) for current setup and sign-in steps. Open a terminal in the folder, type `claude`, and review the one-time trust prompt. Confirm that it shows the kit folder you intended to open before you trust it. Then type `Start the kit`.

If it answers like a general chatbot instead of a household planner, the nudge prompt is in [browser-prompts/claude-code.md](browser-prompts/claude-code.md).

## 2. Codex CLI

Codex reads `AGENTS.md` automatically when you run it inside this folder. Use the [official Codex CLI guide](https://learn.chatgpt.com/docs/codex/cli) for installation, paste the prompt in [browser-prompts/codex-cli.md](browser-prompts/codex-cli.md) once at the start of the session, then type `Start the kit`.

## 3. Limited browser mode

This is ChatGPT, Claude in a browser, or any other chat window on a website. It cannot operate the folder you downloaded, it cannot save your progress locally, and it cannot build final packages of files, so no plan is written into `plans/`. It can give you advice, analysis, drafts, and copy-ready checklists, including a meal plan you copy out yourself. Nothing typed into a browser chat runs this kit.

Before attaching anything, remember that every file and message is sent to that assistant's provider. Use the fictional example first, or remove details you do not want to send. Do not attach Social Security numbers, account numbers, insurance IDs, or other secrets.

The visible instruction bundle, file list, and prompt are in [browser-prompts/limited-browser-mode.md](browser-prompts/limited-browser-mode.md). You do not need to reveal or attach anything from the hidden `.claude` folder.

## 4. Do not have Claude Code or Codex yet?

An assistant you already have open can walk you through the install, one step at a time. The two install prompts are in [browser-prompts/install-the-assistant.md](browser-prompts/install-the-assistant.md).

## If something goes wrong

`docs/STUCK.md` has one next action for each of the common stumbles, including the command not being found and the assistant not being able to see the folder.
