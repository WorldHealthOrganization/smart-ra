#!/usr/bin/env python3
"""Draw a pattern figure (e.g. Fig. 3.6, exchange-patterns.json) as SVG in the
figure theme every generated DPI-H RA figure uses: ArchiMate layer fills
(cat-harness-tools archimate/scripts/figure-theme.ts LAYER_FILL), the navy
title banner, and a key.

Usage: python3 -I tools/figures/draw_patterns.py <data.json> <out.svg> [--check]
With --check it writes nothing and exits 1 when <out.svg> is not what the data draws.
"""
import html
import json
import sys

LAYER_FILL = {"Business": "#ffffb5", "Application": "#b5ffff", "Technology": "#c9e7b7"}
FONT = "Inter, 'Segoe UI', system-ui, -apple-system, Helvetica, Arial, sans-serif"
NODE_W, NODE_H, GAP, PAD, COLS = 80, 32, 24, 20, 3


def outline(fill):
    n = int(fill[1:], 16)
    return "#%02x%02x%02x" % tuple(round(((n >> s) & 255) * 0.55) for s in (16, 8, 0))


def esc(s):
    return html.escape(s, quote=True)


def clip(cx, cy, w, h, tx, ty):
    """Where the line from a box's centre towards (tx, ty) leaves the box."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (w / 2) / abs(dx) if dx else float("inf")
    sy = (h / 2) / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def draw(d):
    pw, ph = d["panelSize"]
    rows = (len(d["panels"]) + COLS - 1) // COLS
    width = PAD * 2 + COLS * pw + (COLS - 1) * GAP
    top = 72
    body_h = rows * (ph + 34) + (rows - 1) * GAP
    out = []
    for i, p in enumerate(d["panels"]):
        r, c = divmod(i, COLS)
        n_in_row = min(COLS, len(d["panels"]) - r * COLS)
        offset = (COLS - n_in_row) * (pw + GAP) / 2  # centre a short last row
        ox = PAD + offset + c * (pw + GAP)
        oy = top + r * (ph + 34 + GAP)
        out.append(f'<rect x="{ox}" y="{oy}" width="{pw}" height="{ph + 34}" rx="6" fill="#fff" stroke="#c8ccd4"/>')
        out.append(f'<text x="{ox + 12}" y="{oy + 20}" style="font:600 12px {FONT};fill:#14213d">{esc(p["title"])}</text>')
        nodes = {}
        for n in p["nodes"]:
            key, label, kind, x, y = n[:5]
            w, h = (n[5], n[6]) if len(n) > 5 else (NODE_W, NODE_H)
            nodes[key] = (ox + x, oy + 34 + y, w, h, label, kind)
        for e in p["edges"]:
            a, b, style = e[:3]
            ax, ay, aw, ah = nodes[a][:4]
            bx, by, bw, bh = nodes[b][:4]
            acx, acy, bcx, bcy = ax + aw / 2, ay + ah / 2, bx + bw / 2, by + bh / 2
            x1, y1 = clip(acx, acy, aw, ah, bcx, bcy)
            x2, y2 = clip(bcx, bcy, bw, bh, acx, acy)
            ln = d["lines"][style]
            dash = f' stroke-dasharray="{ln["dash"]}"' if ln.get("dash") else ""
            arrow = ' marker-end="url(#pf-arrow)"' if ln.get("arrow") else ""
            out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#333" stroke-width="1.4"{dash}{arrow}/>')
            if len(e) > 3:
                out.append(f'<text x="{(x1 + x2) / 2:.1f}" y="{(y1 + y2) / 2 - 5:.1f}" text-anchor="middle" style="font:9px {FONT};fill:#333;paint-order:stroke;stroke:#fff;stroke-width:3px">{esc(e[3])}</text>')
        for x, y, w, h, label, kind in nodes.values():
            fill = LAYER_FILL[d["kinds"][kind]["layer"]]
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{outline(fill)}"/>')
            out.append(f'<text x="{x + w / 2}" y="{y + h / 2 + 4}" text-anchor="middle" style="font:600 11px {FONT};fill:#111">{esc(label)}</text>')
    # key
    ky = top + body_h + GAP
    key = [f'<text x="{PAD + 10}" y="{ky + 20}" style="font:700 13px {FONT};fill:#111">Key</text>']
    cy = ky + 42
    lines_w = 0
    for k in d["kinds"].values():
        fill = LAYER_FILL[k["layer"]]
        key.append(f'<rect x="{PAD + 10}" y="{cy - 8}" width="44" height="16" rx="3" fill="{fill}" stroke="{outline(fill)}"/>'
                   f'<text x="{PAD + 68}" y="{cy + 4}" style="font:11px {FONT};fill:#222">{esc(k["label"])}</text>')
        lines_w = max(lines_w, len(k["label"]))
        cy += 22
    for ln in d["lines"].values():
        dash = f' stroke-dasharray="{ln["dash"]}"' if ln.get("dash") else ""
        arrow = ' marker-end="url(#pf-arrow)"' if ln.get("arrow") else ""
        key.append(f'<line x1="{PAD + 12}" y1="{cy}" x2="{PAD + 52}" y2="{cy}" stroke="#333" stroke-width="1.4"{dash}{arrow}/>'
                   f'<text x="{PAD + 68}" y="{cy + 4}" style="font:11px {FONT};fill:#222">{esc(ln["label"])}</text>')
        lines_w = max(lines_w, len(ln["label"]))
        cy += 22
    key_w = 68 + lines_w * 6.2 + 20
    key_h = cy - ky
    height = ky + key_h + PAD
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height:.0f}" width="{width}" height="{height:.0f}" role="img" aria-labelledby="pf-title">'
            f'<title id="pf-title">{esc(d["title"])}</title>'
            '<defs><marker id="pf-arrow" viewBox="0 0 12 12" refX="11" refY="6" markerWidth="11" markerHeight="11" orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M1 1 L11 6 L1 11 Z" fill="#333"/></marker></defs>'
            f'<rect width="{width}" height="{height:.0f}" fill="#f8f9fb"/>'
            f'<rect width="{width}" height="52" fill="#14213d"/>'
            f'<text x="20" y="24" style="font:700 17px {FONT};fill:#fff">{esc(d["title"])}</text>'
            f'<text x="20" y="41" style="font:italic 10px {FONT};fill:#c9d6e6">Drawn from {esc(d["source"])}</text>')
    frame = f'<rect x="{PAD}" y="{ky}" width="{key_w:.0f}" height="{key_h}" fill="#fafafa" stroke="#bbb"/>'
    return head + "".join(out) + frame + "".join(key) + "</svg>\n"


def main(argv):
    data, dst, *rest = argv
    svg = draw(json.load(open(data, encoding="utf-8")))
    if "--check" in rest:
        try:
            same = open(dst, encoding="utf-8").read() == svg
        except FileNotFoundError:
            same = False
        if not same:
            print(f"{dst} is not what {data} draws; run without --check", file=sys.stderr)
            return 1
        print(f"✓ {dst} matches {data}")
        return 0
    open(dst, "w", encoding="utf-8").write(svg)
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
