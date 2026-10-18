#!/usr/bin/env python3
"""Renders the TL monogram to scripts/data/tl-ascii.txt as 3D block letters.

Needs Pillow, only to rasterise the glyphs. build-art.py itself is stdlib only.
Face characters ("+*#%") and extrusion characters (".:-=") are disjoint sets,
which is how build-art.py colours them differently.

    python3 scripts/make-ascii.py [path/to/bold-font.ttf]
"""
import sys
from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFont

COLS, ROWS = 40, 20
CPW, CPH = 16, 26            # hi-res pixels per character cell (matches the 8.6 x 14 grid in build-art.py)
EXT_X, EXT_Y, EXT_N = 3, 3, 9  # extrusion: 3 px right and down per step, 9 steps
FONT = sys.argv[1] if len(sys.argv) > 1 else "/System/Library/Fonts/Supplemental/Arial Black.ttf"
OUT = Path(__file__).resolve().parent / "data" / "tl-ascii.txt"

W, H = COLS * CPW, ROWS * CPH
target_w, target_h = int(W * 0.78), int(H * 0.82)

font = ImageFont.truetype(FONT, 400)
l, t, r, b = font.getbbox("TL")
glyph = Image.new("L", (r - l, b - t), 0)
ImageDraw.Draw(glyph).text((-l, -t), "TL", font=font, fill=255)
glyph = glyph.crop(glyph.getbbox()).resize((target_w, target_h), Image.LANCZOS)  # stretched tall, like a condensed face
face = Image.new("L", (W, H), 0)
face.paste(glyph, (int(W * 0.05), int(H * 0.05)))

ext = Image.new("L", (W, H), 0)
for k in range(1, EXT_N + 1):
    ext = ImageChops.lighter(ext, ImageChops.offset(face, k * EXT_X, k * EXT_Y))
shadow = ImageChops.subtract(ext, face)

fs = face.resize((COLS, ROWS), Image.BOX)
ss = shadow.resize((COLS, ROWS), Image.BOX)

FACE, SHADE = "+*#%", ".:-="
lines = []
for y in range(ROWS):
    row = ""
    for x in range(COLS):
        f, s = fs.getpixel((x, y)) / 255, ss.getpixel((x, y)) / 255
        if f >= 0.5:
            light = 1 - (x / COLS * 0.5 + y / ROWS * 0.5)  # lit from the upper left
            v = min(0.999, f * (0.30 + 0.75 * light))
            row += FACE[int(v * len(FACE))]
        elif f >= 0.2 and f >= s:
            row += FACE[0]
        elif s >= 0.2 or f > 0:
            row += SHADE[min(len(SHADE) - 1, int(max(s, f) * len(SHADE)))]
        else:
            row += " "
    lines.append(row.rstrip())
while lines and not lines[-1]:
    lines.pop()
OUT.write_text("\n".join(lines) + "\n")
print("\n".join(lines))
