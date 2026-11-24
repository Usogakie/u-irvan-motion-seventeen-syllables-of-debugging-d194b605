"""Write one debugging haiku (5-7-5) to entry.txt.

Reads nothing, needs no network, and uses no clock: the same
seventeen syllables come out on every run.
"""

import os
from pathlib import Path

HAIKU = (
    "Breakpoint set at three\n"
    "the log scrolls past, still no clue\n"
    "dawn finds the typo\n"
)


def main() -> None:
    # The sealed gate: 1 to 200 UTF-8 characters, not only whitespace.
    if not 1 <= len(HAIKU) <= 200 or not HAIKU.strip():
        raise ValueError("haiku fails the 1-200 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
