#!/usr/bin/env python3
"""
Zobar Skill: Multi-Agent Deliberation Council (Senato & Ortak Akıl Motoru).
Simulates an intense, multi-perspective adversarial debate between:
1. Academic Council (Akademisyenler): Theoretical limits, algorithmic complexity, safety proofs.
2. Public Assembly (Halk Meclisi): User ergonomics, affordability, privacy, friction.
3. Workforce & Operations Council (Çalışanlar): On-call burnout, toil, maintainability, tech debt.
4. Final Executive Board Assembly (Nihai Karar Toplantısı): Multi-round cross-examination,
   dissenting opinion logging (azınlık şerhi), and ratified binding consensus.
"""

import sys
import os
import json
import argparse
from typing import Dict, List, Any

# Ensure UTF-8 stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def simulate_academic_council(topic: str) -> Dict[str, Any]:
    """Academic council evaluates theoretical correctness, asymptotic complexity, and citations."""
    topic_lower = topic.lower()
    
    # Rigor scoring heuristics
    is_complex = any(k in topic_lower for k in ["compiler", "engine", "ai", "model", "distributed", "crypto", "voxel"])
    is_risky = any(k in topic_lower for k in ["unbounded", "scrape", "emotion", "surveillance", "predictive"])
    
    base_score = 75
    if is_complex:
        base_score += 15
    if is_risky:
        base_score -= 30

    score = max(20, min(100, base_score))

    critiques = [
        "Asimptotik karmaşıklık analizi: O(N log N) veya O(1) alt sınırları garanti edilmelidir; bellekte kontrolsüz şişme olmamalıdır.",
        "Kanıt taksonomisi: İddialar yalnızca varsayım olarak bırakılamaz; hakemli literatür veya ampirik kıyaslama ile doğrulanmalıdır."
    ]
    if is_risky:
        critiques.append("Etik ve algoritma güvenliği: Deterministik olmayan LLM çıktılarının kritik döngülere doğrudan bağlanması kabul edilemez.")

    return {
        "council_name": "Akademisyenler Heyeti (Academic Council)",
        "lead_delegate": "Prof. Dr. Alan Systems (Teorik Bilgisayar Bilimi & Sistem Mimarisi)",
        "score": score,
        "verdict": "ONAY" if score >= 70 else ("ŞARTLI REVİZYON" if score >= 50 else "RED"),
        "key_citations": [
            "Knuth, D. E. (The Art of Computer Programming, Vol 1-3)",
            "Lamport, L. (Time, Clocks, and the Ordering of Events in a Distributed System)",
            "Dean, J. & Ghemawat, S. (MapReduce / Large-Scale Distributed Computing)"
        ],
        "substantive_arguments": critiques
    }

def simulate_public_assembly(topic: str) -> Dict[str, Any]:
    """Public assembly evaluates cognitive overload, privacy, pricing fairness, and community utility."""
    topic_lower = topic.lower()

    is_accessible = any(k in topic_lower for k in ["open", "free", "ui", "glassy", "design", "game", "mod", "minecraft"])
    is_invasive = any(k in topic_lower for k in ["tracking", "biometric", "workplace monitoring", "dismissal", "telemetry"])

    base_score = 70
    if is_accessible:
        base_score += 20
    if is_invasive:
        base_score -= 45

    score = max(15, min(100, base_score))

    concerns = [
        "Kullanıcı deneyimi: Karmaşık mühendislik jargonunun arkasında son kullanıcıyı boğan bir arayüz olmamalıdır.",
        "Maliyet ve şeffaflık: Kullanıcı ne ödeyeceğini ve verilerinin nereye gittiğini tek bakışta bilmelidir."
    ]
    if is_invasive:
        concerns.append("Halkın Mahremiyet Şerhi: Bireysel hayatı gözetleyen algoritmalar halk meclisinde kabul göremez.")

    return {
        "council_name": "Halk Meclisi & Topluluk Oylaması (Public Assembly)",
        "lead_delegate": "Topluluk Temsilcisi & Tüketici Hakları Ombudsmanı",
        "score": score,
        "turnout_rate_pct": 89.4,
        "verdict": "HALK DESTEĞİ" if score >= 70 else ("KAYGILI ÇOĞUNLUK" if score >= 50 else "TOPLUMSAL VETO"),
        "substantive_arguments": concerns
    }

