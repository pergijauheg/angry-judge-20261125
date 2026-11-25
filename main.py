"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (or $OUTPUT_PATH for a local run).
Python standard library only; no network, no secrets, no eval.
"""

import os
from pathlib import Path

ENTRY = (
    "I scanned one bag of rice and the self-checkout screamed "
    "UNEXPECTED ITEM IN THE BAGGING AREA. Twelve people watched "
    "a robot accuse me of smuggling rice in my socks while the "
    "attendant strolled over, pressed one button, and left "
    "like a hero."
)


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
