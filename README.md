# Notes From a Passive-Aggressive Fridge

[![Rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/cryptocollectorid/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/cryptocollectorid/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

Entry for the [make.fun bounty](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7): one funny passive-aggressive note a smart fridge leaves for its owner — a single line, dry, petty and specific.

## The note

> I moved your yogurt behind the oat milk. You will find it when you stop slamming my door at 2 a.m.

## Run

```sh
python3 main.py   # writes the note to /output/entry.txt (98 characters, one line)
```

`main.py` validates the entry against the sealed gate (UTF-8, 1–200 characters, exactly one non-blank line, no control characters) and verifies the written file by reading it back.
