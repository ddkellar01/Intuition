"""Flying-disc drone gestures -- hands-free control of the council.

The drones Darion supplied are hand-operated: your hand is the
controller. Gestures map to council commands -- stated here, nowhere
hidden:

  push ......... next expert
  hold ......... grand answer
  pull ......... previous expert
  flip ......... re-route the question (new ranking)
  wave ......... stop / dismiss

State is a cursor over the 13 experts plus the last question asked.
"""

GESTURES = {
    "push": "next_expert",
    "hold": "grand_answer",
    "pull": "prev_expert",
    "flip": "reroute",
    "wave": "stop",
}


class DroneControl:
    def __init__(self, brain):
        self.brain = brain
        from .registry import expert_ids
        self.expert_ids = expert_ids()
        self.cursor = 0
        self.last_question = None

    def gesture(self, name, question=None):
        if name not in GESTURES:
            raise ValueError(f"unknown gesture '{name}' -- "
                             f"known: {', '.join(GESTURES)}")
        cmd = GESTURES[name]
        if question:
            self.last_question = question
        if cmd == "next_expert":
            self.cursor = (self.cursor + 1) % len(self.expert_ids)
            return ("expert", self.expert_ids[self.cursor])
        if cmd == "prev_expert":
            self.cursor = (self.cursor - 1) % len(self.expert_ids)
            return ("expert", self.expert_ids[self.cursor])
        if cmd == "grand_answer":
            if not self.last_question:
                return ("error", "hold needs a question first")
            return ("grand", self.brain.grand(self.last_question))
        if cmd == "reroute":
            if not self.last_question:
                return ("error", "flip needs a question first")
            return ("route", self.brain.route(self.last_question))
        return ("stopped", None)
