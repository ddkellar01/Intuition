# Intuition

> Intuition (ASI, NNL, LLM, ML, SML, LML): 13 AI/agent systems merged into one council — ask each expert on its own, ask all of them at once, or get the grand answer synthesized from every expert, with every fact cited to the file it came from. Pure Python, stdlib only.

Repo description (exactly 350 characters):

```
Intuition (ASI, NNL, LLM, ML, SML, LML): 13 AI systems merged into one council - Gemini, Grok, Claude Code, DeepSeek, Copilot, Perplexity, Codex, Workspace, Flow + 4 Docker systems. Ask each expert, ask all, or get the grand answer. Hardware: Quest Pro, EEG, 8K camera, drones, voice, hologram. Pure Python stdlib. All 58 pytest passing, smoke green.
```

**13 systems, one intuition.** Gemini 4 Frontier, xAI Grok, Claude Code, DeepSeek-V3/R1, Google Workspace Studio Flows, Google Flow Filmmaking, GitHub Copilot & Copilot Studio, Perplexity AI, OpenAI Codex — plus Darion's own four Docker systems: Deconstruction, Malware Sandbox Suite, App Data Compressor, and Honeyroot-X. 161 files merged, transcribed from the source notes in `docs/SOURCES_AS_SUPPLIED.md`, mapped in `docs/MERGE_MAP.md`.

## Ask each, ask all, grand answer

```bash
pip install .

intuition list                                   # the 13 experts
intuition files malware_sandbox                  # one expert's merged files
intuition ask deepseek "Multi-head Latent Attention MLA"
intuition ask honeyroot "fake SSH shell capturing credentials"
intuition ask-all "what is mixture of experts routing"   # every expert answers
intuition route "compress an archive with zstd"          # who should answer?
intuition grand "Model Context Protocol MCP tool execution and safety"
intuition grand "eBPF tracing" --report          # full markdown report
intuition stats                                  # experts, files, NNL accuracy
intuition docker                                 # the 4 merged credkellar images
```

## The AI stack — what each layer actually is

| Layer | Module | What it does |
|---|---|---|
| **ASI** | `asi.py` | The layer above the experts: routes, asks one, asks each, synthesizes the grand answer. Adds no facts of its own. |
| **NNL** | `nnl.py` | Neural Network Layer — an MLP with backprop (pure stdlib, deterministic seed) trained on the merged sources' own file descriptions to route questions to experts. |
| **LLM** | `llm.py` | KB-grounded reasoner: composes each expert's answer only from facts its local model retrieved, with file citations. Optional Gemini polish (`GEMINI_API_KEY`) — grounded facts and citations are kept, failures fall back to the grounded draft. |
| **ML** | `ml.py` | Routing ensemble: LML relevance 0.50 + SML kNN 0.30 + NNL probability 0.20, plus logistic confidence. Weights are stated in the code, nowhere else. |
| **SML** | `sml.py` | Small ML: kNN router over file-description examples + a logistic confidence squash. |
| **LML** | `lml.py` | Local Model Layer: one TF-IDF model per expert, over its own files only. An expert cannot answer from another expert's files — that is what makes "ask each" mean something. |

## The grand answer

Ask all 13, then synthesize (`grand.py`):

- **Best-grounded facts** across all experts, ranked by expert confidence
- **Consensus** — concepts 2+ experts independently surface
- **Unique insights** — facts only one expert carries
- **Overall confidence** — mean of the 13 expert confidences

Nothing enters the grand answer that no expert said.

## The merge — 13 sources

| # | Expert | Root as supplied | Files |
|---|---|---|---|
| 1 | Gemini 4 Frontier | `gemini-4-frontier/` | 21 |
| 2 | xAI Grok | `grok-system/` | 11 |
| 3 | Claude Code | `claude-code-environment/` | 9 |
| 4 | DeepSeek-V3 / R1 | `deepseek-v3-r1/` | 14 |
| 5 | Google Workspace Studio Flows | `google-workspace-studio-flows/` | 7 |
| 6 | Google Flow Filmmaking | `google-flow-filmmaking/` | 12 |
| 7 | GitHub Copilot & Copilot Studio | `copilot-ecosystem/` | 10 |
| 8 | Perplexity AI | `perplexity-core/` | 5 |
| 9 | OpenAI Codex | `openai-codex-platform/` | 12 |
| 10 | Deconstruction | `docker.io/credkellar/deconstruction:latest` | 6 |
| 11 | Malware Sandbox Suite | `docker.io/credkellar/malware-sandbox-suite:latest` | 24 |
| 12 | App Data Compressor | `credkellar/app-data-compressor` | 17 |
| 13 | Honeyroot-X | `credkellar/honeyroot-x` | 13 |

Full map: [docs/MERGE_MAP.md](docs/MERGE_MAP.md) · Sources exactly as supplied: [docs/SOURCES_AS_SUPPLIED.md](docs/SOURCES_AS_SUPPLIED.md) · Council design: [docs/COUNCIL.md](docs/COUNCIL.md)

## Hardware layer — added 2026-10-28, all included

Seven devices/concepts he supplied, each with a real adapter module — full table and honesty notes in [docs/HARDWARE.md](docs/HARDWARE.md):

| Device | Module | Role |
|---|---|---|
| Meta Quest Pro — $799.99 as shown | `hardware.py` | MR council room, passthrough panels |
| Kodak Ultra Mini Projector — no price in screenshot | `projection.py` | Wall output: projection brief, max 9 lines |
| Flying Disc Drones ×3 listings — $22.99 / $16.99 / Force1 Scoot | `drone.py` | Gesture control: push / pull / hold / flip / wave |
| EEG Headband (SereniBrain/iHANK) — $179.99 as shown | `eeg.py` | Focus/relaxation from band ratios → answer mode |
| Voice Mode UI (his concept image) | `voice.py` | Spoken brief first, full answer on request |
| Holographic Projector (his concept image) | `projection.py` | Hologram target for the same brief |
| 8K Cinematic Camera — no brand/price supplied | `camera.py` | The eyes: see · take pics · record, captures cited by id |

```bash
intuition hardware            # all 7, with prices exactly as shown
intuition hardware eeg_headband
intuition voice "what is a honeypot"
intuition project "what is mixture of experts routing"
```

Known shown-price total: **$1,002.97** — only prices actually visible in his screenshots are recorded.

## Verify

```bash
pip install pytest .
pytest -q            # 58 tests
python scripts/smoke.py
```

## Docker

```bash
docker build -t credkellar/intuition:latest .
docker compose up intuition          # the council
docker compose --profile fleet up    # + the 4 merged credkellar images
```

MIT license.
