#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line keeps the fortune voice -- small, oracular, slightly formal --
and lets the punchline break it: the balance comes back doubled, but
only as a lesson, never as money.
"""

import os
import sys

ENTRY = "The cookie says: your balance will return, doubled \u2014 as a lesson, not as money."

MAX_WORDS = 20
MAX_CHARS = 160


def validate(text: str) -> None:
    """Enforce the sealed gate: 1-160 UTF-8 chars, at most 20 words."""
    if not text.strip():
        raise SystemExit("entry is blank")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 160 cap")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise SystemExit(f"entry is {len(words)} words, over the 20 cap")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read it back: the grader scores exactly what lands on disk, so a
    # write that did not land byte-exact must fail here, not later.
    with open(path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise SystemExit("entry.txt read-back does not match ENTRY")
    return 0


if __name__ == "__main__":
    sys.exit(main())
