#!/usr/bin/env python3
"""u-suroso-69-one-liner-laugh-lab-6ccf3aae — "One-Liner Laugh Lab".

The program writes one short text to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. The joke is deadpan and specific — the sock
was lying face-down dressed as dust and never once objected, so the vacuum
filed it under lunch. The twist lands on the last words: a bureaucratic
filing, not an apology.

Deterministic: the same bytes on every run. Standard library only. No
network, no input, no model calls.
"""

import os

TEXT = (
    "It was lying face-down, dressed as dust, and never once said "
    "'not food' \u2014 so I filed it under lunch."
)

# The gate allows 1-200 Unicode code points: refuse to write anything else.
# The line is 100 characters, well inside the gate, with no trailing newline:
# the scorer counts the file's characters, and one line means one line.
LENGTH = len(TEXT)
if LENGTH < 1 or LENGTH > 200:
    raise SystemExit(f"entry text is {LENGTH} characters, outside 1-200")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
