# Hierarchy

## Contents
- Principle: de-emphasize to create hierarchy
- Tools beyond font size: color and weight
- Text on colored backgrounds
- Emphasize by de-emphasizing
- Labels are a last resort
- Visual hierarchy ≠ document hierarchy
- Balancing weight and contrast
- Action hierarchy (buttons)

## Principle: de-emphasize to create hierarchy
- Hierarchy (how important elements look relative to each other) is the biggest single factor in a UI feeling "designed", more than color, typeface, or layout.
- When everything competes for attention, the page reads as one noisy wall. Decide what matters most on each view, then actively push secondary and tertiary content back.

## Tools beyond font size: color and weight
- Don't drive hierarchy with font size alone: it produces oversized primary text and undersized secondary text.
- Emphasize with **weight** (bolder at a reasonable size). De-emphasize with **color** (softer grey) rather than shrinking text until it's hard to read.
- Text colors: 2–3 levels.
  - Dark: primary content (titles, key values).
  - Grey: secondary (metadata, dates, descriptions).
  - Lighter grey: tertiary (footnotes, fine print).
- Font weights: 2 is usually enough for UI.
  - Normal (400 or 500, depending on the font) for most text.
  - Bold (600 or 700) for emphasis.
- No weights below 400 for UI text. Thin weights are only for large display headings. To de-emphasize, use a lighter color or a smaller size, never a thinner weight.

## Text on colored backgrounds
- Grey text on a colored background looks wrong. What de-emphasizes on white is *reduced contrast*, not greyness.
- Don't use white with reduced opacity either: it looks washed out or disabled, and on images/patterns the background shows through.
- Do: pick a color with the **same hue as the background**, then adjust saturation and lightness until contrast is reduced but the text doesn't look faded. E.g. on a dark green header, secondary text is a pale green tint, not a neutral grey.

## Emphasize by de-emphasizing
- If the key element doesn't stand out and adding emphasis doesn't help, soften what competes with it.
  - Active nav item not popping → give inactive items a softer color.
  - Sidebar competing with main content → remove the sidebar's background; let it sit on the page background.

## Labels are a last resort
Applies to displaying data, not form inputs (forms keep their labels).
- `Label: value` formatting gives every datum equal weight and kills hierarchy.
- **Drop the label** when the format or context says what the data is: an email, a phone number, a price, or a job title under a person's name needs no label.
- **Merge label into value** when the value alone is ambiguous: `Seats: 4` → `4 seats left`; `Bathrooms: 2` → `2 bathrooms`. Merged units can be styled freely.
- **Labels needed** (many similar values to scan, e.g. dashboard stats): keep them, but as supporting content: smaller, lower contrast, and/or lighter weight than the value.
- **Emphasize the label** only when users scan for the label, e.g. spec sheets ("Weight", "Battery"). Even then, keep the value readable: label slightly darker, value slightly lighter is enough.

## Visual hierarchy ≠ document hierarchy
- Choose elements for semantics (`h1`–`h6`, `section`, etc.), then style for visual hierarchy. Don't let default heading sizes decide.
- In app UIs, page and section titles often act like labels: supporting, not the focus. Keep them modest; the section's content should dominate.
- A title the content makes obvious can be visually hidden but kept in the markup for accessibility.

## Balancing weight and contrast
Bold reads as emphasized because it covers more surface area. Apply the same logic to any element:
- **Heavy element too loud** (solid icon next to text, thick shapes): you can't thin it, so lower its contrast with a softer color.
- **Light element too faint** (1px border in a soft color): don't darken it, which looks harsh; increase its weight (e.g. 2px) and keep the soft color.

## Action hierarchy (buttons)
- Style actions by importance first, semantics second. Most views have:
  - **One primary action:** obvious, solid high-contrast background.
  - **A few secondary actions:** clear but not prominent: outline or low-contrast background.
  - **Tertiary actions:** discoverable but quiet: link style.
- Multiple solid buttons side by side = no hierarchy.
- **Destructive ≠ big red button.** If deleting/removing isn't the view's primary action, give it secondary or tertiary styling. Put the bold red treatment on the confirmation step, where destroying is the primary action.
