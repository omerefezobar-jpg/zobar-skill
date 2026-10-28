#!/usr/bin/env python3
"""
Zobar Skill: Evidence Provenance, Lineage & Freshness Engine.
Tracks the academic, statutory, and empirical lineage of every finding and architectural decision.

FEATURES:
1. Ground Truth Categorization:
   - STATUTORY_GROUND_TRUTH: Official EU AI Act, MDR Rule 11, GDPR articles.
   - PEER_REVIEWED_EMPIRICAL: OpenAlex / arXiv publications with verified citations.
   - INDUSTRY_TELEMETRY: Live npm/PyPI registry metrics, GitHub stars, commercial pricing.
   - ARCHITECTURAL_HEURISTIC: Established systems engineering models (Roofline, Little's Law, Amdahl).
   - MODEL_HYPOTHESIS: Unverified LLM hypotheses explicitly flagged for human verification.
2. Causal Lineage: Maps which architecture decision was caused by which piece of evidence.
3. Freshness & Staleness Detection: Detects stale data older than retention limits.
"""

import sys
import os
import json
import datetime
import argparse
from typing import Dict, List, Any, Optional

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CONFIDENCE_TIERS = {
    "STATUTORY_GROUND_TRUTH": {
        "level": 1,
        "trust_score": 1.0,
        "description": "Resmî kanun, AB tüzüğü veya emsal yargı kararı (Kesin bağlayıcı)."
    },
    "PEER_REVIEWED_EMPIRICAL": {
        "level": 2,
        "trust_score": 0.95,
        "description": "Hakemli akademik makale, üniversite müfredatı veya laboratuvar deneyi."
    },
    "INDUSTRY_TELEMETRY": {
        "level": 3,
        "trust_score": 0.85,
        "description": "Canlı paket kayıtları, pazar lideri fiyatlandırmaları ve GitHub telemetrisi."
    },
    "ARCHITECTURAL_HEURISTIC": {
        "level": 4,
        "trust_score": 0.80,
        "description": "Matematiksel sistem mühendisliği prensipleri (Roofline, Little's Law vb.)."
    },
    "MODEL_HYPOTHESIS": {
        "level": 5,
        "trust_score": 0.50,
        "description": "Yapay zeka çıkarımı veya varsayım; bağımsız doğrulama gerektirir."
    }
}

