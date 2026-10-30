"""Registry of the 13 merged sources."""
from .sources_data import SOURCES

_BY_ID = {s["id"]: s for s in SOURCES}


def list_sources():
    return list(SOURCES)


def get_source(expert_id):
    if expert_id not in _BY_ID:
        raise KeyError(f"unknown expert '{expert_id}' -- "
                       f"known: {', '.join(_BY_ID)}")
    return _BY_ID[expert_id]


def expert_ids():
    return [s["id"] for s in SOURCES]


def total_files():
    return sum(len(s["files"]) for s in SOURCES)


def docker_images():
    return [(s["id"], s["docker"]) for s in SOURCES if s["docker"]]


def routing_examples():
    """(text, expert_id) examples derived from the sources themselves:
    every file description is an example of its expert's territory."""
    out = []
    for s in SOURCES:
        out.append((s["domain"], s["id"]))
        for path, desc in s["files"]:
            out.append((f"{path} {desc}", s["id"]))
    return out