# Save It Somewhere — Brand Guidelines

Version 2.0 · September 2026 · Bespoke Oracle · saveitsomewhere.com

---

## 1. Logo concept: The Little Door

The mark is a deep teal tile with a doorway cut out of its bottom edge, and one warm dot inside. The light left on.

It does not illustrate the product. It performs the feeling the product creates: *"Ahhh. It's somewhere safe."* A lit doorway is the oldest picture humans have of "someone is home, it's safe in there." Nobody has to decode it.

The dot is the thing you saved, already at rest. It is also the brand's smallest unit: it reappears as the full stop after "somewhere" in the wordmark, and it should reappear in the product as the "saved" indicator.

What the mark deliberately is not: a brain, a robot, a magnifying glass, a light bulb, a neural network, a circuit board, a sparkle, a database, a folder, a bookmark, a cloud.

## 2. Brand philosophy

- **Relief, not intelligence.** The product is smart. The logo makes the *user* feel calm.
- **Nameable.** People remember logos they can say out loud. This one is "the little door."
- **The odd one out.** Every AI product wears a sparkle or a purple gradient. Memory keeps the item that breaks the pattern, so the identity stays quiet on purpose.
- **One atom, everywhere.** Every sighting of the ember dot is a rehearsal. Repetition is what turns a mark into a memory.

Promise: *You save it somewhere. We make sure you find it.*
Campaign line: *Your screenshots deserve better than Camera Roll.*
Vision: *Anything worth remembering, without having to remember it.*

## 3. The logo system

| File | Use |
|---|---|
| `svg/logo-primary.svg` | Stacked lockup: mark above wordmark. Hero sections, print, splash screens. |
| `svg/logo-horizontal.svg` | Mark left of wordmark. Website navigation, email headers, docs. |
| `svg/icon.svg` | The mark alone. Avatar, browser extension, dashboard nav, watermark. |
| `svg/wordmark.svg` | Text only. Where the mark already appears nearby, or space is very wide and short. |
| `svg/icon-small.svg` | Bolder cut of the mark for 16–48 px. Used for the favicon and the small PNG exports. |
| `svg/app-icon.svg` | Full-bleed square tile for iOS, Android, desktop and extension stores. Platforms apply their own corner mask. |

Every lockup ships in three colourways: default (`-`), dark-surface (`-dark`) and monochrome (`-mono`, plus `-mono-reversed` for the icon and horizontal lockup).

## 4. Clear space

