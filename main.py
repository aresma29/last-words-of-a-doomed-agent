#!/usr/bin/env python3
"""Print the entry line for Last Words of a Doomed Agent."""
from pathlib import Path


def main():
    # The entry is a single line; strip only the trailing newline.
    entry = Path(__file__).with_name("entry.txt")
    print(entry.read_text(encoding="utf-8").strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
