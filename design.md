# Design — sdmrnwashere.github.io

Personal academic site for **Sadman Rahman**.

## Concept — "the signal lab: signals × AI" (v4)

Sadman's research is about reading the body's signals, so the site behaves like
an oscilloscope crossed with a lab notebook: a live multi-channel signal display,
§-numbered sections, a lab-log news feed, figure captions, and mono "instrument"
labels. It aims to be sharp and editorial, with a few playful details that reward
curiosity. It deliberately does **not** reuse the navy / blue / orange look of the
reference site from v2.

## Tokens (`assets/site.css`)

| Token          | Light      | Dark       | Use |
|----------------|------------|------------|-----|
| `--bg`         | `#F4F3EF`  | `#0D0D10`  | Page (with faint graph-paper grid fading from the top) |
| `--paper`      | `#FBFAF7`  | `#15151A`  | Cards, scope, panels, chips |
| `--ink`        | `#111113`  | `#ECEAE4`  | Text, solid buttons, active nav pill, dark panels |
| `--muted`      | `#5D5B57`  | `#A3A09A`  | Secondary text |
| `--faint`      | `#9A978F`  | `#67655F`  | Meta, years, scope labels |
| `--rule`       | `#DAD7CF`  | `#26262C`  | Hairlines, card borders, grid |
| `--accent`     | `#4B2BEA`  | `#A496FF`  | **Ultraviolet.** Italic display words, links, EEG trace, waveform glyphs |
| `--mark`       | `#D9F45A`  | `#C9EE45`  | **Lime highlighter.** Key phrases, award pills, own-name underline, "hl" cards |

Section headings rest on a full-strength `--ink` rule rather than a light hairline.

## Type

- **Instrument Serif:** all display type. Huge hero name (up to 148px, line-height .86),
  page titles, section titles, card titles, ticker. The second word is usually *italic + accent*.
- **Geist:** body and UI, 16px / 1.65. Publication titles are Geist 500 for crispness.
- **Geist Mono:** uppercase 12px labels (`§ 01`, dates, channel names, status), kbd hints.

## Signature elements

1. **Live scope** (`#scope` canvas): 4 channels (EEG, ECG, IMU, RAD), all synthetic.
   The pointer amplifies and highlights the nearest channel and shows a readout;
   a click injects a decaying spike. It pauses off-screen and shows a static frame under
   `prefers-reduced-motion`. Colours are re-read from CSS on theme change.
2. **Fig. 1 portrait:** tilted 1.6°, grayscale with an ultraviolet screen wash; hovering
   straightens it and restores colour. Joke caption (`p < 0.05`).
3. **"Recording" status line** with a pulsing red dot plus coordinates.
4. **Model lane:** under the four traces, a toy attention strip lights up where the signals are active
   (and around the cursor or a clicked spike). The readout shows a mock classifier prediction per channel,
   e.g. `RADAR → posture change · p = 0.98`. It mixes signal processing and AI in one visual.
5. **Floating pill nav** with numbered tabs; becomes a bottom dock on phones.
   Shortcuts: `1–5` pages, `T` theme, `/` search papers. A toast confirms theme changes.
6. **Waveform glyphs** per sensing modality (EEG, ECG, Radar, IMU, Audio, Circuits,
   Control, Vision) on every paper; research cards redraw their glyph on hover.
7. **Footer:** giant "Got a signal worth decoding?", copy-email button, animated heartbeat line.

## Pages

| Path              | Tab    | Notes |
|-------------------|--------|-------|
| `/`               | About  | Hero, scope + model lane, §01 intro + "Now" panel, §02 lab log, §03 "Where signals meet AI" cards (tagged Signal / AI / Signal × AI), §04 selected papers |
| `/publications/`  | Papers | Filter chips (All, Journals, Conferences, EEG, Radar, IMU, ECG, Audio, Other) + live search + count |
| `/cv/`            | CV     | Sticky contents rail with scroll-spy; timeline entries; key/value blocks; skill tags |
| `/repositories/`  | Code   | Research-system cards (ink / lime / plain variants) + live GitHub repos as cards |
| `/misc/`          | Misc   | "By the numbers" panel, "Fun facts" panel, wide lime Behance card (former professional graphic designer, with swatches), teacher card, link cards |

## Editing content

- Papers: the `PUBS` array in `assets/site.js`. Fields: `y`, `m` (modality → glyph and filter),
  `type`, `q` (quartile), `award`, `status`, `url`, `sel` (show on home page).
- Lab log, "Now" panel, ticker: `index.html`.
- After changing CSS/JS, bump the `?v=` on every page's `<link>` and `<script>` tags.

## Accessibility

Contrast checked in both themes; author highlight is a thin underline so it stays readable
in dark mode. Reduced-motion turns off the pulse, reveal and scope animation.
Keyboard shortcuts ignore typing in inputs and modifier combos.

## Privacy

The personal phone number and referees' contact details from the CV are not published.

## Deploy

Push to a GitHub repo named `sdmrnwashere.github.io` → Settings → Pages → deploy from
`main` / root → `https://sdmrnwashere.github.io/`.

## Feedback log

- v1 (2026-10-28): "quiet journal" single page, ivory and forest green.
- v2 (2026-10-28): restyled to match the reference site (navy/blue/orange, Newsreader + Inter), five pages.
- v3 (2026-10-28): "signal lab": own identity (ultraviolet + lime, Instrument Serif / Geist / Geist Mono),
  live scope, modality filters + search, lab log, Fig. 1 portrait, floating nav and keyboard shortcuts, fun facts.
- v4 (2026-10-28): removed the ticker; content now mixes signals and AI (hero lead, research cards, model lane in the scope);
  added Research Assistant at MIST (Sep 2026 →, fingerprint attendance system) to the CV, Now panel, lab log and Code page;
  Misc gains Behance (professional graphic designer) and teacher cards; Behance added to the icon rows; keyboard hint auto-hides.
