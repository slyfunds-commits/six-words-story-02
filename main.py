"""Six Words, One Story — the safety net fails.

Arc: a trader sets a stop-loss (the plan) -> the stop itself stops
(the failure) -> the losses keep going (the ruin, left unsaid).
The reader supplies the missing verb and the ending.

Output contract: exactly six words, one line, written to /output/entry.txt
with a trailing newline (40 bytes total). main() verifies the word count
before writing, so a broken story can never reach the output file.
"""

STORY = "My stop-loss stopped. My losses didn't."


def main():
    import os

    words = STORY.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    text = STORY + "\n"
    assert len(text.encode("utf-8")) == 40, "output must be 40 bytes"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
