___________________________________________________

# 🧠 Intuition

**Thirteen AI and agent systems merged into one council — ask each expert on its own, ask all of them at once, or get the grand answer synthesized from every expert, with every fact cited to the file it came from. Pure Python, stdlib only.**

[![CI](https://github.com/ddkellar01/Intuition/actions/workflows/ci.yml/badge.svg)](https://github.com/ddkellar01/Intuition/actions/workflows/ci.yml)
[![Docker Publish](https://github.com/ddkellar01/Intuition/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/ddkellar01/Intuition/actions/workflows/docker-publish.yml)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen)
![Docker](https://img.shields.io/badge/Docker-credkellar%2Fintuition-2496ED?logo=docker&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

**13 systems, one intuition:** Gemini 4 Frontier · xAI Grok · Claude Code · DeepSeek-V3/R1 · Google Workspace Studio Flows · Google Flow Filmmaking · GitHub Copilot & Copilot Studio · Perplexity AI · OpenAI Codex — plus four of Darion's own Docker systems: Deconstruction, Malware Sandbox Suite, App Data Compressor, and Honeyroot-X. **161 files merged**, transcribed from the source notes in `docs/SOURCES_AS_SUPPLIED.md`, mapped in `docs/MERGE_MAP.md`.

---

## 🧰 Tech Stack Badges & Architecture

### 💻 Core Programming Languages & Core Systems
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) — 100% of the system, **pure standard library, zero runtime dependencies**

**The AI stack — what each layer actually is:**
- **ASI** — the synthesis layer on top: route a question, ask one expert, ask each, or synthesize the grand answer; adds no facts of its own
- **NNL** — a multi-layer perceptron with backprop, written from scratch in stdlib, trained on the sources' own file descriptions to vote on routing
- **LLM** — a grounded reasoner: composes answers ONLY from retrieved facts with file citations (optional Gemini polish via `GEMINI_API_KEY`, facts never added)
- **ML** — the routing ensemble: LML relevance + SML kNN votes + NNL probabilities, fixed stated weights (0.50 / 0.30 / 0.20)
- **SML** — small ML: kNN routing over labelled examples + a logistic confidence scorer
- **LML** — one local TF-IDF model per expert, over that expert's own files only

### ⛓️ Web3 & Infrastructure
Honest note: **no blockchain / Web3 components.** The infrastructure layer is containers: four of the 13 merged systems are Darion's own published Docker images (`credkellar/deconstruction`, `credkellar/malware-sandbox-suite`, `credkellar/app-data-compressor`, `credkellar/honeyroot-x`), Intuition itself ships as `credkellar/intuition`, and `docker-compose.yml` can raise all five together under the `fleet` profile.

### ⚙️ Platform Support & Hardware Architecture
![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
- Runs anywhere Python 3.10+ runs; the Docker image is a 43 MB multi-stage `python:3.12-slim` build, non-root, with an import healthcheck
- **Hardware layer (8 devices, one adapter each)** — Meta Quest Pro (mixed-reality council interface), Kodak Ultra Mini projector + Holographic Assistant Projector (projection briefs), hand-operated flying-disc drones (gesture control), SereniBrain/iHANK EEG headband (focus-adaptive answers), Voice Mode UI (spoken briefs), 8K cinematic camera (see / take pics / record), lie-detector sensor (arousal context)

### ⚡ Low-Level Infrastructure & Performance
- **Zero dependencies** — TF-IDF, cosine similarity, kNN, logistic regression, and an MLP with backprop are all implemented from scratch on the stdlib
- Deterministic NNL training (fixed seed) — routing is reproducible and tests are stable
- Lazy model training: the router trains once, on first use, from the sources themselves — no model files, no downloads, instant cold start for everything else

### 🛠️ DevOps & Build Tools
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker_Hub-2496ED?logo=docker&logoColor=white)
- **CI** (`ci.yml`) — `pip install pytest .`, `pytest -q` (**62 tests**), then `scripts/smoke.py`, on Python 3.12
- **Docker Publish** (`docker-publish.yml`) — builds and pushes `credkellar/intuition` (`latest` + commit-sha tags) on every push to `main` and on `v*` tags

### ☁️ Cloud Providers
- Cloud-agnostic: the council runs **fully offline**. The only optional cloud touchpoint is the Gemini API for answer polish — bring your own `GEMINI_API_KEY`, and any failure falls back to the grounded answer

---

## 🎯 What this does — step by step

1. **Merge** — 13 systems' structures (161 files with their descriptions) are transcribed into one registry (`sources_data.py`); nothing is invented to fill a gap
2. **Build the experts** — each source becomes an Expert with its own local TF-IDF model over *its own* files only
3. **Ask one expert** — it retrieves its best-matching files, scores confidence, and composes a grounded answer citing each file
4. **Or route the question** — the ensemble (LML relevance + SML kNN + NNL MLP) ranks all 13 experts by fit
5. **Or ask each** — every expert answers the same question, low-confidence ones included, so you see who knows what
6. **Or get the grand answer** — all 13 answers are synthesized: facts ranked by confidence, concepts 2+ experts surface independently marked **consensus**, single-expert findings marked **unique insights**, overall confidence = the mean
7. **Polish (optional)** — with a Gemini key, the grounded draft may be rewritten for clarity; citations are preserved and no facts are added
8. **Present it your way** — CLI text, `--json`, a full markdown `--report`, a ≤9-line projection brief for a wall/hologram, or a short spoken brief for Voice Mode
9. **Layer the hardware** — EEG focus picks full vs brief answers, drone gestures drive the council, the 8K camera's captures become citable context, lie-detector arousal flags follow-up questions

---

## 😎 Why is this cool? — 10 reasons

1. **A council, not a chatbot** — 13 specialists with separate knowledge, plus a synthesis layer that shows where they agree and where only one knows
2. **No expert can bluff** — each answers only from its own files; ask Grok about the malware sandbox and it honestly has nothing
3. **Every fact is cited** — answers name the file each fact came from; the grand answer keeps the citations per fact
4. **The router is real ML, hand-built** — a working MLP with backprop, kNN, and TF-IDF, all from scratch, zero dependencies
5. **Consensus is computed, not claimed** — a concept counts as consensus only when 2+ experts surface it independently
6. **It runs anywhere, offline** — one `pip install .` or one Docker pull; no keys, no network, no GPU
7. **Your body is an input** — EEG focus literally changes how long your answer is; a hand gesture over a drone flips the question to a new routing
8. **The camera is a citizen** — captures get IDs and citations, and you ask the council about what it saw, same grounding rule as everything else
9. **The lie detector refuses to lie** — it measures arousal and flags follow-ups; the honesty rule is written in the code, the docs, and the tests
10. **Four of the experts are real running systems** — Darion's own published Docker images, raisable together with Intuition in one compose fleet

---

## 🛡️ What problems this solves — 10 solutions

1. **Knowledge scattered across 13 projects** → one registry, one CLI, one question reaches all of them
2. **LLM answers you can't verify** → grounded composition: nothing is stated that no merged file supports, and the file is cited
3. **One model pretending to know everything** → per-expert local models make ignorance visible instead of hallucinated over
4. **"Which system handles this?"** → the routing ensemble ranks experts with three independent methods, weights stated in code
5. **Synthesis that hides disagreement** → consensus and unique insights are separated and labelled in every grand answer
6. **Heavy stacks for a simple idea** → zero dependencies; the whole AI stack is stdlib Python you can read end-to-end
7. **Answers too long when you're unfocused** → the EEG layer serves the spoken brief first and the full answer on demand
8. **Projectors and holograms fed raw markdown** → projection briefs are formatted for the wall: few lines, large ideas, max 9 lines enforced
9. **Polygraph hype** → the sensor's output is a stress index and a follow-up flag — the defensible use, documented as such
10. **Merged-project amnesia** → `docs/SOURCES_AS_SUPPLIED.md` and `docs/MERGE_MAP.md` record exactly what came from where, including what was illegible and omitted

---

## 🚀 How to install — step by step

1. **Clone it**
   ```bash
   git clone https://github.com/ddkellar01/Intuition.git
   cd Intuition

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
