# Critique: signup.html

**Verdict:** The page looks amateur because every element is shouting at once and none of it follows the conventions people expect from a signup form. The page has five fonts and three competing button colors, the headline is in caps, the gray text is hard to read, and the form asks for too much. It also has real functional and legal problems on top of the visual ones.

Issues are listed below in priority order.

---

## 1. Functional and accessibility bugs (fix first)

| Problem | Where | Why it matters |
|---|---|---|
| `<label>` elements aren't linked to inputs (no `for`/`id`) | every field | Clicking a label doesn't focus its field, and screen readers announce unnamed inputs. |
| No `<form>` element, no `name` attributes, no `required` | whole page | Enter doesn't submit and nothing gets posted. The browser can't validate. |
| No `autocomplete` attributes | name, email, password | Password managers and autofill can't help. This is the biggest friction point on any signup. |
| No `<meta name="viewport">` | `<head>` | On a phone the page renders at desktop width and gets shrunk to tiny text. |
| The checkbox label is bare text, not a `<label>` | terms row | The tap target is a 13px box. |
| The password rule ("8 characters with a number and symbol") is only a hint | password | Nothing checks it, so users find out only after a failed submit, or never. |
| **Contrast failures:** `#999` hints on `#eee` (~2.5:1), `#aaa` legal text on `#eee` (~2.1:1), yellow on orange button (~1.9:1), `#777` intro on `#eee` (~4.0:1) | hints, legal, CTA, intro | All fail WCAG AA (4.5:1). The legal text and the main button are the two things that most need to be readable. |
| No visible focus styles beyond the browser default, and the 3px outset borders hide them | inputs, buttons | Keyboard users lose their place. |

## 2. Legal / trust problems

- **Marketing consent is bundled into the signup.** "By creating an account you agree to receive … marketing communications" means opting in by default. That isn't valid consent under GDPR/PECR, and it reads as shady. Make it a separate checkbox that starts unchecked.
- **"Terms of Service and Privacy Policy" aren't links.** People are asked to agree to documents they can't open.
- **"Join thousands of happy users"** is an unverifiable claim placed exactly where trust matters. Use a concrete fact instead (30 days free, no card).

## 3. Too many fields and too many decisions

There are 8 inputs plus 2 buttons. Every extra field lowers completion.

- **Confirm password**: drop it and add a show/hide toggle. Typos get caught by looking at the password, not by typing it twice.
- **First name + last name**: merge into one "Full name" field. It's faster, and it works for names that don't split cleanly.
- **"How did you hear about us?"**: this serves marketing, not the user. Move it to onboarding or drop it. Its "Please select..." placeholder is also a selectable value.
- **Cancel button**: on a standalone signup page there's nothing to cancel. Worse, it's styled at the same weight as the main action, so the two compete. Replace it with a quiet "Already have an account? Sign in" link.
- **Company name (optional)**: keep it, but explain why you're asking (it goes on invoices). An optional field with no stated purpose looks like data harvesting.

## 4. Typography

- **Three type families with no system:** Times New Roman body, Impact headline, and system UI on the inputs and buttons. Impact plus Times is the classic "made in 2003" combination.
- **All-caps headline with triple exclamation marks** ("CREATE YOUR ACCOUNT TODAY!!!"). It reads as spam. Use sentence case and say what the user gets.
- **The intro is a 50-word run-on paragraph at `line-height: 1.1`** and spans the full width of the box (~140 characters per line on desktop). Body text needs about 1.5 line-height and ≤ 75 characters per line.
- **Labels end with colons and are bold 16px**, which makes them heavier than the input text. Labels should be quieter than what people type.
- **"SIGN UP NOW"** is another all-caps button. It also says "sign up" while the headline says "create account". Pick one verb and use it everywhere.

## 5. Layout and visual hierarchy

- **Everything is centered**, including the form labels. Centered labels over left-aligned input text make the eye jump back and forth. Forms should be left-aligned in one column.
- **The box is `width: 90%`** with no max-width, so on a wide monitor the inputs are ~1600px wide. A signup form should be about 360–420px.
- **Inputs are `width: 95%`** inside a centered container, so they never line up with anything. **`padding: 3px`** makes them about 24px tall, well under the 44px minimum touch target.
- **Spacing is arbitrary**: 5px, 6px, 9px, 14px, 15px, 2px. No rhythm, so nothing groups visually.
- **The 2px #555 box border, the 3px outset button borders and the gradient button** are Windows 98 chrome. Each one adds visual noise and no information.
- **The feature list sits outside the card** in white on bright blue, under the fold, where it looks like a footer nobody reads. It's actually the best argument for signing up. Bring it next to the form.

## 6. Color

- **Bright `#4a90d9` background + gray card + orange/yellow CTA + blue Cancel button** means four saturated colors fighting, with no brand logic connecting them.
- The Cancel button reuses the page background color, so it looks like a hole in the card.
- A calm neutral ground with **one** action color would make the CTA the obvious next step.

---

## What the fixed version does

`signup-fixed.html` applies all of the above:

- **Fields:** cut to 3 required fields (full name, work email, password) plus optional company. The password has a show/hide toggle and live rule checks.
- **Form markup:** real `<form>` with `for`/`id` labels, `autocomplete` attributes, `required`, inline error messages linked via `aria-describedby`, and validation on blur and submit.
- **Consent:** marketing is a separate, unchecked opt-in, and Terms and Privacy are real links.
- **Copy and type:** one typeface (Schibsted Grotesk), sentence-case copy, and a single verb ("Create account") used throughout.
- **Layout and color:** one neutral palette with a single ledger-green action color. Everything passes AA contrast in light and dark mode.
- **Memorable element:** a live invoice preview beside the form. It fills in with your name and company as you type, which shows what the product does instead of listing features in a run-on sentence.
- **Responsive and accessibility:** the preview stacks under the form on mobile, 44px+ touch targets, visible focus rings, and `prefers-reduced-motion` respected.
