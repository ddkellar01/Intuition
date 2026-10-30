"""ASI -- the top layer: Intuition itself.

ASI here is not a claim, it is an architecture position: the layer
above every expert that (1) routes a question, (2) can ask any single
expert, (3) can ask each expert, and (4) synthesizes the grand answer.
It adds no facts of its own -- every fact traces to one of the 13
merged sources and the file it came from.
"""
from .council import Council
from .experts import build_experts
from .grand import synthesize
from .router import route


class Intuition:
    def __init__(self):
        self.experts = build_experts()
        self.council = Council(self.experts)

    # ask each / ask one
    def ask(self, expert_id, question, polish=False):
        return self.council.ask_one(expert_id, question, polish=polish)

    def ask_each(self, question, expert_ids=None, polish=False):
        return self.council.ask_each(question, expert_ids, polish=polish)

    # routing
    def route(self, question):
        return route(question, self.experts)

    def ask_routed(self, question, top=3, polish=False):
        return self.council.ask_routed(question, top=top, polish=polish)

    # the grand answer
    def grand(self, question, polish=False):
        answers = self.council.ask_each(question, polish=polish)
        return synthesize(question, answers)