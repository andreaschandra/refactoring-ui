---
name: refactoring-ui
description: Applies tactical web UI design rules (hierarchy, spacing, typography, color, depth, images, finishing touches) to generate new interfaces or critique existing ones. Use when designing or building a web page, component, or layout, or when asked to review, critique, polish, or improve the look of a UI, screenshot, or HTML/CSS. Framework-agnostic.
---

# Refactoring UI

Two modes. Pick one from the request; if both apply, generate first, then critique your own output.

## Mode A — Generate

1. State the personality in one line (audience → typeface direction, radius, accent, copy tone), and put it as a comment at the top of the output (e.g. a CSS comment) so it travels with the file.
2. Define the system before any markup, as tokens:
   - Spacing and sizing (default scale in `references/layout-spacing.md`), font size (default scale in `references/typography.md`), font weight, line height, color palette in OKLCH (8–10 greys, primary and accent hues with 100–900 shades; see `references/color.md`), shadow, radius, border width.
   - Only use values from these scales.
3. Build the core feature first, hierarchy before color, then the minimal shell. Apply the reference files for each concern (routing table below).
4. Run `references/review-checklist.md` on the result and fix every failed item before returning.

## Mode B — Critique

1. Read `references/review-checklist.md` in full.
2. Evaluate the UI against every item; read the matching reference file when an item fails.
3. Output issues ranked by visual impact:
   `[impact: high|med|low] <issue> → <concrete fix with values>`
4. End with the 3 changes that would improve it most.
5. Then a short **Beyond visual design** section: only blocking accessibility or functional issues (missing viewport meta, no landmarks, unlabeled controls, missing focus styles, dead or broken flows). Max ~5 bullets; skip the section if there are none.

## Routing table

Read only the files the task needs. Each file lists its contents at the top.

| Concern | File |
|---|---|
| Review checklist (all modes) | `references/review-checklist.md` |
| Starting a design: feature-first, scope, personality, value systems | `references/process.md` |
| Hierarchy: emphasis via weight/color, text on color, labels, heading sizes, button hierarchy | `references/hierarchy.md` |
| Layout & spacing: white space, spacing/sizing scale, widths, grids, responsive sizing, grouping | `references/layout-spacing.md` |
| Typography: type scale, fonts, line length, line height, baseline alignment, links, alignment, letter-spacing | `references/typography.md` |
| Color: OKLCH, palette size, shade scales, saturation, hue rotation, tinted greys, contrast, color-blindness | `references/color.md` |
<!-- rows added per chapter -->

## Core principles

- **Systematize everything.** Every size, space, color, weight, shadow, and radius comes from a small predefined scale. No ad hoc values.
- **Feature first.** Design what the user came to do before the shell around it.
- **Hierarchy before color.** The UI must read correctly in grayscale; color only enhances.
- **No implied features.** Never show a control or promise that the page can't fulfil.
- **More space around groups than within them.** Start generous, then remove.
- **Color supports, never carries.** Meaning must survive without color; contrast meets WCAG.
- **Emphasize by de-emphasizing.** Decide the #1 element per view and quiet everything competing with it; one primary action per view.
<!-- added per chapter; keep to the few rules that apply to every task -->
