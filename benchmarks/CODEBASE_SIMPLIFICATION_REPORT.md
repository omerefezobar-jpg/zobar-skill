# 🧹 Zobar Skill: Kod Tabanı Sadeleştirme ve Pruning Denetim Raporu
*Oluşturulma Tarihi: 2026-10-29 02:41:19 | Toplam Script Sayısı: 49 | Toplam Satır (LOC): 14826*

> Bu rapor, **Pillar 5 (Özellik eklemekten önce sadeleştir)** gereksinimini karşılamak amacıyla oluşturulmuştur.
> Kullanılmayan, tek seferlik üretici (one-off) veya tekrarlı modülleri tespit ederek bakım maliyetini düşürmeyi hedefler.

## 1. Yönetici Özeti (Executive Summary)
- **Çekirdek Sistem Motorları (Mission-Critical):** 5 modül
- **Aktif Alan Motorları (Active Domain Engines):** 39 modül
- **Arşivlenebilir Tek Seferlik Üreteçler (One-Off Generators):** 5 modül

## 2. Arşivleme ve Sadeleştirme Adayları (One-Off Vault Generators)
Aşağıdaki 5 script yalnızca `references/` altındaki JSON veri tabanlarını (S-Tier vault, 3D asetler, modern bileşenler) oluşturmak için tek seferlik çalıştırılmıştır. Çalışma zamanında (runtime) sistem doğrudan bu JSON dosyalarını okuduğundan, bu scriptlerin ana pipeline'da bulunması bakım yükü yaratır:

