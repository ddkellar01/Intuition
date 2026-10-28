"""Smoke: list -> ask one -> ask each -> grand. Run: python scripts/smoke.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from intuition import Intuition, list_sources, total_files

brain = Intuition()
print(f"experts: {len(list_sources())}  merged files: {total_files()}")

ans = brain.ask("malware_sandbox", "eBPF kernel syscall telemetry and pcap capture")
assert "ebpf_collector.py" in ans.text, ans.text
print(f"ask-one OK (confidence {ans.confidence})")

answers = brain.ask_each("what is mixture of experts routing")
assert len(answers) == 13
print("ask-each OK: 13 answers")

g = brain.grand("Model Context Protocol MCP tool execution and safety")
assert len(g.answers) == 13 and g.ranked_facts
print(f"grand OK (confidence {g.confidence}, consensus terms: {len(g.consensus)})")

from intuition.hardware import known_cost_total, list_devices
from intuition.camera import Camera8K
from intuition.eeg import EEGReading, council_context
from intuition.projection import projection_brief
from intuition.voice import VoiceSession

assert len(list_devices()) == 8 and known_cost_total() == 1002.97
from intuition.lie_detector import PhysioReading, assess
_base = PhysioReading(2.0, 70, 14)
assert assess(PhysioReading(8.0, 110, 24), _base)["state"] == "high"
assert assess(_base, _base)["follow_up"] is False
print("lie detector OK: calm unflagged, stressed flagged for follow-up")
cam = Camera8K()
cap = cam.take_pic("a whiteboard with a system diagram")
ctx = council_context(EEGReading(5, 5, 10, 40, 10, 30))
assert ctx["answer_mode"] == "full"
brief, _ = VoiceSession(brain).hear("what is a honeypot")
assert "grand answer" in brief
assert "CONFIDENCE" in projection_brief(g)
print(f"hardware OK: 8 devices, camera {cap.capture_id}, EEG mode full, voice + projection briefs OK")
print("\n" + g.text)
print("\nSMOKE GREEN")
