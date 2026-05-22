--
title: Markdown Demo
tags: []
outgoing links: []
--

# Markdown Demo

A reference for local markdown features.

--

## Transclusion

Include content from another page: `[!pagename]`

Example - transcluding the shields table:
[!endworld/mecha/systems/tables#heavy-shield|Heavy Shield Table]

--

## Foldable Sections

Prefix a heading with `!` to make it collapsible: `## !Heading`

## !Demo Foldable

This content starts collapsed. Click the heading to expand it.

--

## Section Transclusion

Transclude just part of a page with `#fragment`: `[!pagename#heading]`

Matches headings case-insensitively (foldable `!` prefix is ignored). Use `[!pagename#heading]` (no `|`) to keep the original heading, or `[!pagename#heading|New Name]` to rename it.

Example - transcluding this foldable section:
[!demo#demo-foldable]

--

## Section Tooltip

Show page content on hover: `[!t:page]`, `[!t:page#heading]`, or `[!t:page#heading|Custom Text]`

Hover over [!t:demo#section-tooltip] to preview that section.

--

## Infolet

Show an item tooltip: `[!q:itemname]`

Renders a hover tooltip with the item's description from the database.

--

## Clock

Inline progress clock: `[clock|name|current|total]`

Renders a clickable clock element. Linked clocks reference another page: `[clock|name@pagename]`

--

## Checkbox

Task list: `- [ ] task` / `- [x] done`

- [ ] unfinished
- [x] completed

--

## Glitch Text

Cyberpunk glitch effect: `g~text~g` or `g~text~g~replacement~g`

g~hello~g - g~world~g~W0RLD~g

--

## Wiki Links

Internal links are auto-validated. `<a href="existingpage">` gets a `/wiki/` path. Broken links get a `missing` class.

--

## Multi-line Headers

Automatic - if a heading spans multiple lines, only the first line stays in the `<h...>` tag.
