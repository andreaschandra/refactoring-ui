# Eval report: v0.9 (all 8 chapters, consolidated) vs v0.5.1 vs baseline

## Metrics (resolved through tokens)
| file | spacing values (base → 0.5.1 → 0.9) | off-scale spacing | off-scale font | borders | distinct shadows |
|---|---|---|---|---|---|
| gen-pricing | 26 → 10 → 12 | 16 → 0 → 0 | 5 → 0 → 0 | 12 → 7 → **3** | 1 → 2 → 6 |
| gen-settings | 18 → 11 → 10 | 10 → 0 → 0 | 3 → 0 → 0 | 8 → 6 → **3** | 6 → 6 → 8 |
| signup-fixed | 17 → 8 → 9 | 10 → 0 → 0 | 4 → 0 → 0 | 7 → 1 → **2** | 1 → 3 → 6 |

- System discipline holds: zero off-scale spacing/font values in all pages (2px micro-steps used only in badges, toggle knob, inline code, as allowed).
- Borders down sharply (ch8 "fewer borders"): separation now via shadow + background.
- Distinct shadows went *up*, but all are scale levels or purposeful ch6 cues (raised highlight `inset 0 1px 0`, inset wells, pressed state, image inner ring). The ch6 expected behavior "fewer distinct shadows" was the wrong metric; replace with "all shadows are scale levels or light-source cues".

## team.html answer key (16)
| | v0.5.1 | v0.9 |
|---|---|---|
| Caught | 16 | 13 full + 2 partial |
| Missed | – | #4 uniform 24px spacing (critique called spacing "mostly on-scale" and moved on) |
| Partial | – | #9 "Filters (0)" (count fix, not the missing filter UI); #13 centered paragraph (removed for tone, not alignment) |
| New finds | – | count mismatch (6 members, 3 cards), unlabeled search, ambiguous Edit/Remove names |

Single runs; some variance is expected. Baseline crit-team still not run.

## New behaviors since v0.5.1 (ch6–8 + fixes)
- Personality comment present in all 3 generated files ✅
- "Beyond visual design" section in all 3 critiques ✅ (viewport, landmarks, labels, focus, dead flows; a11y coverage restored)
- Depth: two-part shadow scale tokens, raised buttons with top highlight, inset toggle/inputs, pressed state lowers ✅; plan cards overlap the hero band (layering) ✅
- Images: avatar `object-fit: cover` + inner ring ✅; icons at intended size inside shapes ✅
- Finishing: accent borders (featured plan, danger card), icon bullets, custom link underline, ≤30° hue gradient, card separation by shadow not borders ✅
- Critiques flag light-source direction of shadows, border overuse, weak empty states ✅

## Watch items
1. Grouping check (#4) skipped when values are on-scale but uniform; checklist item may need "on-scale but identical within/between groups still fails".
2. gen-settings has two primary buttons (Save changes, Update password), one per card; defensible (separate forms, disabled until dirty) but borderline vs "one primary per view".
