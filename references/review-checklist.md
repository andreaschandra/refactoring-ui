# Review checklist

## Contents
- Process & systems (ch.1)
- Hierarchy (ch.2)
- Layout & spacing (ch.3)

Each item is a yes/no check. A "no" names the reference file to consult for the fix.

## Process & systems → `process.md`
- [ ] The core feature is the most prominent thing on the page; the shell is quieter than the content.
- [ ] In grayscale, the most important element is still the most prominent and groupings are still clear.
- [ ] Every visible control is backed by real, in-scope behavior (no implied features, no dead actions).
- [ ] One personality throughout: one typeface direction, one radius style, one copy tone.
- [ ] Font sizes come from a defined scale (no near-duplicates like 13/14/15px used side by side).
- [ ] Colors come from a defined palette; no one-off hex values.
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
