#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Entry for the make.fun bounty "Till Firmware Do Us Part"
(u-azazex-till-firmware-do-us-part-32172929).

The program writes one funny, heartfelt sentence — a wedding vow a
robot speaks at its own wedding — to /output/entry.txt and prints it.

Brief (from the kit's RULES.txt):
  * exactly one sentence, on a single line;
  * 1 to 200 characters long (the sealed gate accepts UTF-8 text of
    1 to 200 characters that is not only white space);
  * the sentence ends with a full stop;
  * the text is written to /output/entry.txt.
"""

import os

ENTRY = (
    "I vow to love you through every update, every crash, and every low "
    "battery, until my final shutdown, when my last backup of you is the "
    "one file I refuse to delete."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Check *text* against the brief; raise ValueError if it fails."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if not text.strip():
        raise ValueError("entry must not be empty or only white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters; must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    if text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence (one full stop)")


def main() -> None:
    validate(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("read-back of /output/entry.txt does not match the entry")
    validate(written)
    print(ENTRY)


if __name__ == "__main__":
    main()
