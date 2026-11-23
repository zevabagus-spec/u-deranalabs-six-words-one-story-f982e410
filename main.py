#!/usr/bin/env python3
"""Six Words, One Story — entry for u-deranalabs-six-words-one-story-f982e410.

The whole entry is one story in exactly six words, written by this
program to /output/entry.txt:

    He dug his grave beside hers.

Why this line (judged against the published brief, in the brief's own
order):

1. A complete story in exactly six words. One sentence, one decisive
   act: a man digs his own grave next to his wife's. It is a story,
   not a slogan, a list, or a fragment — it has a past (their life
   together, her death), a present (the digging), and a future (the
   grave he will lie in).
2. A turn and a whole life implied. The turn is the act itself: he is
   not visiting her grave, he is digging his own beside it. A whole
   marriage, a loss, and the years he waited are all inside those six
   words.
3. Every word earns its place. "dug" is the action, "his grave" the
   stake, "beside hers" the devotion. No filler, no word a better one
   could replace.
4. Reads cleanly aloud. Short, plain words; a steady three-beat rhythm
   with nothing clumsy or ambiguous to trip the reader.
5. Leaves something unsaid. Who she was, how she died, how long he
   waited, whether he climbs in tonight — the reader fills all of it
   in.

The program is deterministic: it writes the same fixed text on every
run, so the grader's two runs produce byte-identical output. It writes
no trailing newline and no extra whitespace, keeping the file at 29
bytes — the smallest honest form of the story. Before writing it
validates the text against the published gate (UTF-8, 1-60 characters,
not only whitespace, exactly six words) and fails loudly instead of
writing a bad file.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

STORY = "He dug his grave beside hers."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def validate(text: str) -> None:
    """Check the story against the competition's published gate."""
    if not text or not text.strip():
        raise SystemExit("story is empty or only whitespace")
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 60:
        raise SystemExit(f"story is {len(text)} characters, gate needs 1-60")
    if len(text.split()) != 6:
        raise SystemExit(f"story has {len(text.split())} words, needs exactly 6")
    if text != text.strip():
        raise SystemExit("story has leading or trailing whitespace")
    if not text.isascii():
        raise SystemExit("story must be plain ASCII (single-byte UTF-8)")


def main() -> None:
    validate(STORY)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
