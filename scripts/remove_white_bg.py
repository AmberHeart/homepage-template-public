#!/usr/bin/env python3
"""
Remove near-white background and export transparent PNG.

Features:
- Works for JPG/PNG input
- Removes only near-white pixels connected to image border
- Preserves inner white details inside logos
- Optional: remove all near-white pixels in the whole image

Usage:
  python scripts/remove_white_bg.py images/input-image.png
  python scripts/remove_white_bg.py images/input-image.png images/logo.png --threshold 245
  python scripts/remove_white_bg.py images/input-image.png --all-white
"""

from __future__ import annotations

import argparse
from collections import deque
from pathlib import Path

from PIL import Image


def is_near_white(pixel: tuple[int, int, int], threshold: int) -> bool:
    r, g, b = pixel
    return r >= threshold and g >= threshold and b >= threshold


def remove_white_bg(input_path: Path, output_path: Path, threshold: int, all_white: bool) -> None:
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    px = img.load()

    bg = [[False] * w for _ in range(h)]
    if all_white:
        for y in range(h):
            for x in range(w):
                if is_near_white(px[x, y][:3], threshold):
                    bg[y][x] = True
    else:
        # Mark near-white pixels connected to image borders as background.
        q: deque[tuple[int, int]] = deque()

        def try_push(x: int, y: int) -> None:
            if bg[y][x]:
                return
            if is_near_white(px[x, y][:3], threshold):
                bg[y][x] = True
                q.append((x, y))

        for x in range(w):
            try_push(x, 0)
            try_push(x, h - 1)
        for y in range(h):
            try_push(0, y)
            try_push(w - 1, y)

        while q:
            x, y = q.popleft()
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < w and 0 <= ny < h and not bg[ny][nx]:
                    if is_near_white(px[nx, ny][:3], threshold):
                        bg[ny][nx] = True
                        q.append((nx, ny))

    # Apply transparency to detected background.
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if bg[y][x]:
                px[x, y] = (r, g, b, 0)
            else:
                px[x, y] = (r, g, b, a)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(output_path, "PNG")


def default_output_name(input_path: Path) -> Path:
    return input_path.with_name(f"{input_path.stem}-transparent.png")


def main() -> None:
    parser = argparse.ArgumentParser(description="Remove white background to transparent PNG.")
    parser.add_argument("inputs", nargs="+", help="Input image paths (.jpg/.png)")
    parser.add_argument(
        "--threshold",
        type=int,
        default=245,
        help="Near-white threshold (0-255), default=245",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="",
        help="Optional output directory; default writes next to each input",
    )
    parser.add_argument(
        "--all-white",
        action="store_true",
        help="Remove all near-white pixels (not only border-connected background)",
    )
    args = parser.parse_args()

    threshold = max(0, min(255, args.threshold))
    out_dir = Path(args.output_dir) if args.output_dir else None

    for p in args.inputs:
        in_path = Path(p)
        if not in_path.exists():
            print(f"[skip] not found: {in_path}")
            continue

        out_path = (
            (out_dir / f"{in_path.stem}-transparent.png")
            if out_dir is not None
            else default_output_name(in_path)
        )
        remove_white_bg(in_path, out_path, threshold, args.all_white)
        print(f"[ok] {in_path} -> {out_path}")


if __name__ == "__main__":
    main()
