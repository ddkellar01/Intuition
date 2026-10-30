"""Markdown report builder for council / grand answers."""


def grand_report(grand):
    lines = [f"# Grand Answer", "", f"**Question:** {grand.question}", "",
             f"**Overall confidence:** {grand.confidence}", "", "## Synthesis", "",
             "```", grand.text, "```", "", "## Every expert, in full", ""]
    for a in grand.answers:
        lines.append(f"### {a.expert_name} (`{a.expert_id}`) -- confidence {a.confidence}")
        lines.append("")
        lines.append(a.text)
        lines.append("")
    return "\n".join(lines)


def answer_report(answer):
    lines = [f"# {answer.expert_name}", "",
             f"**Question:** {answer.question}", "",
             f"**Confidence:** {answer.confidence}", "", answer.text, ""]
    return "\n".join(lines)
