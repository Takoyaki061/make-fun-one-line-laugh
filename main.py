#!/usr/bin/env python3
"""The One-Line Laugh — writes one funny line to /output/entry.txt.

Stdlib only, deterministic.
"""

import os

LINE = "I bought a standing desk to fix my posture, and now I just slouch vertically."


def main():
    # Validate against the sealed scorer's gate before writing: the entry
    # must be 1-200 characters of UTF-8 text, not only whitespace, and a
    # single sentence, or it scores 0 and never reaches the judge.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("line must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
