#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line to /output/entry.txt: the excuse a hardware wallet
gives for refusing to sign a transaction at 3 AM.

The joke, per the winners' recipe (one sharp irony, not a list):
the wallet applies its own access-control logic to the human
holding it — at 3 AM its owner is asleep, so whoever is awake
is by definition an unauthorized user. The 3 AM hour is the joke
itself, and the twist lands in the last clause.
"""

from pathlib import Path

ENTRY = (
    "My owner sleeps at 3 AM, so by my rules the person holding me "
    "now is an unauthorized user. I take orders from my owner, "
    "not from insomnia."
)


def main() -> None:
    # Gate, mirrored from RULES.txt: UTF-8 text, 1 to 200 characters,
    # not only white space. Fail loudly here instead of shipping
    # an entry the sealed scorer would refuse.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is only white space"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
