# The Council — ask each, ask all, grand answer

## Three ways to ask

1. **Ask one** — `intuition ask <expert> "<question>"`
   That expert's LML model retrieves from its own files only; the LLM
   layer composes the answer from those facts, citing each file.
2. **Ask each** — `intuition ask-all "<question>"`
   All 13 experts answer the same question. Low-confidence answers are
   shown, not hidden — you can see who knows what and who doesn't.
3. **Grand answer** — `intuition grand "<question>"`
   All 13 answers, synthesized: best-grounded facts ranked by
   confidence, consensus concepts (2+ experts), unique insights
   (1 expert), overall confidence = mean of the 13.

## Routing (when you don't know who to ask)

`intuition route "<question>"` ranks all 13 experts with the ML
ensemble: LML domain relevance (0.50) + SML kNN votes (0.30) + NNL
MLP probability (0.20). The NNL is trained on the sources' own file
descriptions (shuffled SGD — unshuffled, it collapses to the last
expert it saw; that bug was caught and fixed during the build).

## Honesty rules

- An expert cannot cite a file it does not have.
- The grand answer contains nothing no expert said.
- Confidence is computed (logistic over retrieval strength), not asserted.
- "ASI" is an architecture position — the synthesis layer — not a
  claim about the system's intelligence.
