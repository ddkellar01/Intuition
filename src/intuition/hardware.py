"""Hardware layer -- everything Darion added on 2026-10-28, as supplied.

Six entries from his Amazon screenshots / screen video / concept images.
Prices and ratings are recorded ONLY where the screenshot showed them;
where none was visible the field is None -- never invented.

Every device has a stated software role in Intuition (interface layer):
  quest_pro ....... mixed-reality council interface (spatial display + tracking input)
  kodak_projector . shared-room projection output for grand answers
  flying_drones ... gesture-controlled hover input (hand-operated, no controller)
  eeg_headband .... brainwave context input (focus / relaxation state)
  voice_mode ...... voice-first interface spec (mic orb UI as supplied)
  holo_projector .. hologram display target (concept image as supplied)
  camera_8k ....... the eyes: 8K cinematic camera -- see, take pics, record
                    (added by Darion 2026-10-28, no brand/price supplied)
"""

DEVICES = [
    {
        "id": "quest_pro",
        "name": "Meta Quest Pro",
        "kind": "interface",  # display + tracking input
        "source": "Amazon screen video, Meta Store listing",
        "price_usd": 799.99,
        "price_note": "-20%, list $999.99, In Stock (video frame); used -25% $749.99 also shown",
        "rating": "3.8 (778)",
        "specs": [
            "Quest Pro System style, 256GB storage, 12GB RAM (as shown in video details)",
            "Full color mixed-reality passthrough -- work in VR while seeing the physical world",
            "Self-tracking controllers with advanced haptics; eye/face tracking for Meta Avatars",
            "Counterbalanced, sleeker ergonomic headset; multiple room-sized displays in VR",
            "In the box (as listed): VR headset, Meta Quest Pro controllers, charging dock, "
            "partial light blockers, protective cover, wrist straps, stylus tips, charging cables",
        ],
        "role": "The council in mixed reality: ask an expert face-to-face in passthrough, "
                "pin each expert's answer as a room-sized panel, grand answer on the main panel.",
    },
    {
        "id": "kodak_projector",
        "name": "Kodak Ultra Mini Portable Projector",
        "kind": "output",
        "source": "Amazon screenshot, KODAK Store listing",
        "price_usd": None,
        "price_note": "no price visible in the screenshot supplied",
        "rating": "4.0 (2,951)",
        "specs": [
            "HD 1080p support, LED DLP, rechargeable pico projector",
            "Up to 100 inch display, built-in speaker",
            "HDMI, USB and Micro SD inputs (title as shown, truncated in screenshot)",
            "Compatible with iPhone, iPad, Android phones (title as shown, truncated)",
            "Color: Silver (as shown)",
        ],
        "role": "Shared-room output: throws the projection brief of a grand answer "
                "(see projection.py) onto a wall at up to 100 inches.",
    },
    {
        "id": "flying_drones",
        "name": "Hand Operated Flying Disc Drones",
        "kind": "input",
        "source": "Amazon search screenshot: 'flying disc drone'",
        "price_usd": None,
        "price_note": "three listings shown, recorded under variants",
        "rating": None,
        "specs": [
            "Hand operated / hands-free motion control -- gesture input, no controller",
            "360 degree hover / flip flying-disc (UFO) form factor with LED lights",
        ],
        "variants": [
            {"name": "Hand Operated Flying Toy Drone for Kids, 360 Hands Free Motion",
             "price_usd": 22.99, "rating": "4.3 (696)", "note": "1K+ bought in past month, Ages: 6 years and up"},
            {"name": "Hand Operated Drone Toy for Kids - Easy Fly Hover Drone with AI Motion",
             "price_usd": 16.99, "rating": "3.8 (230)", "note": "200+ bought in past month, Save 5% on $29.00 of select items"},
            {"name": "Force1 Scoot Hand Operated Drone for Kids or Adults - Hands Free",
             "price_usd": None, "rating": "4.0 (11.8K)", "note": "1K+ bought in past month; price cut off in screenshot"},
        ],
        "role": "Gesture input for the council: hand gestures over the hovering disc map to "
                "council commands (see drone.py) -- push to advance expert, hold to ask for "
                "the grand answer, flip to re-route the question.",
    },
    {
        "id": "eeg_headband",
        "name": "EEG Neurofeedback Headband (SereniBrain / iHANK)",
        "kind": "input",
        "source": "Amazon screenshot, Brand: SereniBrain",
        "price_usd": 179.99,
        "price_note": "-10% (as shown)",
        "rating": "4.0 (115)",
        "specs": [
            "EEG neurofeedback headband for meditation & brainwave monitoring",
            "Real-Time Brain Activity Tracker with App -- Train Focus, Relaxation & Sleep Preparation",
            "Band ratios shown in app: Delta, Theta, Alpha, Beta, Gamma, SMR; current score example 86",
            "Color: Dark Grey (as shown); 50+ bought in past month",
        ],
        "role": "Brainwave context input: band powers become a focus/relaxation state "
                "(see eeg.py) that adapts answer length -- deep focus gets the full "
                "grand answer, low focus gets the short spoken brief first.",
    },
    {
        "id": "voice_mode",
        "name": "Voice Mode UI (concept as supplied)",
        "kind": "interface",
        "source": "concept image supplied by Darion (not a product listing)",
        "price_usd": None,
        "price_note": "design reference, not a purchasable product",
        "rating": None,
        "specs": [
            "Glassmorphism voice interface on blue/violet gradient: central glowing mic orb "
            "with waveform, transcript card with speaker/copy/like actions",
            "Left rail: sparkle, home, chat, layers, settings icons; Voice Mode toggle pill",
            "Bottom chat input with mic button",
        ],
        "role": "The voice-first face of Intuition (see voice.py): speak the question, hear "
                "the short spoken brief, open the full written grand answer on request.",
    },
    {
        "id": "holo_projector",
        "name": "Holographic Assistant Projector (concept as supplied)",
        "kind": "output",
        "source": "concept image supplied by Darion (not a product listing)",
        "price_usd": None,
        "price_note": "design reference, not a purchasable product",
        "rating": None,
        "specs": [
            "Round puck base projector casting a volumetric holographic AI face "
            "with orbital ring UI, viewed by a standing user",
        ],
        "role": "Display target the projection brief is formatted for: one face, one "
                "answer, a few large lines -- the grand answer as a hologram, fed by the "
                "Kodak projector / Quest Pro class of outputs.",
    },
    {
        "id": "camera_8k",
        "name": "8K Cinematic Camera",
        "kind": "input",
        "source": "added by Darion in chat 2026-10-28 -- no brand, model or price supplied",
        "price_usd": None,
        "price_note": "no brand/model/price supplied -- none invented",
        "rating": None,
        "specs": [
            "8K cinematic video recording",
            "Still photography (take pics)",
            "Live vision feed (to see)",
        ],
        "role": "The eyes of Intuition (see camera.py): the live feed is the council's "
                "vision input, stills are captured as cited evidence frames, and 8K "
                "recordings are sessions the experts can be asked about.",
    },
]

_BY_ID = {d["id"]: d for d in DEVICES}


def list_devices():
    return list(DEVICES)


def get_device(device_id):
    if device_id not in _BY_ID:
        raise KeyError(f"unknown device '{device_id}' -- known: {', '.join(_BY_ID)}")
    return _BY_ID[device_id]


def devices_by_kind(kind):
    return [d for d in DEVICES if d["kind"] == kind]


def known_cost_total():
    """Sum of prices actually shown in his screenshots (variants at their
    first-listed price). Concept art and the Kodak listing show no price
    and are excluded -- stated, not silently zero-filled."""
    total = 0.0
    for d in DEVICES:
        if d["price_usd"]:
            total += d["price_usd"]
    total += 22.99  # first flying-disc drone variant, as shown
    return round(total, 2)
