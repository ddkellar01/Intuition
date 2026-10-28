import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest

from intuition import Intuition
from intuition.camera import Camera8K
from intuition.cli import main
from intuition.drone import DroneControl, GESTURES
from intuition.eeg import EEGReading, classify, council_context
from intuition.hardware import (devices_by_kind, get_device,
                                known_cost_total, list_devices)
from intuition.projection import MAX_LINES, projection_brief
from intuition.voice import VoiceSession, spoken_brief


@pytest.fixture(scope="module")
def brain():
    return Intuition()


# --- all is included --------------------------------------------------
def test_eight_devices_included():
    ids = [d["id"] for d in list_devices()]
    assert ids == ["quest_pro", "kodak_projector", "flying_drones",
                   "eeg_headband", "voice_mode", "holo_projector",
                   "camera_8k", "lie_detector"]


def test_every_device_has_role_and_source():
    for d in list_devices():
        assert d["role"] and d["source"] and d["specs"]


def test_prices_exactly_as_shown():
    assert get_device("quest_pro")["price_usd"] == 799.99
    assert get_device("eeg_headband")["price_usd"] == 179.99
    # Kodak screenshot showed no price -- must stay uninvented
    assert get_device("kodak_projector")["price_usd"] is None
    # camera arrived with no brand/price -- must stay uninvented
    cam = get_device("camera_8k")
    assert cam["price_usd"] is None and "8K" in cam["name"]


def test_all_three_drone_variants_included():
    variants = get_device("flying_drones")["variants"]
    assert len(variants) == 3
    prices = {v["price_usd"] for v in variants}
    assert 22.99 in prices and 16.99 in prices
    assert any("Force1 Scoot" in v["name"] for v in variants)


def test_device_kinds():
    assert {d["id"] for d in devices_by_kind("input")} == {
        "flying_drones", "eeg_headband", "camera_8k", "lie_detector"}
    assert {d["id"] for d in devices_by_kind("output")} == {
        "kodak_projector", "holo_projector"}


def test_known_cost_total_only_counts_shown_prices():
    # 799.99 Quest Pro + 179.99 EEG + 22.99 first drone variant
    assert known_cost_total() == 1002.97


# --- EEG ----------------------------------------------------------------
def test_eeg_focused_reading_gets_full_mode():
    r = EEGReading(delta=5, theta=5, alpha=10, beta=40, gamma=10, smr=30)
    focus, _, mode = classify(r)
    assert focus >= 0.6 and mode == "full"


def test_eeg_drowsy_reading_gets_brief_mode():
    r = EEGReading(delta=40, theta=40, alpha=10, beta=5, gamma=2, smr=3)
    focus, _, mode = classify(r)
    assert focus < 0.3 and mode == "brief"


def test_eeg_context_shape():
    ctx = council_context(EEGReading(10, 10, 20, 20, 10, 10))
    assert ctx["answer_mode"] in ("full", "standard", "brief")
    assert set(ctx["band_ratios"]) == {"delta", "theta", "alpha",
                                       "beta", "gamma", "smr"}


# --- camera --------------------------------------------------------------
def test_camera_three_modes():
    cam = Camera8K()
    a = cam.see("a desk with a laptop")
    b = cam.take_pic("a whiteboard diagram")
    c = cam.record("a drone flight demo", 12.5)
    assert (a.mode, b.mode, c.mode) == ("see", "pic", "record")
    assert len({a.capture_id, b.capture_id, c.capture_id}) == 3
    assert c.duration_s == 12.5 and "8K" in c.resolution
    assert "whiteboard" in b.citation()


def test_camera_ask_about_uses_council(brain):
    cam = Camera8K()
    cap = cam.see("a fake SSH login attempt on a terminal")
    g = cam.ask_about(brain, cap)
    assert len(g.answers) == 13


# --- voice / projection ---------------------------------------------------
def test_voice_brief_is_spoken_style(brain):
    brief, g = VoiceSession(brain).hear("what is a honeypot fake SSH shell")
    assert "grand answer" in brief and "13 experts" in brief
    assert "(" not in brief.split("says:")[0]  # no paths read aloud up front


def test_spoken_brief_built_from_grand(brain):
    g = brain.grand("eBPF telemetry")
    brief = spoken_brief(g)
    assert str(g.confidence) in brief


def test_projection_brief_fits_wall(brain):
    g = brain.grand("Model Context Protocol MCP")
    brief = projection_brief(g)
    assert len(brief.splitlines()) <= MAX_LINES
    assert "CONFIDENCE" in brief and "13 EXPERTS" in brief


# --- drone ------------------------------------------------------------------
def test_drone_gesture_map_complete():
    assert set(GESTURES.values()) == {"next_expert", "grand_answer",
                                      "prev_expert", "reroute", "stop"}


def test_drone_navigation_and_grand(brain):
    d = DroneControl(brain)
    kind, eid = d.gesture("push")
    assert kind == "expert" and eid == d.expert_ids[1]
    kind, eid = d.gesture("pull")
    assert eid == d.expert_ids[0]
    kind, g = d.gesture("hold", question="what is zstd compression")
    assert kind == "grand" and len(g.answers) == 13
    assert d.gesture("wave") == ("stopped", None)
    with pytest.raises(ValueError):
        d.gesture("spin")


# --- lie detector ---------------------------------------------------------
from intuition.lie_detector import PhysioReading, assess, stress_index

BASE = PhysioReading(gsr_us=2.0, heart_rate_bpm=70, respiration_bpm=14)


def test_lie_detector_included_no_price_invented():
    d = get_device("lie_detector")
    assert d["price_usd"] is None and "GSR" in " ".join(d["specs"])


def test_calm_reading_no_flag():
    a = assess(BASE, BASE, topic="the timeline")
    assert a["stress"] == 0.0 and a["state"] == "calm"
    assert a["follow_up"] is False and a["follow_up_question"] is None


def test_stressed_reading_flags_follow_up_not_a_lie():
    hot = PhysioReading(gsr_us=8.0, heart_rate_bpm=110, respiration_bpm=24)
    a = assess(hot, BASE, topic="the timeline")
    assert a["stress"] == 1.0 and a["state"] == "high" and a["follow_up"]
    assert "walk me through the timeline" in a["follow_up_question"]
    # the module must never claim deception
    assert "not deception" in a["note"] and "lying" not in a["state"]


def test_stress_index_bounds():
    assert stress_index(BASE, BASE) == 0.0
    wild = PhysioReading(gsr_us=50, heart_rate_bpm=200, respiration_bpm=60)
    assert stress_index(wild, BASE) == 1.0


# --- CLI ----------------------------------------------------------------------
def test_cli_hardware(capsys):
    assert main(["hardware"]) == 0
    out = capsys.readouterr().out
    assert "quest_pro" in out and "lie_detector" in out and "1002.97" in out


def test_cli_hardware_detail(capsys):
    assert main(["hardware", "eeg_headband"]) == 0
    out = capsys.readouterr().out
    assert "179.99" in out and "Delta" in out


def test_cli_voice_and_project(capsys):
    assert main(["voice", "what is mixture of experts routing"]) == 0
    assert "grand answer" in capsys.readouterr().out
    assert main(["project", "what is a honeypot"]) == 0
    assert "CONFIDENCE" in capsys.readouterr().out
