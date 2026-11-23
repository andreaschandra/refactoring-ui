# UI Critique: `dashboard.html` (Sales Dashboard)

**Overall:** The content is right for a sales dashboard: KPIs, recent orders, top products. The visual design works against it. Everything is bold, bordered or shadowed, so nothing stands out. The KPI numbers, which matter most, are styled almost exactly like their labels. There are also some functional gaps: a "Delete Selected" button with nothing to select, and an empty state that mentions a date range the page doesn't have.

Priorities: **P1** fix first (broken or misleading), **P2** big clarity win, **P3** polish.

---

## P1: Broken or misleading

### 1. The empty state mentions a date range control that doesn't exist
"No data available for the selected period. Please select a different date range…" There is no date picker anywhere on the page. The KPI changes (`+12.4%`) also don't say what they're compared against.
**Fix:** Add one date-range control at the top of the content (e.g. "Last 30 days ▾"). It gives the empty state something to point to and the KPIs a baseline. Label the changes, e.g. `+12.4% vs previous 30 days`.

### 2. "Delete Selected" can't select anything
The table has no checkboxes or row selection, so the button can't work. It also sits in the same row as Refresh and Print and looks the same as them, which makes a destructive bulk action easy to hit by accident.
**Fix:** Either add a checkbox column and show bulk actions only when rows are selected, or remove the button. Give destructive actions their own style (red text or outline) and a confirmation step.

### 3. Some text fails contrast badly
| Element | Colors | Ratio | WCAG AA needs |
|---|---|---|---|
| Welcome / last-login text in header | `#888` on `#3b5998` | **~1.9:1** | 4.5:1 |
| Empty-state message | `#bbb` on `#fff`, 12px | **~1.9:1** | 4.5:1 |
| Negative change (`-2.0%`) | `red` on `#fff`, 14px bold | ~4.0:1 | 4.5:1 |

The empty state is the only content in its section, but it's the faintest text on the page.
**Fix:** Use white or near-white (`rgba(255,255,255,.8)`) on the blue header. Use about `#666` or darker for secondary text. Use a darker red such as `#c62828`.

### 4. Positive and negative are shown by color alone
Green vs red is the only difference between `+12.4%` and `-2.0%`, which fails for colour-blind users.
**Fix:** Add ▲/▼ arrows next to the sign and color.

---

## P2: Hierarchy and clarity

### 5. KPI hierarchy is backwards
The labels are 18px bold `#333` and the values are 19px bold `#000`, so the numbers barely stand out from their labels.
**Fix:** Make the value the dominant element (28–32px, semibold, `font-variant-numeric: tabular-nums`). Make the label small and quiet (13px, regular, muted gray, sentence case, no trailing colon). Left-align the card content instead of centering it. Drop the cents on the headline figure (`$48,291`).

### 6. Too much is bold or boxed
- `box-shadow: 4px 4px 8px #000` on cards is a hard black shadow that looks dated and heavy.
- `border-bottom: 3px solid #000` on the header and `2px solid #000` on every button.
- Borders on the nav, on each section, and on every table cell, so the table sits inside a box inside a box.
- Nearly every text style has `font-weight: bold`. When everything is bold, bold stops signalling anything.

**Fix:** Pick one way to separate content. Either white cards on a light gray page (`#f5f6f8`) with a 1px `#e3e5e8` border or a soft shadow (`0 1px 2px rgba(0,0,0,.06)`), or plain whitespace. Keep bold for headings and KPI values.

### 7. Five equal buttons and fifteen row buttons
The toolbar has Export CSV, Print, Refresh, Delete Selected and New Order, all with the same style. Each table row adds View, Edit and Delete, so four rows already have 12 buttons, and the count grows with every row.
**Fix:**
- **New Order** becomes the single primary button, placed top right of the section.
- Export and Print become secondary or ghost buttons, or go into an "Export ▾" menu. Refresh can be an icon button, or dropped if the data refreshes on its own.
- Make each row clickable to view the order. Put Edit and Delete in a `⋯` menu at the end of the row.

