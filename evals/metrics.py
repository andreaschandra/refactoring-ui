"""Count design-system discipline in HTML outputs: distinct font sizes, spacing values, colors, weights, shadows, borders.

Usage: python evals/metrics.py evals/runs/<run>/*.html
Lower distinct counts = tighter system. Compare across runs, not in absolute terms.
"""
import re
import sys
from pathlib import Path

SPACING_PROPS = r"(?:margin|padding|gap|row-gap|column-gap|top|right|bottom|left|inset)(?:-[a-z]+)?"


def css_of(html: str) -> str:
    return "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))


def decls(css: str, prop_re: str) -> list[str]:
    return re.findall(rf"(?<![\w-]){prop_re}\s*:\s*([^;}}]+)", css, re.I)


def px_values(values: list[str]) -> set[str]:
    return {m for v in values for m in re.findall(r"-?\d*\.?\d+(?:px|rem|em)", v) if not re.fullmatch(r"-?0+(?:\.0+)?\w+", m)}


def metrics(path: Path) -> dict:
    css = css_of(path.read_text(encoding="utf-8"))
    font_sizes = decls(css, "font-size") + [
        m for v in decls(css, "font") for m in re.findall(r"(\d+(?:\.\d+)?px)", v)
    ]
    return {
        "font-sizes": len(px_values(font_sizes)),
        "spacing": len(px_values(decls(css, SPACING_PROPS))),
        "colors": len({c.lower() for c in re.findall(r"#[0-9a-f]{3,8}\b|(?:rgba?|hsla?|oklch|oklab|lch|lab)\([^)]*\)", css, re.I)}),
        "weights": len({w.strip() for w in decls(css, "font-weight")}),
        "shadows": len(decls(css, "box-shadow")),
        "borders": len([b for b in decls(css, r"border(?:-(?:top|right|bottom|left))?") if b.strip() not in ("0", "none")]),
        "tokens": len(re.findall(r"--[\w-]+\s*:", css)),
    }


if __name__ == "__main__":
    files = [Path(p) for p in sys.argv[1:]]
    rows = [(f.name, metrics(f)) for f in files]
    keys = list(rows[0][1])
    print("| file | " + " | ".join(keys) + " |")
    print("|---|" + "---|" * len(keys))
    for name, m in rows:
        print(f"| {name} | " + " | ".join(str(m[k]) for k in keys) + " |")
