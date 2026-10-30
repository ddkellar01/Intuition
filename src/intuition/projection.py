"""Projection brief -- grand answers formatted for a wall / hologram.

Targets: Kodak Ultra Mini projector (up to 100 inch) and the
holographic puck concept. Rule for both: few lines, large ideas --
the question, the top facts, the consensus. Detail stays in the
written grand answer; the projection is the headline layer.
"""
MAX_LINES = 9


def projection_brief(grand):
    lines = [f"Q: {grand.question}", ""]
    for name, _, desc, conf in grand.ranked_facts[:3]:
        lines.append(f"{name}: {desc} ({conf})")
    if grand.consensus:
        lines.append("")
        lines.append("AGREE: " + ", ".join(t for t, _ in grand.consensus[:4]))
    lines.append("")
    lines.append(f"CONFIDENCE: {grand.confidence}  |  {len(grand.answers)} EXPERTS")
    return "\n".join(lines[:MAX_LINES])