"""EEG adapter for the SereniBrain / iHANK neurofeedback headband.

Input = band powers in the bands the app itself shows: Delta, Theta,
Alpha, Beta, Gamma, SMR. Output = a council context: focus and
relaxation scores plus the answer mode they imply.

Scores are plain ratios, stated here -- no trained model, no medical
claims. This is a focus/relaxation UX signal, nothing clinical.
"""
from dataclasses import dataclass

BANDS = ("delta", "theta", "alpha", "beta", "gamma", "smr")


@dataclass
class EEGReading:
    delta: float
    theta: float
    alpha: float
    beta: float
    gamma: float
    smr: float

    def total(self):
        return sum(getattr(self, b) for b in BANDS) or 1.0

    def ratios(self):
        t = self.total()
        return {b: round(getattr(self, b) / t, 4) for b in BANDS}


def classify(reading):
    """-> (focus, relaxation, mode) each score 0..1.
    focus      ~ beta + smr share against theta (engagement pattern)
    relaxation ~ alpha share against beta
    mode: 'full' (deep focus), 'brief' (low focus: spoken brief first),
          'standard' otherwise."""
    r = reading.ratios()
    focus = round(min(1.0, (r["beta"] + r["smr"]) / max(r["theta"], 0.01) / 3.0), 4)
    relaxation = round(min(1.0, r["alpha"] / max(r["beta"], 0.01) / 3.0), 4)
    mode = "full" if focus >= 0.6 else "brief" if focus < 0.3 else "standard"
    return focus, relaxation, mode


def council_context(reading):
    focus, relaxation, mode = classify(reading)
    return {"eeg_focus": focus, "eeg_relaxation": relaxation,
            "answer_mode": mode, "band_ratios": reading.ratios()}
