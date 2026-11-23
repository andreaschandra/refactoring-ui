# Depth

## Contents
- Light comes from above: raised and inset elements
- Elevation scale (default shadows)
- Two-part shadows
- Shadows and interaction
- Depth in flat designs
- Overlapping layers
- Restraint

## Light comes from above: raised and inset elements
Decide the profile you want (raised or inset), then mimic a light source above the screen, viewed slightly from above.
- **Raised** (e.g. a button with flat top/bottom edges):
  1. Top edge catches light: make it slightly lighter than the face, via a top border or `inset 0 1px 0 <lighter shade>`.
  2. It blocks light below it: add a small dark shadow offset downward only, e.g. `0 1px 2px`. Keep blur to a couple of px; these shadows are sharp.
- **Inset** (wells, text inputs, checkboxes):
  1. Only the bottom lip is visible and faces up: make it lighter via a bottom border or `inset 0 -1px 0 <lighter shade>`.
  2. The edge above shades the top: add a small dark inset shadow offset downward, e.g. `inset 0 2px 2px`, so it doesn't show at the bottom.
- Pick highlight colors by hand from the palette (a lighter shade of the same hue). Don't overlay semi-transparent white; it desaturates the color underneath.

## Elevation scale (default shadows)
- Shadows place elements on a z-axis. Small, tight shadows = slightly raised; large, soft shadows = close to the user. Closer elements draw more attention.
- Define a fixed scale; **5 levels** is usually enough. Set the smallest and largest, then step roughly linearly between them. Default scale:

  | Level | Shadow | Typical use |
  |---|---|---|
  | 1 | `0 1px 3px oklch(0% 0 0 / .2)` | buttons, small raised controls |
  | 2 | `0 4px 6px oklch(0% 0 0 / .2)` | cards |
  | 3 | `0 5px 15px oklch(0% 0 0 / .2)` | dropdowns, popovers |
  | 4 | `0 10px 24px oklch(0% 0 0 / .2)` | sticky/floating panels |
  | 5 | `0 15px 35px oklch(0% 0 0 / .2)` | modals |

  Tune the opacity to the background; a tinted shadow color from the grey scale (dark grey with alpha) is fine.
- Pick a shadow by deciding where the element sits on the z-axis, not by tweaking the shadow itself. No shadows outside the scale.

## Two-part shadows
For more control, compose each level from two shadows doing different jobs:
- **Direct-light shadow:** larger and softer, with a clear vertical offset and large blur. The cast shadow behind the object.
- **Ambient-occlusion shadow:** tighter and darker, small offset and blur. The dark area right underneath where little light reaches.
- The tight shadow fades with elevation: distinct at level 1, almost or fully gone at level 5.
- Example level 1: `0 1px 3px oklch(0% 0 0 / .12), 0 1px 2px oklch(0% 0 0 / .24)`; example level 5: `0 15px 35px oklch(0% 0 0 / .15), 0 3px 6px oklch(0% 0 0 / .05)`.

## Shadows and interaction
- Use elevation changes as feedback:
  - Draggable item being dragged: raise it (add or enlarge its shadow) so it pops above the list.
  - Button pressed (`:active`): lower it (smaller shadow or none), as if pushed into the page.

## Depth in flat designs
Flat design drops gradients and realistic shadows, not depth.
- **Color:** lighter feels closer, darker feels farther (especially within one hue). Raised = lighter than the background; inset = darker than the background. Works in non-flat designs too.
- **Solid shadows:** short vertical offset, zero blur (e.g. `0 2px 0 <darker shade>`), to lift a card or button while staying flat.

## Overlapping layers
- Overlap elements to create layers instead of nesting everything inside containers:
  - A card offset so it straddles the boundary between two background sections.
  - An element taller than its parent so it overhangs both edges.
  - Small components too, e.g. carousel arrows overlapping the slide edge.
- Overlapping images clash; give each an "invisible border" in the background color (e.g. `box-shadow: 0 0 0 4px <page background>` or a border) so there's always a gap between them.

## Restraint
- Borrow cues from the physical world; don't chase photorealism. Heavy, many-layered effects make a UI busy and unclear.
- Depth should mean something: elevation = importance or interaction state. If every element floats, nothing does.
