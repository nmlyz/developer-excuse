#!/usr/bin/env python3
"""developer-excuse: write one single-line developer excuse to a file.

Running this program writes the excuse to /output/entry.txt as UTF-8
text: one line, terminated by a newline. It prints nothing on success.
Only the Python standard library is used, and the output is identical
on every run.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The excuse in three beats: the promise, the correction, the reveal.
_BEATS = (
    "I told the on-call it was a one-line change.",
    "It was one line.",
    "The line was `DROP DATABASE`.",
)

ENTRY = " ".join(_BEATS)


def build_entry():
    """Return the excuse as a single line of text."""
    return ENTRY


def validate_entry(text):
    """Check the excuse before it is written.

    The entry must be a single line of 1 to 200 characters, with no
    control characters and no leading or trailing whitespace.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters long")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    return text


def write_entry(path=OUTPUT_PATH):
    """Write the excuse to path, creating the output directory if needed.

    The file itself is set to mode 0644; the output directory is left
    untouched.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = validate_entry(build_entry())
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    os.chmod(path, 0o644)
    # Read the file back and confirm it holds exactly the validated text.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != (text + "\n").encode("utf-8"):
        raise IOError("written file does not match the entry")
    return path


def main():
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
