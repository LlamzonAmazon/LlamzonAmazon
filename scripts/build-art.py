#!/usr/bin/env python3
"""Generates the SVGs the README uses into assets/. Standard library only.

    python3 scripts/build-art.py

Square corners everywhere: no asset uses a corner radius.

  header-*.svg          a code block, in GitHub's code block colours
  badges/*.svg          flat badges, brand colour and icon per tool

The header has dark and light variants chosen in the README with <picture>;
badges are one file each. Headings, tables, lists, rules and notes are plain markdown, so
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
        f'<rect width="{W}" height="{H}" fill="{bg}"/>\n'
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
                o.append(f'<rect x="{rx + j * 19}" y="{y - 11:.1f}" width="14" height="14" fill="{sw(name, mode)}"/>')
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


# ---------------------------------------------------------------- flat badges

def lum(hex_):
    r, g, bl = [int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(bl)


def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


# slug, label, brand colour, simple-icons slug or None
BADGES = [
    ("website", "Website", "#14b8a6", None),
    ("linkedin", "LinkedIn", "#0A66C2", "linkedin"),
    ("paper", "IEEE GLOBECOM 2026 paper", "#00629B", None),
    ("python", "Python", "#3776AB", "python"),
    ("typescript", "TypeScript", "#3178C6", "typescript"),
    ("sql", "SQL", "#336791", "postgresql"),
    ("bash", "Bash", "#4EAA25", "gnubash"),
    ("kql", "KQL", "#0078D4", None),
    ("fastapi", "FastAPI", "#009688", "fastapi"),
    ("nodejs", "Node.js", "#339933", "nodedotjs"),
    ("postgresql", "PostgreSQL", "#4169E1", "postgresql"),
    ("clickhouse", "ClickHouse", "#FFCC01", "clickhouse"),
    ("supabase", "Supabase", "#3FCF8E", "supabase"),
    ("pandas", "pandas", "#150458", "pandas"),
    ("react", "React", "#61DAFB", "react"),
    ("nextjs", "Next.js", "#000000", "nextdotjs"),
    ("vite", "Vite", "#646CFF", "vite"),
    ("tailwind", "Tailwind", "#06B6D4", "tailwindcss"),
    ("d3", "D3", "#F9A03C", "d3dotjs"),
    ("cloudflare", "Cloudflare", "#F38020", "cloudflare"),
    ("aws", "AWS", "#232F3E", "amazonwebservices"),
    ("azure", "Azure", "#0078D4", None),
    ("terraform", "Terraform", "#844FBA", "terraform"),
    ("docker", "Docker", "#2496ED", "docker"),
    ("actions", "GitHub Actions", "#2088FF", "githubactions"),
    ("semgrep", "Semgrep", "#1FC5A4", None),
    ("sentinel", "Sentinel", "#0078D4", None),
    ("entra", "Entra ID", "#0078D4", None),
    ("claude", "Claude", "#D97757", "claude"),
    ("ollama", "Ollama", "#FFFFFF", "ollama"),
    ("pytorch", "PyTorch", "#EE4C2C", "pytorch"),
]


def badge(slug, label, color, icon):
    """28px flat badge: square corners, brand colour, optional icon, uppercase tracked text in the README font."""
    fg = "#ffffff" if contrast(color, "#ffffff") >= contrast(color, "#000000") else "#000000"
    text = label.upper()
    cw = 8.4  # pinned advance per character at 11px bold with 1.2px tracking
    tw = len(text) * cw
    icon_w = 24 if icon else 0
    w = int(12 + icon_w + tw + 12)
    d = None
    if icon:
        d = re.search(r'<path d="([^"]+)"', (DATA / "icons" / f"{icon}.svg").read_text()).group(1)
    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="28" viewBox="0 0 {w} 28" role="img" aria-label="{escape(label)}">\n',
        f'<rect x=".5" y=".5" width="{w - 1}" height="27" fill="{color}" stroke="#808080" stroke-opacity=".35"/>\n',
    ]
    if d:
        o.append(f'<path transform="translate(12 7) scale(.5833)" fill="{fg}" d="{d}"/>\n')
    o.append(
        f'<text x="{12 + icon_w}" y="18" font-family="{SANS}" font-size="11" font-weight="700" letter-spacing="1.2" '
        f'fill="{fg}" textLength="{tw:.1f}" lengthAdjust="spacing">{escape(text)}</text>\n</svg>\n'
    )
    write(OUT / "badges" / f"{slug}.svg", "".join(o))


if __name__ == "__main__":
    for m in ("dark", "light"):
        header(m)
    for b in BADGES:
        badge(*b)
    print(f"wrote {len(list(OUT.rglob('*.svg')))} svgs to {OUT}")