| Dosya | Satır (LOC) | Açıklama | Öneri |
|---|---|---|---|
| `build_asset_vault.py` | 260 | LOW_RISK_PRUNE (Runtime bağımlılığı yok, references/*.json hazır) | `scripts/archive/` dizinine taşı veya dondur |
| `build_s_tier_vault_200.py` | 900 | LOW_RISK_PRUNE (Runtime bağımlılığı yok, references/*.json hazır) | `scripts/archive/` dizinine taşı veya dondur |
| `expand_assets_and_3d_vault.py` | 367 | LOW_RISK_PRUNE (Runtime bağımlılığı yok, references/*.json hazır) | `scripts/archive/` dizinine taşı veya dondur |
| `expand_modern_components.py` | 424 | LOW_RISK_PRUNE (Runtime bağımlılığı yok, references/*.json hazır) | `scripts/archive/` dizinine taşı veya dondur |
| `expand_s_tier_vault_400.py` | 1799 | LOW_RISK_PRUNE (Runtime bağımlılığı yok, references/*.json hazır) | `scripts/archive/` dizinine taşı veya dondur |

## 3. Tekrarlı Fonksiyonlar & Konsolidasyon Fırsatları
Aşağıdaki tekrarlı yardımcı rutinler tespit edilmiştir:
1. **`sys.stdout.reconfigure(encoding='utf-8')`**: 32 farklı scriptte tekrar ediyor.
2. **Metin Temizleme ve Stop-Word Tokenizer**: 6 farklı araştırma ve kanıt motorunda bağımsız uygulanmış.
3. **JSON Yükleme & Hata Yakalama Blokları**: 14 scriptte birebir aynı `try-except` kalıbı bulunuyor.

**Çözüm:** `scripts/common_core_utils.py` oluşturularak bu tekrarlar tek bir sıfır-bağımlılık yardımcı modülünde birleştirilebilir.

## 4. Tüm Modüllerin Bağımlılık & Olgunluk Tablosu
| Modül Adı | LOC | Sınıflar | Fonksiyonlar | Referans Sayısı | Kategori |
|---|---|---|---|---|---|
| `analyze_heavy_app_architecture.py` | 98 | - | 3 | 2 | ACTIVE_DOMAIN_ENGINE |
| `benchmark_competitors.py` | 263 | - | 5 | 3 | ACTIVE_DOMAIN_ENGINE |
| `build_asset_vault.py` | 260 | - | 0 | 0 | ONE_OFF_GENERATOR |
| `build_s_tier_vault_200.py` | 900 | - | 1 | 0 | ONE_OFF_GENERATOR |
| `business_school_case_engine.py` | 187 | BusinessSchoolCaseEngine | 2 | 1 | ACTIVE_DOMAIN_ENGINE |
| `codebase_simplifier_and_pruner.py` | 201 | CodebaseAuditor | 5 | 0 | ACTIVE_DOMAIN_ENGINE |
| `context_compressor.py` | 180 | ContextCompressor | 6 | 2 | ACTIVE_DOMAIN_ENGINE |
| `continual_memory_engine.py` | 204 | ContinualMemoryEngine | 7 | 3 | ACTIVE_DOMAIN_ENGINE |
| `creative_evolutionary_designer.py` | 216 | - | 5 | 3 | ACTIVE_DOMAIN_ENGINE |
| `design_system_generator.py` | 186 | ModernDesignStylesEngine | 4 | 1 | ACTIVE_DOMAIN_ENGINE |
| `dpo_lora_dataset_pipeline.py` | 133 | DPOLoRADatasetPipeline | 6 | 1 | ACTIVE_DOMAIN_ENGINE |
| `ecs_game_engine.py` | 295 | Transform2D, Velocity2D, BoundingBox2D, SpatialQuadtree, ECSWorld, MovementSystem, CollisionSystem, DeterministicGameLoop | 23 | 3 | ACTIVE_DOMAIN_ENGINE |
| `evidence_provenance_engine.py` | 340 | EvidenceProvenanceGraph, ClaimEvidenceQualityScorer | 10 | 6 | ACTIVE_DOMAIN_ENGINE |
| `expand_assets_and_3d_vault.py` | 367 | - | 2 | 0 | ONE_OFF_GENERATOR |
| `expand_modern_components.py` | 424 | - | 1 | 0 | ONE_OFF_GENERATOR |
| `expand_s_tier_vault_400.py` | 1799 | - | 3 | 0 | ONE_OFF_GENERATOR |
| `export_html_report.py` | 294 | - | 9 | 1 | ACTIVE_DOMAIN_ENGINE |
| `feedback_outcome_learning_engine.py` | 177 | FeedbackOutcomeEngine | 7 | 4 | ACTIVE_DOMAIN_ENGINE |
| `fetch_academic_papers.py` | 101 | - | 2 | 2 | ACTIVE_DOMAIN_ENGINE |
| `fetch_university_research.py` | 881 | - | 5 | 2 | ACTIVE_DOMAIN_ENGINE |
| `freelance_agency_growth_engine.py` | 151 | - | 3 | 3 | ACTIVE_DOMAIN_ENGINE |
| `game_modding_engine.py` | 258 | - | 4 | 3 | ACTIVE_DOMAIN_ENGINE |
| `human_delight_psychology_engine.py` | 142 | - | 3 | 3 | ACTIVE_DOMAIN_ENGINE |
| `image_prompt_synthesizer.py` | 134 | ImagePromptSynthesizer | 2 | 2 | ACTIVE_DOMAIN_ENGINE |
| `llm_hardware_accelerator.py` | 116 | PagedAttentionManager, SpeculativeDecodingSimulator, ModelQuantizationBenchmark | 5 | 1 | ACTIVE_DOMAIN_ENGINE |
| `mcp_skill_integrator.py` | 168 | MCPSkillIntegrator | 3 | 1 | MISSION_CRITICAL_CORE |
| `mine_user_sentiment.py` | 305 | - | 9 | 3 | ACTIVE_DOMAIN_ENGINE |
| `modern_component_snippets.py` | 66 | ModernComponentsEngine | 5 | 3 | ACTIVE_DOMAIN_ENGINE |
| `module_maturity_auditor.py` | 421 | ModuleMaturityAuditor | 5 | 1 | ACTIVE_DOMAIN_ENGINE |
| `multi_agent_deliberation_council.py` | 344 | - | 6 | 4 | ACTIVE_DOMAIN_ENGINE |
| `query_asset_vault.py` | 106 | AssetVaultQueryEngine | 4 | 2 | ACTIVE_DOMAIN_ENGINE |
| `realtime_audio_voice_engine.py` | 157 | OpusPacket, DiscordSFURouter, ElevenLabsStreamingTTS | 8 | 2 | ACTIVE_DOMAIN_ENGINE |
| `recommend_ui_patterns.py` | 143 | - | 3 | 2 | ACTIVE_DOMAIN_ENGINE |
| `reverse_engineering_analyst.py` | 221 | - | 6 | 3 | ACTIVE_DOMAIN_ENGINE |
| `scan_regulations.py` | 588 | - | 2 | 6 | MISSION_CRITICAL_CORE |
| `search_prior_art.py` | 96 | - | 2 | 2 | ACTIVE_DOMAIN_ENGINE |
| `security_permission_guard.py` | 534 | SecuritySandboxViolation, PythonASTSecurityVisitor, SecurityPermissionGuard | 16 | 8 | MISSION_CRITICAL_CORE |
| `semantic_cache.py` | 301 | SemanticCache | 11 | 5 | ACTIVE_DOMAIN_ENGINE |
| `skill_registry_and_installer_engine.py` | 153 | - | 4 | 3 | ACTIVE_DOMAIN_ENGINE |
| `smart_model_router.py` | 203 | SmartModelRouter | 3 | 2 | ACTIVE_DOMAIN_ENGINE |
| `supabase_db_optimizer.py` | 117 | SupabaseDBOptimizer | 2 | 2 | ACTIVE_DOMAIN_ENGINE |
| `synthesize_architecture.py` | 99 | - | 2 | 4 | ACTIVE_DOMAIN_ENGINE |
| `systems_math_engine.py` | 245 | SystemsMathEngine | 5 | 4 | ACTIVE_DOMAIN_ENGINE |
| `trend_trick_harvester_engine.py` | 599 | TrendTrickHarvesterEngine | 21 | 3 | ACTIVE_DOMAIN_ENGINE |
| `unified_system_orchestrator.py` | 424 | UnifiedSystemOrchestrator | 5 | 5 | MISSION_CRITICAL_CORE |
| `unit_economics_investor_simulator.py` | 111 | UnitEconomicsSimulator | 3 | 3 | ACTIVE_DOMAIN_ENGINE |
| `validate_inventions.py` | 222 | - | 3 | 2 | ACTIVE_DOMAIN_ENGINE |
| `vibe_coding_bridge.py` | 112 | VibeCodingBridge | 3 | 1 | ACTIVE_DOMAIN_ENGINE |
| `zobar_mcp_server.py` | 784 | ZobarMCPServer | 5 | 8 | MISSION_CRITICAL_CORE |

## 5. Sonuç ve Eylem Planı (Action Plan)
1. **Tek Seferlik Üreteçleri Dondur**: 5 adet `build_*` ve `expand_*` scriptini arşiv dizinine taşıyarak runtime kod yüzeyini daralt.
2. **Ortak Yardımcıları Birleştir**: `common_core_utils.py` ile UTF-8 ve JSON util tekrarlarını ortadan kaldır.
3. **Bağımsız Benchmark & AST Koruması**: Bağımsız kör benchmark (12 vaka) ve AST sandbox korumasını koru.