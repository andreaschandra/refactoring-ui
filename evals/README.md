# Evals

5 fixed tasks in `cases.json`: 2 generate, 3 critique. `ANSWER_KEY.md` lists planted issues per fixture; never copy it into a run folder. Outputs are plain HTML/CSS so they can be rendered and diffed; the skill itself stays framework-agnostic.

## Run

For each run, use a **fresh Claude Code session** (no prior context) in this `evals/` folder:

```bash
mkdir -p runs/<run-name> && cd runs/<run-name>
claude
# paste each case's "query" verbatim, one session per case
```

- `runs/baseline/` — skill **not** installed (move `~/.claude/skills/refactoring-ui` aside first).
- `runs/v0.N/` — skill installed at version after chapter N.

## Triggering

Since v0.9 the skill triggers only when named or for explicit visual-design critiques. For skill runs, start each generate prompt with `/refactoring-ui` (or append "Use the Refactoring UI skill."). Critique prompts trigger on their own; prefixing them too is harmless. Baseline runs use the plain prompts.

## Record per run

- Output files named per `cases.json`.
- `notes.md`: did the skill trigger? which reference files did Claude read, in what order? anything skipped or read twice?

## Compare

Open `runs/<prev>/X.html` and `runs/<new>/X.html` side by side; check each `expected_behavior` item (filled in as chapters are added).
