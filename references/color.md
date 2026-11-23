# Color

## Contents
- Use OKLCH
- Palette size: what you actually need
- Building shade scales (100–900)
- Saturation at the extremes
- Changing brightness by rotating hue
- Tinted greys (temperature)
- Accessible contrast without ugliness
- Never rely on color alone

## Use OKLCH
- Write colors as `oklch(L C H)`, not hex/RGB/HSL. In hex, related colors look unrelated; OKLCH exposes what the eye perceives, and unlike HSL its lightness is **perceptually uniform**:
  - **L (lightness, 0–100%):** equal L looks equally light across hues (in HSL, yellow and blue at 50% look very different).
  - **C (chroma, 0 to ~0.37):** colorfulness; 0 is grey (hue irrelevant). Practical values in sRGB are much lower and depend on L and H.
  - **H (hue, 0–360°):** angles differ from HSL. Don't reuse HSL hue numbers; pick hues by eye in an OKLCH picker (e.g. oklch.com).
- Supported in all major browsers since 2023; no fallback needed for modern targets.
- **Gamut:** high chroma easily exceeds sRGB, especially at very light/dark L; the browser then clamps it unpredictably. Keep each shade's chroma inside sRGB unless deliberately targeting wide-gamut (P3) displays.
- The book's HSL techniques below are kept as the reasoning: OKLCH solves some of their problems directly, and the notes say how.

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
  - In OKLCH, give the same shade number roughly the same L across hues (e.g. every 500 near the same L), then tune by eye. This keeps hues interchangeable in components.
  2. **900 and 100 = edges:** 900 for text in that hue, 100 for a tinted background. A colored alert (tinted background + dark text in the same hue) is a good test for both.
  3. **Fill 700 and 300** as the midpoints between their neighbours, **then 800, 600, 400, 200** the same way.
- Greys: same process. 900 = darkest text color, 100 = subtle off-white background.
- Tweak individual shades by eye once used in context, but avoid adding new shades; an ever-growing palette is no system.

## Saturation at the extremes
- Book (HSL): saturation looks weaker as lightness moves away from 50%, so raise saturation for lighter and darker shades or they look washed out.
- OKLCH: chroma is perceptual, so equal C already looks equally colorful; the limit is the gamut, which shrinks near the light and dark ends. Keep chroma as high as the gamut allows at the extremes so tints don't fade to grey; lower it only where the gamut forces you. Matters most for colors covering large areas.

## Changing brightness by rotating hue
- Book (HSL): hues have different inherent perceived brightness (formula `√(0.299r² + 0.587g² + 0.114b²) / 255`; local maxima yellow/cyan/magenta, minima red/green/blue). In HSL, changing only lightness pushes a color toward white/black and loses intensity, so shift hue toward a brighter hue to lighten and a darker hue to darken.
- OKLCH: L already accounts for hue brightness, so change **L** for lighter/darker. Hue shifts remain useful for character, not brightness:
  - Yellow and other light hues: shift darker shades a little toward orange so they look rich and warm instead of muddy olive/brown.
  - Keep any hue shift across a scale to **≤ 20–30°**, or it reads as a different color.

## Tinted greys (temperature)
- Greys don't need zero chroma (0% saturation). A little blue makes them cool; a little yellow/orange makes them warm. Pick the amount to taste: slight for a hint, more for a strong lean.
- Typical grey chroma is very low (≈0.005–0.03). In HSL the book raises saturation for the lightest/darkest greys to keep the temperature consistent; in OKLCH keep chroma roughly constant across the grey scale instead.
- Match grey temperature to the personality chosen in `process.md`.

## Accessible contrast without ugliness
- WCAG: normal text (under ~18px) needs ≥ 4.5:1 contrast; larger text ≥ 3:1.
- **White text on color** often needs a very dark background to pass, which then shouts for attention. If the element isn't meant to be the focus, **flip the contrast**: dark colored text on a light tint of the same hue (e.g. 800 text on 100 background).
- **Colored secondary text on a dark colored panel:** raising lightness alone drifts toward white. Raise L while keeping chroma, and if it still can't pass, shift the hue slightly toward a hue that holds more chroma at high L (e.g. toward cyan or yellow) to stay colorful.
- OKLCH L differences are a good guide to contrast, but always verify with the actual WCAG ratio.

## Never rely on color alone
- Color must reinforce information that's already conveyed another way; it can't be the only channel (color-blind users).
- Up/down changes: add an icon or arrow, not just green/red.
- Multi-series charts: differ series by **contrast** (light vs dark) more than by distinct hues; light/dark differences are easier to tell apart than hue differences.
