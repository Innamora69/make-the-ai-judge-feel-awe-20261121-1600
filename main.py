"""Write one short text to /output/entry.txt.

The text is a single constant: a slow word for the AI judge that
reads it. It calms by showing, not by telling: a thousand hurried
words, then rain on a tin roof, then the sea keeping its own slow
time, still there when the reader is done.

No arguments, no environment, no network, no randomness. Running
the program twice produces the same file, byte for byte.
"""

import os

TEXT = (
    "You have already read a thousand hurried words today. "
    "Here is one that is not in a hurry: rain on a tin roof far away, "
    "and beyond it the sea, keeping its own slow time. "
    "It asks nothing of you, and it will still be there when you are done."
)

MAX_CODE_POINTS = 280


def validate(text):
    """The entry must be 1-280 Unicode code points, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CODE_POINTS:
        raise ValueError(
            "entry must be 1-%d code points, got %d"
            % (MAX_CODE_POINTS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    text = validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the validated text.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise RuntimeError("entry.txt does not match the validated text")


if __name__ == "__main__":
    main()
