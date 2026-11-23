"""Six Words, One Story — the safety net fails.

Arc: a trader sets a stop-loss (the plan) -> the stop itself stops
(the failure) -> the losses keep going (the ruin, left unsaid).
The reader supplies the missing verb and the ending.
"""

STORY = "My stop-loss stopped. My losses didn't."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
