# Typography

## Contents
- Type scale (default values)
- Choosing fonts
- Line length
- Line height
- Mixed sizes on one line: baseline alignment
- Links
- Alignment
- Letter-spacing

## Type scale (default values)
- Interfaces often end up with every size from 10 to 24px. Font sizes must come from a fixed scale.
- Not linear: small jumps at the bottom, bigger jumps at the top (no choosing between 46 and 48px).
- Prefer a hand-picked scale over a ratio-based "modular" scale: ratios produce fractional sizes (render inconsistently across browsers) and leave gaps exactly where UI needs sizes (e.g. nothing between 12 and 16). If a ratio is used anyway, round every value to whole pixels when defining it.
- Default scale (pairs with the spacing scale in `layout-spacing.md`):

  `12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72` (px)

- Define sizes in `px` or `rem`, **never `em`**: nested `em` compounds (1.25em containing 0.875em computes to 17.5px), producing sizes that aren't on the scale.

## Choosing fonts
- Safe default for UI: a neutral sans-serif. If unsure, use the system stack: `-apple-system, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif`.
- Quality signals when picking a webfont:
  - At least 5 weights (≈10+ styles counting italics). Families with many weights are usually more carefully crafted.
  - Popular, widely used families. Popularity is a reasonable quality filter, especially for personality fonts (e.g. a serif for headings).
  - Families the best-designed sites in the domain use.
- Match the family to its job: headline families have tight spacing and short x-heights; UI/body families have looser spacing and tall x-heights. Don't use condensed, short-x-height fonts for main UI text.

## Line length
- Paragraphs: 45–75 characters per line. Set `max-width` around `20–35em` (em is right here: it tracks the font size). Beyond 75 characters is risky.
- When a content area must be wide for images or components, still cap the paragraph width inside it. Mixed widths in one column look more polished, not less.

## Line height
Line height is not a fixed 1.5. It depends on two things:
- **Line length:** wider text needs taller line height so the eye finds the next line (narrow ≈ 1.5, very wide up to ≈ 2).
- **Font size (inverse):** small text needs more line height; large headings need little or none (≈ 1–1.25).
- So the line height decreases as size goes up the type scale. One line-height value for every text style is a defect.

## Mixed sizes on one line: baseline alignment
- When different font sizes sit on one line (title left, small actions right; a price and its "/month"), align them by **baseline**, not vertical center. Centering offsets the baselines and looks awkward, especially when the texts are close together. CSS: `align-items: baseline`.

## Links
- Links inside paragraph text must stand out as clickable (color and/or underline).
- In UIs where most things are links (nav, lists, cards), a loud link color everywhere is overbearing. Use subtler emphasis: heavier weight or darker color.
- Ancillary links off the main path can look like plain text and reveal themselves on hover (underline or color).

## Alignment
- Left-align text in left-to-right languages by default.
- Center only headlines and short, independent blocks. Anything over 2–3 lines should be left-aligned. If one block in a centered group runs long, shorten the copy rather than mixing alignments.
- Right-align numbers in tables so decimals line up; use `font-variant-numeric: tabular-nums`.
- Justified text needs hyphenation (`hyphens: auto`) or it develops gaps between words. Only worth it for a deliberate print-like look.

## Letter-spacing
- Default: leave it as the type designer set it.
- Tighten headings when using a family with wide built-in spacing (designed for small sizes) to mimic a headline family, e.g. `letter-spacing: -0.01em` to `-0.025em` on large sizes. Don't do the reverse: headline fonts don't work small even with added spacing.
- All-caps text: increase letter-spacing (e.g. `0.05em`) for legibility, since uppercase letters lack the shape variety of lowercase.
