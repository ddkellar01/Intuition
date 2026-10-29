"""
Intuition Council Module
"""

# Relative import fix for local router module within the package
from .router import router


class Council:
    def __init__(self, experts):
        """
        experts: list of Expert objects or dict mapping expert_id -> Expert
        """
        if isinstance(experts, list):
            self.experts = {e.id: e for e in experts}
        else:
            self.experts = experts  # dict id -> Expert

    def ask(self, expert_id, question, polish=False):
        if expert_id not in self.experts:
            raise ValueError(
                f"Unknown expert '{expert_id}'. Known: "
                f"{', '.join(self.experts.keys())}"
            )
        return self.experts[expert_id].ask(question, polish=polish)

    def route(self, question, expert_ids=None, polish=False):
        """
        Route question to specific expert(s) or all experts.
        """
        if expert_ids is None:
            ids = list(self.experts.keys())
        elif isinstance(expert_ids, str):
            ids = [expert_ids]
        else:
            ids = expert_ids

        results = {}
        for eid in ids:
            if eid in self.experts:
                results[eid] = self.ask(eid, question, polish=polish)
        return results

    def select(self, question, top=3, polish=False):
        """
        Select top matching experts for a question using router logic.
        """
        ranked = router.rank(question, self.experts)
        results = []
        for eid, score in ranked[:top]:
            answer = self.ask(eid, question, polish=polish)
            results.append({"expert_id": eid, "score": score, "answer": answer})
        return results
