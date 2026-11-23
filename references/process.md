# Process: starting a design

## Contents
- Feature first, shell last
- Hierarchy before color
- Scope: smallest useful version, no implied features
- Personality: decide it, then apply it consistently
- Systems: constrain every value
- Choosing between scale values

## Feature first, shell last
- An app is a set of features. Design the feature the user actually came for (the form, the table, the result list) before nav, header, sidebar, footer, or logo placement.
- Shell decisions need information from several features; make them last and keep them minimal. If the page works without a piece of shell, leave it out.
- Generate: list the elements the core task needs (fields, actions, data shown), build those first, then add only the shell the request asks for.
- Critique: if the shell is louder or more elaborate than the core feature, flag it.

## Hierarchy before color
- Establish hierarchy with size, weight, spacing, and contrast first; add color last, as enhancement.
- Test: in grayscale, is the most important element still the most prominent? Is grouping still obvious? If hierarchy depends on hue, it is weak.
- Generate: lay out the page with greys only in your head (or a first pass), then apply the palette.
- Critique: mentally desaturate the UI. Any element that only stands out because of its color is a hierarchy issue.

## Scope: smallest useful version, no implied features
- Ship the smallest useful version of a feature; design nice-to-haves later.
- Never show UI for functionality that does not exist or is out of scope: no attachment slot on a comment box that can't attach, no bulk-action button without row selection, no filter chip with no filter behind it.
- Don't design every edge case up front, but do handle the obvious states the feature will hit (empty, error, long content) at the level the request implies.
- Generate: every control on the page must be backed by in-scope behavior. Don't add sections the user didn't ask for to look complete.
- Critique: flag controls, copy, or empty states that promise something the page cannot do.

## Personality: decide it, then apply it consistently
Pick a personality from the audience (e.g. serious/trustworthy, neutral, playful, premium) before choosing values. Four levers carry most of it:

| Lever | Formal / classic | Neutral | Playful |
|---|---|---|---|
| Typeface | serif | neutral sans | rounded sans |
| Border radius | none | small | large |
| Color | blue = safe, familiar; gold = premium; pink = fun (go with how it feels to the audience) | | |
| Copy tone | impersonal, official | plain | casual, friendly |

- Language is part of the design: wording sets tone as much as color or type does.
- Unsure of the personality? Match what the target audience already uses, but don't copy a direct competitor's look.
- Consistency beats choice: one radius style across the UI (don't mix square and rounded corners); one tone of voice.
- Generate: state the chosen personality in one line, then let it drive typeface, radius, accent color, and copy.
- Critique: flag mixed signals (rounded buttons with square cards, playful copy on a formal layout, competing typefaces).

## Systems: constrain every value
- Never pick values ad hoc. Define small sets up front and only use those.
- Systematize: font size, font weight, line height, color (8–10 shades per hue), margin, padding, width, height, box shadow, border radius, border width, opacity.
- Values in a scale must be visibly different from their neighbours; near-duplicates (12px vs 13px, 10% vs 15% shadow) are a sign of no system.
- When a new kind of decision comes up, add it to the system instead of solving it once.
- Default sets where the book gives none (adjust to the personality, but keep the set small):
  - **Radius:** `0, 4, 8, 12, 16, full (9999px)`. Formal → 0–4; neutral → 4–8; playful → 12–16. Pills and avatars use full.
  - **Border width:** `1, 2, 4` px (4 mainly for accent borders).
  - **Opacity:** `.5` disabled, `.7` muted overlays/scrims, `1`. Don't use opacity to de-emphasize text (see `hierarchy.md`).
  - Font size, spacing, color, and shadow scales live in their own files.
- Generate: declare these scales as tokens/variables before writing components; no literal values outside the scales.
- Critique: count distinct values per property. Many near-identical values = no system; the fix is a scale, not individual tweaks.

## Choosing between scale values
Process of elimination: guess the middle option, compare with its neighbours on the scale. If both neighbours look worse, keep it. If one looks better, repeat with that one as the new middle.
