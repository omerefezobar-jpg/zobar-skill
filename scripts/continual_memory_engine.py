"""
Continual Memory Engine (Episodic & Knowledge Graph User Memory)
Zobar Skill — Her Sohbette Öğrenen 3 Katmanlı Hafıza Motoru

Mimari:
1. Katman A: Çalışma Belleği (Aktif sohbet)
2. Katman B: Epizodik Bilgi Grafiği (Knowledge Graph Triples: [Özne, İlişki, Nesne])
3. Katman C: Kullanıcı Tercih Profili & Stil Kılavuzu (Kalıcı hafıza)

Her etkileşimde kullanıcının düzeltmelerini, teknoloji tercihlerini ve stil isteklerini
anında hafızaya işler ve yeni istemlere dinamik enjekte eder.
"""

import os
import re
import time
import json
from typing import Dict, Any, List, Optional, Tuple


class ContinualMemoryEngine:
    def __init__(self, memory_file: Optional[str] = None):
        if memory_file:
            self.memory_file = memory_file
        else:
            base_dir = os.path.join(os.path.dirname(__file__), "..", "references")
            os.makedirs(base_dir, exist_ok=True)
            self.memory_file = os.path.join(base_dir, "user_knowledge_graph.json")

        self.triples: List[Dict[str, Any]] = []
        self.user_profile: Dict[str, Any] = {
            "preferred_languages": [],
            "preferred_frameworks": [],
            "core_architectures": [],
            "performance_goals": [],
            "disliked_patterns": [],
            "last_updated": time.time(),
        }
        self.load()

    def load(self) -> None:
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.triples = data.get("triples", [])
                    self.user_profile = data.get("user_profile", self.user_profile)
            except Exception:
                pass

    def save(self) -> None:
        try:
            with open(self.memory_file, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "version": "1.0",
                        "triples": self.triples,
                        "user_profile": self.user_profile,
                        "total_triples_count": len(self.triples),
                        "last_saved": time.time(),
                    },
                    f,
                    indent=2,
                    ensure_ascii=False,
                )
        except Exception:
            pass

    def add_triple(self, subject: str, predicate: str, obj: str, confidence: float = 1.0) -> None:
        # Check if identical triple already exists to update confidence / timestamp
        for t in self.triples:
            if t["subject"].lower() == subject.lower() and t["predicate"].lower() == predicate.lower() and t["object"].lower() == obj.lower():
                t["confidence"] = min(t.get("confidence", 1.0) + 0.1, 2.0)
                t["last_reinforced"] = time.time()
                self.save()
                return

        new_triple = {
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "confidence": confidence,
            "created_at": time.time(),
            "last_reinforced": time.time(),
        }
        self.triples.append(new_triple)
        self.save()

    def learn_from_text(self, text: str) -> List[Dict[str, str]]:
        """
        Extracts user preferences, technologies, and constraints from conversation text.
        """
        extracted = []
        text_lower = text.lower()

        # Language extractions
        languages = ["python", "rust", "typescript", "c++", "go", "sql", "elixir"]
        for lang in languages:
            if re.search(rf"\b{lang}\b", text_lower):
                if lang not in self.user_profile["preferred_languages"]:
                    self.user_profile["preferred_languages"].append(lang)
                self.add_triple("user", "prefers_language", lang)
                extracted.append({"predicate": "prefers_language", "object": lang})

        # Framework / Stack extractions
        frameworks = ["supabase", "tauri", "react", "next.js", "webrtc", "opus", "redis", "postgres", "pgvector"]
        for fw in frameworks:
            if re.search(rf"\b{fw}\b", text_lower):
                if fw not in self.user_profile["preferred_frameworks"]:
                    self.user_profile["preferred_frameworks"].append(fw)
                self.add_triple("user", "uses_framework", fw)
                extracted.append({"predicate": "uses_framework", "object": fw})

        # Architectural and performance principles
        if re.search(r"\b(ecs|entity component system)\b", text_lower):
            self.add_triple("project", "architecture_pattern", "ECS")
            if "ECS" not in self.user_profile["core_architectures"]:
                self.user_profile["core_architectures"].append("ECS")
            extracted.append({"predicate": "architecture_pattern", "object": "ECS"})

        if re.search(r"\b(hızlı|hız|ultra-fast|low latency|gecikme|sub-millisecond)\b", text_lower):
            self.add_triple("user", "demands_performance", "Sub-Millisecond & Zero-Copy")
            if "Sub-Millisecond" not in self.user_profile["performance_goals"]:
                self.user_profile["performance_goals"].append("Sub-Millisecond")
            extracted.append({"predicate": "demands_performance", "object": "Sub-Millisecond"})

        if re.search(r"\b(sıfır maliyet|sıfır bütçe|para harcamadan|finops|bütçe minimal)\b", text_lower):
            self.add_triple("user", "budget_policy", "Zero-Cost & Free-Tier Leverage")
            if "Zero-Cost Leverage" not in self.user_profile["performance_goals"]:
                self.user_profile["performance_goals"].append("Zero-Cost Leverage")
            extracted.append({"predicate": "budget_policy", "object": "Zero-Cost Leverage"})

        self.user_profile["last_updated"] = time.time()
        self.save()
        return extracted

    BILINGUAL_SYNONYMS = {
        "mimari": ["architecture", "pattern", "mimari", "ecs"],
        "architecture": ["mimari", "pattern", "ecs"],
        "veritabanı": ["database", "framework", "supabase", "postgres", "veritabanı"],
        "database": ["veritabanı", "supabase", "postgres"],
        "dil": ["language", "rust", "python", "typescript", "c++", "go"],
        "language": ["dil", "rust", "python"],
        "performans": ["performance", "speed", "hız", "hızlı", "latency", "sub-millisecond"],
        "bütçe": ["budget", "cost", "maliyet", "finops", "zero-cost"],
    }

    def recall_relevant_memories(self, query: str) -> List[Dict[str, Any]]:
        """
        Retrieves triples relevant to the query to inject into context using bilingual expansion.
        """
        raw_words = set(re.findall(r"\w+", query.lower()))
        expanded_words = set(raw_words)
        for w in raw_words:
            for key, syns in self.BILINGUAL_SYNONYMS.items():
                if w.startswith(key) or key.startswith(w):
                    expanded_words.update(syns)

        matched = []

        for t in self.triples:
            subject_words = set(re.findall(r"\w+", t["subject"].lower()))
            object_words = set(re.findall(r"\w+", t["object"].lower()))
            predicate_words = set(re.findall(r"\w+", t["predicate"].lower()))

            all_triple_words = subject_words | object_words | predicate_words
            overlap = expanded_words & all_triple_words
            if overlap:
                matched.append(t)

        # Sort by confidence
        matched.sort(key=lambda x: x.get("confidence", 1.0), reverse=True)
        return matched

    def build_memory_prompt_injection(self) -> str:
        """
        Returns a concise system prompt injection containing persistent user memory.
        """
        lines = ["[ÖĞRENİLEN KULLANICI PROFİLİ VE ALIŞKANLIKLAR]"]
        if self.user_profile["preferred_languages"]:
            lines.append(f"• Tercih Edilen Diller: {', '.join(self.user_profile['preferred_languages']).upper()}")
        if self.user_profile["preferred_frameworks"]:
            lines.append(f"• Tercih Edilen Altyapı: {', '.join(self.user_profile['preferred_frameworks']).upper()}")
        if self.user_profile["core_architectures"]:
            lines.append(f"• Temel Mimariler: {', '.join(self.user_profile['core_architectures'])}")
        if self.user_profile["performance_goals"]:
            lines.append(f"• Performans İlkeleri: {', '.join(self.user_profile['performance_goals'])}")
        
        # High confidence triples
        top_triples = sorted(self.triples, key=lambda x: x.get("confidence", 1.0), reverse=True)[:5]
        if top_triples:
            facts = [f"({t['subject']} -> {t['predicate']} -> {t['object']})" for t in top_triples]
            lines.append(f"• Aktif Bilgi Grafiği Doğruları: {'; '.join(facts)}")

        return "\n".join(lines)


if __name__ == "__main__":
    mem = ContinualMemoryEngine()
    mem.learn_from_text("Ben projelerimde Rust ve Supabase kullanıyorum, ayrıca mimari olarak ECS tercih ediyorum ve her şey çok hızlı olmalı.")
    print("Enjekte Edilecek Hafıza Bloğu:\n")
    print(mem.build_memory_prompt_injection())
