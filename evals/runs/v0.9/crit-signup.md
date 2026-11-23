# Critique — `signup.html` (Create account)

Reviewed against the Refactoring UI checklist. Issues ranked by visual impact; fixes use the default scales (spacing `4, 8, 12, 16, 24, 32, 48, 64`; type `12, 14, 16, 18, 20, 24, 30`; radius `0, 4, 8, 12, 16, full`; 5-level shadow scale; OKLCH palette).

## Issues

- **[impact: high] The primary button is unreadable and looks like a 2003 banner ad.** Yellow text on an orange→red gradient is ~1.5:1 contrast, with a `3px outset` bevel and all-caps "SIGN UP NOW". → Solid `primary-600` (`oklch(52% 0.17 255)`) with white text (~5:1), `16px / 700`, sentence case "Create account", `radius: 8px`, padding `12px 24px`, full width of the form, `1px` lighter top highlight (`inset 0 1px 0 primary-500`) + shadow level 1. Hover `primary-700`; pressed drops the shadow.

- **[impact: high] Two equal-weight solid buttons, and the second one is a dead action.** "Cancel" is the same size and weight as Sign up, painted the page's own blue so it nearly disappears into the background — and there's nothing to cancel back to. → Remove Cancel. Replace it with a tertiary link that does something: "Already have an account? **Log in**" (`14px`, `grey-600` text, link in `primary-700 / 700`) under the button.

- **[impact: high] Shouting headline in a second display font.** `40px` Impact, ALL CAPS, three exclamation marks — on top of a Times New Roman body. Two clashing families, neither suited to UI, and a tone that reads as spam. → One family: system stack (`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`). Headline "Create your account", `30px / 700 / grey-900`, `line-height: 1.2` (`24px` under 640px). Put the real hook in a quieter subline: "Free for 30 days. No credit card required." `18px / 400 / grey-600`.

- **[impact: high] Too many fields for a signup.** First + last name, confirm password, company, and "How did you hear about us?" — seven inputs plus a checkbox before the user sees any value. → Keep three: **Full name**, **Work email**, **Password** (with a Show toggle instead of Confirm password). Ask for company and attribution during onboarding.

- **[impact: high] The form stretches to 90% of the viewport.** On a 1440px screen every input is ~1200px wide; the intro paragraph runs ~180 characters per line. → Form card `max-width: 400px`; paragraphs `max-width: 32rem` (~60ch). On ≥ 880px, add a second column for the value proposition instead of widening the form.

- **[impact: high] Contrast failures throughout.** Intro `#777` on `#eee` ≈ 3.9:1; hints `#999` at 11px ≈ 2.5:1; legal `#aaa` at 10px ≈ 2:1; feature list white on `#4a90d9` at 15px ≈ 3.3:1. → All secondary text `grey-600` (`oklch(46% 0.02 255)`, ≈ 6:1 on white), minimum `14px` for hints, `12px` only for legal fine print and still `grey-600`.

- **[impact: med] Labels outshout the inputs; inputs are cramped.** Labels are `16px bold` with colons; inputs have `3px` padding, a pure-black border, and a `2px` gap to their label. → Labels `14px / 700 / grey-800`, no colon, `8px` above the input. Inputs `16px` text (prevents iOS zoom), padding `12px`, `1px grey-300` border, `radius: 8px`, subtle inset shadow (`inset 0 1px 2px oklch(0% 0 0 / .06)`), focus = `primary-600` border + `3px primary-200` ring.

- **[impact: med] No grouping — field spacing equals everything else.** Rows sit `6px` apart with `9px` label margins, so label↔input and field↔field spacing are nearly identical. → `8px` label → input, `4px` input → hint, `24px` between fields, `32px` before the submit button, `24px` button → "Log in" link.

- **[impact: med] Saturated blue page + grey box + `2px #555` border.** The page background is the loudest surface and the form sits in a hard-bordered grey slab. → Page `grey-50` with a ≤30° tint gradient toward `primary-50`; form on a white card, `radius: 12px`, shadow level 2, padding `32px` (`24px` on mobile), no border.

- **[impact: med] The selling points are buried below the form in low-contrast white text, as a `✔`-separated run-on line.** → Move them beside the form (desktop) / below it (mobile) as a real list: 4 items, each a `24px` `primary-100` circle with a `16px primary-700` check, item text `16px / grey-700`, `12px` between items. Drop vague ones ("24/7 support" stays only if true).

- **[impact: med] Everything is centered, including a 4-line paragraph and justified legal text without hyphenation.** → Left-align all form content and paragraphs; only short headline blocks may center. Never justify the legal text.

- **[impact: med] No spacing or type system.** Spacing values seen: 2, 3, 4, 5, 6, 9, 14, 15, 30, 40px. Font sizes: 10, 11, 14, 15, 16, 17, 22, 40px (14/15, 16/17 are near-duplicates). Colors are ad hoc hex with pure-black borders. → Snap to the scales above; define greys and a primary hue (~255) in OKLCH as tokens; no `#000`.

- **[impact: low] Default checkbox and wordy legal copy.** → Use `accent-color: primary-600`, `16px` box, align the label to the first line. Merge the two consent notes into one line under the button: "By creating an account you agree to our Terms and Privacy Policy." (`12px`, `grey-600`, links underlined).

- **[impact: low] Intro paragraph is a feature dump with `line-height: 1.1`.** → Cut to one sentence (the 30-day/no-card promise) and set body `line-height: 1.5`; headings `1.2`.

## Top 3 changes

1. **One clear primary action:** solid `primary-600` "Create account" button with readable white text; delete Cancel; add a tertiary "Log in" link.
2. **Cut and constrain the form:** 3 fields (name, email, password with Show) in a `400px` white card on a `grey-50` page, with `24px` between fields and `8px` label→input.
3. **One calm type system:** system sans only, `30px` sentence-case headline, `18px` grey subline, all secondary text `grey-600` ≥ 4.5:1, left-aligned.

## Beyond visual design

- **No `<meta name="viewport">`** — the page renders zoomed-out on phones. Add `width=device-width, initial-scale=1`.
- **Labels aren't associated with inputs** (no `for`/`id`, checkbox has no `<label>`), and there's **no `<form>`, `name`, `autocomplete`, or `required`** — screen readers can't name fields, password managers can't fill them, and the button submits nothing.
- **No landmarks or `lang`** — wrap content in `<main>`, add `<html lang="en">`.
- **Marketing consent is implied, not asked.** "By creating an account you agree to receive marketing communications" bundles consent into signup; make it an unchecked, optional opt-in checkbox.
- **Terms of Service / Privacy Policy aren't links**, so the user is asked to agree to documents they can't open.
