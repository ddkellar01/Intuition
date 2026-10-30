"""ML -- Machine Learning ensemble for routing and confidence.

Combines three independent votes for 'which expert should answer':
  1. LML domain relevance (TF-IDF cosine to the expert's domain text)
  2. SML kNN votes over file-description examples
  3. NNL MLP probabilities
Weights are fixed and stated here -- no hidden magic numbers elsewhere.
"""
from .sml import logistic

WEIGHTS = {"lml": 0.50, "sml": 0.30, "nnl": 0.20}


def ensemble_scores(lml_scores, knn_votes, nnl_probs, expert_ids):
    knn_max = max(knn_votes.values()) if knn_votes else 0.0
    out = {}
    for eid in expert_ids:
        knn = (knn_votes.get(eid, 0.0) / knn_max) if knn_max else 0.0
        out[eid] = round(
            WEIGHTS["lml"] * lml_scores.get(eid, 0.0)
            + WEIGHTS["sml"] * knn
            + WEIGHTS["nnl"] * nnl_probs.get(eid, 0.0), 4)
    return out


def confidence(best_file_score, domain_relevance):
    """Answer confidence from retrieval strength, squashed by logistic."""
    raw = 0.7 * best_file_score + 0.3 * domain_relevance
    return round(logistic(raw), 4)