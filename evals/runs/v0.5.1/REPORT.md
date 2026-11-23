# Eval report: v0.5.1 (chapters 1–5) vs baseline

## Metrics (metrics.py, values resolved through tokens)
| file | font sizes | spacing values | off-scale spacing | off-scale font sizes | one-off color literals |
|---|---|---|---|---|---|
| gen-pricing | 11 → 9 | 26 → 10 | 16 → 0 | 5 → 0 | 1 → 0 |
| gen-settings | 7 → 6 | 18 → 11 | 10 → 0 | 4 → 0 | 5 → 2 (alpha variants of grey-900) |
| signup-fixed | 7 → 4 | 17 → 8 | 10 → 0 | 4 → 0 | 1 → 0 |

Distinct color count went up (shade scales are used as intended); all colors come from tokens.
Shadow declarations went up (4/12/5 vs 2/6/1): chapter 6 (depth) not yet distilled; watch this.

## team.html answer key (16 planted issues)
v0.5.1 caught 16/16, including #5 (borders) and #14 (empty state/icon) from chapters not yet distilled. Baseline crit-team: not run.

## Expected behaviors (ch1–5)
| | pricing | settings | signup-fixed | crit-dashboard | crit-signup | crit-team |
|---|---|---|---|---|---|---|
| Tokens for spacing/type/weight/radius/shadow | ✅ | ✅ | ✅ | – | – | – |
| Personality stated | ? (not in file) | ? | ✅ (comment) | ✅ (proposes) | ✅ | ✅ |
| One primary action; destructive not primary | ✅ | ✅ red only in dialog | ✅ | ✅ flags | ✅ flags | ✅ flags |
| No naive Label: value | ✅ | ✅ | ✅ | ✅ flags | ✅ flags | ✅ flags |
| 2 weights, none < 400 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Spacing on scale / grouping | ✅ | ✅ | ✅ | ✅ flags | ✅ flags | ✅ flags |
| Max-widths, line length | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Type scale, line-height varies | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OKLCH palette, no pure black | ✅ | ✅ | ✅ | ✅ proposes | ✅ proposes | ✅ proposes |
| Color not sole signal | ✅ icon on save note | ✅ icon+text status | ✅ | ✅ flags | – | ✅ status dot + text |
| Critique format (impact-ranked + top 3) | – | – | – | ✅ | ✅ | ✅ |

## Observations
- Biggest win: system discipline. Zero off-scale spacing/font values in all generated pages (baseline 10–16 off-scale spacing values each).
- Critiques now lead with visual design and give exact token values; baseline led with functional/legal issues.
- Loss: accessibility/semantics coverage dropped in crit-dashboard (baseline flagged viewport meta, landmarks, aria-labels, focus styles; v0.5.1 doesn't). Contrast is still covered.
- Personality line: required by SKILL.md step 1, only visible in signup-fixed (as a CSS comment). Possibly stated in chat only; unverified.
- Skill triggered in critique runs ("Reviewed against the full refactoring-ui checklist"). Trigger for generate runs not recorded.
