#!/usr/bin/env python3
"""Generates the SVGs the README uses into assets/. Standard library only.

    python3 scripts/build-art.py

Everything here is a replica of a GitHub (Primer) component, in GitHub's own
colours and the README font stack:

  header-*.svg          a code block, styled like GitHub's <pre>
  buttons/*.svg         Primer secondary buttons
  labels/*.svg          Primer labels (accent, success, done, severe, danger)

Dark and light variants are written side by side and chosen in the README with
<picture>. Headings, tables, lists, rules and notes are plain markdown, so
GitHub renders them itself. The header types in once and the cursor blinks;
nothing else animates, and prefers-reduced-motion turns that off.
"""
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
DATA = ROOT / "scripts" / "data"

W = 760

# The GitHub README font stack. It is the only font any asset uses.
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"

# GitHub Primer values, (light, dark).
PRIMER = {
    "canvas-muted": ("#f6f8fa", "#151b23"),   # code block background
    "fg": ("#1f2328", "#f0f6fc"),
    "fg-muted": ("#59636e", "#9198a1"),
    "btn-bg": ("#f6f8fa", "#212830"),
    "btn-border": ("#d1d9e0", "#3d444d"),
    "btn-fg": ("#25292e", "#f0f6fc"),
    # label variants: (border light, border dark, text light, text dark)
    "accent": ("#0969da", "#1f6feb", "#0969da", "#4493f8"),
    "success": ("#1f883d", "#238636", "#1a7f37", "#3fb950"),
    "done": ("#8250df", "#8957e5", "#8250df", "#ab7df8"),
    "severe": ("#bc4c00", "#bd561d", "#bc4c00", "#db6d28"),
    "danger": ("#cf222e", "#da3633", "#d1242f", "#f85149"),
}
# Primer text colours, used for the header's accents and colour swatches
SWATCH = {
    "green": ("#1a7f37", "#3fb950"),
    "blue": ("#0969da", "#4493f8"),
    "purple": ("#8250df", "#ab7df8"),
    "yellow": ("#9a6700", "#d29922"),
    "orange": ("#bc4c00", "#db6d28"),
    "red": ("#d1242f", "#f85149"),
    "pink": ("#bf3989", "#db61a2"),
}


def pv(key, mode):
    return PRIMER[key][0 if mode == "light" else 1]


def sw(name, mode):
    return SWATCH[name][0 if mode == "light" else 1]


def write(path, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body)


# ---------------------------------------------------------------- header

