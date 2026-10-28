"""Lie detector sensor -- polygraph-style physiological input.

Signals (the classic polygraph set): skin conductance (GSR / electro-
dermal activity), heart rate, respiration rate -- each compared
against the subject's own calibrated baseline.

HONESTY RULE, stated up front: this sensor measures AROUSAL, not
deception. Elevated GSR / heart rate / respiration means the subject
is stressed or excited -- it does NOT prove a lie, and this module
never outputs a lying/truth verdict. What it outputs is a stress
index and a follow-up flag: 'ask another question here'. That is the
only defensible use, and it is the use Intuition makes of it --
during Voice Mode Q&A, flagged answers get a suggested follow-up
question from the council.
"""
from dataclasses import dataclass


@dataclass
class PhysioReading:
    gsr_us: float          # skin conductance, microsiemens
    heart_rate_bpm: float
    respiration_bpm: float


def stress_index(reading, baseline):
    """0..1 arousal vs baseline. Weights stated: GSR .50 (fastest,
    strongest arousal channel), heart rate .30, respiration .20."""
    gsr = min(1.0, max(0.0, (reading.gsr_us - baseline.gsr_us)
                       / max(baseline.gsr_us, 0.1)))
    hr = min(1.0, max(0.0, (reading.heart_rate_bpm - baseline.heart_rate_bpm) / 40.0))
    resp = min(1.0, max(0.0, (reading.respiration_bpm - baseline.respiration_bpm) / 10.0))
    return round(0.50 * gsr + 0.30 * hr + 0.20 * resp, 4)


def assess(reading, baseline, topic="that answer"):
    """-> dict: stress, state, follow_up flag, follow-up question, note.
    States: calm / elevated / high -- arousal labels, never lie labels."""
    stress = stress_index(reading, baseline)
    state = "calm" if stress < 0.3 else "elevated" if stress < 0.65 else "high"
    follow_up = stress >= 0.3
    return {
        "stress": stress,
        "state": state,
        "follow_up": follow_up,
        "follow_up_question": (
            f"Before we move on -- can you walk me through {topic} once more, "
            f"step by step?" if follow_up else None),
        "note": "arousal is not deception: this flags a moment to ask a "
                "follow-up, never a conclusion about truthfulness",
    }
