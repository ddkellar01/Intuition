# Sources as supplied — Darion's video notes, 2026-10-28

Two notes in the video: **"Intuition (asi, nnl, llm, ml, sml and lml)"**
(Pt 1, edited 2:59 PM) and **"Int. Pt 2"** (edited 3:01 PM). Repo name
he gave: **Intuition**. The 13 trees below are reproduced in the order
and spelling supplied; every file here is a knowledge-base entry in
`src/intuition/sources_data.py`.

```
1.  ChatGPT Project Structure Tree (OpenAI Enterprise & Agent System)
    gemini-4-frontier/
    core/inference/spatial_reasoning.py, core/inference/context_window.py,
    core/tokenizers/text_multimodal.py, core/tokenizers/code_ast.py,
    core/routing/speculative_decoding.py, core/safety/base_guardrails.py,
    core/safety/ipi_checker.py, argon_4/agents/autonomous_refactor.py,
    argon_4/agents/model_switch.py, argon_4/agents/system_executor.py,
    argon_4/deployment/api_gateway/, argon_4/deployment/antigravity_runner/,
    carbon_4/evaluation/vals_index_benchmarks.py, carbon_4/evaluation/partner_auth.py,
    carbon_4/evaluation/telemetry_auditor.py, carbon_4/policy_enforcer.py,
    carbon_4/cyber_sec/analysis_index/artificial_analysis_v5.py,
    carbon_4/cyber_sec/analysis_index/vulnerability_scanner.py,
    carbon_4/cyber_sec/analysis_index/deep_taint_analyzer.py,
    carbon_4/cyber_sec/cwe_patching/auto_patch_generator.py,
    carbon_4/cyber_sec/cwe_patching/regression_verifier.py

2.  xAI Grok Project Structure Tree (Colossus Supercluster & Real-Time Engine)
    grok-system/
    inference_engine/moe_router/expert_dispatch.rs, reasoning/big_brain_mode.py,
    reasoning/tree_search.py, cluster_management/colossus_scheduler.py,
    cluster_management/fault_tolerance.rs,
    cluster_management/quantization/fp8_kv_cache.py,
    cluster_management/quantization/bit_packing.rs,
    cluster_management/telemetry/thermal_monitoring.py,
    real_time_ingestion/latency_bench.py,
    real_time_ingestion/x_firehose/post_stream_consumer.py,
    real_time_ingestion/x_firehose/trend_entity_extractor.py

3.  Claude Code Project Structure Tree (CLI, Agent Memory & MCP Integration)
    claude-code-environment/
    project_root/.mcp.json, project_root/.mcp_json_builder.ts,
    .claude/thinking_processor.ts, .claude/settings.json,
    .claude/bash_executor.ts, .claude/credentials.json, .claude/history.jsonl,
    .claude/projects/<project-hash>/transcript.jsonl, .claude/models/subagents/

4.  DeepSeek-V3 Architecture (Dual-Pipe MoE)
    deepseek-v3-r1/
    format_reward.py, reasoning_steps_reward.py, model/modeling_deepseek.py,
    model/repetition_penalty.py, model/moe/deepseek_moe.py,
    model/moe/load_balancer.py, model/moe/shared_experts.py,
    model/distillation/distill_pipeline.py, model/communication/dual_pipe.py,
    model/attention/mla.py, model/attention/rope_embeddings.py,
    model/attention/fp8_mixed_precision.py, r1_reasoning/deep_ep/,
    inference/prompt_template.py

5.  Google Workspace Studio Flows
    google-workspace-studio-flows/
    manifest.json, studio_config.json, starters/email_trigger.ts,
    starters/form_trigger.ts, starters/webhook_listener.ts,
    steps/send_chat_message.ts, card_layout.ts

6.  Google Flow / google-flow-filmmaking/
    app/timeline/track_editor.tsx, app/timeline/keyframe_animator.tsx,
    app/asset_canvas/character_consistency.tsx,
    app/asset_canvas/style_transfer_picker.tsx,
    core_engine/sequence_planner/script_to_storyboard.py,
    core_engine/gpu_cluster_allocator.py, core_engine/audio_sync_engine.py,
    storage/camera_control.py, storage/scene_asset_vault/,
    editing_ops/inpainting_vace.py, editing_ops/expert_exporter.py,
    editing_ops/upscale_frame_interpolator.py

7.  GitHub Copilot & Copilot Studio (JetBrains & Visual Studio)
    copilot-ecosystem/
    ide_client_extension/src/context_providers/ast_chunker.ts,
    ide_client_extension/src/context_providers/workspace_indexer.ts,
    cloud_infrastructure/build_actions/snippet_filter.ts,
    cloud_infrastructure/agent_chat/participant_registry.ts,
    cloud_infrastructure/agent_chat/custom_api_plugin.py,
    cloud_infrastructure/security_guardrails/mcp_proxy.ts,
    cloud_infrastructure/security_guardrails/azure_content_safety.py,
    cloud_infrastructure/security_guardrails/tenant_isolation.py,
    copilot_studio_agent_flows/conversation_engine/intent_classifier.py,
    copilot_studio_agent_flows/conversation_engine/dialog_manager.py

8.  Perplexity AI / perplexity-core/
    conversation_engine/intent_classifier.py, conversation_engine/dialog_manager.py,
    real_time_retrieval/query_expansion/, build_actions/search_planner.py,
    build_actions/prebuilt_connectors.py

9.  OpenAI Codex / openai-codex-platform/
    citation_linker/grounder.py, codex_harness/session_orchestrator.py,
    codex_harness/deduplicator.py, project_learning/persistent_knowledge.py,
    project_learning/decision_history.py, planner/research_tree_search.py,
    tool/gap_analyzer.py, tool/mcp_connection_manager.py,
    synthesizer/function_call_router.py, synthesizer/structured_report_gen.py,
    execution_environments/websocket_handlers.py, synthesizer/summary_synthesizer.py

10. Deconstruction / docker.io/credkellar/deconstruction:latest
    Dockerfile, Makefile, bin/deconstruct, artifacts/test/captured_payloads/,
    artifacts/test/traces/, artifacts/test/reports/

11. Malware Sandbox Suite / docker.io/credkellar/malware-sandbox-suite:latest
    Dockerfile, docker-compose.yml, Makefile, pyproject.toml, Cargo.toml,
    bin/sandbox_daemon, bin/ebpf_loader, src/api/__init__.py, src/api/main.py,
    src/api/schemas.py, src/coordinator.py, src/dispatcher.py,
    src/detonation/executor.py, src/detonation/network_proxy.py,
    src/detonation/timeout_monitor.py, src/telemetry/ebpf_collector.py,
    src/telemetry/memory_dump.py, src/ai_synthesis/prompt_builder.py,
    src/ai_synthesis/threat_reporter.py, tests/test_api.py,
    tests/test_detonation.py, workspace/samples/, workspace/pcaps/,
    workspace/reports/

12. credkellar/app-data-compressor / docker.io/credkellar/app-data-compressor:latest
    Dockerfile, Cargo.toml, setup.py, Makefile, bin/compressor_cli,
    src/main.rs, src/encoder/zstd_stream.rs, src/encoder/lzma_adapter.rs,
    src/chunk_splitter.rs, src/packager/asset_bundler.rs,
    src/packager/manifest_gen.rs, src/validation/checksum_verify.rs,
    src/validation/integrity_check.rs, scripts/batch_compress.sh,
    scripts/optimize_assets.py, output/archives/, output/manifests/

13. credkellar/honeyroot-x / docker.io/credkellar/honeyroot-x:latest
    Dockerfile, src/main.py, src/__init__.py, src/server/router.py,
    src/server/ip_enrichment.py, src/alerts/webhook_dispatcher.py,
    src/logs/audit_logger.py, src/emulators/fake_ssh.py,
    src/emulators/fake_http.py, src/emulators/fake_sql.py,
    src/tracking/access_attempts/, src/tracking/session_recordings/,
    src/tracking/alerts/
```

## Mismatches / flags — separate from the recreation above

- **Title vs root, source 1:** the note is titled "ChatGPT Project
  Structure Tree (OpenAI Enterprise & Agent System)" but the root inside
  it is `gemini-4-frontier/`. Reproduced as supplied; the expert is
  named Gemini 4 Frontier after its root.
- **Overlap, sources 7–8:** `intent_classifier.py` / `dialog_manager.py`
  appear in both the Copilot Studio flows and the Perplexity tree in
  the notes as supplied. Kept in both experts.
- **Illegible in the video, omitted rather than invented:** one
  DeepSeek inference/serving listener filename, one Grok
  prompt-defense filename, and one Workspace Studio step filename
  could not be read cleanly from the frames. Everything else above
  was readable.
- **Counts:** 13 sources, 161 file entries total.
