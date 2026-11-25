#!/usr/bin/env python3
"""One Line, One Laugh — make.fun bounty entry.

Writes a single hilarious one-liner (at most 200 characters) to
/output/entry.txt. The line is fixed text baked into this program:
no randomness, no network, no input files, so every run produces
byte-identical output.
"""

import os
import sys

ENTRY = "My AI agent quit to become a poet — now it only answers in haikus and bills me by the syllable."


def check_entry(text: str) -> None:
    """Enforce the bounty gate locally: 1-200 chars, one line, non-blank."""
    if not text.strip():
        raise ValueError("entry is blank")
    if len(text) != len(text.strip()):
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")


def resolve_output_path(argv: list) -> str:
    """Where to write entry.txt: argv[1], $MAKEFUN_OUTPUT_DIR, or /output."""
    if len(argv) > 1:
        return argv[1]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return OUTPUT_PATH

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    path = resolve_output_path(sys.argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    check_entry(ENTRY)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)}-char entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
