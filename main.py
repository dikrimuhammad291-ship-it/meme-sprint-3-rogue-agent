#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue.

Copies the meme image (meme.png, 1024x1024, under 1 MiB) to
entry.png in the output directory.
Standard library only, deterministic, no network.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "meme.png"

MAX_BYTES = 1_048_576


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    if not SOURCE.is_file():
        raise FileNotFoundError(f"meme image missing: {SOURCE}")
    if SOURCE.stat().st_size > MAX_BYTES:
        raise ValueError("meme image exceeds the 1 MiB cap")
    shutil.copyfile(SOURCE, out_dir / "entry.png")
    # Belt and braces: the file the grader reads must itself be in cap.
    if (out_dir / "entry.png").stat().st_size > MAX_BYTES:
        raise ValueError("entry.png exceeds the 1 MiB cap")


if __name__ == "__main__":
    main()
