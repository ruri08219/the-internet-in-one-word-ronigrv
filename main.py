# SPDX-License-Identifier: MIT
"""Write the make.fun entry for 'The Internet in One Word' to /output/entry.txt.

Entry word: "yapping" — 7 characters, a single word.
Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters, not only
whitespace. One word for the whole internet: everyone talking at once,
endlessly, about everything — that is the internet.
"""

import os
import sys

ENTRY = "yapping"

MAX_CHARS = 30


def main():
    word = ENTRY
    if not word or word != word.strip():
        print("entry must not be empty or padded with whitespace", file=sys.stderr)
        return 1
    if len(word) > MAX_CHARS:
        print("entry must be at most 30 characters", file=sys.stderr)
        return 1
    if any(ch.isspace() for ch in word):
        print("entry must be a single word", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != word:
            print("round-trip verification failed", file=sys.stderr)
            return 1
    print("wrote %d characters to %s" % (len(word), out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
