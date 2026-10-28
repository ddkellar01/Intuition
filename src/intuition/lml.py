"""LML -- Local Model Layer: one small local model per expert.

Each expert's local model is its own TF-IDF index over its own files
(name + description as supplied). Asking an expert = querying its local
model. No expert can answer from another expert's files -- that is
what makes 'ask each' mean something.
"""
from .text import tfidf_vectors, query_vector, cosine


class LocalModel:
    def __init__(self, source):
        self.source = source
        self.docs = [f"{path} -- {desc}" for path, desc in source["files"]]
        self.vecs, self.idf = tfidf_vectors(
            [source["domain"]] + self.docs)
        self.domain_vec = self.vecs[0]
        self.file_vecs = self.vecs[1:]

    def relevance(self, question):
        """How relevant is this question to this expert's whole domain?"""
        q = query_vector(question, self.idf)
        return cosine(q, self.domain_vec)

    def retrieve(self, question, top=4):
        """Top matching files in this expert, as (path, description, score)."""
        q = query_vector(question, self.idf)
        scored = []
        for (path, desc), vec in zip(self.source["files"], self.file_vecs):
            s = cosine(q, vec)
            if s > 0:
                scored.append((path, desc, round(s, 4)))
        scored.sort(key=lambda r: -r[2])
        return scored[:top]
