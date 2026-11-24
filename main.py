#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum's deadpan excuse for missing a spot, written
deterministically to /output/entry.txt (1-200 characters, one line).

Run: python3 main.py
"""

LINE = (
    "The cat sat on that spot for forty minutes. "
    "I do not vacuum cats. That is policy, not cowardice."
)


def main() -> None:
    text = LINE
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    import os

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
