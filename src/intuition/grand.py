"""The Grand Answer: ask ALL experts, then synthesize one answer.

Synthesis rules (stated, not hidden):
  - Facts are ranked by their expert's confidence.
  - A concept is CONSENSUS when 2+ experts independently surface it
    (shared tokens across their retrieved facts).
  - A fact is a UNIQUE insight when only its expert surfaces it.
  - Nothing is added that no expert said: the grand answer is built
    only from the 13 answers.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass, field

from .text import tokens


@dataclass
class GrandAnswer:
    question: str
    answers: list = field(default_factory=list)      # list[Answer]
    ranked_facts: list = field(default_factory=list)  # [(expert, path, desc, conf)]
    consensus: list = field(default_factory=list)     # [(concept, [expert_ids])]
    unique: list = field(default_factory=list)        # [(expert, path, desc)]
    confidence: float = 0.0
    text: str = ""


def _concepts(answers):
    concept_experts = defaultdict(set)
    for a in answers:
        seen = set()
        for _, desc, _ in a.facts:
            for t in set(tokens(desc)):
                if len(t) > 3:
                    seen.add(t)
        for t in seen:
            concept_experts[t].add(a.expert_id)
    return concept_experts


def synthesize(question, answers):
    ranked = []
    for a in answers:
        for path, desc, _ in a.facts:
            ranked.append((a.expert_name, path, desc, a.confidence))
    ranked.sort(key=lambda r: -r[3])
    ranked = ranked[:14]

    concept_experts = _concepts(answers)
    consensus = sorted(
        [(t, sorted(ids)) for t, ids in concept_experts.items()
         if len(ids) >= 2],
        key=lambda r: -len(r[1]))[:10]

    consensus_tokens = {t for t, _ in consensus}
    unique = []
    for a in answers:
        for path, desc, _ in a.facts:
            toks = {t for t in tokens(desc) if len(t) > 3}
            if toks and not (toks & consensus_tokens):
                unique.append((a.expert_name, path, desc))
    unique = unique[:8]

    conf = round(sum(a.confidence for a in answers) / max(len(answers), 1), 4)

    lines = [f"GRAND ANSWER -- \"{question}\"", ""]
    lines.append("Best-grounded facts across all 13 experts:")
    for name, path, desc, c in ranked:
        lines.append(f"- [{name} | confidence {c}] {desc} ({path})")
    lines.append("")
    lines.append("Consensus (2+ experts independently):")
    if consensus:
        for term, ids in consensus:
            lines.append(f"- {term}: {', '.join(ids)}")
    else:
        lines.append("- none -- the experts' territories do not overlap on this question")
    lines.append("")
    lines.append("Unique insights (one expert only):")
    for name, path, desc in unique:
        lines.append(f"- [{name}] {desc} ({path})")
    if not unique:
        lines.append("- none")
    lines.append("")
    lines.append(f"Overall confidence: {conf} "
                 f"(mean of {len(answers)} expert confidences)")
    return GrandAnswer(question, answers, ranked, consensus, unique,
                       conf, "\n".join(lines))