class EvidenceProvenanceGraph:
    def __init__(self):
        self.evidence_nodes: Dict[str, Dict[str, Any]] = {}
        self.causal_links: List[Dict[str, Any]] = []

    def record_evidence(
        self,
        evidence_id: str,
        source_type: str,
        citation: str,
        claim_supported: str,
        confidence_tier: str = "STATUTORY_GROUND_TRUTH",
        url_or_identifier: str = "",
        published_year: int = 2024
    ) -> Dict[str, Any]:
        """Registers a verified piece of evidence with its confidence tier and timestamp."""
        tier = confidence_tier if confidence_tier in CONFIDENCE_TIERS else "MODEL_HYPOTHESIS"
        now = datetime.datetime.now(datetime.timezone.utc)
        
        # Calculate staleness: market/telemetry data stale after 1 year, laws valid until superseded
        current_year = now.year
        age_years = current_year - published_year
        is_stale = False
        if tier == "INDUSTRY_TELEMETRY" and age_years > 1:
            is_stale = True
        elif tier == "MODEL_HYPOTHESIS" and age_years > 2:
            is_stale = True

        node = {
            "evidence_id": evidence_id,
            "source_type": source_type,
            "citation": citation,
            "url_or_identifier": url_or_identifier,
            "claim_supported": claim_supported,
            "confidence_tier": tier,
            "trust_weight": CONFIDENCE_TIERS[tier]["trust_score"],
            "published_year": published_year,
            "age_years": age_years,
            "is_stale": is_stale,
            "retrieved_at_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "verification_status": "DOĞRULANMIŞ BULGU" if tier != "MODEL_HYPOTHESIS" else "MODEL HİPOTEZİ (TEST GEREKTİRİR)"
        }
        self.evidence_nodes[evidence_id] = node
        return node

    def link_decision(self, decision_id: str, decision_summary: str, evidence_ids: List[str]):
        """Creates causal lineage linking an architectural/legal decision to its underlying evidence."""
        self.causal_links.append({
            "decision_id": decision_id,
            "decision_summary": decision_summary,
            "backed_by_evidence_ids": evidence_ids,
            "linked_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        })

    def audit_evidence_integrity(self) -> Dict[str, Any]:
        """Calculates provenance integrity, trust distribution, and identifies ungrounded hypotheses."""
        total_nodes = len(self.evidence_nodes)
        if total_nodes == 0:
            return {"total_evidence": 0, "verified_ratio": 0.0, "stale_sources_count": 0, "trust_index": 0.0}

        verified_nodes = sum(1 for n in self.evidence_nodes.values() if n["confidence_tier"] != "MODEL_HYPOTHESIS")
        stale_nodes = sum(1 for n in self.evidence_nodes.values() if n["is_stale"])
        avg_trust = sum(n["trust_weight"] for n in self.evidence_nodes.values()) / total_nodes

        return {
            "total_evidence_count": total_nodes,
            "verified_evidence_count": verified_nodes,
            "hypotheses_count": total_nodes - verified_nodes,
            "verified_ratio_pct": round((verified_nodes / total_nodes) * 100.0, 1),
            "stale_sources_count": stale_nodes,
            "aggregate_trust_index": round(avg_trust, 3),
            "lineage_links_count": len(self.causal_links)
        }

    def export_provenance_dossier(self) -> Dict[str, Any]:
        """Exports the complete machine-readable and human-verifiable provenance dossier."""
        return {
            "audit_summary": self.audit_evidence_integrity(),
            "evidence_nodes": list(self.evidence_nodes.values()),
            "causal_lineage": self.causal_links
        }

def build_default_evidence_graph() -> EvidenceProvenanceGraph:
    """Instantiates a populated evidence graph with core legal and systems engineering foundations."""
    g = EvidenceProvenanceGraph()

    g.record_evidence(
        evidence_id="EVID-EU-AI-ACT-2024",
        source_type="Statutory Regulation",
        citation="Regulation (EU) 2024/1689 of the European Parliament and of the Council (Artificial Intelligence Act)",
        claim_supported="Madde 5(1) yasaklı sistemler ve Ek III yüksek riskli sistemlerin yasal sınıflandırma temeli.",
        confidence_tier="STATUTORY_GROUND_TRUTH",
        url_or_identifier="https://eur-lex.europa.eu/eli/reg/2024/1689/oj",
        published_year=2024
    )

    g.record_evidence(
        evidence_id="EVID-EU-DIR-2009-24",
        source_type="Statutory Directive & Safe Harbor",
        citation="Directive 2009/24/EC on the legal protection of computer programs (Articles 5(3) & 6)",
        claim_supported="Birlikte çalışabilirlik (Interoperability) amacıyla yapılan tersine mühendisliğin yasal güvencesi.",
        confidence_tier="STATUTORY_GROUND_TRUTH",
        url_or_identifier="Directive 2009/24/EC Article 6",
        published_year=2009
    )

    g.record_evidence(
        evidence_id="EVID-BERKELEY-ROOFLINE",
        source_type="Peer-Reviewed Systems Paper",
        citation="Williams, S., Waterman, A., & Patterson, D. (2009). Roofline: an insightful visual performance model for multicore architectures. Communications of the ACM, 52(4), 65-76.",
        claim_supported="Bellek bant genişliği ve donanım tepe FLOP sınırlarının matematiksel modellemesi.",
        confidence_tier="PEER_REVIEWED_EMPIRICAL",
        url_or_identifier="doi:10.1145/1498765.1498785",
        published_year=2009
    )

    g.record_evidence(
        evidence_id="EVID-GREEDY-MESHING",
        source_type="Algorithmic Computer Graphics Specification",
        citation="Mikola Lysenko (2012). Meshing in Minecraft: Part 2 (Greedy Meshing algorithm for voxel rendering).",
        claim_supported="Voksel chunk çizim çağrılarının (draw calls) %85-92 oranında azaltılması.",
        confidence_tier="ARCHITECTURAL_HEURISTIC",
        url_or_identifier="https://0fps.net/2012/06/30/meshing-in-minecraft-part-2/",
        published_year=2012
    )

    g.link_decision(
        decision_id="DEC-01-CLEAN-ROOM",
        decision_summary="Tersine mühendislik araçlarında Çin Seddi (Clean-Room) zorunluluğu getirilmesi.",
        evidence_ids=["EVID-EU-DIR-2009-24"]
    )

    g.link_decision(
        decision_id="DEC-02-VOXEL-OPTIMIZATION",
        decision_summary="Voksel oyun motorunda naif küp çizimi yerine Greedy Meshing kullanılması.",
        evidence_ids=["EVID-GREEDY-MESHING", "EVID-BERKELEY-ROOFLINE"]
    )

    return g

def main():
    parser = argparse.ArgumentParser(description="Zobar Skill Evidence Provenance & Lineage Engine.")
    parser.add_argument("--audit", action="store_true", help="Audit evidence integrity and freshness")
    args = parser.parse_args()

    print(f"\n=================================================================")
    print(f" 📜 KAYNAK, KANIT VE İZLENEBİLİRLİK (PROVENANCE) GRAFİĞİ")
    print(f"=================================================================\n")

    g = build_default_evidence_graph()
    audit = g.audit_evidence_integrity()
    print(f"📊 Toplam Kanıt Kaydı    : {audit['total_evidence_count']}")
    print(f"✅ Doğrulanmış Kaynak    : {audit['verified_evidence_count']} (%{audit['verified_ratio_pct']})")
    print(f"⚠️ Model Hipotezleri     : {audit['hypotheses_count']}")
    print(f"⏳ Güncelliğini Yitiren  : {audit['stale_sources_count']}")
    print(f"💎 Güvenilirlik Endeksi  : {audit['aggregate_trust_index']}/1.000\n")

    print("🔗 Karar - Kanıt Nedensellik Bağlantıları (Causal Lineage):")
    for link in g.causal_links:
        print(f"   • Karar [{link['decision_id']}]: {link['decision_summary']}")
        print(f"     Dayandığı Kanıtlar: {link['backed_by_evidence_ids']}\n")

if __name__ == "__main__":
    main()
