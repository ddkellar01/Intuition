# Hardware layer — added 2026-10-28, all included

Everything Darion supplied in the second drop (5 Amazon screenshots /
1 screen video / 2 concept images) plus the 8K cinematic camera he
named in chat. Nothing dropped, nothing priced that wasn't priced on
his screenshots.

| # | Device / concept | Kind | Price as shown | Its job in Intuition |
|---|---|---|---|---|
| 1 | Meta Quest Pro (256GB, 12GB RAM) | interface | **$799.99** (−20%, list $999.99) | MR council room: experts as panels, passthrough workspace |
| 2 | Kodak Ultra Mini Portable Projector (Silver) | output | not visible in screenshot | Wall output for the projection brief (up to 100") |
| 3 | Hand Operated Flying Disc Drones — 3 listings | input | $22.99 / $16.99 / Force1 Scoot (price cut off) | Gesture control of the council (`drone.py`) |
| 4 | EEG Neurofeedback Headband — SereniBrain / iHANK (Dark Grey) | input | **$179.99** (−10%) | Brainwave context: focus/relaxation → answer mode (`eeg.py`) |
| 5 | Voice Mode UI (concept image) | interface | design reference | Voice-first face: mic orb, transcript card (`voice.py`) |
| 6 | Holographic Assistant Projector (concept image) | output | design reference | Hologram target for the projection brief (`projection.py`) |
| 7 | 8K Cinematic Camera | input | none supplied | The eyes: see / take pics / record (`camera.py`) |

Known shown-price total: **$1,002.97** (Quest Pro + EEG + first drone
variant). Kodak, the Force1 variant, both concepts and the camera show
no price in what he supplied, so none is recorded.

## How the pieces fit the council

- **See** — Quest Pro passthrough + the 8K camera feed: what the
  system looks at becomes a cited capture (`cam-####`) the council
  can be asked about.
- **Hear / speak** — Voice Mode: transcript in, spoken brief out,
  full grand answer on request. EEG state picks the mode: deep focus
  (focus ≥ 0.6) gets the full answer, low focus (< 0.3) gets the
  spoken brief first. Ratios only — focus ≈ (beta+SMR)/theta,
  relaxation ≈ alpha/beta. A UX signal, not a medical claim.
- **Show** — Kodak projector throws the projection brief on a wall;
  the hologram puck is the same brief as a face in the room: question,
  top 3 facts, consensus, confidence. Max 9 lines by design.
- **Gesture** — the flying disc is the controller: push = next expert,
  pull = previous, hold = grand answer, flip = re-route, wave = stop.

## Honesty notes

- No device here is physically connected to this repo's runtime; each
  module is the adapter contract + the data exactly as supplied.
- Voice Mode and the hologram are **his concept images**, recorded as
  design references, not products.
- The Kodak listing title was truncated in his screenshot ("and Micro
  SD — Compatible with iPhone iPad Android Pho…"); recorded as shown.