### 8. Table alignment and status
- Every cell is centered. Left-align text columns and right-align **Amount** with tabular numerals so the decimal points line up.
- Status is plain text. Use small colored badges (Shipped = green, Pending = amber, Cancelled = gray), each with a text label so they don't rely on color alone.
- Padding is cramped (`4px`). Use about `10px 12px` and drop the vertical cell borders, keeping only thin row dividers.
- Add a "View all orders →" link under the table.

### 9. The nav doesn't show where you are
The links use default `blue`, all bold, with no active state. Settings, Help and Logout sit in the same row as the main sections.
**Fix:** Give the current page a clear active style (underline, bold or background, plus `aria-current="page"`). Move Settings, Help and Logout into a user menu at the top right of the header. Use neutral link colors on a quiet nav bar.

### 10. Header copy
- "SalesTracker Pro Dashboard": the nav already says Dashboard. Use the product name alone, or "Dashboard" as the page title.
- A last-login time down to the second (`09:14:33`) is noise. Drop it or shorten it ("Last login yesterday"). "Welcome back, John" can go in the user menu.
- `#3b5998` is Facebook's old brand blue, so it reads as borrowed. Pick your own accent color.

### 11. No trends
A dashboard with no chart shows only the current numbers, not how they got there. Add a revenue-over-time line chart for the selected period, or at least a sparkline in each KPI card.

---

## P3: System and polish

### 12. No type or spacing scale
There are 8 font sizes (12, 13, 14, 15, 18, 19, 21, 26) and arbitrary spacing values (3, 5, 7, 9, 10, 11, 12, 13, 14, 17 px). Sizes that close together look like mistakes rather than choices.
**Fix:** Define tokens and use them everywhere:
```css
:root {
  /* type */
  --fs-xs: 12px; --fs-sm: 13px; --fs-base: 14px; --fs-lg: 18px; --fs-xl: 24px; --fs-kpi: 30px;
  /* space (4px grid) */
  --s-1: 4px; --s-2: 8px; --s-3: 12px; --s-4: 16px; --s-6: 24px; --s-8: 32px;
  /* color */
  --bg: #f5f6f8; --surface: #fff; --border: #e3e5e8;
  --text: #1a1d21; --text-muted: #5f6670;
  --accent: #2f5bea; --pos: #1e7a34; --neg: #c62828;
}
```
Use a system font stack (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`) instead of Arial.

### 13. Mobile and responsiveness
There's no `<meta name="viewport">`. The four KPI cards sit in a flex row that never wraps, and the 6-column table will overflow on a phone.
**Fix:** Add the viewport meta. Lay out the cards with `grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))`. Wrap the table in a horizontally scrollable container, or turn rows into stacked cards under about 640px.

### 14. Semantics and accessibility
- Add `lang="en"` on `<html>`.
- Use `<header>`, `<nav>` and `<main>` instead of plain divs. Put the table header row in `<thead>` with `scope="col"`.
- Row buttons all read "View", "Edit", "Delete" to a screen reader. Add context, e.g. `aria-label="Delete order #10482"`.
- Give buttons `type="button"` and visible `:focus-visible` styles.
- Use `<time datetime="…">` for dates. Consider a friendlier display format ("Nov 22") in the table.

### 15. Empty state design
Beyond the contrast fix (#3), make it a short, centered block: a short heading ("No product sales in this period"), one line of help, and a "Change date range" button. Cut the "contact support if you believe this is an error" line.

---

## Suggested order of work
1. Add a date range control and label the KPI changes (#1). Fix contrast and color-only signals (#3, #4).
2. Fix the bulk-delete flow (#2) and button hierarchy (#7).
3. Rework the KPI cards (#5) and remove most borders, shadows and bold (#6).
4. Clean up the table (#8), nav (#9) and header (#10).
5. Add tokens (#12), responsiveness (#13) and semantics (#14), then a trend chart (#11).