def simulate_workforce_council(topic: str) -> Dict[str, Any]:
    """Workforce council evaluates on-call fatigue, technical debt, CI/CD maintainability, and implementation toil."""
    topic_lower = topic.lower()

    is_heavy_toil = any(k in topic_lower for k in ["microservice", "distributed", "realtime", "k8s", "c++", "kernel"])
    has_ergonomic_tools = any(k in topic_lower for k in ["standard library", "zero-copy", "script", "cli", "clean-room", "cache"])

    base_score = 68
    if has_ergonomic_tools:
        base_score += 18
    if is_heavy_toil:
        base_score -= 15

    score = max(25, min(100, base_score))

    feedback = [
        "Operasyonel sürdürülebilirlik: Gece 03:00 nöbetinde alarm üretecek kırılgan bağımlılıklar eklenmemelidir.",
        "Temiz kod ve test edilebilirlik: 100% deterministik, çevrimdışı çalışabilen mock testler şarttır."
    ]
    if is_heavy_toil:
        feedback.append("Teknik Borç Uyarısı: Aşırı mühendislik (over-engineering) yerine sade standart kütüphane tercih edilmelidir.")

    return {
        "council_name": "Çalışanlar & Saha Mühendisleri Heyeti (Workforce & Operations Council)",
        "lead_delegate": "Kıdemli Saha Güvenilirlik Mühendisi (Lead SRE & Senior Devs)",
        "score": score,
        "verdict": "SAHA ONAYI" if score >= 70 else ("YÜKSEK İŞ YÜKÜ RİSKİ" if score >= 50 else "RED"),
        "substantive_arguments": feedback
    }

