#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review (160 characters or fewer) of an
everyday essential to /output/entry.txt. Deterministic: the same review,
byte for byte, on every run. Standard library only, no network.

The review targets the sun. The grievance is the sharpest true one every
reader recognises: it rises every morning without fail, weekends included,
and never apologises. The sting lands in the last few words, as a bad
product would be summed up: no snooze button, no days off, no refund.
"""

import os

REVIEW = (
    "The sun rises every morning without fail, including weekends, "
    "and has never once apologised. "
    "No snooze button, no days off, no refund."
)


def main() -> None:
    text = REVIEW
    assert 1 <= len(text) <= 160, f"review is {len(text)} characters"
    assert text.strip() == text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
