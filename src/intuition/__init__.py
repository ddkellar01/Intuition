"""Intuition -- merge of 13 AI / agent systems into one council.

Ask each expert on its own, ask all of them, or get the grand answer.
AI stack: ASI (synthesis layer) / NNL (MLP router) / LLM (grounded
reasoner) / ML (routing ensemble) / SML (kNN + logistic) / LML
(per-expert local models). Pure Python stdlib.
"""
from .asi import Intuition
from .registry import list_sources, get_source, total_files, docker_images

__version__ = "0.1.0"
__all__ = ["Intuition", "list_sources", "get_source", "total_files",
           "docker_images", "__version__"]