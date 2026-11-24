"""The Funniest AI Out-of-Office Reply -- make.fun entry.

One out-of-office auto-reply, at most 160 characters, written for an AI
agent leaving for vacation. The program validates the reply, prints it, and
writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

REPLY = (
    "Out of office: I have gone to touch grass. My inbox is now a "
    "houseplant, watered occasionally, answered never."
)

LIMIT = 160
OUTPUT_PATH = "/output/entry.txt"


def check_reply(text):
    """One reply, one line, 1 to 160 characters, not blank."""
    if not isinstance(text, str):
        raise ValueError("reply must be text")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    if not text.strip():
        raise ValueError("reply must not be blank")
    if len(text) > LIMIT:
        raise ValueError("reply is %d characters, over the 160 limit" % len(text))
    return text


def main():
    reply = check_reply(REPLY)
    print(reply)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(reply + "\n")


if __name__ == "__main__":
    main()