def header(mode):
    bg, fg, dim = pv("canvas-muted", mode), pv("fg", mode), pv("fg-muted", mode)
    green, blue = sw("green", mode), sw("blue", mode)
    art = (DATA / "tl-ascii.txt").read_text().splitlines()
    cols = max(len(r) for r in art)
    cw, lh, fs = 8.6, 14, 11  # one glyph per cell; the widest glyph (%) fits the 8.6 cell, so nothing overlaps
    ax, ay = 28, 62
    art_w, art_h = cols * cw, len(art) * lh
    rx, vx = ax + art_w + 26, ax + art_w + 26 + 98
    step = 15.5
    rows = [
        ("user",), ("sep",),
        ("kv", "Role", "Forward Deployed Engineer"),
        ("kv", "Focus", "production AI agents, F&B operators"),
        ("kv", "Background", "blue-team SOC, then full-stack"),
        ("kv", "Education", "BSc Honours CS, Western University"),
        ("kv", "Languages", "Python, TypeScript, SQL"),
        ("kv", "Infra", "Cloudflare, AWS, Azure"),
        ("kv", "Published", "IEEE GLOBECOM 2026, first author"),
        ("blank",), ("title", "contacts"), ("sep",),
        ("kv2", "Web", "llamzon.ca"),
        ("kv2", "LinkedIn", "in/thomasllamzon"),
        ("kv2", "GitHub", "LlamzonAmazon"),
        ("blank",), ("swatch",),
    ]
    H = int(ay + max(art_h, len(rows) * step) + 56)

    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">\n<style>\n'
        f".sans{{font-family:{SANS}}}\n"
        "@keyframes fade{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:none}}\n"
        "@keyframes show{from{fill-opacity:0}to{fill-opacity:1}}\n"
        "@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}\n"
        ".f{animation:fade .45s ease-out both}\n"
        ".cur{animation:blink 1.1s step-end infinite}\n"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important}}\n"
        "</style>\n"
        f'<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="{ax}" y1="{ay}" x2="{ax + art_w}" y2="{ay + art_h}">'
        f'<stop offset="0" stop-color="{green}"/><stop offset="1" stop-color="{blue}"/></linearGradient></defs>\n'
        f'<rect width="{W}" height="{H}" rx="6" fill="{bg}"/>\n'
    ]

    # typed command
    o.append(f'<text class="sans" x="{ax}" y="36" font-size="13" font-weight="600">')
    for i, ch in enumerate("$ tfetch"):
        d = 0.25 + i * 0.09
        o.append(f'<tspan fill="{green if i == 0 else fg}" style="animation:show .01s step-end both;animation-delay:{d:.2f}s">{escape(ch)}</tspan>')
    o.append("</text>\n")

    # ascii art: every glyph sits at its own grid x (text-anchor middle), so the
    # proportional README font cannot misalign rows. Extrusion glyphs are dimmer than the face.
    FACE = set("+*#%")
    o.append(f'<g class="sans" font-size="{fs}" font-weight="600">\n')
    for r, line in enumerate(art):
        d = 0.9 + r * 0.04
        yy = ay + r * lh + fs
        for chars, fill, op in (
            ([(i, c) for i, c in enumerate(line) if c in FACE], "url(#g)", 1),
            ([(i, c) for i, c in enumerate(line) if c != " " and c not in FACE], dim, .8),
        ):
            if not chars:
                continue
            xs = " ".join(f"{ax + (i + .5) * cw:.1f}" for i, _ in chars)
            txt = escape("".join(c for _, c in chars))
            o.append(
                f'<text class="f" x="{xs}" y="{yy:.1f}" text-anchor="middle" fill="{fill}" fill-opacity="{op}" '
                f'style="animation-delay:{d:.2f}s">{txt}</text>\n'
            )
    o.append("</g>\n")

    # right column
    y = ay + 11
    for i, row in enumerate(rows):
        d = 1.0 + i * 0.07
        kind = row[0]
        s = f'class="f sans" font-size="12" style="animation-delay:{d:.2f}s"'
        if kind == "user":
            o.append(
                f'<text {s} x="{rx}" y="{y:.1f}" font-weight="700"><tspan fill="{green}">thomas</tspan>'
                f'<tspan fill="{dim}">@</tspan><tspan fill="{blue}">llamzon</tspan></text>\n'
            )
        elif kind == "sep":
            o.append(f'<text {s} x="{rx}" y="{y:.1f}" fill="{dim}">{"-" * 14}</text>\n')
        elif kind == "title":
            o.append(f'<text {s} x="{rx}" y="{y:.1f}" fill="{blue}" font-weight="700">{row[1]}</text>\n')
        elif kind in ("kv", "kv2"):
            kc = green if kind == "kv" else blue
            o.append(
                f'<text {s} x="{rx}" y="{y:.1f}"><tspan fill="{kc}" font-weight="700">{escape(row[1])}</tspan>'
                f'<tspan x="{vx}" fill="{fg}">{escape(row[2])}</tspan></text>\n'
            )
        elif kind == "swatch":
            o.append(f'<g class="f" style="animation-delay:{d:.2f}s">')
            for j, name in enumerate(["green", "blue", "purple", "yellow", "orange", "red", "pink"]):
                o.append(f'<rect x="{rx + j * 19}" y="{y - 11:.1f}" width="14" height="14" rx="2" fill="{sw(name, mode)}"/>')
            o.append("</g>\n")
        y += step

    py = H - 22
    o.append(
        f'<text class="f sans" x="{ax}" y="{py}" font-size="13" font-weight="600" style="animation-delay:2.6s">'
        f'<tspan fill="{green}">$</tspan></text>\n'
        f'<rect class="cur" x="{ax + 14}" y="{py - 12}" width="8" height="15" fill="{fg}" style="animation-delay:2.6s"/>\n'
    )
    o.append("</svg>\n")
    write(OUT / f"header-{mode}.svg", "".join(o))


# ---------------------------------------------------------------- Primer buttons

