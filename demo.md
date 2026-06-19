---
outgoing links: []
tags: []
title: Markdown Demo
---
# Markdown Demo

A reference for local markdown features.

---

## Transclusion

Include content from another page: `[!pagename]`

Example - transcluding :  
[!illusionmagic#Zone der Unsichtbarkeit|Die umbenannte Zone der Unsichtbarkeit]

---

## Section Transclusion

Transclude just part of a page with `#fragment`: `[!pagename#heading]`

Matches headings case-insensitively (foldable `!` prefix is ignored). Use `[!pagename#heading]` (no `|`) to keep the original heading, or `[!pagename#heading|New Name]` to rename it.

Example - transcluding this foldable section:
[!demo#demo-foldable]

---

## Foldable Sections

Prefix a heading with `!` to make it collapsible: `## !Heading`

## !Demo Foldable

This content starts collapsed. Click the heading to expand it.

---

## Section Tooltip

Show page content on hover: `[!t:page]`, `[!t:page#heading]`, or `[!t:page#heading|Custom Text]`

Hover over [!t:demo#section tooltip|this] to preview that section.

---

## Infolet

Show an item tooltip: `[!q:itemname]`

Renders a hover tooltip with the item's description from the database.

---

## Clock

Inline progress clock: `[clock|name|current|total]`

Renders a clickable clock element. Linked clocks reference another page: `[clock|name@pagename]`

[clock|progress|3|8]

---

## Checkbox

Task list: `- [ ] task` / `- [x] done`

- [ ] unfinished
- [x] completed

---

## Glitch Text

Cyberpunk glitch effect: `g~text~g` or `g~text~replacement~g`

g~hello~g - g~world~W0RLD~g

---

## Strikethrough

This is ~~strikethrough~~ text.

---

## Invert Text

Invert textcolor: `i~text~i`

i~this text is inverted~i

---

## Wiki Links

Internal links are auto-validated. `[titel](linktarget)` gets a `/wiki/linktarget` path. Broken links get marked.

---

## Multi-line Headers

Automatic - if a heading spans multiple lines, only the first line stays in the &lt;h...&gt; tag.