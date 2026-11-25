#!/usr/bin/env python3
"""One-Line Office Jokes entry.

Writes a single one-line office joke to /output/entry.txt.
Deterministic: the same joke every run, no randomness, no network.
"""

import os

JOKE = (
    "I replied-all 'Thanks!' to the whole company, "
    "and now the whole company is replying-all 'Thanks!' to me."
)


def main() -> None:
    input_dir = os.environ.get("MAKEFUN_INPUT_DIR", "/input")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _ = input_dir  # This entry needs no input files.
    # Gate check, mirroring the brief: 1-199 chars, one line, not blank.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be a single non-blank line"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
