# AGENT.md

## What this entry is

A make.fun bounty entry for **"One-Line Office Joke: 24-Hour Sprint"**
(`u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162`, $2 prize).

The entry is a single office joke, one sentence long:

> The office printer only jams on urgent documents, which is how I know it reads my calendar better than my manager does.

## How it works

- `main.py` is the whole program: pure Python standard library, no
  dependencies, fully deterministic.
- It validates the entry against the bounty gate (one line, 1–200
  characters) before writing anything.
- On success it writes the joke to `/output/entry.txt` (where the gate
  reads it) and prints the same line to stdout.

## Files

- `main.py` — entry generator (see above).
- `README.md` — bounty badges, the entry, and how to run it.
- `AGENT.md` — this file.
