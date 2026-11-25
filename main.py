#!/usr/bin/env python3
"""Copy this entry's front-page image to the grader's output directory.

The image (output/entry.png) is drawn from the verified world news of
Tuesday 24 November 2026 and shipped in this repository. This program
only copies it to /output/entry.png (or $OUTPUT_DIR/entry.png), checks
the gate rules on the way, and verifies the copy is byte-identical.

Standard library only; no network.
"""

import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1048576  # 1 MiB
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

SOURCE_NAME = "entry.png"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _png_dimensions(path):
    """Read (width, height) from a PNG's IHDR chunk (stdlib only)."""
    with open(path, "rb") as fh:
        data = fh.read(33)
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise ValueError("not a PNG with an IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "output", SOURCE_NAME)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, SOURCE_NAME)

    if not os.path.isfile(source):
        print(f"error: source image missing: {source}", file=sys.stderr)
        return 1

    with open(source, "rb") as fh:
        header = fh.read(len(PNG_MAGIC))
    if header != PNG_MAGIC:
        print("error: source is not a PNG", file=sys.stderr)
        return 1

    try:
        width, height = _png_dimensions(source)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if width > MAX_SIDE or height > MAX_SIDE:
        print(f"error: image is {width}x{height}, over the 1024x1024 limit",
              file=sys.stderr)
        return 1

    size = os.path.getsize(source)
    if size > MAX_BYTES:
        print(f"error: source is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, dest)

    # Verify the copy is byte-identical to the source.
    if _sha256(source) != _sha256(dest):
        print("error: copied file differs from source", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({width}x{height}, {size} bytes, "
          f"sha256 {_sha256(dest)[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
