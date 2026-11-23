# Layout and spacing

## Contents
- White space: start generous, then remove
- Spacing and sizing scale (default values)
- Width: don't fill the screen
- Grids: fixed vs fluid widths
- Responsive sizing: scale things independently
- Grouping: avoid ambiguous spacing

## White space: start generous, then remove
- Adding space until something stops looking cramped leaves it at "barely acceptable". Start with clearly too much space and reduce it.
- What feels like slightly too much around one element is usually right once the full page is assembled.
- Dense layouts are fine when there's a reason (e.g. a dashboard that must fit on one screen), but density must be a deliberate choice, never the default.
- Generate: pick spacing one step larger than your first instinct. Critique: cramped padding and margins are a top-impact fix.

## Spacing and sizing scale (default values)
- One scale covers margin, padding, gap, element widths and heights, and icon sizes.
- Not linear. "Multiples of 4" still leaves near-identical choices (e.g. 120 vs 124). Adjacent values must be at least ~25% apart, so steps are tight at the small end and widen as values grow.
- Build it from a base of 16px (the browser default) using factors and multiples. Default scale:

  `4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 640, 768` (px)

- Use it by stepping: if a gap isn't enough, take the next value, not the next pixel.
- Any value off the scale is a defect unless it is content-driven (e.g. 1px borders, an image's intrinsic size).

## Width: don't fill the screen
- Use the width the content needs. If a form works at 600px, make it 600px wide on a 1400px screen; extra margin around the edges is harmless, stretched content is hard to read.
- Sections don't have to be full-width just because the nav or header is. Size each element for its own content; don't make one worse to match another.
- Design the small screen first (~400px) and widen from there; most of the layout survives with fewer changes than expected.
- If a narrow element looks unbalanced in a wide layout, add columns instead of widening it (e.g. a form at its ideal width with explanatory text in a side column).
- The reverse also holds: if content needs a lot of space, use it; don't cram.

## Grids: fixed vs fluid widths
- A 12-column grid is a set of allowed percentage widths. It's useful for order, but not every element should be fluid.
- Sidebars, cards, form panels, and similar elements usually have an optimal width. Give them a **fixed width** (sidebar) or a **max-width** (card, form) and let the main area flex to fill the rest; the main area can use its own internal grid.
- Percentage widths make a sidebar too wide on large screens and too narrow (wrapping, truncation) on small ones.
- Don't shrink an element until the viewport forces it: `max-width: 500px; width: 100%` beats column spans that change per breakpoint (those can make an element *wider* on medium screens than on large ones).
- Inside components, only use percentages when you actually want proportional scaling.

## Responsive sizing: scale things independently
- Size relationships don't hold across contexts. A headline at 2.5× body text on desktop is too big on mobile; on small screens it should be closer to 1.5–1.7× body.
- Large elements must shrink faster than small ones as the screen narrows; the gap between big and small shrinks on small screens. Set each breakpoint's sizes explicitly instead of coupling them with `em` multipliers.
- Same inside components: a large button should get disproportionately more padding, and a small button disproportionately less, than its font size implies. Tune padding per size; don't derive it from font size.

## Grouping: avoid ambiguous spacing
- Without borders or backgrounds, spacing alone shows what belongs together. **Space around a group must be clearly larger than space within it.**
- Common failures:
  - Form: gap between label and its input equals gap between fields, so labels float between inputs. Fix: tight label→input, larger field→field.
  - Headings: equal space above and below a heading. Fix: more space above (separating from the previous section) than below (attaching to its content).
  - Lists: space between items equals line spacing within an item. Fix: more space between items.
  - Horizontal groups (e.g. icon + label pairs, inline stats): same rule along the row.
- One spacing value used for every gap, within and between groups alike, is itself a grouping failure.
