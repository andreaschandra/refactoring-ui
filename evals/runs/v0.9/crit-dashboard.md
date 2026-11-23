# Critique — `dashboard.html` (Sales Dashboard)

Reviewed against the Refactoring UI checklist. Issues ranked by visual impact; fixes use the default scales (spacing `4, 8, 12, 16, 24, 32, 48, 64`; type `12, 14, 16, 18, 20, 24, 30, 36`; radius `0, 4, 8, 12, 16, full`; 5-level shadow scale).

## Issues

- **[impact: high] Stat cards have no hierarchy — the label (18px bold) is as loud as the number (19px bold).** The value is the #1 element on the page and it barely beats its own label. → Value `30px / 700 / grey-900`, `line-height: 1.2`; label `14px / 400 / grey-600`, no trailing colon ("Total Revenue" not "Total Revenue:"); change `14px / 700`. Left-align card content instead of centering. Drop the `.00` from `$48,291`.

- **[impact: high] Heavy black drop shadow on every card (`4px 4px 8px #000`).** It's the darkest thing on the page, off any scale, and lit from the top-left instead of above. → Elevation level 2: `0 4px 6px oklch(0% 0 0 / .1), 0 2px 4px oklch(0% 0 0 / .06)`, remove the `1px solid #999` border, add `border-radius: 8px` and a white card on a `grey-50` page background (`oklch(98.5% 0.003 250)`).

- **[impact: high] Five equal-weight solid buttons above the table, plus three more per row.** 17 identical dark-blue buttons with black 2px borders; nothing is primary, and "Delete Selected" looks exactly like "New Order". → One primary: **New Order**, solid `primary-600`, right-aligned in the section header. Export CSV / Print / Refresh → secondary (white bg, `1px grey-300` border, `grey-700` text) or icon buttons. Delete Selected → tertiary text button in `red-700`, shown only when rows are selected (there are no checkboxes, so it's currently a dead action). Row actions: make the order ID the "View" link, move Edit/Delete into a `⋯` menu or reveal on row hover.

- **[impact: high] Borders everywhere: header bottom (3px black), nav box, every section, every card, every table cell.** The page reads as a grid of boxes, not grouped content. → Remove section and nav borders; separate with space (`32px` between sections) and background (white cards on `grey-50`). Table: drop vertical cell borders, keep only `1px grey-200` row dividers; header row with no fill, `12px / 700 / uppercase / letter-spacing .05em / grey-600`.

- **[impact: high] Header text fails contrast.** `#888` on `#3b5998` is ~2:1 (needs 4.5:1). → Use a light tint of the header hue, e.g. `oklch(85% 0.05 265)`, or move the welcome text out of the header. Also trim it: drop "Last login: …09:14:33" or show it as "Last login yesterday" in a quieter spot.

- **[impact: med] Shell is louder than the content.** 26px bold "SalesTracker Pro Dashboard" in a saturated bar, and 8 bold 15px pure-`blue` nav links all compete with the KPIs. → Logo/product name `18px / 700`; nav links `14px / 500-ish (or 400) / grey-600`, active item `grey-900` + `2px primary-600` underline; move Logout (and Settings/Help) to a user menu on the right. Header height via padding `12px 24px`.

- **[impact: med] No spacing or type system.** Spacing values seen: 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 17px. Font sizes: 12, 13, 14, 15, 18, 19, 21, 26px (18 vs 19, 13 vs 14 are near-duplicates). → Snap to the scales above: page gutter `24px`, card padding `24px`, gap between cards `24px`, section title → content `16px`, table cell padding `12px 16px`. Type: 12 / 14 / 16 / 18 / 30 only.

- **[impact: med] Table alignment.** Everything is centered; amounts don't line up. → Left-align text columns, right-align Amount with `font-variant-numeric: tabular-nums`; right-align the Actions column. Format dates as "Nov 22" (year is implied).

- **[impact: med] Status is plain text and change % is color-only.** Shipped/Pending/Cancelled are indistinguishable at a glance; `+12.4%` vs `-2.0%` relies on green/red, and pure `red` on white is ~4:1 (fails at 14px). → Status pills: `12px / 700`, padding `2px 8px`, `radius: full`, flipped contrast (Shipped `green-100` bg / `green-800` text; Pending `amber-100` / `amber-800`; Cancelled `grey-100` / `grey-700`). Change: add ▲/▼ icons and use `green-700` / `red-700`, plus context ("vs last month").

- **[impact: med] Empty state is an apologetic light-grey footnote.** `#bbb` at 12px is ~1.9:1 contrast and the copy blames the user. There's also no date-range control on the page, so "select a different date range" is an implied feature. → Center a small icon (`48px` in a `grey-100` circle), headline `16px / 700 / grey-900` "No product sales yet this period", one line `14px / grey-600`, and a secondary button that actually changes the range — or add the date-range picker to the page header so the advice is actionable.

- **[impact: med] Colors are ad hoc hex values with pure black.** `#000` text, black borders, `blue` links, `green`, `red`, `#3b5998`. → Define an OKLCH palette: 9 cool greys (e.g. `grey-900 oklch(22% 0.02 260)` → `grey-50 oklch(98.5% 0.003 250)`), primary hue ~265 with 100–900 shades, and green/amber/red semantic shades. Body text `grey-900`, never `#000`.

- **[impact: low] Content stretches full width.** The table and cards span any viewport. → Wrap content in `max-width: 1280px; margin: 0 auto; padding: 0 24px`.

- **[impact: low] Arial for a data-heavy UI.** Workable, but few weights and no tabular figures by default. → System stack (`system-ui, -apple-system, "Segoe UI", sans-serif`) or Inter, with `tabular-nums` on numbers. Line height: `1.5` body, `1.2` for the 30px values.

- **[impact: low] Section titles at 21px bold are oversized for an app UI.** → `18px / 700 / grey-900`; put the section's actions on the same row (flex, space-between).

## Top 3 changes

1. **Fix the KPI cards:** big 30px values, small grey 14px labels without colons, left-aligned, level-2 shadow instead of the black drop shadow, no border.
2. **Collapse the button wall:** one primary "New Order", secondary/icon buttons for Export/Print/Refresh, row actions behind the order link + a `⋯` menu, destructive actions tertiary.
3. **Replace borders with space and background:** `grey-50` page, white rounded sections, row-divider-only table with right-aligned tabular amounts and status pills — all on the 4/8/12/16/24/32 spacing scale.

## Beyond visual design

- **Missing viewport meta** — add `<meta name="viewport" content="width=device-width, initial-scale=1">`; the 4-up flex cards and 6-column table will also need a stacked/scrolling layout below ~640px.
- **No landmarks** — use `<header>`, `<nav aria-label="Main">`, `<main>`, and `<section aria-labelledby>`; mark the current page with `aria-current="page"`. Also add `lang="en"` to `<html>`.
- **Ambiguous row buttons** — 4× "View / Edit / Delete" with no context for screen readers; add `aria-label="Delete order #10482"` (or visually hidden text). Table needs `<thead>`/`<tbody>` and `scope="col"` on headers.
- **Dead/unsafe flows** — "Delete Selected" has no row selection; per-row Delete has no confirmation step; nav links all point to `#`.
- **Focus styles** — custom buttons with `2px solid #000` borders need a visible `:focus-visible` ring (e.g. `outline: 2px solid primary-500; outline-offset: 2px`).
