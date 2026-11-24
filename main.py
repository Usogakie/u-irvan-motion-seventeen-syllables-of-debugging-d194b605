"""Write one debugging haiku (5-7-5) to entry.txt.

Reads nothing, needs no network, and uses no clock: the same
seventeen syllables come out on every run.

The haiku follows the classic 5-7-5 shape and tells a whole night of
debugging in three lines: a breakpoint set at three in the morning,
logs scrolling past with no clue, and dawn revealing that the bug was
only a typo. The shape is checked in code before anything is written.
"""

import os
from pathlib import Path

HAIKU = (
    "Breakpoint set at three\n"
    "the log scrolls past, still no clue\n"
    "dawn finds the typo\n"
)


def _count_syllables(word: str) -> int:
    """Count syllables by vowel groups, discounting a silent trailing e."""
    w = word.strip(",.!?;:").lower()
    if not w:
        return 0
    groups = 0
    prev_vowel = False
    for ch in w:
        vowel = ch in "aeiouy"
        if vowel and not prev_vowel:
            groups += 1
        prev_vowel = vowel
    if w.endswith("e") and groups > 1:
        groups -= 1
    return max(groups, 1)


def _check_shape(haiku: str) -> None:
    """Require exactly three lines with 5, 7 and 5 syllables."""
    lines = haiku.strip().split("\n")
    if len(lines) != 3:
        raise ValueError("haiku must have exactly three lines")
    counts = [sum(_count_syllables(w) for w in line.split()) for line in lines]
    if counts != [5, 7, 5]:
        raise ValueError(f"haiku is not 5-7-5, got {counts}")


def main() -> None:
    # The sealed gate: 1 to 200 UTF-8 characters, not only whitespace.
    if not 1 <= len(HAIKU) <= 200 or not HAIKU.strip():
        raise ValueError("haiku fails the 1-200 character gate")
    _check_shape(HAIKU)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
