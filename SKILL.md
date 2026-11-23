---
name: refactoring-ui
description: Applies tactical web UI design rules (hierarchy, spacing, typography, color, depth, images, finishing touches) to generate new interfaces or critique existing ones. Use when designing or building a web page, component, or layout, or when asked to review, critique, polish, or improve the look of a UI, screenshot, or HTML/CSS. Framework-agnostic.
---

# Refactoring UI

Two modes. Pick one from the request; if both apply, generate first, then critique your own output.

## Mode A — Generate

1. Define the system before any markup:
   - Spacing scale, type scale, color palette (greys + primary + accents, with shades), shadow scale, radius.
   - Only use values from these scales.
2. Build the layout, applying the reference files for each concern (routing table below).
3. Run `references/review-checklist.md` on the result and fix every failed item before returning.

## Mode B — Critique

1. Read `references/review-checklist.md` in full.
2. Evaluate the UI against every item; read the matching reference file when an item fails.
3. Output issues ranked by visual impact:
   `[impact: high|med|low] <issue> → <concrete fix with values>`
4. End with the 3 changes that would improve it most.

## Routing table

Read only the files the task needs. Each file lists its contents at the top.

| Concern | File |
|---|---|
| Review checklist (all modes) | `references/review-checklist.md` |
<!-- rows added per chapter -->

## Core principles

<!-- added per chapter; keep to the few rules that apply to every task -->
