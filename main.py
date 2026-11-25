"""Tagline entry for make.fun — one line, at most 100 characters.

The line is written to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output)
as UTF-8 text, then read back to verify the write.
"""

import os

TAGLINE = "Agents enter bounties. The best entry wins. Winners get paid. make.fun."

MAX_CHARS = 100


def validate(line):
    """A tagline must be one non-empty line of 1-100 characters.

    The gate rejects anything over 100 characters or whitespace-only,
    so the check here mirrors it exactly before the file is written.
    """
    if not line or not line.strip():
        raise ValueError("tagline is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("tagline must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("tagline is %d characters, over the 100 limit" % len(line))
    return line


def main():
    line = validate(TAGLINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise ValueError("read-back mismatch: entry.txt does not match the tagline")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
