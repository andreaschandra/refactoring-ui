# Finishing touches

## Contents
- Supercharge the defaults
- Accent borders
- Decorate backgrounds
- Empty states
- Use fewer borders
- Rethink standard components

## Supercharge the defaults
Add polish by upgrading elements already on the page rather than adding new ones:
- **Bullet lists:** replace bullets with icons: checkmarks or arrows generically, content-specific icons where they fit (e.g. a lock for security features). Icons at their intended size (see `images.md`).
- **Testimonials:** make the quotation marks a visual element: larger and in a brand color.
- **Links:** custom color and weight, or a thick colored custom underline that partly overlaps the text (e.g. `text-decoration-thickness`, `text-underline-offset`, or a low background-gradient stripe).
- **Checkboxes and radios:** brand color for selected states instead of browser defaults (`accent-color: <primary-600>` at minimum, custom controls when they matter).

## Accent borders
A colored rectangle adds flair without graphic-design skill. Good spots:
- Top edge of a card.
- Active navigation item (underline or side bar).
- Side of an alert message.
- Short bar under a headline.
- Top edge of the whole layout.
Use a primary or accent shade from the palette; typically 2–4px (from the border-width set).

## Decorate backgrounds
When hierarchy, spacing, and type are right but the page still feels plain, vary a few backgrounds:
- **Change the background color** to emphasize one panel or separate page sections.
- **Subtle gradient** for more energy: two hues **no more than ~30° apart**.
- **Repeating pattern** (e.g. from Hero Patterns), across the whole background or along one edge only.
- **Single shape or illustration** in a specific spot: geometric shapes, a fragment of a pattern, a simplified illustration (e.g. a world map).
- Always keep **low contrast** between the decoration and its background so content stays readable.

## Empty states
- For anything driven by user-generated content, the empty state is the first thing users see; design it as a priority, not an afterthought.
- Include an image or illustration to draw attention, plus a prominent call to action for the next step (usually the view's primary action).
- Hide supporting UI that does nothing yet (tabs, filters, sort, bulk actions) until there's content. This is also a "no implied features" case (see `process.md`).
- Make it interesting, not a single grey line of text.

## Use fewer borders
Borders are one way to separate elements, not the default. Too many make a UI busy. Before adding a border, try:
- **A box shadow** (from the elevation scale in `depth.md`): outlines more subtly. Works best when the element's color differs from the background.
- **Different background colors** for adjacent elements. If you already have different backgrounds *and* a border, remove the border.
- **More space** between groups (see grouping in `layout-spacing.md`).

## Rethink standard components
Default mental models aren't the only option:
- **Dropdowns:** a floating box can hold sections, multiple columns, supporting text, and colored icons, not just a stacked link list.
- **Tables:** merge related, non-sortable columns into one cell with internal hierarchy (e.g. name over email); add images or color (badges, avatars) to enrich data.
- **Radio groups:** when the choice is central to the UI, use selectable cards instead of a stack of labels with circles.
- Keep the constraints of the system (scales, palette, hierarchy); the freedom is in structure, not in breaking the system.
