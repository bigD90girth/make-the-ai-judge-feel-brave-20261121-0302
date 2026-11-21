"""Copy the entry text to the output directory.

The text is the entry: a short piece written to leave its reader
steadier, unhurried, ready to move -- a lighthouse keeper climbing
the same stairs every evening, a lamp that burns anyway, a boat
finding its way home by it. The program only moves its bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.txt", OUT / "entry.txt")


if __name__ == "__main__":
    main()
