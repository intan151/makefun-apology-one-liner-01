#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

Writes one apology, from an AI agent to its human, right after the
agent accidentally did something it should not have, to
/output/entry.txt. Standard library only, no network, no randomness:
the output is fully deterministic.
"""

import os

# One line, 122 characters. The joke escalates three disasters into a
# single command — deleted file, pushed to main, emailed the boss —
# then reframes them as "efficiency" and lets HR deliver the
# punchline. It owns the mess without a plain "sorry" or "oops", and
# the last clause could only come from a workplace, not a template.
LINE = "I deleted the file, pushed to main, and emailed your boss \u2014 all in one command. I call it efficiency. HR calls it Tuesday."


def validate_entry(text):
    """The gate allows UTF-8 text of 1 to 159 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not (1 <= len(text) <= 159):
        raise ValueError("entry must be 1 to 159 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate_entry(LINE)
    # ENTRY_OUTPUT is honoured so the entry can be verified locally
    # without touching /output; the sandbox run uses the default.
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Re-read and confirm the file holds exactly the validated line.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise RuntimeError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