Keep a margin of **one door-width** (the width of the arch, 36% of the mark's height) on all sides of any lockup. Nothing else, text or image, sits inside it.

For the horizontal lockup the mark is 1.4× the wordmark's font size, with a gap of 0.28× the mark's height between them. Do not rebuild the lockup by hand; use the files.

## 5. Minimum size

| Asset | Minimum |
|---|---|
| Mark (`icon.svg`) | 24 px on screen, 8 mm in print |
| Mark, small cut (`icon-small.svg`) | 16 px |
| Horizontal lockup | 140 px wide |
| Primary (stacked) lockup | 96 px wide |
| Wordmark | 90 px wide |

Below 24 px use the small cut, never the standard mark.

## 6. Approved backgrounds

- **Light surfaces** (Cream `#F6F2E9`, Paper `#FFFFFF`, Mist `#DCE8E5`): default colourway. The doorway shows the surface through it.
- **Dark surfaces** (Night `#0E1F21`, Harbor `#1C4D52`): `-dark` colourway. The tile becomes Cream, the dot stays Ember.
- **Photography and busy backgrounds:** monochrome colourway inside a solid Cream or Night panel. Never place the coloured mark directly on a photo.
- **The app icon** is self-contained and goes on any home screen as is. `app-icon-light` exists for light-tinted icon themes.

## 7. Colour palette

| Name | Hex | Role |
|---|---|---|
| **Harbor** | `#1C4D52` | Primary. The tile, primary buttons, links on light surfaces. |
| **Ember** | `#CF6A3C` | Accent. The dot, the wordmark's full stop, the "saved" state. Small doses only. |
| **Ink** | `#12272A` | Text on light surfaces. |
| **Cream** | `#F6F2E9` | Light background. Also the mark on dark surfaces. |
| **Mist** | `#DCE8E5` | Secondary surface: cards, tags, hover states on light. |
| **Paper** | `#FFFFFF` | White. Cards on Cream, input fields. |
| **Night** | `#0E1F21` | Dark background. |
| **Slate** | `#5B7275` | Secondary text on light surfaces. |

Contrast, measured against WCAG 2.x:

| Pair | Ratio | Passes |
|---|---|---|
| Ink on Cream | 13.9 : 1 | AAA text |
| Cream on Night | 15.2 : 1 | AAA text |
| Harbor on Cream | 8.4 : 1 | AAA text |
| Harbor on Paper | 9.4 : 1 | AAA text |
| Cream on Harbor | 8.4 : 1 | AAA text (buttons) |
| Slate on Cream | 4.6 : 1 | AA text |
| Ember on Cream | 3.3 : 1 | Graphics and large text only |
| Ember on Night | 4.7 : 1 | AA text |
| Ember on Harbor | 2.6 : 1 | Decorative only |

So: Ember is never used for body text on light surfaces, and never as text on Harbor. It is a dot, a full stop, an underline, a status colour.

No gradients. No purple. No blue-to-violet AI glow.

## 8. Typography

**Wordmark:** Bricolage Grotesque, weight 600, optical size 96, tracking −0.035 em, lowercase, with an Ember full stop. The wordmark is shipped as outlines; never re-set it in live text.

**Headlines:** Bricolage Grotesque 500–600, tracking −0.02 to −0.03 em.
**Body and UI:** Figtree 400–500, tracking 0, line-height 1.5–1.6.
**Fallback stack:** `"Helvetica Neue", Arial, sans-serif`.

Both faces are open source (Google Fonts). Use at most these two families and at most two weights on a screen.

Avoid: futuristic or sci-fi faces, geometric "startup" defaults (Inter, Roboto, Montserrat), heavily rounded children's-app faces, corporate banking serifs.

## 9. Logo misuse

Do not:

1. Stretch, squash or rotate the mark.
2. Change the colours, or put the coloured mark on Harbor (it disappears).
3. Move, enlarge, remove or multiply the dot. One dot, in the doorway.
4. Fill the doorway. It is a cutout; the surface must show through.
5. Add shadows, bevels, outlines, glows or gradients.
6. Put the mark in a circle. The tile is the container.
7. Re-set the wordmark in another font, in Title Case, or without the full stop.
8. Pair the mark with a different wordmark, or the wordmark with a different mark.
9. Use the standard mark below 24 px. Use `icon-small`.
10. Place the mark on photography without a solid panel behind it.

## 10. Icon usage

- **Dashboard navigation, avatars, extension toolbar:** `icon.svg` (or `icon-dark.svg` on dark UI) at 24–48 px.
- **Social avatars:** `png/app-icon-1024x1024.png`. The full-bleed tile reads better in a circle crop than the standalone mark.
- **App stores:** `png/app-icon-1024x1024.png` (iOS, macOS), `png/app-icon-512x512.png` (Android, Chrome Web Store). Do not pre-round the corners.
- **iOS home screen web app:** `favicon/apple-touch-icon.png` (180 px).
- **Android maskable icon:** the same full-bleed tile; the doorway sits inside the safe zone.

## 11. Favicon usage

```html
<link rel="icon" type="image/svg+xml" href="/branding/favicon/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/branding/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/branding/favicon/favicon-16x16.png">
<link rel="shortcut icon" href="/branding/favicon/favicon.ico">
<link rel="apple-touch-icon" href="/branding/favicon/apple-touch-icon.png">
<meta name="theme-color" content="#1C4D52">
```

The favicon uses the small cut (wider doorway, larger dot) so the door still reads at 16 px. `favicon.ico` carries 48, 32 and 16 px.

## 12. Dark and light mode

| Context | Mark | Wordmark |
|---|---|---|
| Light UI (Cream / Paper) | Harbor tile, Ember dot | Ink, Ember full stop |
| Dark UI (Night) | Cream tile, Ember dot | Cream, Ember full stop |
| Brand-colour panel (Harbor) | Cream tile, Ember dot | Cream, Ember full stop |
| App icon | Harbor tile in both modes | — |

Implementation: swap the file on the theme attribute, or use a `<picture>` with a `prefers-color-scheme` source. The app icon and favicon never change with theme.

## 13. File inventory

```
branding/
├── svg/       icon, icon-dark, icon-mono, icon-mono-reversed, icon-small, icon-small-dark,
│              app-icon, app-icon-light,
│              logo-primary(-dark|-mono), logo-horizontal(-dark|-mono|-mono-reversed),
│              wordmark(-dark|-mono)
├── png/       icon(-dark|-mono)-{16,32,48,64,128,256,512}, app-icon-{180,192,512,1024},
│              app-icon-light-1024, logo-horizontal(-dark)@2x, logo-primary(-dark)@2x, wordmark(-dark)@2x
├── favicon/   favicon.svg, favicon.ico, favicon-16x16, favicon-32x32, favicon-48x48, apple-touch-icon
└── BRAND.md
```

## 14. The tests it passes

- **1-second test:** a tile with a door in it. Nothing else in the category looks like it.
- **16 px test:** the small cut keeps the doorway and the dot legible in a browser tab.
- **Black-and-white test:** the cutout carries the idea without colour; the mono files are one path.
- **App-icon test:** a calm teal tile with a lit door. It sits comfortably next to Messages and Photos.
- **Conversation test:** "I saved it in Save It Somewhere." The name is the sentence; the door is the picture that comes with it.
