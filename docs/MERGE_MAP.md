# Merge Map — where each of the 13 sources lives in Intuition

Every source became one **Expert** (`src/intuition/sources_data.py` is the
registry data; `src/intuition/experts.py` builds one Expert per source).
Each expert's files, exactly as named in Darion's video notes, are its
knowledge base — its LML local model indexes only its own files.

| Expert id | Source (title as supplied) | Lives here as |
|---|---|---|
| `gemini_frontier` | ChatGPT Project Structure Tree (OpenAI Enterprise & Agent System) — root `gemini-4-frontier/` | Expert: spatial reasoning, 1M context, speculative decoding, Argon 4 agents, Carbon 4 security/CWE patching |
| `grok` | xAI Grok Project Structure Tree (Colossus Supercluster & Real-Time Engine) | Expert: MoE dispatch, TTC/tree-search reasoning, Colossus GPU scheduling, FP8 KV cache, X firehose |
| `claude_code` | Claude Code Project Structure Tree (CLI, Agent Memory & MCP Integration) | Expert: MCP registrations, extended thinking, persistent state, session transcripts |
| `deepseek` | DeepSeek-V3 Architecture (Dual-Pipe MoE) | Expert: MLA, DualPipe, fine-grained MoE, FP8, R1 rewards/distillation |
| `workspace_studio` | Google Workspace Studio Flows | Expert: flow starters/triggers (Gmail, Forms, webhooks), steps, cards |
| `google_flow` | Google Flow / google-flow-filmmaking | Expert: timeline editing, storyboard planning, lip-sync, inpainting, export |
| `copilot` | GitHub Copilot & Copilot Studio (JetBrains & Visual Studio) | Expert: AST chunking, workspace indexing, agent chat, MCP proxy, content safety, tenant isolation |
| `perplexity` | Perplexity AI / perplexity-core | Expert: intent/Dialog, real-time retrieval, query expansion, 1,400+ connectors |
| `codex` | OpenAI Codex / openai-codex-platform | Expert: citation grounding, session orchestration, project learning, research planning |
| `deconstruction` | Deconstruction — `docker.io/credkellar/deconstruction:latest` | Expert + Docker fleet service: payloads, eBPF traces, deconstruction reports |
| `malware_sandbox` | Malware Sandbox Suite — `docker.io/credkellar/malware-sandbox-suite:latest` | Expert + Docker fleet service: detonation, eBPF telemetry, MITM pcap, threat reports |
| `app_compressor` | `credkellar/app-data-compressor` | Expert + Docker fleet service: zstd/LZMA2 compression, chunking, checksum manifests |
| `honeyroot` | `credkellar/honeyroot-x` | Expert + Docker fleet service: SSH/HTTP/SQL honeypot emulators, IP enrichment, alerts |

## Cross-cutting layers (from the name he gave it: ASI, NNL, LLM, ML, SML, LML)

- ASI = `asi.py` (top layer / grand synthesis) · NNL = `nnl.py` (MLP router)
- LLM = `llm.py` (grounded reasoner) · ML = `ml.py` (ensemble + confidence)
- SML = `sml.py` (kNN + logistic) · LML = `lml.py` (per-expert TF-IDF models)
- Council = `council.py` (ask one / ask each / ask routed) · Grand = `grand.py`
