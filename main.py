#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line comedy joke.

The program writes the joke to <output dir>/entry.txt (default /output,
or $MAKEFUN_OUTPUT_DIR when set) and prints it to stdout. It self-checks
the gate before writing: one line, 1-280 chars, not only whitespace.
Pure standard library, deterministic.
"""

import os
import sys

JOKE = (
    "My smart fridge just asked for couples therapy: it says I only open it "
    "at 3 AM, stare inside for ten minutes, and leave without committing to anything."
)


def main() -> None:
    joke = JOKE.strip()
    if not joke or len(joke) > 280 or "\n" in joke:
        print("entry fails gate: must be one line, 1-280 chars", file=sys.stderr)
        sys.exit(1)
    print(joke)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    with open(path, encoding="utf-8") as f:
        assert f.read().strip() == joke, "entry.txt does not match the joke"


if __name__ == "__main__":
    main()
