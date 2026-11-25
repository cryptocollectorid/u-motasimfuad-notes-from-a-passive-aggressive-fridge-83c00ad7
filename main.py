#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one dry, petty note from a smart fridge to its owner to
/output/entry.txt. Gate (competition.yaml): UTF-8 text of 1-200
characters, not only whitespace, a single non-blank line.
"""

import os
import sys

ENTRY = "I moved your yogurt behind the oat milk. You will find it when you stop slamming my door at 2 a.m."

MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text: str) -> None:
    """Fail loudly if the entry breaks the sealed gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = text.splitlines()
    if len(lines) != 1 or not lines[0].strip():
        raise ValueError("entry must be exactly one non-blank line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")


def write_entry(text: str, out_path: str = "/output/entry.txt") -> None:
    validate_entry(text)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Round-trip verification: the file must hold exactly the entry.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("round-trip check failed: file content differs from entry")
    validate_entry(written)
    print(f"Wrote {len(text)} characters to {out_path}")


def main() -> int:
    write_entry(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
