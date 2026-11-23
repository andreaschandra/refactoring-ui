# Critique: dashboard.html

Reviewed against the full refactoring-ui checklist. The main problem is that **everything is bold, bordered and the same size**, so nothing reads as the #1 element. The KPI values should be the focus, but they are 19px, only 1px bigger than their own labels. The shell (blue header, black rule, bold nav) and 23 identical solid buttons are louder than the data. In grayscale, the black card shadows and the header bar are the most prominent things on the page.

## Issues, ranked by visual impact

### High

- **[impact: high] KPI cards have no hierarchy.** The label (18px bold #333) and value (19px bold #000) are almost identical, the labels end in colons (`Total Revenue:`), and everything is centered. → Make the value the hero and the label supporting content: label 14px / 400 / grey-600, no colon, above the value. Value 30px / 700 / grey-900 with `font-variant-numeric: tabular-nums`. Left-align the card contents and drop the `.00` from `$48,291`.
- **[impact: high] Button soup with no action hierarchy.** There are 5 toolbar buttons plus 3 per row, all solid brand blue with a 2px black border. → Make **New Order** the one primary action (solid primary-600, white text, 8px 16px padding) and move it to the right of the section title. Export CSV becomes secondary (outline: 1px grey-300 border, grey-800 text). Print and Refresh become tertiary icon or link buttons, or are removed (the browser already prints and reloads). In each row, make the order ID a link to View and put Edit and Delete in a quiet `⋯` overflow menu. Delete stays out of the red style until the confirmation dialog.
- **[impact: high] Implied features.** "Delete Selected" appears without row checkboxes. The empty state says "for the selected period" and "select a different date range", but the page has no date picker. The `+12.4%` deltas don't say what they compare against. → Remove "Delete Selected" (or add a checkbox column and show the bulk bar only when rows are selected). Add a real period selector (e.g. "Last 30 days ▾") at the top right of the content area, or drop the date-range wording. Add context under each delta: "vs previous 30 days".
- **[impact: high] Harsh depth and borders everywhere.** The cards use `box-shadow: 4px 4px 8px #000`. The header has a 3px black rule. Cards, sections, nav, table cells and buttons each have their own grey or black border (#999, #ccc, #aaa, #000). → Use one shadow scale, e.g. `sm: 0 1px 2px oklch(0% 0 0 / .06), 0 1px 3px oklch(0% 0 0 / .10)`, for cards. Remove the black header rule and the nav and section boxes, and separate them with space instead. In the table, keep only horizontal 1px grey-200 row dividers (no vertical cell borders).
- **[impact: high] The shell outshouts the content.** The h1 "SalesTracker Pro Dashboard" is 26px bold on a solid brand bar, larger than any data on the page. → Make the header a white or grey-50 bar with the product name at 18px/700 and the nav inline on the right. Give the page its own modest title ("Overview", 24px/700) above the KPIs. Remove the "Welcome back… Last login: 2026-11-22 09:14:33" line, or move it to a user menu with a friendly format ("Last login yesterday, 9:14").

### Medium

- **[impact: med] Failing contrast.**
  - Header subtitle: #888 on #3b5998 ≈ 2.0:1, which is grey text on a colored background.
  - Empty state: #bbb on white ≈ 1.9:1.
  - Negative delta: #f00 on white ≈ 4.0:1 at 14px.

  → Meet 4.5:1 everywhere. On a colored header, use a light tint of the header hue (e.g. `oklch(88% 0.04 265)`), not grey. Use grey-600 for empty-state text, and red-700 (`oklch(50% 0.19 27)`) or a red-100 badge with red-800 text for negatives.
- **[impact: med] Color is the only signal for deltas.** Green and red carry the meaning. → Add arrows (`▲ 12.4%`, `▼ 2.0%`) and show them as flipped-contrast pills: green-100 background with green-800 text, and red-100 with red-800, 12px/600, 4px 8px padding, 9999px or 4px radius.
- **[impact: med] Nav has no active state and everything competes.** Eight bold, default-blue links, with Logout and Help mixed in with the destinations. → Make links 14px/500 grey-600. Mark the active item with grey-900 plus a 2px primary-600 underline or a primary-50 pill. Move Help and Logout into a user menu on the right.
- **[impact: med] The table is hard to scan.** Every cell is centered, Amount isn't right-aligned, padding is 4px, and the column headers sit on a #ddd fill with bold text. → Left-align text columns and right-align Amount with `tabular-nums`. Use cell padding of 12px 16px. Headers: 12px/600 uppercase, `letter-spacing: .05em`, grey-500, no background fill. Show Status as a pill (Shipped = green-100/green-800, Pending = amber-100/amber-800, Cancelled = grey-100/grey-700). Write dates as "Nov 22" in grey-600.
- **[impact: med] No spacing system, and the grouping is ambiguous.** Padding and margin values include 13/17, 7, 11, 10, 5, 9, 14, 4, 12, 8, 3/10, 6/12 and 2. The card gap (10px) is about the same as the card padding (9px), and section padding is 8px. → Use only `4, 8, 12, 16, 24, 32, 48, 64`. Page gutter 32px, card padding 24px, gap between cards 24px, gap between sections 48px. Put 32px above section titles and 16px below them, so space around groups is larger than space within them.
- **[impact: med] No type scale, and every weight is bold.** Sizes in use are 26, 21, 19, 18, 15, 14, 13 and 12 (several are near-duplicates and off-scale). → Use `12, 14, 16, 18, 20, 24, 30` and only two weights (400 and 600/700). Section titles ("Recent Orders", "Top Products") should be 18px/600, smaller than the KPI values, because in an app UI they act as labels.
- **[impact: med] The empty state is fine print.** It is 12px light grey with two long sentences that blame the user. → Center it in a 128px-tall area: one line at 16px grey-700 ("No product sales in the last 30 days"), a 14px grey-500 hint below, and an optional link-style "Change period" action (only if the period selector exists).
- **[impact: med] Colors are ad hoc.** The page uses pure #000 text, #3b5998, `blue`, `green`, `red` and five unrelated greys. → Define tokens in OKLCH: 9 cool greys (e.g. grey-900 `oklch(21% 0.02 260)` down to grey-50 `oklch(98% 0.005 260)`), a primary hue with 100 to 900 shades (500 ≈ `oklch(55% 0.17 265)`), and green, amber and red at 100, 700 and 800. Use nothing outside these.

### Low

- **[impact: low] Generic typeface.** → Swap Arial for the system stack (`-apple-system, "Segoe UI", Roboto, "Noto Sans", sans-serif`) or Inter, and set body text to 14 or 16px.
- **[impact: low] Line height isn't set.** → Body 1.5, KPI values and titles 1.2.
- **[impact: low] The layout stretches indefinitely on wide screens.** → Wrap the content in `max-width: 1280px; margin: 0 auto`. Lay out the KPI cards with `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` so they wrap to 2×2 and then 1 column on narrow screens.
- **[impact: low] Radius and personality are undecided.** Everything has square browser defaults. → Pick "neutral/professional": 6px radius on cards, buttons and inputs, and 9999px on status and delta pills. Use plain copy ("Recent orders", not "SalesTracker Pro Dashboard").

## The 3 changes that would improve it most

1. **Rebuild the KPI cards around the number.** Use a 30px/700 value, a 14px grey-600 label without the colon, a left-aligned layout, and an arrowed, tinted delta pill with a "vs previous 30 days" note. This gives the page a clear #1 element.
2. **Collapse the 23 buttons into a real action hierarchy.** Keep one primary "New Order", one secondary "Export CSV", and per-row actions in an overflow menu. Delete the fake "Delete Selected" and the unused Print and Refresh buttons.
3. **Remove the noise and put a system behind it.** Remove the black shadows, black rules and per-cell borders. Then apply one spacing scale (24px card padding, 48px between sections), one type scale with two weights, and an OKLCH grey and primary palette. This also quiets the header and nav so the data leads.
