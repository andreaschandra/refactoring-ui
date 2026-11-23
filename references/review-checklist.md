# Review checklist

## Contents
- Process & systems (ch.1)
- Hierarchy (ch.2)
- Layout & spacing (ch.3)
- Typography (ch.4)
- Color (ch.5)

Each item is a yes/no check. A "no" names the reference file to consult for the fix.

## Process & systems → `process.md`
- [ ] The core feature is the most prominent thing on the page; the shell is quieter than the content.
- [ ] In grayscale, the most important element is still the most prominent and groupings are still clear.
- [ ] Every visible control is backed by real, in-scope behavior (no implied features, no dead actions).
- [ ] One personality throughout: one typeface direction, one radius style, one copy tone.
- [ ] Font weights, shadows, radii, border widths, and opacities each use a small fixed set.

## Hierarchy → `hierarchy.md`
- [ ] Each view has a clear #1 element; secondary and tertiary content is visibly pushed back.
- [ ] Hierarchy uses weight and color, not font size alone (no oversized primaries or tiny secondaries).
- [ ] Text uses at most 2–3 color levels (dark / grey / light grey) and 2 weights (normal, bold); no UI text below 400.
- [ ] All de-emphasized text still meets 4.5:1 contrast (3:1 for large text).
- [ ] No grey or white-with-opacity text on colored backgrounds; secondary text there is a tint of the background hue.
- [ ] Competing elements are softened rather than the key element being made louder.
- [ ] Data isn't shown as `Label: value` where format, context, or a merged phrase would do; remaining labels are quieter than their values (except spec-sheet style pages).
- [ ] Heading sizes follow visual importance, not tag level; section titles in app UIs are modest.
- [ ] Heavy elements (solid icons) are softened in color; faint elements gain width rather than darker color.
- [ ] One primary action per view (solid); secondary = outline/low contrast; tertiary = link style.
- [ ] Destructive actions that aren't primary use secondary/tertiary style; the strong red style appears on the confirmation step.

## Layout & spacing → `layout-spacing.md`
- [ ] Spacing is generous by default; any dense area is a deliberate choice with a reason.
- [ ] All spacing and sizing values come from a non-linear scale (adjacent steps ≥~25% apart); no off-scale values except content-driven ones (1px borders, intrinsic media sizes).
- [ ] Content uses only the width it needs (forms, cards, text blocks have max-widths); not everything is full-width because the nav is.
- [ ] Sidebars and optimal-width elements use fixed or max-widths, not grid percentages; the main area flexes.
- [ ] Responsive sizes are set per breakpoint; large type and elements shrink more than small ones on narrow screens.
- [ ] Component padding is tuned per size (large buttons roomier, small buttons tighter), not derived proportionally from font size.
- [ ] Space between groups is clearly larger than space within groups (form fields, heading above vs below, list items, horizontal groups).

## Typography → `typography.md`
- [ ] Font sizes come from a hand-picked, non-linear type scale; no near-duplicates; defined in px/rem, never em.
- [ ] UI text uses a neutral, well-crafted family (≥5 weights) or the system stack; no condensed / short x-height fonts for body or UI text.
- [ ] Paragraphs are capped at 45–75 characters per line, even inside wide content areas.
- [ ] Line height varies: taller for small or wide text, ~1–1.25 for large headings; not one value everywhere.
- [ ] Mixed font sizes on one line are baseline-aligned, not centered.
- [ ] Inline links in prose look clickable; links in link-heavy UI use subtle emphasis; ancillary links reveal on hover.
- [ ] Text is left-aligned; only headlines and short blocks (≤2–3 lines) are centered.
- [ ] Numbers in tables are right-aligned with tabular figures.
- [ ] Justified text has hyphenation enabled (or isn't justified).
- [ ] Letter-spacing is untouched except: tightened on large headings in wide-spaced families, widened on all-caps text.

## Color → `color.md`
- [ ] Colors are defined in OKLCH (in-gamut chroma) from a predefined palette; no one-off values and no on-the-fly lighten/darken.
- [ ] Palette has 8–10 greys, 5–10 shades per primary hue, and shaded accent/semantic colors (red, amber, green), with accents used sparingly.
- [ ] No pure black; greys step evenly from very dark grey to near-white.
- [ ] Light and dark shades stay colorful (chroma as high as the gamut allows); same shade number ≈ same L across hues; yellow-type hues shift slightly toward orange when darkening.
- [ ] Grey temperature (cool/warm/neutral) is deliberate and consistent with the personality.
- [ ] Text meets 4.5:1 (normal) / 3:1 (large); non-focal colored elements use flipped contrast (dark text on light tint) instead of white on dark color.
- [ ] Color is never the only signal: changes have icons/arrows, chart series differ in lightness as well as hue, states have text.
