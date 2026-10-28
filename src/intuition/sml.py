"""SML -- Small Machine Learning: kNN routing + a tiny logistic scorer.

Deterministic, stdlib-only. Used as one vote in the routing ensemble.
"""
import math
from .text import tokens


class KNNRouter:
    """kNN over labelled example texts (one label = one expert id)."""

    def __init__(self, examples):
        # examples: list[(text, label)]
        self.examples = examples
        vocab = {}
        for text, _ in examples:
            for t in set(tokens(text)):
                vocab[t] = vocab.get(t, 0) + 1
        self.vocab = vocab

    def _vec(self, text):
        s = set(tokens(text))
        return {t: 1.0 for t in s if t in self.vocab}

    @staticmethod
    def _sim(a, b):
        if not a or not b:
            return 0.0
        inter = len(set(a) & set(b))
        return inter / math.sqrt(len(a) * len(b))

    def predict(self, query, k=5):
        q = self._vec(query)
        scored = [(self._sim(q, self._vec(text)), label)
                  for text, label in self.examples]
        scored.sort(reverse=True)
        votes = {}
        for sim, label in scored[:k]:
            if sim > 0:
                votes[label] = votes.get(label, 0.0) + sim
        return votes  # label -> vote weight


def logistic(x, steepness=6.0, midpoint=0.18):
    """Squash a raw retrieval score into a 0..1 confidence."""
    return 1.0 / (1.0 + math.exp(-steepness * (x - midpoint)))
