# Critique — `team.html` (Team Members, Northwind Admin)

Reviewed against the Refactoring UI checklist. Issues ranked by visual impact; fixes use the default scales (spacing `4, 8, 12, 16, 24, 32, 48, 64`; type `12, 14, 16, 18, 20, 24, 30`; radius `0, 4, 8, 12, 16, full`; 5-level shadow scale; OKLCH palette).

The basics are already in place: a system font stack, a viewport meta tag, Tailwind-like hex colors, and mostly on-scale spacing (8/12/16/24/32). The problems are in hierarchy, button weight, labels and borders rather than raw polish.

## Issues

- **[impact: high] Four solid primary buttons per screen, and the destructive one is as loud as the rest.** "Invite Member" plus a solid indigo "Edit" on every card all look equally primary. "Remove" is a solid grey block the same size as Edit, so a destructive action gets equal billing on every card. "Filters" and "Export" are also solid grey blocks (`#6c757d`), which makes the toolbar heavy. → Only **Invite member** stays solid (`primary-600`). Filters/Export → secondary: white background, `1px grey-300` border, `grey-700` text, `radius: 8px`. On cards, make the whole card (or the name) open the member. Move Edit/Remove into a `⋯` menu at the card's top right (`32px` icon button, `grey-500` icon), with Remove as `red-700` text inside the menu. Use the red solid style only on the confirmation dialog.

- **[impact: high] The banner is the loudest thing on the page, and its subtitle fails contrast.** A full-width saturated indigo band with a `32px` title is louder than the team itself. The subtitle is grey `#9ca3af` on `#4f46e5`, about 2.5:1 (needs 4.5:1), and grey text on a colored background looks washed out. → Drop the colored band. Put the page header on the page background: title "Team" `24px / 700 / grey-900`, `line-height: 1.25`, and a description `14px / grey-600` capped at `max-width: 60ch`. If you keep the band, use a light tint of the indigo for the subtitle, e.g. `oklch(88% 0.06 277)`, instead of grey.

- **[impact: high] Card details are a `Label: value` list with bold labels louder than the values.** "**Email:** aisha@…", "**Role:** Admin", "**Status:** Active", "**Last active:** 2 hours ago": four rows, each with a divider, where the labels carry the weight. → Let format and context replace the labels:
  - email as a second line under the name (`14px / grey-600`), with the job title after it or merged in ("Engineering Lead · aisha@northwind.io");
  - role as a small badge next to the name (`12px / 700`, padding `2px 8px`, `radius: full`; Admin `primary-100` / `primary-800`, Member `grey-100` / `grey-700`);
  - status and activity merged into one line: a `8px` dot plus "Active · 2 hours ago" / "Away · 3 days ago" (`14px / grey-600`). The text keeps the meaning without relying on color.

  This cuts each card from 4 bordered rows to about 2 lines.

- **[impact: high] Borders everywhere.** There are card borders, a divider under each card header, a divider under every detail row, a bordered stats box and borders on the table rows. The page reads as stacked boxes. → Cards: white on the `grey-50` page with shadow level 1 (`0 1px 3px oklch(0% 0 0 / .12), 0 1px 2px oklch(0% 0 0 / .08)`) and no border. Remove the header divider and the detail-row dividers, and separate them with spacing (`16px` from header to details). In the table, keep only the `1px grey-200` row dividers.

- **[impact: med] The tone and placement of the seat info are wrong.** "Woohoo! 🎉 Your team is growing!" is centered under the toolbar in an admin tool, and the one important fact, **6 of 10 seats used**, is buried in the middle of three lines. "Upgrade anytime from the billing page" isn't a link. → Move seat usage into the header row, aligned to the right: "6 of 10 seats used" (`14px / grey-700`) over a `4px`-tall progress bar (`primary-600` on `grey-200`, `radius: full`), plus an "Upgrade" text link (`primary-700 / 700`) to the billing page. Delete the paragraph.

- **[impact: med] Three content layers with no clear #1.** The banner, a toolbar, a centered paragraph, cards, an untitled table and an empty state all have similar weight. → Order the page as: header (title + seats + Invite) → search/filter row → member grid → a modest "Pending invitations" section. Give the table a title ("Seats by role", `16px / 700`) or fold it into the seat-usage summary. Three rows of role counts rarely need a full table.

