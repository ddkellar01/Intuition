"""LLM -- Large Language Model reasoner (KB-grounded).

Offline by default: composes an answer ONLY from the facts the expert's
local model retrieved, citing the file each fact came from. It never
invents a file or a capability that is not in the merged sources.

If GEMINI_API_KEY is set, `polish()` optionally rewrites the grounded
draft with gemini-2.5-flash via the public API -- the grounded facts
and citations are passed in and the result is still labelled as this
expert's answer. Any API failure falls back to the grounded draft.
"""
import json
import os
import urllib.request


def compose_answer(expert_name, question, facts):
    """facts: list[(path, description, score)] -> grounded answer text."""
    if not facts:
        return (f"{expert_name}: nothing in my merged structure answers "
                f"\"{question}\" directly. My domain is different -- try "
                f"the grand answer, which asks every expert.")
    lines = [f"{expert_name} -- on \"{question}\":"]
    for path, desc, _ in facts:
        lines.append(f"- {desc} ({path})")
    lines.append(
        "That is what my own files cover; anything beyond them is "
        "another expert's territory.")
    return "\n".join(lines)


def polish(text, question):
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        return text
    try:
        body = json.dumps({
            "contents": [{"parts": [{"text":
                "Rewrite this grounded answer clearly, keeping every "
                "file citation exactly as written. Do not add facts.\n\n"
                f"Question: {question}\n\n{text}"}]}],
        }).encode()
        req = urllib.request.Request(
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"gemini-2.5-flash:generateContent?key={key}",
            data=body, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read())
        return data["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception:
        return text
