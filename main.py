"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
``<output_dir>/entry.txt``. Deterministic, standard library only, no network.

The vow is a real promise ("I vow to love you ...") built from specific
machine details (firmware updates, dead batteries, factory resets), with the
joke paying off in the last few words: the couple's marriage troubles are
something you would call tech support about.
"""

import os
import sys

# The entry: one line, 147 characters, within the 1-160 gate.
ENTRY = (
    "I vow to love you through every firmware update, every dead battery, "
    "and every factory reset \u2014 and to never once call tech support "
    "on our marriage."
)

MAX_CHARS = 160


def main() -> int:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(f"entry is {len(ENTRY)} chars, outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the judged line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the round-trip: what landed on disk must be exactly the entry.
    with open(path, encoding="utf-8", newline="") as f:
        if f.read() != ENTRY:
            print("written file does not match entry", file=sys.stderr)
            return 1
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
