"""CLI: intuition list | files <expert> | ask <expert> <q...>
        intuition ask-all <q...> | route <q...> | grand <q...>
        intuition hardware [device] | voice <q...> | project <q...>
        intuition stats | docker"""
import json
import sys

from .asi import Intuition
from .registry import docker_images, get_source, list_sources, total_files
from .report import grand_report
from .router import nnl_accuracy

USAGE = __doc__


def _q(args):
    return " ".join(args)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(USAGE)
        return 0
    cmd, rest = argv[0], argv[1:]

    if cmd == "list":
        for s in list_sources():
            docker = f"  [{s['docker']}]" if s["docker"] else ""
            print(f"{s['id']:18} {s['name']} -- {s['root']} "
                  f"({len(s['files'])} files){docker}")
        print(f"\n{len(list_sources())} experts, {total_files()} merged files")
        return 0

    if cmd == "files":
        if not rest:
            print("usage: intuition files <expert>"); return 2
        s = get_source(rest[0])
        print(f"{s['name']} -- {s['title_as_supplied']}\nroot: {s['root']}")
        for path, desc in s["files"]:
            print(f"  {path}  # {desc}")
        return 0

    if cmd == "hardware":
        from .hardware import get_device, known_cost_total, list_devices
        if rest:
            d = get_device(rest[0])
            price = f"${d['price_usd']}" if d["price_usd"] else "price not shown"
            print(f"{d['name']} [{d['kind']}] -- {price} ({d['price_note']})")
            print(f"source: {d['source']}")
            for s in d["specs"]:
                print(f"  - {s}")
            for v in d.get("variants", []):
                vp = f"${v['price_usd']}" if v["price_usd"] else "price not shown"
                print(f"  variant: {v['name']} -- {vp}, {v['rating']}")
            print(f"role: {d['role']}")
            return 0
        for d in list_devices():
            price = f"${d['price_usd']}" if d["price_usd"] else "no price shown"
            print(f"{d['id']:18} {d['name']} [{d['kind']}] -- {price}")
        print(f"\n{len(list_devices())} devices/concepts added; "
              f"known shown-price total: ${known_cost_total()} "
              f"(first drone variant; Kodak, concepts, camera show no price)")
        return 0

    if cmd == "docker":
        for eid, img in docker_images():
            print(f"{eid:18} {img}")
        return 0

    if cmd == "stats":
        print(f"experts: {len(list_sources())}")
        print(f"merged files: {total_files()}")
        print(f"docker images merged: {len(docker_images())}")
        print(f"NNL routing accuracy (held on training examples): "
              f"{nnl_accuracy():.3f}")
        return 0

    if cmd in ("ask", "ask-all", "route", "grand", "voice", "project"):
        brain = Intuition()
        if cmd == "ask":
            if len(rest) < 2:
                print("usage: intuition ask <expert> <question...>"); return 2
            ans = brain.ask(rest[0], _q(rest[1:]))
            print(ans.text)
            print(f"\nconfidence: {ans.confidence}")
            return 0
        if not rest:
            print(f"usage: intuition {cmd} <question...>"); return 2
        question = _q(rest)
        if cmd == "route":
            for eid, score in brain.route(question):
                print(f"{score:.4f}  {eid}")
            return 0
        if cmd == "ask-all":
            for ans in brain.ask_each(question):
                print(ans.text)
                print(f"confidence: {ans.confidence}\n---")
            return 0
        if cmd == "voice":
            from .voice import VoiceSession
            brief, _ = VoiceSession(brain).hear(question)
            print(brief)
            return 0
        if cmd == "project":
            from .projection import projection_brief
            print(projection_brief(brain.grand(question)))
            return 0
        if cmd == "grand":
            g = brain.grand(question)
            if "--report" in rest:
                print(grand_report(g))
            elif "--json" in rest:
                print(json.dumps({
                    "question": g.question, "confidence": g.confidence,
                    "consensus": g.consensus,
                    "answers": [a.to_dict() for a in g.answers]}, indent=2))
            else:
                print(g.text)
            return 0

    print(f"unknown command '{cmd}'\n{USAGE}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