- **[impact: med] The grid doesn't respond to screen size, and the content has no max width.** `repeat(3, 1fr)` squeezes three cards into a phone screen. The search field stretches across any viewport. → `grid-template-columns: repeat(auto-fill, minmax(288px, 1fr))`. Wrap the page in `max-width: 1152px; margin: 0 auto; padding: 32px 24px` (`16px` side padding under 640px). Search `max-width: 384px`.

- **[impact: med] Mixed radius styles.** Pill search (`999px`), `4px` buttons, `16px` cards, `8px` stats box, `4px` status badges and a near-square `2px` avatar. → One style: `8px` for inputs/buttons/table container, `12px` for cards, `full` for avatars and badges. A square-ish avatar inside a soft round card looks like a mistake.

- **[impact: med] One line height everywhere (`1.6`), including the 32px title.** This leaves a tall gap in the banner and loose card headers. → Body `1.5`; `14px` meta text `1.43` (20px); headings `1.25`; badges `1`.

- **[impact: med] The empty state is a faint footnote.** "No pending invitations" in `#9ca3af` on `#f9fafb` is about 2.5:1, under a `40px` ✉ glyph in pale indigo, with no action. → A `48px` `primary-100` circle with a `24px primary-600` envelope icon, the title "No pending invitations" `16px / 700 / grey-900`, a line "Invited people appear here until they accept." `14px / grey-600`, and a secondary "Invite member" button. Give the section the heading "Pending invitations".

- **[impact: med] The table's alignment and hierarchy are inverted.** The header (`15px` bold, near-black) is larger than the body (`14px`). Numbers are left-aligned, and "Seats used 10%" is confusing next to "6 of 10 seats". → Header `12px / 700 / uppercase / letter-spacing .05em / grey-600`; right-align the numeric columns with `font-variant-numeric: tabular-nums`; show seats as "1 of 10" or drop the column.

- **[impact: low] Font sizes and greys have drifted.** Sizes used: 13, 14, 15, 16, 32px, where 13/14/15 are near-duplicates and 15 and 13 are off the scale. The cool Tailwind greys sit next to Bootstrap's warmer `#6c757d`. → Use only 12 / 14 / 16 / 24: body `14px` in app chrome and `16px` for names. Define one cool grey ramp (hue ~260) in OKLCH and drop `#6c757d`.

- **[impact: low] The avatar initials are default-looking.** Bold indigo letters on `#c7d2fe`, every avatar the same. → `radius: full`, `40px`, `14px / 700` initials. Rotate tint/text pairs per member (`primary-100/800`, `amber-100/800`, `green-100/800`…) so people are easy to tell apart, and show uploaded photos with `object-fit: cover` and an inner `1px oklch(0% 0 0 / .1)` ring when they exist.

- **[impact: low] Title Case and a bare count in the toolbar.** "Invite Member", "Filters (0)". → Sentence case ("Invite member"). Show the filter count only when it is above 0, as a small badge.

## Top 3 changes

1. **Fix the button hierarchy:** one solid "Invite member"; Filters/Export as secondary; per-card Edit/Remove moved into a `⋯` menu with Remove as red text and a confirmation step.
2. **Rebuild the member card:** name with a role badge, email under the name, a status dot plus "Active · 2 hours ago", a round avatar, and a shadow instead of borders and dividers. It drops from 6 lines with 5 rules to 3 lines with none.
3. **Quiet the shell and surface the real info:** replace the indigo banner with a plain `24px` header, and put "6 of 10 seats used" with a progress bar and an Upgrade link next to Invite. Delete the "Woohoo!" paragraph.

## Beyond visual design

- **Count mismatch:** the page says 6 members, and the table sums to 6, but only 3 cards are shown, with no pagination or "show all".
- **Search input has no label** (placeholder only). Add `<label class="visually-hidden">` or `aria-label="Search members"`.
- **Ambiguous button names:** three "Edit" and three "Remove" buttons with no context for screen readers. Use `aria-label="Edit Aisha Rahman"` etc. Remove also has no confirmation.
- **No landmarks or table semantics:** wrap the banner in `<header>` and the content in `<main>`; give the table a `<caption>` and `<th scope="col">`.
- **Implied feature:** "Upgrade anytime from the billing page" names a destination without linking to it.
