#!/usr/bin/env python3
"""One Line, One Laugh — writes a single original funny line to /output/entry.txt.

Pure standard library. The joke is written by the program itself: one line,
at most 140 characters, no setup paragraph, no explanation, no meme.
"""
import os

JOKE = "My smart fridge keeps suggesting salads, so I unplugged it \u2014 I don't need judgment from something that holds my ice cream."

def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 140, f"joke is {len(text)} chars, must be 1-140"
    assert text == text.strip() and "\n" not in text
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
