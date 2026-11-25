"""Monday, Reviewed in One Line.

Writes the funniest one-line review of my own Monday to
/output/entry.txt. Single line, under 200 characters, no title,
no explanation -- just the review.
"""

import os

ENTRY = (
    "One star: Monday's 9am meeting should've been an email, "
    "my inbox doubled by lunch, and my coffee went cold before "
    "my first sip -- would not Monday again."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
