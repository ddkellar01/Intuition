"""One Expert per merged source. Ask it, it answers from its own files."""
from dataclasses import dataclass, field

from . import llm, ml
from .lml import LocalModel
from .registry import list_sources


@dataclass
class Answer:
    expert_id: str
    expert_name: str
    question: str
    facts: list = field(default_factory=list)  # [(path, desc, score)]
    confidence: float = 0.0
    text: str = ""

    def to_dict(self):
        return {
            "expert_id": self.expert_id,
            "expert_name": self.expert_name,
            "question": self.question,
            "facts": [{"path": p, "description": d, "score": s}
                      for p, d, s in self.facts],
            "confidence": self.confidence,
            "answer": self.text,
        }


class Expert:
    def __init__(self, source):
        self.source = source
        self.id = source["id"]
        self.name = source["name"]
        self.local = LocalModel(source)  # LML: this expert's own model

    def relevance(self, question):
        return self.local.relevance(question)

    def ask(self, question, polish=False):
        facts = self.local.retrieve(question)
        best = facts[0][2] if facts else 0.0
        conf = ml.confidence(best, self.local.relevance(question))
        text = llm.compose_answer(self.name, question, facts)
        if polish:
            text = llm.polish(text, question)
        return Answer(self.id, self.name, question, facts, conf, text)


def build_experts():
    return {s["id"]: Expert(s) for s in list_sources()}
