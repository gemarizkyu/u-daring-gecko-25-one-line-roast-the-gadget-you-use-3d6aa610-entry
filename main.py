#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original line (at most 200 characters) roasting a
gadget/app used every day to /output/entry.txt.

No network, no model calls, no randomness: the same line every run, so
the replay matches the live run exactly.
"""

import os

LINE = "My phone's autocorrect never fixes a typo — it just promotes it into a formal apology I have to send my boss."
# The joke turns the phone's most "helpful" feature against itself: instead
# of correcting the typo, autocorrect upgrades it into something worse —
# a formal apology to the boss. One concrete daily detail, one punchline.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
