"""The Council: ask each expert, ask one, or ask the routed best."""
from .router import route


class Council:
    def __init__(self, experts):
        self.experts = experts  # dict id -> Expert

    def ask_one(self, expert_id, question, polish=False):
        if expert_id not in self.experts:
            raise KeyError(f"unknown expert '{expert_id}' -- known: "
                           f"{', '.join(self.experts)}")
        return self.experts[expert_id].ask(question, polish=polish)

    def ask_each(self, question, expert_ids=None, polish=False):
        """Ask every expert (or the given subset). Every expert answers
        -- even a low-confidence one, so you can see who knows what."""
        ids = expert_ids or list(self.experts)
        return [self.experts[eid].ask(question, polish=polish)
                for eid in ids]

    def ask_routed(self, question, top=3, polish=False):
        ranked = route(question, self.experts)
        return [(eid, score, self.experts[eid].ask(question, polish=polish))
                for eid, score in ranked[:top]]
