"""NNL -- Neural Network Layer: a small MLP with backprop, pure stdlib.

Trained on routing examples derived from the merged sources themselves:
each expert's file descriptions are examples labelled with that expert.
The MLP learns token-hash features -> expert. Deterministic seed, so
training is reproducible and tests are stable.
"""
import hashlib
import math
import random

DIM = 64
HIDDEN = 32


def _features(text):
    from .text import tokens
    x = [0.0] * DIM
    for t in tokens(text):
        h = int(hashlib.md5(t.encode()).hexdigest()[:8], 16)
        x[h % DIM] += 1.0
    n = math.sqrt(sum(v * v for v in x)) or 1.0
    return [v / n for v in x]


class MLP:
    def __init__(self, labels, seed=13):
        self.labels = list(labels)
        rng = random.Random(seed)
        self.w1 = [[rng.uniform(-0.3, 0.3) for _ in range(DIM)] for _ in range(HIDDEN)]
        self.b1 = [0.0] * HIDDEN
        self.w2 = [[rng.uniform(-0.3, 0.3) for _ in range(HIDDEN)] for _ in range(len(labels))]
        self.b2 = [0.0] * len(labels)

    def _forward(self, x):
        h = [math.tanh(sum(w * xi for w, xi in zip(row, x)) + b)
             for row, b in zip(self.w1, self.b1)]
        logits = [sum(w * hj for w, hj in zip(row, h)) + b
                  for row, b in zip(self.w2, self.b2)]
        m = max(logits)
        exps = [math.exp(v - m) for v in logits]
        s = sum(exps) or 1.0
        return h, [e / s for e in exps]

    def train(self, examples, epochs=60, lr=0.5):
        # examples: list[(text, label)]
        data = [(_features(t), self.labels.index(label)) for t, label in examples]
        rng = random.Random(99)
        for _ in range(epochs):
            rng.shuffle(data)  # examples arrive grouped by expert; without
            # shuffling, SGD forgets early experts and collapses to the last
            for x, y in data:
                h, p = self._forward(x)
                delta2 = p[:]
                delta2[y] -= 1.0
                delta1 = [0.0] * HIDDEN
                for j in range(HIDDEN):
                    back = sum(self.w2[c][j] * delta2[c] for c in range(len(self.labels)))
                    delta1[j] = back * (1.0 - h[j] * h[j])
                for c in range(len(self.labels)):
                    for j in range(HIDDEN):
                        self.w2[c][j] -= lr * delta2[c] * h[j]
                    self.b2[c] -= lr * delta2[c]
                for j in range(HIDDEN):
                    for i in range(DIM):
                        if x[i]:
                            self.w1[j][i] -= lr * delta1[j] * x[i]
                    self.b1[j] -= lr * delta1[j]
        return self

    def predict(self, text):
        _, p = self._forward(_features(text))
        return {label: p[i] for i, label in enumerate(self.labels)}

    def accuracy(self, examples):
        if not examples:
            return 0.0
        ok = 0
        for text, label in examples:
            pred = max(self.predict(text).items(), key=lambda kv: kv[1])[0]
            ok += 1 if pred == label else 0
        return ok / len(examples)