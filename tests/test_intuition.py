import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest

from intuition import Intuition, docker_images, get_source, list_sources, total_files
from intuition.cli import main
from intuition.registry import expert_ids, routing_examples
from intuition.router import nnl_accuracy


@pytest.fixture(scope="module")
def brain():
    return Intuition()


# --- the merge -------------------------------------------------------
def test_thirteen_sources_merged():
    assert len(list_sources()) == 13


def test_all_expert_ids():
    assert expert_ids() == [
        "gemini_frontier", "grok", "claude_code", "deepseek",
        "workspace_studio", "google_flow", "copilot", "perplexity",
        "codex", "deconstruction", "malware_sandbox", "app_compressor",
        "honeyroot"]


def test_merged_file_count():
    assert total_files() >= 140


def test_four_docker_images_merged():
    imgs = [img for _, img in docker_images()]
    assert "docker.io/credkellar/deconstruction:latest" in imgs
    assert "docker.io/credkellar/malware-sandbox-suite:latest" in imgs
    assert "docker.io/credkellar/app-data-compressor:latest" in imgs
    assert "docker.io/credkellar/honeyroot-x:latest" in imgs


def test_every_source_has_files_and_domain():
    for s in list_sources():
        assert s["files"] and s["domain"] and s["root"]


def test_unknown_expert_raises():
    with pytest.raises(KeyError):
        get_source("nope")


# --- ask each --------------------------------------------------------
@pytest.mark.parametrize("expert,question,expect", [
    ("gemini_frontier", "how does speculative decoding routing work", "speculative_decoding.py"),
    ("gemini_frontier", "automated CVE CWE security patch synthesis", "auto_patch_generator.py"),
    ("grok", "Monte Carlo Tree Search for math and code", "tree_search.py"),
    ("grok", "FP8 key value cache memory management", "fp8_kv_cache.py"),
    ("claude_code", "Model Context Protocol server registrations", ".mcp.json"),
    ("deepseek", "Multi-head Latent Attention MLA", "mla.py"),
    ("deepseek", "auxiliary loss free load balancer routing for mixture of experts", "load_balancer.py"),
    ("workspace_studio", "Google Forms submission trigger", "form_trigger.ts"),
    ("google_flow", "script to storyboard sequence planning", "script_to_storyboard.py"),
    ("copilot", "tenant isolation OAuth token validator", "tenant_isolation.py"),
    ("perplexity", "prebuilt enterprise connectors M365 Sharepoint", "prebuilt_connectors.py"),
    ("codex", "links generated claims to web source URLs citation", "grounder.py"),
    ("malware_sandbox", "eBPF kernel syscall file access event listener", "ebpf_collector.py"),
    ("malware_sandbox", "MITM proxy pcap dumper network", "network_proxy.py"),
    ("app_compressor", "Zstandard dictionary based compressor", "zstd_stream.rs"),
    ("app_compressor", "SHA-256 BLAKE3 checksum verification", "checksum_verify.rs"),
    ("honeyroot", "fake SSH shell capturing credentials and commands", "fake_ssh.py"),
    ("honeyroot", "ASN geolocation threat intelligence tagger", "ip_enrichment.py"),
])
def test_ask_each_expert_cites_its_own_file(brain, expert, question, expect):
    ans = brain.ask(expert, question)
    paths = [p for p, _, _ in ans.facts]
    assert any(expect in p for p in paths), f"{expert}: {paths}"
    assert ans.confidence > 0.3
    assert expect in ans.text


def test_expert_cannot_answer_outside_its_files(brain):
    ans = brain.ask("honeyroot", "how does FP8 KV cache quantization work")
    assert "fp8_kv_cache" not in ans.text


def test_ask_each_returns_all_13(brain):
    answers = brain.ask_each("what is mixture of experts routing")
    assert len(answers) == 13
    assert {a.expert_id for a in answers} == set(expert_ids())


# --- routing ---------------------------------------------------------
@pytest.mark.parametrize("question,expect_top", [
    ("how do I detonate a malware sample with eBPF telemetry", "malware_sandbox"),
    ("compress an archive with zstd and verify checksums", "app_compressor"),
    ("fake SSH honeypot capturing attacker credentials", "honeyroot"),
    ("Monte Carlo tree search and GPU cluster scheduling", "grok"),
])
def test_router_top1(brain, question, expect_top):
    ranked = brain.route(question)
    assert ranked[0][0] == expect_top, ranked[:3]


def test_nnl_learned_routing():
    assert nnl_accuracy() > 0.5


def test_routing_examples_cover_all_experts():
    labels = {label for _, label in routing_examples()}
    assert labels == set(expert_ids())


# --- the grand answer -------------------------------------------------
def test_grand_answer_structure(brain):
    g = brain.grand("how should I route a question to a mixture of experts model safely")
    assert len(g.answers) == 13
    assert g.ranked_facts
    assert 0.0 <= g.confidence <= 1.0
    assert "GRAND ANSWER" in g.text
    assert "Consensus" in g.text
    assert "Unique insights" in g.text


def test_grand_answer_only_uses_expert_facts(brain):
    g = brain.grand("eBPF tracing and pcap capture")
    cited = {path for _, path, _, _ in g.ranked_facts}
    all_files = {p for s in list_sources() for p, _ in s["files"]}
    assert cited <= all_files


def test_grand_consensus_on_shared_topic(brain):
    g = brain.grand("Model Context Protocol MCP tool execution")
    # claude_code, copilot and codex all carry MCP files
    assert g.consensus, "expected cross-expert consensus on MCP"


# --- CLI ---------------------------------------------------------------
def test_cli_list(capsys):
    assert main(["list"]) == 0
    out = capsys.readouterr().out
    assert "13 experts" in out and "honeyroot" in out


def test_cli_ask(capsys):
    assert main(["ask", "deepseek", "Multi-head Latent Attention"]) == 0
    assert "mla.py" in capsys.readouterr().out


def test_cli_grand(capsys):
    assert main(["grand", "what is a honeypot fake SSH shell"]) == 0
    assert "GRAND ANSWER" in capsys.readouterr().out


def test_cli_files_and_docker(capsys):
    assert main(["files", "malware_sandbox"]) == 0
    assert "ebpf_collector.py" in capsys.readouterr().out
    assert main(["docker"]) == 0
    assert "honeyroot-x" in capsys.readouterr().out
