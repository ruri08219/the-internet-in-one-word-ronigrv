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


def check_word(word):
    """Return an error message if word is invalid, else None."""
    if not word or word != word.strip():
        return "entry must not be empty or padded with whitespace"
    if len(word) > MAX_CHARS:
        return "entry must be at most 30 characters"
    if any(ch.isspace() for ch in word):
        return "entry must be a single word"
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        return "entry must not contain control characters"
    return None


def main():
    word = ENTRY
    error = check_word(word)
    if error is not None:
        print(error, file=sys.stderr)
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
