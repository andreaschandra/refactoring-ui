# Answer key: planted issues in fixtures

Used to score critique runs: count how many planted issues each run catches. Never copy this file into a run folder.

## team.html (subtle: looks fine at first glance)
| # | Issue | Chapter |
|---|---|---|
| 1 | Grey text (`#9ca3af`) on the indigo banner: low contrast, should be a lighter tint of the background hue | hierarchy (ch2) |
| 2 | Heading line-height 1.6, same as body; large text needs tighter line-height | typography |
| 3 | Banner subtitle has no max-width: very long line length | typography |
| 4 | Spacing inside groups = spacing between groups (24px everywhere): grouping is ambiguous | layout & spacing |
| 5 | Borders used for every separation (card border + header divider + per-row dividers + table rows) | depth / layout |
| 6 | "Label: value" pairs (Email:, Role:, Status:) where the format makes labels unnecessary | hierarchy (ch2) |
| 7 | Two filled buttons per card with equal weight; "Remove" (destructive) styled as a neutral filled button | hierarchy (ch2) |
| 8 | Three filled buttons in the toolbar; secondary actions not de-emphasized | hierarchy (ch2) |
| 9 | "Filters (0)" with no filter UI: implied feature | process (ch1) |
| 10 | Mixed radius: pill search, 4px buttons, 16px cards, 8px table, 2px avatar | process (ch1) |
| 11 | Mixed personality: playful copy ("Woohoo! 🎉") in a formal admin tool | process (ch1) |
| 12 | Near-duplicate values: font sizes 13/14/15/16, two different greys (`#6b7280`, `#6c757d`) from different palettes | process (ch1) |
| 13 | Long centered paragraph (intro) | typography |
| 14 | Icon scaled up to 40px as a font glyph (blurry/clunky); weak empty state | images / finishing |
| 15 | Numeric columns left-aligned | typography |
| 16 | Table header (15px) larger than its cells (14px) but no other emphasis cue; flat hierarchy | hierarchy (ch2) |

## dashboard.html / signup.html (obvious)
Planted: arbitrary spacing, many font sizes, everything bold, heavy borders + hard shadows, grey text on color, too many equal buttons, unnecessary labels, long centered text, mixed fonts (signup), all-caps shouting (signup).
