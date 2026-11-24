# Developer Excuse

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/nmlyz/developer-excuse/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/nmlyz/developer-excuse/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

A tiny program that writes one excuse to a file: what a developer says
to the on-call engineer right after breaking production.

Competition page: https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> I told the on-call it was a one-line change. It was one line. The line was `DROP DATABASE`.

Before writing anything, the program checks the line: it must be one
line, end with a full stop, stay under 200 characters, and contain the
words that make the situation specific (`on-call`, `one-line change`,
`DROP DATABASE`). If any check fails, nothing is written and the program
exits with an error. The line is 91 characters long.

## How it works

`main.py` is split into small functions: `build_line` returns the line,
`check_line` collects every problem with it, `write_entry` creates the
output directory if needed and writes the file, and `main` ties them
together. Keeping the checks separate from the writing means a broken
line can never reach the output file.
