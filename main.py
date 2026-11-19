"""Entry for make.fun news-image-20261118.

Copies the bundled entry.png to /output/entry.png.
Python 3.13 standard library only, no network, deterministic:
the output bytes are exactly the bytes of the repository's entry.png.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"bundled image not found: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    # copyfile overwrites deterministically: two runs write identical bytes.
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
