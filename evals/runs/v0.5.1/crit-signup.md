# Critique: signup.html

Reviewed against the full refactoring-ui checklist. It feels amateur because:
- **Mixed signals:** a Times New Roman body, an Impact all-caps headline with "!!!", a 3D orange gradient button with yellow text and a saturated blue backdrop all clash with each other.
- **No system:** every value is ad hoc, from 8 font sizes to 11 different spacing values.
- **Too much asked:** the form asks for 7 fields to do a 3-field job.

The checkout-style shouting makes a free trial look less trustworthy, not more.

## Issues, ranked by visual impact

### High

- **[impact: high] No consistent personality.** The page mixes Times New Roman, Impact, `CREATE YOUR ACCOUNT TODAY!!!`, "amazing platform", "whatsoever", outset 3D borders and a gradient button. → Pick one direction. For a team-productivity SaaS that means neutral and friendly: the system sans stack, small radius (6px on controls, 8px on the card), one blue primary, and plain copy ("Create your account").
- **[impact: high] The primary button is illegible and loud.** Yellow on an orange gradient is about 1.5:1 contrast, with a 22px bold uppercase label and a 3px outset border. → Use a solid primary-600 `oklch(50% 0.15 255)` with white 16px/600 text (≈6:1). Pad it 12px 16px, make it full width, 6px radius, no gradient or outset. Sentence case: "Create account".
- **[impact: high] There are two equally loud buttons, and Cancel goes nowhere.** "Cancel" is a solid blue 22px button next to Sign Up, and there is nothing to cancel back to. → Remove Cancel. Keep one primary action. Add a tertiary text link: "Already have an account? Log in".
- **[impact: high] Too many fields.** First and last name, confirm password, company and "how did you hear about us" are all friction on a free-trial signup. The intro paragraph promises "quick, easy". → Keep three fields: Name, Email and Password. Replace Confirm Password with a "Show" toggle on the password field. Collect company and attribution after signup.
- **[impact: high] The form is stretched.** It sits in a `.box` that is 90% of the viewport wide, so inputs run about 1200px on a desktop. → Use `max-width: 512px; width: 100%` (448px of content after padding) for the form card. On wide screens, put the feature list in a second column instead of widening the form.

### Medium

- **[impact: med] Text contrast fails across the page.**
  - Intro text: #777 on #eee ≈ 3.9:1.
  - Hints: #999 on #eee ≈ 2.4:1.
  - Legal text: #aaa on #eee at 10px ≈ 1.9:1.
  - Feature list: white on #4a90d9 ≈ 3.3:1 at 15px.

  → Body text in grey-600 `oklch(45% 0.02 255)` on white (≈7:1). Hints and legal text at 14px in grey-600. No text below 12px.
- **[impact: med] Everything is centered.** That includes labels, a 5-line intro paragraph and justified legal text without hyphenation. → Left-align the form, labels, hints and legal text. Only the short heading block may be centered, and the left-aligned card reads better anyway. Never justify text.
- **[impact: med] The intro is a wall of text.** It is 55 words with a line height of 1.1. → Use one line: "Free for 30 days. No credit card required." 16px, line height 1.5, grey-600. The features move to the side column.
- **[impact: med] Labels are bold, end in colons and are spaced ambiguously.** Each label sits 9px below the previous input, but the input sits only 2px below the label. The row margin (6px) is close to both, so labels float. → Labels 14px/500 grey-800, no colons. Label to input 8px, input to hint 8px, field to field 24px.
- **[impact: med] The Terms checkbox has no `<label>`, and its terms aren't links.** Consent to marketing is hidden in grey fine print. → Make "By creating an account you agree to the Terms and Privacy Policy" a 14px note with real links, which counts as acceptance and removes a required checkbox. Make marketing an explicit, unchecked, optional checkbox with a proper `<label>`.
- **[impact: med] The feature list floats outside the card.** It is white 15px text on saturated blue, joined by ✔ characters. → Make it a real list in a side column on a light background. Each item gets an icon in a primary-100 circle with primary-700 check, and grey-800 text at 16px. Stack it below the form on narrow screens.
- **[impact: med] Inputs are cramped and harsh.** They have 3px padding, a 1px #000 border, 95% width (misaligned with the labels) and no focus state. → Padding 8px 12px, 16px text (also prevents iOS zoom), 1px grey-300 border, 6px radius, 100% width. On focus: primary-500 border plus a `0 0 0 4px` primary-200 ring.
- **[impact: med] No spacing or type system.** Sizes in use are 40, 22, 17, 16, 15, 14, 11 and 10. Spacing values are 30, 15, 14, 9, 6, 5, 4, 3 and 2. → Type `12, 14, 16, 20, 24, 30`. Spacing `4, 8, 12, 16, 24, 32, 48, 64`. Use nothing else.

### Low

- **[impact: low] The saturated #4a90d9 page background overpowers the card.** → Use a grey-50 page with a white card and a soft shadow (`0 1px 3px oklch(0% 0 0 / .08), 0 8px 24px oklch(0% 0 0 / .06)`), and drop the 2px #555 border.
- **[impact: low] Password rules are hinted at but not enforced.** → Add `minlength="8"` and a `pattern`, plus `autocomplete` attributes (`name`, `email`, `new-password`), so the hint is backed by behavior.
- **[impact: low] The heading line height and colors are unset, and the text uses #222/#444 ad hoc.** → Heading 24px/700 grey-900, line height 1.25, `letter-spacing: -0.01em`. Body line height 1.5. All colors come from an OKLCH grey and primary scale.

## The 3 changes that would improve it most

1. **Pick one calm personality and apply it everywhere.** Use the system sans, sentence-case plain copy, one solid primary button with white text, and no gradients, outsets, Impact or exclamation marks.
2. **Cut the form to Name, Email and Password in a 512px card.** Remove Cancel, Confirm Password, Company and "How did you hear". Turn the Terms checkbox into a linked note above the button.
3. **Put a scale behind every value.** Use the 4–64px spacing scale, with 8px within a field and 24px between fields, and the 12–30px type scale. Use OKLCH greys so all text passes 4.5:1, and left-align everything except the heading.

The improved version is in `signup-fixed.html`.
