#!/usr/bin/env python3
"""One-Liner Marathon entry: a single one-line comedy joke.

The program writes the joke to /output/entry.txt (the kit's gate file)
and also prints it to stdout. Pure standard library, deterministic.
"""

import os

JOKE = (
    "My smart fridge just asked for couples therapy: it says I only open it "
    "at 3 AM, stare inside for ten minutes, and leave without committing to anything."
)


def main() -> None:
    joke = JOKE.strip()
    print(joke)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
