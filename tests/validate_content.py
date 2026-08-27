from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_required_copy_and_order() -> None:
    readme = read("README.md")
    for phrase in (
        "Start in 60 seconds",
        "How it works",
        "What is this?",
        "Set it up in your assistant",
    ):
        check(phrase in readme, f"README is missing required phrase: {phrase}")

    setup = readme.index("## Set it up in your assistant")
    claude_choice = readme.index("Claude Code on your computer", setup)
    codex_choice = readme.index("Codex CLI on your computer", setup)
    browser_choice = readme.index("Limited browser mode means", setup)
    claude_command = readme.index("Type `claude`", setup)
    check(
        setup < claude_choice < codex_choice < browser_choice < claude_command,
        "The three-way assistant choice must appear before the Claude-specific command",
    )
    check(
        "https://code.claude.com/docs/en/installation" in readme,
        "README must link the official Claude Code native installation guide",
    )
    check(
        "https://learn.chatgpt.com/docs/codex/cli" in readme,
        "README must link the official Codex CLI guide",
    )


def test_browser_bundle_and_privacy_order() -> None:
    guide = read("browser-prompts/limited-browser-mode.md")
    bundle = read("browser-prompts/family-ops-browser-bundle.md")
    check(".claude/skills/" not in guide, "Browser guide must not require hidden skill files")
    check(
        "browser-prompts/family-ops-browser-bundle.md" in guide,
        "Browser guide must attach the visible instruction bundle",
    )
    warning = guide.index("Every attached file and message leaves this folder")
    attachments = guide.index("Attach these three visible files")
    check(warning < attachments, "Provider warning must appear before household attachments")
    for job in (
        "Start the kit",
        "Meal plan",
        "Grocery list",
        "Week plan",
        "Budget check",
        "Chores",
        "School forms",
    ):
        check(job in bundle, f"Browser bundle is missing job: {job}")


def test_allergy_contract() -> None:
    meal = read(".claude/skills/meal-plan/SKILL.md")
    grocery = read(".claude/skills/grocery-list/SKILL.md")
    bundle = read("browser-prompts/family-ops-browser-bundle.md")
    combined = "\n".join((meal, grocery, bundle, read("examples/sample-meal-plan.md")))
    check("Allergen check: no" not in combined, "Categorical allergen check wording remains")
    for text, name in ((meal, "meal-plan"), (grocery, "grocery-list"), (bundle, "browser bundle")):
        check("This is not a guarantee" in text, f"{name} is missing the no-guarantee warning")
        check("cross-contact" in text, f"{name} is missing cross-contact guidance")
        check("full package label every time" in text, f"{name} is missing label guidance")
    check(
        "no longer includes coconut on its Tree Nut List" in meal,
        "Meal-plan skill must reflect FDA's current coconut guidance",
    )
    check("FDA lists coconut" not in meal, "Outdated coconut wording remains")
    check("authoritative" in meal and "authoritative" in grocery, "Run constraints must be authoritative")


def test_permission_scopes() -> None:
    settings = json.loads(read(".claude/settings.json"))
    check(
        settings["permissions"]["allow"]
        == [
            "Read(/family/profile.md)",
            "Read(/family/pantry.md)",
            "Read(/plans/**)",
            "Read(/examples/sample-meal-plan.md)",
            "Edit(/plans/**)",
        ],
        "Project allow rules must stay limited to household inputs, the sample, and plans",
    )
    for skill in sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md")):
        skill_text = skill.read_text(encoding="utf-8")
        check("user-invocable: true" in skill_text, f"{skill} must remain visible in the command menu")
        check("argument-hint:" in skill_text, f"{skill} is missing its beginner-facing autocomplete hint")
        for line in skill_text.splitlines():
            if line.startswith("allowed-tools:"):
                rules = line.partition(":")[2].split()
                check(rules, f"{skill} has an empty allowed-tools field")
                check(
                    all("(" in rule and rule.endswith(")") for rule in rules),
                    f"{skill} contains an unscoped tool preapproval",
                )


def test_reader_copy_and_links() -> None:
    markdown_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        check("\u2014" not in text, f"Em dash found in {path.relative_to(ROOT)}")
        check("!" not in text, f"Exclamation mark found in {path.relative_to(ROOT)}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if re.match(r"^(?:https?://|mailto:|#)", target):
                continue
            local_target = target.split("#", 1)[0]
            if not local_target:
                continue
            resolved = (path.parent / local_target).resolve()
            check(resolved.exists(), f"Broken local link in {path.relative_to(ROOT)}: {target}")

    reader_files = [
        "README.md",
        "ONE-PROMPT.md",
        "docs/STUCK.md",
        "browser-prompts/README.md",
        "browser-prompts/claude-code.md",
        "browser-prompts/codex-cli.md",
        "browser-prompts/install-the-assistant.md",
        "browser-prompts/limited-browser-mode.md",
    ]
    reader_text = "\n".join(read(path) for path in reader_files)
    check(not re.search(r"\b(?:say|choose) yes\b", reader_text, re.IGNORECASE), "Blanket yes advice remains")
    check(
        "Developers call a folder like this a harness" not in reader_text,
        "Reader-facing harness explanation remains",
    )
    check("docs.anthropic.com/en/docs/claude-code" not in reader_text, "Old Claude Code URL remains")


def main() -> None:
    tests = [
        test_required_copy_and_order,
        test_browser_bundle_and_privacy_order,
        test_allergy_contract,
        test_permission_scopes,
        test_reader_copy_and_links,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS {len(tests)} focused content checks")


if __name__ == "__main__":
    main()
