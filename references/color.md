# Color

## Contents
- Use HSL
- Palette size: what you actually need
- Building shade scales (100–900)
- Saturation at the extremes
- Changing brightness by rotating hue
- Tinted greys (temperature)
- Accessible contrast without ugliness
- Never rely on color alone

## Use HSL
- Write colors as `hsl()`, not hex/RGB. In hex, related colors look unrelated; HSL exposes what the eye perceives:
  - **Hue** (0–360°): position on the wheel. 0° red, 120° green, 240° blue.
  - **Saturation** (0–100%): 0% is grey (hue irrelevant), 100% is vivid.
  - **Lightness** (0–100%): 0% black, 100% white, 50% the pure hue.
- HSL ≠ HSB (design tools use HSB). In HSB, 100% brightness is only white at 0% saturation. Browsers take HSL, so specify HSL for the web.

## Palette size: what you actually need
A 5-color generated palette can't build a real UI. A complete palette has three groups:
- **Greys: 8–10 shades.** Text, backgrounds, panels, and form controls are mostly grey. Don't use pure black; start at a very dark grey and step evenly to near-white.
- **Primary: 1–2 hues × 5–10 shades.** Used for primary actions, active nav, etc. These define the brand look. Ultra-light shades tint backgrounds (alerts); dark shades work for text.
- **Accents: several hues × several shades.** For highlighting (a new feature) and semantic states: red = destructive/error, yellow/amber = warning, green = success/positive. Use them sparingly. Data-heavy UIs (charts, calendars, tags) may need more.
- A complex UI can reasonably need ~10 hues × 5–10 shades.

## Building shade scales (100–900)
- Define every shade up front. Never generate shades on the fly (`lighten()`, `darken()`, `color-mix()` at use sites); that yields dozens of near-identical variants.
- Per hue, 9 shades named 100 (lightest) to 900 (darkest):
  1. **500 = base:** for primary/accent hues, a shade that works as a button background. Choose by eye; no fixed lightness rule.
  2. **900 and 100 = edges:** 900 for text in that hue, 100 for a tinted background. A colored alert (tinted background + dark text in the same hue) is a good test for both.
  3. **Fill 700 and 300** as the midpoints between their neighbours, **then 800, 600, 400, 200** the same way.
- Greys: same process. 900 = darkest text color, 100 = subtle off-white background.
- Tweak individual shades by eye once used in context, but avoid adding new shades; an ever-growing palette is no system.

## Saturation at the extremes
- Saturation looks weaker as lightness moves away from 50%. Raise saturation for lighter and darker shades so they don't look washed out. This matters most for colors covering large areas.

## Changing brightness by rotating hue
- Hues have different inherent perceived brightness. Perceived brightness = `√(0.299r² + 0.587g² + 0.114b²) / 255`. Local maxima: yellow 60°, cyan 180°, magenta 300°. Local minima: red 0°, green 120°, blue 240°.
- Changing only lightness pushes a color toward white/black and loses intensity. Alternative or complement:
  - Lighter: rotate hue **toward** 60°, 180°, or 300° (whichever is nearest).
  - Darker: rotate hue **toward** 0°, 120°, or 240°.
- Keep rotation to **≤ 20–30°**, or it reads as a different color.
- Typical use: yellow scales. Shift darker shades toward orange so they look rich and warm instead of muddy brown.

## Tinted greys (temperature)
- Greys don't need 0% saturation. A little blue makes them cool; a little yellow/orange makes them warm. Pick the amount to taste: slight for a hint, more for a strong lean.
- Like other hues, raise saturation for the lightest and darkest greys to keep the temperature consistent.
- Match grey temperature to the personality chosen in `process.md`.

## Accessible contrast without ugliness
- WCAG: normal text (under ~18px) needs ≥ 4.5:1 contrast; larger text ≥ 3:1.
- **White text on color** often needs a very dark background to pass, which then shouts for attention. If the element isn't meant to be the focus, **flip the contrast**: dark colored text on a light tint of the same hue (e.g. 800 text on 100 background).
- **Colored secondary text on a dark colored panel:** adjusting lightness alone pushes it toward white. Instead, rotate the hue toward a brighter hue (cyan, magenta, yellow) to gain contrast while staying colorful.

## Never rely on color alone
- Color must reinforce information that's already conveyed another way; it can't be the only channel (color-blind users).
- Up/down changes: add an icon or arrow, not just green/red.
- Multi-series charts: differ series by **contrast** (light vs dark) more than by distinct hues; light/dark differences are easier to tell apart than hue differences.
