"""
Smart Model Router & AI Cascade Engine (FinOps Optimization)
Zobar Skill — Intelligent Tier-Based LLM Cost Cutter

Saves 80-95% in recurring LLM API expenses by dynamically routing prompts
to the optimal cost/intelligence tier:
- Tier 0: Semantic Cache (0 USD, < 5ms)
- Tier 1: Local / Edge / Ultra-Cheap (e.g. Gemini 1.5 Flash, Llama 3.2, GPT-4o-Mini - $0.15/1M tokens)
- Tier 2: Frontier S-Tier Reasoning (e.g. Claude 3.5 Sonnet, GPT-4o, o1 - $3.00-$15.00/1M tokens)
"""

import re
import json
from typing import Dict, Any, List, Optional
try:
    from scripts.semantic_cache import SemanticCache
except ImportError:
    from semantic_cache import SemanticCache


class SmartModelRouter:
    # Model catalog with actual per-1M-token pricing (input/output)
    MODEL_CATALOG = {
        # Tier 1: Ultra-cheap / fast
        "gemini-1.5-flash": {
            "tier": 1,
            "cost_in_per_m": 0.075,
            "cost_out_per_m": 0.30,
            "avg_latency_ms": 320,
            "description": "Ultra-fast multimodal, ideal for summarization, QA, data formatting",
        },
        "gpt-4o-mini": {
            "tier": 1,
            "cost_in_per_m": 0.15,
            "cost_out_per_m": 0.60,
            "avg_latency_ms": 410,
            "description": "High-efficiency general purpose lightweight model",
        },
        "claude-3-5-haiku": {
            "tier": 1,
            "cost_in_per_m": 0.25,
            "cost_out_per_m": 1.25,
            "avg_latency_ms": 300,
            "description": "High-speed reasoning and light coding assistant",
        },
        "local-llama-3.2-3b": {
            "tier": 1,
            "cost_in_per_m": 0.00,
            "cost_out_per_m": 0.00,
            "avg_latency_ms": 180,
            "description": "Completely free local/edge model running via Ollama/vLLM",
        },
        # Tier 2: Heavy Frontier
        "claude-3-5-sonnet": {
            "tier": 2,
            "cost_in_per_m": 3.00,
            "cost_out_per_m": 15.00,
            "avg_latency_ms": 1600,
            "description": "State-of-the-art coding, architecture, deep reasoning",
        },
        "gpt-4o": {
            "tier": 2,
            "cost_in_per_m": 2.50,
            "cost_out_per_m": 10.00,
            "avg_latency_ms": 1400,
            "description": "Multimodal frontier reasoning engine",
        },
        "o1-preview": {
            "tier": 2,
            "cost_in_per_m": 15.00,
            "cost_out_per_m": 60.00,
            "avg_latency_ms": 4500,
            "description": "Deep chain-of-thought mathematical proof & complex algorithmic synthesis",
        },
    }

    # Triggers that justify Tier 2 expensive models
    TIER2_TRIGGERS = [
        r"(mimari\w*|architecture\w*|dağıtık\w*|distributed\w*|concurrency|eşzamanlı\w*|lock-free|kilit\w*|paxos|raft|consensus)",
        r"(derleyici\w*|compiler\w*|ast\b|byte\s*code|lexer\w*|parser\w*|llvm)",
        r"(formal proof|matematiksel ispat\w*|statutory\w*|mevzuat\w*|eu ai act|gdpr|kvkk|regülasyon\w*)",
        r"(multi-file|büyük refactor\w*|memory leak\w*|bellek sızıntı\w*|kernel\w*|driver\w*|vulkan\w*|webgpu\w*|shader\w*)",
        r"(b\+\s*tree|lsm\s*tree|game engine|oyun motoru|ecs\b|hft\b|high frequency|arbitraj\w*|quant\b)",
    ]

    # Triggers that are perfectly fine for Tier 1
    TIER1_TRIGGERS = [
        r"(özetle\w*|summarize\w*|translate\w*|çevir\w*|formatla\w*|json convert|regex)",
        r"(tanımla\w*|explain simply|örnek ver\w*|simple example|markdown düzenle\w*)",
        r"(kullanıcı adı|email doğrula\w*|test verisi\w*|mock data|dummy json)",
    ]

    def __init__(self, semantic_cache: Optional[SemanticCache] = None, enable_cache: bool = True):
        self.enable_cache = enable_cache
        self.cache = semantic_cache or (SemanticCache() if enable_cache else None)

    def analyze_complexity(self, prompt: str) -> Dict[str, Any]:
        prompt_lower = prompt.lower()
        word_count = len(prompt.split())
        
        # Scoring metrics
        tier2_matches = [
            m.group(0) for pattern in self.TIER2_TRIGGERS 
            for m in [re.search(pattern, prompt_lower)] if m
        ]
        tier1_matches = [
            m.group(0) for pattern in self.TIER1_TRIGGERS 
            for m in [re.search(pattern, prompt_lower)] if m
        ]

        # Calculate a normalized complexity score (0.0 to 1.0)
        base_score = 0.2
        if word_count > 300:
            base_score += 0.25
        elif word_count > 100:
            base_score += 0.15

        base_score += len(tier2_matches) * 0.25
        base_score -= len(tier1_matches) * 0.15
        complexity_score = min(max(base_score, 0.05), 1.0)

        requires_frontier = complexity_score >= 0.55 or len(tier2_matches) >= 2

        return {
            "word_count": word_count,
            "estimated_input_tokens": int(word_count * 1.35),
            "complexity_score": round(complexity_score, 2),
            "requires_frontier": requires_frontier,
            "tier2_detected_keywords": tier2_matches,
            "tier1_detected_keywords": tier1_matches,
        }

    def route(self, prompt: str, target_latency_budget_ms: Optional[int] = None) -> Dict[str, Any]:
        # 1. Tier 0: Check Semantic Cache
        if self.enable_cache and self.cache:
            cached_res = self.cache.get(prompt)
            if cached_res:
                return {
                    "tier": 0,
                    "model": "semantic-cache-hit",
                    "source": "cache",
                    "estimated_cost_usd": 0.0,
                    "estimated_latency_ms": cached_res["cache_latency_ms"],
                    "similarity_score": cached_res["similarity"],
                    "response": cached_res["response"],
                    "justification": f"Tam veya yüksek benzerlikli ({cached_res['similarity']}) önbellek eşleşmesi bulundu. API çağrısı yapılmadı.",
                    "savings_usd": cached_res["saved_usd"],
                }

        # 2. Analyze Prompt Complexity
        analysis = self.analyze_complexity(prompt)
        input_tokens = analysis["estimated_input_tokens"]
        expected_output_tokens = min(max(int(input_tokens * 1.5), 200), 2000)

        # 3. Decision Logic
        if analysis["requires_frontier"] and (not target_latency_budget_ms or target_latency_budget_ms > 800):
            selected_model = "claude-3-5-sonnet"
            tier = 2
            justification = f"Görev yüksek karmaşıklık ({analysis['complexity_score']}) ve kritik teknik/mimari derinlik içeriyor ({', '.join(analysis['tier2_detected_keywords']) or 'uzun girdi'})."
        else:
            # Routine / Fast / Cost-effective
            selected_model = "gpt-4o-mini"
            tier = 1
            justification = f"Görev rutin, özetleme veya orta düzey karmaşıklıkta ({analysis['complexity_score']}). Tier 1 hafif model yeterli."

        model_info = self.MODEL_CATALOG[selected_model]
        cost_in = (input_tokens / 1_000_000.0) * model_info["cost_in_per_m"]
        cost_out = (expected_output_tokens / 1_000_000.0) * model_info["cost_out_per_m"]
        total_estimated_cost = round(cost_in + cost_out, 6)

        # Compare with frontier baseline (e.g. GPT-4o)
        frontier_baseline = (input_tokens / 1_000_000.0 * 2.50) + (expected_output_tokens / 1_000_000.0 * 10.00)
        saved_vs_frontier = max(round(frontier_baseline - total_estimated_cost, 6), 0.0)

        return {
            "tier": tier,
            "model": selected_model,
            "source": "model_catalog",
            "estimated_cost_usd": total_estimated_cost,
            "estimated_latency_ms": model_info["avg_latency_ms"],
            "analysis": analysis,
            "justification": justification,
            "savings_vs_frontier_usd": saved_vs_frontier,
            "cost_reduction_percent": round((saved_vs_frontier / frontier_baseline * 100.0), 1) if frontier_baseline > 0 and tier == 1 else 0.0,
        }


if __name__ == "__main__":
    router = SmartModelRouter()
    
    test_queries = [
        "React ile basit bir sayaç (counter) butonu nasıl yapılır?",
        "PostgreSQL'de distributed multi-region transaction lock-free concurrency mimarisini ve B+ Tree disk bloklarını açıkla.",
        "Şu kullanıcı listesindeki emailleri JSON formatına dönüştür ve doğrula.",
    ]
    
    for q in test_queries:
        res = router.route(q)
        print("="*60)
        print(f"QUERY: {q[:60]}...")
        print(f"ROUTED TO: {res['model']} (Tier {res['tier']})")
        print(f"COST: ${res['estimated_cost_usd']} | LATENCY: ~{res['estimated_latency_ms']}ms")
        print(f"REASON: {res['justification']}")
