"""Router: which expert(s) should answer a question?

ML ensemble of LML relevance + SML kNN votes + NNL MLP probabilities.
The NNL is trained once, lazily, on the sources' own examples.
"""
from . import ml
from .nnl import MLP
from .registry import expert_ids, routing_examples
from .sml import KNNRouter

_knn = None
_mlp = None


def _models():
    global _knn, _mlp
    if _knn is None:
        examples = routing_examples()
        _knn = KNNRouter(examples)
        _mlp = MLP(expert_ids()).train(examples, epochs=40)
    return _knn, _mlp


def route(question, experts):
    """experts: dict id -> Expert. Returns [(expert_id, score)] ranked."""
    knn, mlp = _models()
    lml_scores = {eid: e.relevance(question) for eid, e in experts.items()}
    scores = ml.ensemble_scores(
        lml_scores, knn.predict(question), mlp.predict(question),
        expert_ids())
    return sorted(scores.items(), key=lambda kv: -kv[1])


def nnl_accuracy():
    _, mlp = _models()
    return mlp.accuracy(routing_examples())
