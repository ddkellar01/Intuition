"""The 13 merged sources, transcribed from Darion's video notes
(Intuition Pt 1 + Int. Pt 2, edited 2026-10-28 2:59 PM / 3:01 PM).

Every file entry below is a file named in those notes, with the
description the note gave it. Where a name was illegible in the video
it is omitted here and flagged in docs/SOURCES_AS_SUPPLIED.md --
nothing is invented to fill a blur.
"""

SOURCES = [
    {
        "id": "gemini_frontier",
        "name": "Gemini 4 Frontier",
        "title_as_supplied": "ChatGPT Project Structure Tree (OpenAI Enterprise & Agent System)",
        "root": "gemini-4-frontier/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "Common Gemini 4 and Carbon runtime across Argon and Carbon: "
                  "spatial reasoning, 1M-token context, multimodal + AST tokenizers, "
                  "speculative decoding, guardrails, Argon 4 software agents, "
                  "Carbon 4 security model, CWE patching.",
        "files": [
            ("core/inference/spatial_reasoning.py", "Spatial & multi-step workflow planner [Argon & Carbon]"),
            ("core/inference/context_window.py", "1M token context window memory manager"),
            ("core/tokenizers/text_multimodal.py", "Text, image, audio, and video multimodal input"),
            ("core/tokenizers/code_ast.py", "AST tokenizer for software/codebases"),
            ("core/routing/speculative_decoding.py", "High-speed speculative token routing"),
            ("core/safety/base_guardrails.py", "Core toxicity & compliance checks"),
            ("core/safety/ipi_checker.py", "Indirect Prompt Injection baseline filter"),
            ("argon_4/agents/autonomous_refactor.py", "Base multi-step software engineering agent"),
            ("argon_4/agents/model_switch.py", "Token-hunger & concurrency load balancer"),
            ("argon_4/agents/system_executor.py", "Unrestricted API/tool execution loop"),
            ("argon_4/deployment/api_gateway/", "Google AI Studio / Gemini API access layer"),
            ("argon_4/deployment/antigravity_runner/", "Cloud environment runner for Gemini Antigravity"),
            ("carbon_4/evaluation/vals_index_benchmarks.py", "Enterprise & economic benchmark validation"),
            ("carbon_4/evaluation/partner_auth.py", "Fairwind Program partner credential telemetry"),
            ("carbon_4/evaluation/telemetry_auditor.py", "Real-time shadow execution audit logger"),
            ("carbon_4/policy_enforcer.py", "Restricted payload & exploit prevention engine"),
            ("carbon_4/cyber_sec/analysis_index/artificial_analysis_v5.py", "Top-spot Intelligence Index v5.0"),
            ("carbon_4/cyber_sec/analysis_index/vulnerability_scanner.py", "88.2% SOTA real-world flaw detector evaluation hooks"),
            ("carbon_4/cyber_sec/analysis_index/deep_taint_analyzer.py", "Multi-file dependency & AST taint tracker"),
            ("carbon_4/cyber_sec/cwe_patching/auto_patch_generator.py", "Automated CVE/CWE security patch synthesis"),
            ("carbon_4/cyber_sec/cwe_patching/regression_verifier.py", "Zero-breakage regression testing harness"),
        ],
    },
    {
        "id": "grok",
        "name": "xAI Grok",
        "title_as_supplied": "xAI Grok Project Structure Tree (Colossus Supercluster & Real-Time Engine)",
        "root": "grok-system/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "High-performance inference backbone on the Colossus supercluster: "
                  "Mixture-of-Experts dispatch, Test-Time Compute reasoning, Monte Carlo "
                  "Tree Search, 100k+ GPU scheduling, FP8 KV cache, real-time X firehose ingestion.",
        "files": [
            ("inference_engine/moe_router/expert_dispatch.rs", "Rust high-throughput Mixture-of-Experts dispatch"),
            ("reasoning/big_brain_mode.py", "Test-Time Compute (TTC) chain-of-thought allocator"),
            ("reasoning/tree_search.py", "Monte Carlo Tree Search for math/code logic paths"),
            ("cluster_management/colossus_scheduler.py", "Colossus Infrastructure Layer: 100k+ GPU job distribution orchestration"),
            ("cluster_management/fault_tolerance.rs", "Instant node recovery without context drop"),
            ("cluster_management/quantization/fp8_kv_cache.py", "Low-latency FP8 Key-Value memory management"),
            ("cluster_management/quantization/bit_packing.rs", "Custom GPU tensor serialization"),
            ("cluster_management/telemetry/thermal_monitoring.py", "Power efficiency & hardware health monitors"),
            ("real_time_ingestion/latency_bench.py", "Sub-100ms response time tracker"),
            ("real_time_ingestion/x_firehose/post_stream_consumer.py", "Live tweet & post filter/vectorizer"),
            ("real_time_ingestion/x_firehose/trend_entity_extractor.py", "Live breaking news tagger"),
        ],
    },
    {
        "id": "claude_code",
        "name": "Claude Code",
        "title_as_supplied": "Claude Code Project Structure Tree (CLI, Agent Memory & MCP Integration)",
        "root": "claude-code-environment/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "CLI agent environment: Model Context Protocol server registrations, "
                  "Claude Opus extended-thinking parsing, global configuration and persistent "
                  "state, shell execution, per-project session transcripts and subagent logs.",
        "files": [
            ("project_root/.mcp.json", "Local Model Context Protocol server registrations"),
            ("project_root/.mcp_json_builder.ts", "Local Model Context Protocol server builder"),
            (".claude/thinking_processor.ts", "Claude Opus 3.5/3.7 Extended Thinking parser"),
            (".claude/settings.json", "Global configuration: system policies, tool access rules & preferences"),
            (".claude/bash_executor.ts", "Local shell command execution engine"),
            (".claude/credentials.json", "Auth tokens & OAuth session state"),
            (".claude/history.jsonl", "Cross-project command & prompt log"),
            (".claude/projects/<project-hash>/transcript.jsonl", "Per-Project Execution State: full session logs (messages, tool uses, thinking tokens)"),
            (".claude/models/subagents/", "Isolated session & subagent execution logs"),
        ],
    },
    {
        "id": "deepseek",
        "name": "DeepSeek-V3 / R1",
        "title_as_supplied": "DeepSeek-V3 Architecture (Dual-Pipe MoE)",
        "root": "deepseek-v3-r1/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "Dual-Pipe Mixture-of-Experts transformer: think-tag format and reasoning-step "
                  "rewards, fine-grained MoE with auxiliary-loss-free load balancing, shared experts, "
                  "Multi-head Latent Attention, FP8 mixed precision, reasoning distillation, "
                  "DeepSeek-R1 Expert Parallelism and GRPO-style reasoning.",
        "files": [
            ("format_reward.py", "Enforcement of <think>...</think> XML layout"),
            ("reasoning_steps_reward.py", "Reward for structural reasoning progression"),
            ("model/modeling_deepseek.py", "Main PyTorch transformer definition"),
            ("model/repetition_penalty.py", "N-gram repetition reduction penalty"),
            ("model/moe/deepseek_moe.py", "Fine-grained Mixture-of-Experts layer"),
            ("model/moe/load_balancer.py", "Auxiliary-loss-free routing algorithm"),
            ("model/moe/shared_experts.py", "Core global experts operating across all tokens"),
            ("model/distillation/distill_pipeline.py", "Reasoning path distillation into Qwen/Llama base models"),
            ("model/communication/dual_pipe.py", "DualPipe parallel computation & communication overlap"),
            ("model/attention/mla.py", "Multi-head Latent Attention (MLA)"),
            ("model/attention/rope_embeddings.py", "Rotary position embeddings"),
            ("model/attention/fp8_mixed_precision.py", "Custom FP8 matrix multiplication kernels"),
            ("r1_reasoning/deep_ep/", "DeepSeek Expert Parallelism communication library"),
            ("inference/prompt_template.py", "System prompt and <think> reasoning tag structure"),
        ],
    },
    {
        "id": "workspace_studio",
        "name": "Google Workspace Studio Flows",
        "title_as_supplied": "Google Workspace Studio Flows",
        "root": "google-workspace-studio-flows/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "Workspace Add-on flows: event starters and triggers (Gmail, Google Forms, "
                  "webhooks), flow steps, contextual response generation, chat messages and "
                  "Workspace UI cards for step configuration.",
        "files": [
            ("manifest.json", "Workspace Add-on manifest (defines flow starters & steps)"),
            ("studio_config.json", "Environment & OAuth config for Google Workspace Studio"),
            ("starters/email_trigger.ts", "Native incoming Gmail message parser"),
            ("starters/form_trigger.ts", "Native Google Forms submission trigger"),
            ("starters/webhook_listener.ts", "Custom external HTTP event receiver integration"),
            ("steps/send_chat_message.ts", "Google Chat message step"),
            ("card_layout.ts", "Google Workspace UI cards for user step configuration"),
        ],
    },
    {
        "id": "google_flow",
        "name": "Google Flow Filmmaking",
        "title_as_supplied": "Google Flow / google-flow-filmmaking",
        "root": "google-flow-filmmaking/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "Web frontend and interactive timeline engine for filmmaking: multi-track "
                  "video/dialogue/FX editing, camera keyframing, character consistency, style "
                  "transfer, script-to-storyboard planning, GPU generation bursts, lip-sync, "
                  "inpainting and final NLE export.",
        "files": [
            ("app/timeline/track_editor.tsx", "Multi-track video, dialogue, and FX editor"),
            ("app/timeline/keyframe_animator.tsx", "Camera keyframing & motion vectors UI"),
            ("app/asset_canvas/character_consistency.tsx", "Subject/character anchor library UI"),
            ("app/asset_canvas/style_transfer_picker.tsx", "Visual continuity & color-grading preset selector"),
            ("core_engine/sequence_planner/script_to_storyboard.py", "Script to storyboard sequence planning"),
            ("core_engine/gpu_cluster_allocator.py", "Multi-TPU/GPU task assigner for generation bursts"),
            ("core_engine/audio_sync_engine.py", "Native dialogue lip-sync & ambient audio generator"),
            ("storage/camera_control.py", "Dynamic camera pan, zoom, and tilt vector injector"),
            ("storage/scene_asset_vault/", "High-res video segment, keyframe & depth map cache"),
            ("editing_ops/inpainting_vace.py", "Target element swap and region-based video edit"),
            ("editing_ops/expert_exporter.py", "Final NLE export packager (MP4, ProRes, EDL)"),
            ("editing_ops/upscale_frame_interpolator.py", "Client-side upscale and temporal smoothing"),
        ],
    },
    {
        "id": "copilot",
        "name": "GitHub Copilot & Copilot Studio",
        "title_as_supplied": "GitHub Copilot & Copilot Studio (JetBrains & Visual Studio)",
        "root": "copilot-ecosystem/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "IDE client extension and cloud infrastructure: AST chunking and workspace "
                  "indexing, agent chat participants (@workspace/@terminal/@vscode), OpenAPI "
                  "plugins, MCP proxy, Azure content safety, tenant isolation, and Copilot "
                  "Studio conversation flows.",
        "files": [
            ("ide_client_extension/src/context_providers/ast_chunker.ts", "Local file AST & active cursor context parser"),
            ("ide_client_extension/src/context_providers/workspace_indexer.ts", "Repository-wide vector & local workspace indexing"),
            ("cloud_infrastructure/build_actions/snippet_filter.ts", "Telemetry & duplicate snippet filter"),
            ("cloud_infrastructure/agent_chat/participant_registry.ts", "Custom @workspace, @terminal, and @vscode router"),
            ("cloud_infrastructure/agent_chat/custom_api_plugin.py", "OpenAPI REST plugin executor"),
            ("cloud_infrastructure/security_guardrails/mcp_proxy.ts", "Model Context Protocol tool dispatcher"),
            ("cloud_infrastructure/security_guardrails/azure_content_safety.py", "Enterprise DLP, toxicity, and prompt injection shield"),
            ("cloud_infrastructure/security_guardrails/tenant_isolation.py", "Per-tenant boundary & OAuth token validator"),
            ("copilot_studio_agent_flows/conversation_engine/intent_classifier.py", "Dynamic NLU and goal extractor"),
            ("copilot_studio_agent_flows/conversation_engine/dialog_manager.py", "Multi-turn variable & state tracking"),
        ],
    },
    {
        "id": "perplexity",
        "name": "Perplexity AI",
        "title_as_supplied": "Perplexity AI / perplexity-core",
        "root": "perplexity-core/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "Multi-stage web search and indexing engine: dynamic NLU intent "
                  "classification, multi-turn dialog management, real-time retrieval, query "
                  "expansion into multi-vector search terms, and 1,400+ enterprise connectors.",
        "files": [
            ("conversation_engine/intent_classifier.py", "Dynamic NLU and goal extractor"),
            ("conversation_engine/dialog_manager.py", "Multi-turn variable & state tracking"),
            ("real_time_retrieval/query_expansion/", "Breaks complex queries into multi-vector search terms"),
            ("build_actions/search_planner.py", "Search planning over enterprise sources"),
            ("build_actions/prebuilt_connectors.py", "1,400+ Enterprise connectors (M365, Sharepoint, Dynamics)"),
        ],
    },
    {
        "id": "codex",
        "name": "OpenAI Codex",
        "title_as_supplied": "OpenAI Codex / openai-codex-platform",
        "root": "openai-codex-platform/",
        "origin": "video note Pt 1",
        "docker": None,
        "domain": "OpenAI-hosted agent session manager: citation grounding to web sources, "
                  "task-loop session orchestration, persistent project learning, iterative "
                  "multi-hop research planning, MCP connection management, function-call "
                  "routing and structured markdown research briefs.",
        "files": [
            ("citation_linker/grounder.py", "Links generated claims directly to web source URLs"),
            ("codex_harness/session_orchestrator.py", "Task loop, model invocation, and event streaming"),
            ("codex_harness/deduplicator.py", "Removes redundant sources and stale references"),
            ("project_learning/persistent_knowledge.py", "Remembers AST patterns, conventions, and past commits"),
            ("project_learning/decision_history.py", "Track accepted/reverted code modifications"),
            ("planner/research_tree_search.py", "Iterative multi-hop hypothesis testing"),
            ("tool/gap_analyzer.py", "Identifies missing context for dynamic follow-up queries"),
            ("tool/mcp_connection_manager.py", "Remote Model Context Protocol execution proxy"),
            ("synthesizer/function_call_router.py", "Handles application server callbacks"),
            ("synthesizer/structured_report_gen.py", "Generates multi-section markdown research briefs"),
            ("execution_environments/websocket_handlers.py", "WebSockets / SSE event emitter"),
            ("synthesizer/summary_synthesizer.py", "Analysis output generator"),
        ],
    },
    {
        "id": "deconstruction",
        "name": "Deconstruction",
        "title_as_supplied": "Deconstruction",
        "root": "deconstruction/",
        "origin": "video note Pt 1",
        "docker": "docker.io/credkellar/deconstruction:latest",
        "domain": "Darion's own analysis drive: runtime bootstrap, captured payloads, eBPF "
                  "kernel traces and network PCAP logs, structure/deconstruction reports, "
                  "shipped as a multi-stage Docker image.",
        "files": [
            ("Dockerfile", "Multi-stage image build configuration"),
            ("Makefile", "Container orchestration, testing, and publish tasks"),
            ("bin/deconstruct", "Core analysis drive entry point"),
            ("artifacts/test/captured_payloads/", "Captured payloads output & working directory"),
            ("artifacts/test/traces/", "eBPF kernel traces, network PCAP logs"),
            ("artifacts/test/reports/", "Structure / deconstruction reports"),
        ],
    },
    {
        "id": "malware_sandbox",
        "name": "Malware Sandbox Suite",
        "title_as_supplied": "Malware Sandbox Suite",
        "root": "malware-sandbox-suite/",
        "origin": "video note Pt 2",
        "docker": "docker.io/credkellar/malware-sandbox-suite:latest",
        "domain": "Darion's own malware detonation sandbox (Python + Rust core + eBPF probes): "
                  "isolated network bridge with Redis queue and worker nodes, FastAPI submission "
                  "API, cgroup-constrained detonation, MITM network proxy with pcap dumping, "
                  "eBPF syscall telemetry, memory dumps and LLM-synthesized threat reports.",
        "files": [
            ("Dockerfile", "Multi-stage secure build (Python + Rust core + eBPF probes)"),
            ("docker-compose.yml", "Isolated network bridge, Redis queue, and worker nodes"),
            ("Makefile", "Build, test, run, and push automation tasks"),
            ("pyproject.toml", "Dependencies configuration (fastapi, pydantic, structlog)"),
            ("Cargo.toml", "Rust workspace configuration for high-speed components"),
            ("bin/sandbox_daemon", "Main orchestrator service entrypoint"),
            ("bin/ebpf_loader", "Kernel-space eBPF tracing hook injector"),
            ("src/api/__init__.py", "FastAPI application package"),
            ("src/api/main.py", "FastAPI application router and webhook handler"),
            ("src/api/schemas.py", "Pydantic models for submission and results"),
            ("src/coordinator.py", "Task queue scheduler and worker dispatcher"),
            ("src/dispatcher.py", "Isolated cgroup sandbox constraint enforcer"),
            ("src/detonation/executor.py", "Sample unpacking and process spawn engine"),
            ("src/detonation/network_proxy.py", "Controlled egress MITM proxy & pcap dumper"),
            ("src/detonation/timeout_monitor.py", "Watchdog for infinite loops & resource exhaustion"),
            ("src/telemetry/ebpf_collector.py", "Kernel syscall and file-access event listener"),
            ("src/telemetry/memory_dump.py", "Process memory snapshot extractor"),
            ("src/ai_synthesis/prompt_builder.py", "Structures execution traces for LLM analysis"),
            ("src/ai_synthesis/threat_reporter.py", "Generates structured markdown/JSON threat briefs"),
            ("tests/test_api.py", "FastAPI endpoint validation tests"),
            ("tests/test_detonation.py", "Controlled benign sample execution tests"),
            ("workspace/samples/", "Ingested binary samples waiting for detonation"),
            ("workspace/pcaps/", "Captured network traffic logs"),
            ("workspace/reports/", "JSON & LLM-synthesized threat reports"),
        ],
    },
    {
        "id": "app_compressor",
        "name": "App Data Compressor",
        "title_as_supplied": "credkellar/app-data-compressor",
        "root": "credkellar/app-data-compressor/",
        "origin": "video note Pt 2",
     
