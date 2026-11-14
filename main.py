#!/usr/bin/env python3
"""make.fun food-picture-01 entry.

Writes one picture of food to /output/entry.png.
Deterministic: copies the bundled entry.jpg bytes unchanged,
no network, no randomness, no timestamps in the output.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.jpg"
OUT = Path("/output/entry.png")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
