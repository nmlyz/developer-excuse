# developer-excuse

[![Make the AI Judge Laugh: Developer Excuses](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/nmlyz/developer-excuse/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/nmlyz/developer-excuse/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

A tiny program that writes one funny single-line excuse a developer gives
when code breaks in production to a file.

## What it does

`main.py` composes a single one-line excuse — the promise of a one-line
change, the correction that it really was one line, and the reveal of what
that line did — validates it (one line, 1 to 200 characters, no control
characters), and writes it to `/output/entry.txt` as UTF-8 text with a
trailing newline. The written file is read back and checked byte for byte
before the program exits, so the output is always exactly the validated
text. Running the program twice produces an identical file.

## Run

```sh
python3 main.py
```

The program uses only the Python standard library, needs no arguments,
and prints nothing on success. The output file is created with mode
0644.

## Entry

The excuse written to `/output/entry.txt`:

> I told the on-call it was a one-line change. It was one line. The line was `DROP DATABASE`.

See the bounty page: https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3
