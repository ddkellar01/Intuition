"""Voice Mode -- the voice-first interface from Darion's concept image.

Pipeline: transcript in -> council -> SPOKEN BRIEF out (short, plain,
no markdown, no file paths read aloud) -> full written answer on
request. The brief is built only from the grand answer's top facts.
"""
import re


def spoken_brief(grand, max_facts=2):
    parts = [f"Here is the grand answer, from all {len(grand.answers)} experts."]
    for name, _, desc, _ in grand.ranked_facts[:max_facts]:
        parts.append(f"{name} says: {desc.rstrip('.')}.")
    if grand.consensus:
        terms = ", ".join(t for t, _ in grand.consensus[:3])
        parts.append(f"The experts agree on: {terms}.")
    parts.append(f"Overall confidence {grand.confidence}. "
                 "Ask for the full answer to hear every expert.")
    text = " ".join(parts)
    return re.sub(r"\s+", " ", text).strip()


class VoiceSession:
    def __init__(self, brain):
        self.brain = brain
        self.last_grand = None

    def hear(self, transcript):
        """A spoken question -> (spoken brief, grand answer object)."""
        self.last_grand = self.brain.grand(transcript)
        return spoken_brief(self.last_grand), self.last_grand

    def full_answer(self):
        if self.last_grand is None:
            return "Nothing asked yet in this voice session."
        return self.last_grand.text