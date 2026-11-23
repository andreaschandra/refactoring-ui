# Images

## Contents
- Photo quality
- Text on images: consistent contrast
- Everything has an intended size (icons, screenshots, logos)
- User-uploaded images

## Photo quality
- Bad photos ruin an otherwise good design. Real projects need professional photography for specific needs or high-quality stock (free sources like Unsplash exist) for generic ones.
- Don't design around throwaway placeholders expecting to swap in amateur shots later; the design won't survive the swap.
- Generate: when no real image is available, use a deliberate placeholder (neutral block at the final aspect ratio, or a clearly labeled slot) and state that real photography is needed. Never design around images you can't supply.
- Critique: flag low-quality or mismatched imagery as a high-impact issue.

## Text on images: consistent contrast
Photos have light and dark regions, so no single text color reads everywhere. The fix is to reduce the image's dynamics, not to change the text:
- **Overlay:** semi-transparent black under light text, white under dark text, e.g. `background: linear-gradient(oklch(0% 0 0 / .5), oklch(0% 0 0 / .5)), url(...)`. Trade-off: darkens or lightens the whole image.
- **Lower image contrast:** `filter: contrast(.7)`, then compensate overall lightness with `brightness()`. More control than an overlay.
- **Colorize:** lower contrast → desaturate → solid brand-color fill with multiply blend (CSS: `filter: contrast(.8) grayscale(1)` on the image plus a colored layer with `mix-blend-mode: multiply`, or `background-blend-mode: multiply`). Also ties the photo to the palette.
- **Text shadow as glow:** large blur, no offset, e.g. `text-shadow: 0 0 24px oklch(0% 0 0 / .6)`. Boosts contrast only around the text; combine with a milder contrast reduction to keep more of the image.
- Verify the result still meets the WCAG ratios in `color.md` over the busiest part of the image.

## Everything has an intended size
- **Don't scale up icons.** Icons drawn for 16–24px look chunky and under-detailed at 3–4×, even as SVG. To fill a larger space, keep the icon near its intended size and put it inside a larger shape with a background (e.g. a 24px icon in a 48px circle with a primary-100 fill and primary-600 icon).
- **Don't scale down screenshots.** Shrinking a full-size screenshot turns 16px text into ~4px noise. Instead:
  - capture at a smaller viewport (e.g. tablet) and give it more room,
  - show a partial, cropped screenshot at near-native scale, or
  - draw a simplified illustration of the UI (details removed, small text replaced by lines).
- **Don't scale down icons or logos either.** Large-size artwork turns to mush when shrunk (favicons are the extreme case). Use a version drawn or simplified for the target size.

## User-uploaded images
You can't art-direct user content, but you can contain it:
- **Fixed shape and size:** display in fixed containers, centered and cropped, never at intrinsic aspect ratio. CSS: `width/height` (or `aspect-ratio`) + `object-fit: cover` on `<img>` (or `background-size: cover`).
- **Prevent background bleed:** when an image's background is close to the UI background, it loses its edge. Don't add a border (clashes with image colors). Use a subtle inner shadow, e.g. `box-shadow: inset 0 0 0 1px oklch(0% 0 0 / .1)` (needs a wrapper or pseudo-element over the image), or a semi-transparent inner border if the inset look is unwanted.