def conduct_executive_board_deliberation(topic: str) -> Dict[str, Any]:
    """
    Executes a 3-round adversarial debate and calculates the binding synthesized mandate.
    Consensus Formula: C = (0.35 * Academic) + (0.35 * Public) + (0.30 * Workforce)
    """
    acad = simulate_academic_council(topic)
    pub = simulate_public_assembly(topic)
    work = simulate_workforce_council(topic)

    w_acad = 0.35
    w_pub = 0.35
    w_work = 0.30

    consensus_score = round((acad["score"] * w_acad) + (pub["score"] * w_pub) + (work["score"] * w_work), 2)

    if consensus_score >= 70.0:
        final_resolution = "ONAYLANDI (RATIFIED BY SENATE)"
        mandate_action = "Özellik derhal üretim protokolüne dahil edilir; tüm heyetlerin mutabakatı sağlanmıştır."
    elif consensus_score >= 50.0:
        final_resolution = "ŞARTLI KABUL (CONDITIONAL WITH AMENDMENTS)"
        mandate_action = "Özellik kabul edilmiş ancak halk ve mühendislerin belirttiği kısıtlamalarla sınırlanmıştır."
    else:
        final_resolution = "REDDEDİLDİ (VETOED BY DELIBERATION COUNCIL)"
        mandate_action = "Yüksek etik, operasyonel veya teorik risk nedeniyle tasarım rafa kaldırılmış veya tamamen değiştirilmelidir."

    # Structured Debate Rounds
    debate_transcript = [
        {
            "round": 1,
            "phase": "Açılış Tezleri ve İlk Değerlendirmeler",
            "dialogue": [
                f"🎓 {acad['lead_delegate']}: 'Konuyu teorik temel ve algoritma sınırları açısından {acad['score']}/100 puanla karşılıyoruz.'",
                f"👥 {pub['lead_delegate']}: 'Halk Meclisi olarak erişilebilirlik, gizlilik ve kullanım kolaylığına {pub['score']}/100 verdik.'",
                f"🛠️ {work['lead_delegate']}: 'Saha ekibi olarak bakım maliyeti ve teknik borcu {work['score']}/100 olarak değerlendirdik.'"
            ]
        },
        {
            "round": 2,
            "phase": "Çapraz Sorgu & Karşıt Görüşler (Adversarial Critique)",
            "dialogue": [
                f"⚔️ Akademisyenler -> Saha Ekibine: '{acad['substantive_arguments'][0]}'",
                f"⚔️ Halk Meclisi -> Akademisyenlere: '{pub['substantive_arguments'][0]}'",
                f"⚔️ Saha Ekibi -> Herkese: '{work['substantive_arguments'][0]}'"
            ]
        },
        {
            "round": 3,
            "phase": "Uzlaşma Maddeleri & Azınlık Şerhi (Compromise & Dissent Log)",
            "dialogue": [
                "🏛️ Senato Başkanı: 'Tüm tarafların çekinceleri tutanağa geçirildi. Nihai ağırlıklı konsensüs hesaplanıyor.'"
            ]
        }
    ]

    # Collect dissenting opinions if any council voted under 65
    dissenting_opinions = []
    if acad["score"] < 65:
        dissenting_opinions.append(f"Akademi Azınlık Şerhi: {acad['substantive_arguments'][-1]}")
    if pub["score"] < 65:
        dissenting_opinions.append(f"Halk Meclisi Azınlık Şerhi: {pub['substantive_arguments'][-1]}")
    if work["score"] < 65:
        dissenting_opinions.append(f"Mühendislik Azınlık Şerhi: {work['substantive_arguments'][-1]}")

    if not dissenting_opinions:
        dissenting_opinions.append("Tam Mutabakat: Ciddi bir azınlık şerhi bulunmamaktadır.")

    return {
        "deliberation_topic": topic,
        "council_scores": {
            "academic": {"score": acad["score"], "weight": w_acad, "verdict": acad["verdict"]},
            "public": {"score": pub["score"], "weight": w_pub, "verdict": pub["verdict"]},
            "workforce": {"score": work["score"], "weight": w_work, "verdict": work["verdict"]}
        },
        "consensus_score": consensus_score,
        "final_resolution": final_resolution,
        "mandate_action": mandate_action,
        "dissenting_opinions_log": dissenting_opinions,
        "debate_transcript": debate_transcript,
        "councils_detail": {
            "academic": acad,
            "public": pub,
            "workforce": work
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Zobar Skill Multi-Agent Deliberation Council.")
    parser.add_argument("topic", help="Topic or architecture proposal to deliberate upon")
    args = parser.parse_args()

    print(f"\n=================================================================")
    print(f" 🏛️ ÇOKLU-AJAN SENATO & KARAR TOPLANTISI: '{args.topic}'")
    print(f"=================================================================\n")

    res = conduct_executive_board_deliberation(args.topic)
    print(f"🎓 Akademisyenler Puanı : {res['council_scores']['academic']['score']}/100 ({res['council_scores']['academic']['verdict']})")
    print(f"👥 Halk Meclisi Puanı   : {res['council_scores']['public']['score']}/100 ({res['council_scores']['public']['verdict']})")
    print(f"🛠️ Saha Çalışanları     : {res['council_scores']['workforce']['score']}/100 ({res['council_scores']['workforce']['verdict']})")
    print(f"\n🎯 Ağırlıklı Konsensüs  : {res['consensus_score']}/100")
    print(f"⚖️ Nihai Karar          : {res['final_resolution']}")
    print(f"📜 Karar Hükmü          : {res['mandate_action']}\n")

    print("📢 Azınlık Şerhleri (Dissenting Opinions):")
    for d in res["dissenting_opinions_log"]:
        print(f"   - {d}")

if __name__ == "__main__":
    main()
