#!/usr/bin/env python3
"""Entry generator for the "One-Line Office Joke" 24-hour sprint.

What this program does: it writes one office joke to the file the
bounty gate reads, ``/output/entry.txt``, and echoes the same line
to standard output so a human can see what was submitted.

The joke plays on a shared office frustration: the printer never
misfires on a random memo, only on the document you need right now.
The punchline lands by suggesting the machine understands your
schedule better than your boss does -- setup and payoff in a single
sentence, no extra words.

The program is deterministic and dependency-free (standard library
only). It re-validates the entry before writing so the output can
never silently drift outside the bounty gate: a single line of
between 1 and 200 characters.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
GATE_MIN = 1
GATE_MAX = 200

ENTRY = "The office printer only jams on urgent documents, which is how I know it reads my calendar better than my manager does."


def entry_is_valid(text):
    """Return True when *text* fits the gate: one line, 1-200 chars."""
    if not isinstance(text, str):
        return False
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        return False
    if text != text.strip():
        return False
    # A single line means no embedded line breaks at all.
    return "\n" not in text and "\r" not in text


def write_entry(text, target):
    """Write *text* to *target*, creating the folder if it is missing."""
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def run():
    if not entry_is_valid(ENTRY):
        sys.stderr.write(
            "entry fails the gate: expected one line of "
            f"{GATE_MIN}-{GATE_MAX} chars, got {len(ENTRY)} chars\n"
        )
        return 1
    write_entry(ENTRY, OUTPUT_PATH)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
