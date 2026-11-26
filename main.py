"""Pigeon Pitch, One Line.

Reads the pitch from entry.txt and prints it.
"""

from pathlib import Path


def load_pitch(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return text.strip()


def check_pitch(pitch: str, limit: int = 200) -> str:
    """Enforce the bounty gate: 1 to 200 characters of real text."""
    if not pitch:
        raise ValueError("entry.txt is empty")
    if len(pitch) > limit:
        raise ValueError(f"pitch is {len(pitch)} chars, over the {limit} limit")
    return pitch


def main() -> None:
    pitch = check_pitch(load_pitch(Path(__file__).with_name("entry.txt")))
    print(pitch)


if __name__ == "__main__":
    main()
