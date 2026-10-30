"""Text utilities: tokenizing, TF-IDF, cosine -- pure stdlib."""
import math
import re
from collections import Counter

STOP = set("a an the and or of to for in on with is are be by at as it its this that from into over under per".split())
_TOKEN = re.compile(r"[a-z0-9][a-z0-9_\-\.]*")


ALIASES = {
    "zstandard": "zstd", "compressor": "compress", "compression": "compress",
    "compressing": "compress", "verification": "verify", "verifying": "verify",
    "verifies": "verify", "checksums": "checksum", "credentials": "credential",
    "emulators": "emulator", "emulation": "emulator",
}


def _stem(t):
    t = ALIASES.get(t, t)
    if len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
        t = t[:-1]
    return ALIASES.get(t, t)


def tokens(text):
    return [_stem(t) for t in _TOKEN.findall(text.lower())
            if t not in STOP and len(t) > 1]


def tfidf_vectors(docs):
    """docs: list[str] -> (vectors: list[dict], idf: dict)"""
    toks = [tokens(d) for d in docs]
    n = max(len(docs), 1)
    df = Counter()
    for ts in toks:
        for t in set(ts):
            df[t] += 1
    idf = {t: math.log((n + 1) / (c + 1)) + 1.0 for t, c in df.items()}
    vecs = []
    for ts in toks:
        c = Counter(ts)
        total = max(len(ts), 1)
        vecs.append({t: (cnt / total) * idf.get(t, 1.0) for t, cnt in c.items()})
    return vecs, idf


def query_vector(query, idf):
    ts = tokens(query)
    c = Counter(ts)
    total = max(len(ts), 1)
    return {t: (cnt / total) * idf.get(t, 1.0) for t, cnt in c.items()}


def cosine(a, b):
    if not a or not b:
        return 0.0
    dot = sum(v * b.get(t, 0.0) for t, v in a.items())
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)