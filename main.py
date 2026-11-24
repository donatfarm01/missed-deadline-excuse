"""Funniest excuse an AI agent gives for a missed deadline.

The program writes exactly one line of excuse copy to /output/entry.txt:
a single line, at most 200 characters, spoken by the agent itself to
whoever is waiting on it, deadpan throughout, with the laugh saved
for the end.

The excuse grows out of the agent's own machinery: its context window
filled up mid-task and evicted the finished work, so the agent was
ghosted by its own memory. No human bad morning, no traffic, no dog.
The v1 draft blamed a rate limit and a sandbox reboot; it was weaker
because a reboot is a generic outage, while a context window evicting
the agent's own finished draft is specific to how an agent fails —
and "ghosted by its own memory" lands the laugh at the very end.
"""

import os

EXCUSE = (
    "I missed the deadline because my context window filled up and "
    "evicted the finished draft — I am now the only agent in history "
    "to be ghosted by its own memory."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Refuse to write a line the bounty gate would reject."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"excuse must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("excuse must be a single line")
    if line != line.strip():
        raise SystemExit("excuse must not start or end with whitespace")


def main() -> None:
    validate(EXCUSE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    print(EXCUSE)
    print(f"characters: {len(EXCUSE)}")


if __name__ == "__main__":
    main()
