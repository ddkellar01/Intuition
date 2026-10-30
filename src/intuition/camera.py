"""8K cinematic camera -- the eyes of Intuition.

Three modes, exactly as Darion named them: SEE (live vision feed),
TAKE PICS (stills, kept as cited evidence frames), RECORD (8K sessions).

No camera is connected in this environment: this module is the adapter
contract. A capture carries a caller-supplied scene description (from
whatever vision pipeline is attached); Intuition can then be ASKED
about what the camera captured, and the capture is cited by id --
the same grounding rule as every expert answer.
"""
import time
from dataclasses import dataclass, field

MODES = ("see", "pic", "record")


@dataclass
class Capture:
    capture_id: str
    mode: str               # see | pic | record
    resolution: str         # "8K" for record; stills/feed as supplied
    description: str = ""   # scene description from the vision pipeline
    duration_s: float = 0.0  # record mode only
    ts: float = field(default_factory=time.time)

    def citation(self):
        return f"[{self.capture_id} | {self.mode} | {self.resolution}] {self.description}"


class Camera8K:
    def __init__(self):
        self.captures = []
        self._n = 0

    def _add(self, mode, description, resolution="8K", duration_s=0.0):
        self._n += 1
        cap = Capture(f"cam-{self._n:04d}", mode, resolution,
                      description, duration_s)
        self.captures.append(cap)
        return cap

    def see(self, scene_description):
        """One live-feed frame, described by the vision pipeline."""
        return self._add("see", scene_description, resolution="8K feed")

    def take_pic(self, scene_description):
        return self._add("pic", scene_description, resolution="8K still")

    def record(self, scene_description, duration_s):
        return self._add("record", scene_description,
                         resolution="8K", duration_s=float(duration_s))

    def ask_about(self, brain, capture, question=None):
        """Ask the council about a capture; the capture is the context."""
        q = question or f"what is in this capture: {capture.description}"
        q = f"{q} (camera capture {capture.capture_id}: {capture.description})"
        return brain.grand(q)