# slug, label, icon source: ("octicon", name) or ("simple", name)
BUTTONS = [
    ("website", "Website", ("octicon", "globe-16")),
    ("linkedin", "LinkedIn", ("simple", "linkedin")),
    ("paper", "IEEE GLOBECOM 2026 paper", ("octicon", "book-16")),
]


def icon_path(kind, name):
    if kind == "octicon":
        return re.search(r'<path d="([^"]+)"', (DATA / "octicons" / f"{name}.svg").read_text()).group(1), 16
    return re.search(r'<path d="([^"]+)"', (DATA / "icons" / f"{name}.svg").read_text()).group(1), 24


def button(slug, label, icon, mode):
    """Primer secondary button: 32px tall, 12px padding, 6px radius, 14px / 500 text, 16px icon."""
    bg, border, fg = pv("btn-bg", mode), pv("btn-border", mode), pv("btn-fg", mode)
    d, native = icon_path(*icon)
    tw = len(label) * 7.6 + 2  # estimate for the README font at 14px / 500; text is not pinned
    w = int(12 + 16 + 8 + tw + 12)
    scale = 16 / native
    o = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="32" viewBox="0 0 {w} 32" role="img" aria-label="{escape(label)}">\n'
        f'<rect x=".5" y=".5" width="{w - 1}" height="31" rx="6" fill="{bg}" stroke="{border}"/>\n'
        f'<path transform="translate(12 8) scale({scale})" fill="{fg}" d="{d}"/>\n'
        f'<text x="36" y="21" font-family="{SANS}" font-size="14" font-weight="500" fill="{fg}">{escape(label)}</text>\n</svg>\n'
    )
    write(OUT / "buttons" / f"{slug}-{mode}.svg", o)


# ---------------------------------------------------------------- Primer labels

# slug, text, variant. The variant is chosen per tool group.
LABELS = [
    ("python", "Python", "accent"), ("typescript", "TypeScript", "accent"), ("sql", "SQL", "accent"),
    ("bash", "Bash", "accent"), ("kql", "KQL", "accent"),
    ("fastapi", "FastAPI", "success"), ("nodejs", "Node.js", "success"), ("postgresql", "PostgreSQL", "success"),
    ("clickhouse", "ClickHouse", "success"), ("supabase", "Supabase", "success"), ("pandas", "pandas", "success"),
    ("react", "React", "done"), ("nextjs", "Next.js", "done"), ("vite", "Vite", "done"),
    ("tailwind", "Tailwind", "done"), ("d3", "D3", "done"),
    ("cloudflare", "Cloudflare", "severe"), ("aws", "AWS", "severe"), ("azure", "Azure", "severe"),
    ("terraform", "Terraform", "severe"), ("docker", "Docker", "severe"), ("actions", "GitHub Actions", "severe"),
    ("semgrep", "Semgrep", "danger"), ("sentinel", "Sentinel", "danger"), ("entra", "Entra ID", "danger"),
    ("claude", "Claude", "danger"), ("ollama", "Ollama", "danger"), ("pytorch", "PyTorch", "danger"),
]


def label(slug, text, variant, mode):
    """Primer Label: 20px tall, 7px side padding, 1px border in the emphasis colour, 12px / 500 text, pill radius."""
    bl, bd, tl, td = PRIMER[variant]
    border = bl if mode == "light" else bd
    color = tl if mode == "light" else td
    tw = len(text) * 6.9 + 1  # estimate for the README font at 12px / 500
    w = int(7 + tw + 7 + 2)
    o = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="20" viewBox="0 0 {w} 20" role="img" aria-label="{escape(text)}">\n'
        f'<rect x=".5" y=".5" width="{w - 1}" height="19" rx="9.5" fill="none" stroke="{border}"/>\n'
        f'<text x="{w / 2:.1f}" y="14" text-anchor="middle" font-family="{SANS}" font-size="12" font-weight="500" fill="{color}">{escape(text)}</text>\n</svg>\n'
    )
    write(OUT / "labels" / f"{slug}-{mode}.svg", o)


if __name__ == "__main__":
    for m in ("dark", "light"):
        header(m)
        for b in BUTTONS:
            button(*b, m)
        for l in LABELS:
            label(*l, m)
    print(f"wrote {len(list(OUT.rglob('*.svg')))} svgs to {OUT}")
