#!/usr/bin/env python3
"""
Zobar Skill — End-to-End 6-Phase Autonomous Deep-Tech Research & Invention Engine
Executes complete automated discovery across all six phases:
1. Academic Ground Truth (University Syllabi, Textbooks, Labs + OpenAlex & arXiv)
2. Community Friction Mining (Hacker News + Reddit with Clause-Level Negation Handling)
3. Hybrid Competitor Benchmark (Commercial Incumbents + Live GitHub & Package Telemetry)
4. Statutory Legal, Prior Art & Regulatory Screener (Codified EU AI Act, MDR Rule 11, GDPR)
5. Automated Technical & UI/UX Component Architecture (Synthesized Rust/Go/Tauri stack)
6. TRIZ Systematic Inventions & Feasibility Validation Gate (Dynamic TRL, ICE, WTP, Failure Modes, Mermaid)
"""

import sys
import argparse
import datetime

from scripts.fetch_academic_papers import fetch_arxiv_papers
from scripts.fetch_university_research import fetch_comprehensive_academic_ground_truth
from scripts.mine_user_sentiment import search_sentiment
from scripts.benchmark_competitors import benchmark_competitors
from scripts.search_prior_art import search_patents
from scripts.scan_regulations import evaluate_compliance
from scripts.synthesize_architecture import synthesize_tech_stack
from scripts.validate_inventions import generate_validated_inventions
from scripts.export_html_report import export_to_html

# Ensure UTF-8 output across all systems
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BANNER = r"""
========================================================================
   ⚡ ZOBAR SKILL — FULL 6-PHASE AUTONOMOUS DEEP-TECH ENGINE ⚡
========================================================================
"""

def generate_dossier(topic: str, output_path: str = None, html_path: str = None):
    print(BANNER)
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"[*] Hedef Konu / Problem: {topic}")
    print(f"[*] Başlangıç Zamanı     : {now_utc}")
    print("[*] 6 Fazlı tam otonom Zobar Skill araştırma akışı başlatılıyor...\n")

    # 1. Akademik Zemin: Üniversite Müfredatları, Hakemli Yayınlar ve arXiv
    print("[1/6] 🏛️ FAZ 1: Üniversite müfredatları (MIT/Stanford), hakemli yayınlar ve arXiv taranıyor...")
    uni_data = fetch_comprehensive_academic_ground_truth(topic, max_papers=2)
    arxiv_papers = fetch_arxiv_papers(topic, max_results=2)
    peer_papers = uni_data.get("peer_reviewed_papers", [])
    curriculum = uni_data.get("curriculum", [])
    labs = uni_data.get("research_labs", [])
    print(f"      -> {len(curriculum)} ders müfredatı | {len(labs)} araştırma laboratuvarı | {len(peer_papers)} hakemli makale | {len(arxiv_papers)} ön baskı tespit edildi.")

    # 2. Topluluk Kullanıcı Acıları & Sürtünme Madenciliği (HN + Reddit)
    print("[2/6] 💬 FAZ 2: Hacker News ve Reddit topluluklarından tümce seviyesinde şikayet madenciliği yapılıyor...")
    sentiment_data = search_sentiment(topic, max_comments=4)
    comments = sentiment_data.get("comments", [])
    sources_summary = sentiment_data.get("summary", "")
    if comments:
        print(f"      -> {len(comments)} adet filtrelenmiş kullanıcı deneyimi analiz edildi. ({sources_summary})")
    else:
        print("      [-] Topluluk kanallarından filtrelenmiş şikayet kaydı bulunamadı.")

    # 3. Hibrit Rakip ve Pazar Benchmark'ı (Ticari + GitHub + Paket Telemetrisi)
    print("[3/6] ⚔️ FAZ 3: Ticari pazar liderleri, GitHub açık kaynak ve paket telemetrisi taranıyor...")
    comp_res = benchmark_competitors(topic, max_results=3)
    commercial_incumbents = comp_res.get("commercial_incumbents", [])
    os_projects = comp_res.get("open_source_telemetry", [])
    packages = comp_res.get("package_registry_telemetry", [])
    print(f"      -> {len(commercial_incumbents)} ticari lider | {len(os_projects)} GitHub projesi | {len(packages)} paket haritalandı.")

    # 4. Hukuki Zırh, Regülasyon ve Ön Patent Taraması
    print("[4/6] ⚖️ FAZ 4: Google Patents, EU AI Act maddeleri ve KVKK/GDPR taranıyor...")
    patents = search_patents(topic, max_results=3)
    compliance = evaluate_compliance(topic)
    print(f"      -> {len(patents)} adet prior art kaydı | EU AI Act: {compliance['eu_ai_act']['tier']}")

    # 5. Otomatik Teknik & UI Bileşen Mimarisi
    print("[5/6] 🛠️ FAZ 5: Sistem mimarisi, çekirdek dil ve UI bileşen yığını sentezleniyor...")
    arch = synthesize_tech_stack(topic)
    print(f"      -> Seçilen Çekirdek: {arch['core_language']} | Arayüz: {arch['ui_architecture']['runtime']}")

    # 6. TRIZ Sistematik İcat Motoru ve Dinamik Doğrulama Kapısı
    print("[6/6] 🚀 FAZ 6: TRIZ çelişki prensipleriyle dinamik TRL/ICE doğrulamalı icatlar üretiliyor...")
    inv_data = generate_validated_inventions(topic)
    print(f"      -> {len(inv_data['inventions'])} adet dinamik TRL ve WTP doğrulamalı icat ve sistem mimarisi Mermaid şeması üretildi.\n")

    # Tam Raporu İnşa Et
    dossier_lines = [
        f"# ZOBAR SKILL RAPORU: {topic.upper()}",
        f"**Rapor Tarihi (UTC):** {now_utc} | **Motor:** Zobar Skill v4.0-Autonomous Engine\n",
        "---",
        "## 🏛️ FAZ 1: Akademik Zemin, Üniversite Müfredatları & Hakemli Literatür",
        "> ⚠️ **Akademik Kanıt Notu:** Bu bölüm seçkin dünya üniversitelerinin (MIT, Stanford, ETH Zürich, Oxford) lisansüstü ders izlencelerini, temel ders kitaplarını, araştırma laboratuvarlarını ve OpenAlex/arXiv üzerinden hakemli ve ön baskı literatürü içermektedir.\n",
    ]

    if curriculum:
        dossier_lines.append("### 📚 Seçkin Üniversite Müfredatları ve Zihinsel Modeller:")
        for c in curriculum:
            dossier_lines.append(f"#### {c['institution']} [{c['course_code']}]: {c['course_title']}")
            dossier_lines.append(f"- **Öğretim Üyeleri:** {', '.join(c['professors'])}")
            dossier_lines.append(f"- **Temel Başvuru Kitabı:** {c['seminal_textbook']}")
            dossier_lines.append(f"- **Resmî Ders İzlencesi:** {c['syllabus_url']}")
            dossier_lines.append("- **Öğretilen Temel İlkeler:**")
            for m in c["core_mental_models"]:
                dossier_lines.append(f"  - {m}")
            dossier_lines.append("")

    if labs:
        dossier_lines.append("### 🔬 Öncü Araştırma Laboratuvarları:")
        for lab in labs:
            dossier_lines.append(f"- **{lab['name']}** ([Laboratuvar Sitesi]({lab['url']})) — *Odak:* {lab['focus']}")
        dossier_lines.append("")

    if peer_papers:
        dossier_lines.append("### 📄 Doğrulanmış Hakemli Yayınlar (OpenAlex):")
        for i, p in enumerate(peer_papers, 1):
            dossier_lines.append(f"#### {i}. {p['title']} ({p['year']} — {p['venue']})")
            dossier_lines.append(f"- **Yazarlar:** {p['authors']}")
            dossier_lines.append(f"- **Atıf Metriği:** {p['evidence_grade']}")
            dossier_lines.append(f"- **Yayın Bağlantısı:** {p['url']}")
            dossier_lines.append(f"- **Teorik Katkı:** {p['summary']}\n")

    if arxiv_papers:
        dossier_lines.append("### 📑 Güncel Akademik Ön Baskılar (arXiv):")
        for i, p in enumerate(arxiv_papers, 1):
            dossier_lines.append(f"#### {i}. {p['title']}")
            dossier_lines.append(f"- **Yazarlar:** {p['authors']} | **Tarih:** {p['published']}")
            dossier_lines.append(f"- **Bağlantı:** {p['url']}")
            dossier_lines.append(f"- **Özet:** {p['summary']}\n")

    dossier_lines.append("---")
    dossier_lines.append("## 💬 FAZ 2: Sahadaki Kullanıcı Sürtünmeleri & Şikayet Madenciliği")
    dossier_lines.append(f"> 📌 **Veri Kapsamı:** {sources_summary if sources_summary else 'Hacker News ve Reddit'}. Tümce seviyesinde sözdizim ayrıştırması ve olumsuzlama (negation) izolasyonu uygulanmıştır.\n")

    if comments:
        for i, c in enumerate(comments, 1):
            friction_level = "🔴 Yüksek Acı (Ağır Şikayet)" if c.get("friction_score", 0) >= 3 else ("🟡 Orta Sürtünme" if c.get("friction_score", 0) >= 1 else "⚪ Nötr / Düşük")
            dossier_lines.append(f"### Şikayet #{i} [{c.get('source', 'Topluluk')}] — {friction_level} (@{c['author']} — {c['date']})")
            dossier_lines.append(f"- **Konu / Başlık:** {c['title']}")
            dossier_lines.append(f"- **Doğrudan URL:** {c['url']}")
            dossier_lines.append(f"- **Hesaplanan Sürtünme Skoru:** {c.get('friction_score', 0)}")
            if c.get("pain_points"):
                dossier_lines.append("- **🎯 Tespit Edilen Odak Acı Cümleleri:**")
                for pp in c["pain_points"]:
                    dossier_lines.append(f"  - > \"{pp}\"")
            dossier_lines.append(f"- **Filtresiz Kullanıcı Görüşü:** > {c['text']}\n")
    else:
        dossier_lines.append("[-] Belirtilen arama kriterlerine uyan şikayet verisi bulunamadı.\n")

    dossier_lines.append("---")
    dossier_lines.append("## ⚔️ FAZ 3: Hibrit Rakip Teardown & Pazar Benchmark'ı")
    dossier_lines.append("> 📊 **Pazar Kapsamı:** Doğrulanmış ticari fiyatlandırma verileri, canlı GitHub telemetrisi ve yayınlanmış paket kayıtları birleştirilmiştir.\n")

    if commercial_incumbents:
        dossier_lines.append("### 🏢 Ticari ve Pazar Lideri Rakipler:")
        for i, ci in enumerate(commercial_incumbents, 1):
            dossier_lines.append(f"#### {i}. {ci['name']} ({ci['type']})")
            dossier_lines.append(f"- **Fiyatlandırma Modeli:** {ci['pricing_tier']} *[{ci.get('pricing_verified', 'Doğrulanmış')}]*")
            dossier_lines.append(f"- **Dağıtım Modeli:** {ci['deployment']}")
            dossier_lines.append(f"- **Yapısal Kör Nokta / Zaaf:** {ci['core_weakness']}")
            dossier_lines.append(f"- **İnceleme URL:** {ci['url']}\n")

    if os_projects:
        dossier_lines.append("### 🌐 Açık Kaynak Ekosistem Telemetrisi (GitHub):")
        for i, cp in enumerate(os_projects, 1):
            dossier_lines.append(f"- **{cp['name']}** (⭐️ {cp['stars']:,} | 🍴 {cp['forks']:,} | ⚠️ {cp['open_issues']} Issue)")
            dossier_lines.append(f"  *Teknoloji / Lisans:* {cp['language']} | {cp['license']} | *Son Commit:* {cp['last_active']}")
            dossier_lines.append(f"  *Repo URL:* {cp['url']}")
        dossier_lines.append("")

    if packages:
        dossier_lines.append("### 📦 Yayınlanmış Paket Telemetrisi (npm/PyPI):")
        for i, pkg in enumerate(packages, 1):
            dossier_lines.append(f"- **{pkg['name']}** v{pkg['version']} (Lisans: `{pkg['license']}` | Yayıncı: `@{pkg['publisher']}`)")
            dossier_lines.append(f"  *Özet:* {pkg['description']}")
            dossier_lines.append(f"  *Paket URL:* {pkg['url']}")
        dossier_lines.append("")

    dossier_lines.append("---")
    dossier_lines.append("## ⚖️ FAZ 4: Hukuki Zırh, Madde Bazlı Mevzuat & Ön Patent Taraması")
    dossier_lines.append(f"> ⚠️ **Yasal Sorumluluk Reddi:** {compliance['statutory_disclaimer']}\n")

    dossier_lines.append(f"### 🇪🇺 EU AI Act Seviyesi: {compliance['eu_ai_act']['tier']}")
    dossier_lines.append(f"- **Mevzuat Maddesi:** {compliance['eu_ai_act']['statutory_basis']}")
    dossier_lines.append(f"- **Resmî Yasal Emsal:** {compliance['eu_ai_act']['official_precedent']}")
    dossier_lines.append(f"- **Güven Derecesi:** {compliance['eu_ai_act']['confidence']}")
    dossier_lines.append(f"- **Hukuki Mütalaa Zorunluluğu:** {'Evet (Kritik)' if compliance['eu_ai_act']['requires_expert_counsel'] else 'Hayır'}")
    dossier_lines.append("- **Zorunlu Hukuki Yükümlülükler:**")
    for ob in compliance['eu_ai_act']['obligations']:
        dossier_lines.append(f"  - {ob}")
    dossier_lines.append("")

    dossier_lines.append("### 🔒 Veri Gizliliği & Egemenliği (KVKK / GDPR):")
    for priv in compliance["data_privacy"]:
        dossier_lines.append(f"- {priv}")
    dossier_lines.append("")

    if patents:
        dossier_lines.append("### 📜 Öncelikli Teknik (Prior Art) Kayıtları:")
        for i, pt in enumerate(patents, 1):
            dossier_lines.append(f"- **Kayıt #{i}:** [{pt['id']}] {pt['title']} — *Hak Sahibi:* {pt['assignee']} ({pt['filing_date']})")
            dossier_lines.append(f"  *Bağlantı:* {pt['url']}")
            if pt.get('snippet'):
                dossier_lines.append(f"  *Özet:* {pt['snippet']}")
        dossier_lines.append("")

    dossier_lines.append("---")
    dossier_lines.append("## 🛠️ FAZ 5: Sistem Mimarisi & UI/UX Bileşen Spesifikasyonu")
    dossier_lines.append(f"- **Çekirdek Dil:** `{arch['core_language']}` — *Seçim Gerekçesi:* {arch['language_justification']}")
    dossier_lines.append(f"- **Temel Kütüphaneler:** `{', '.join(arch['recommended_libraries'])}`")
    dossier_lines.append(f"- **Veri ve Durum Katmanı:** {arch['data_layer']} — *Gerekçe:* {arch['data_justification']}")
    dossier_lines.append(f"- **Arayüz Çalışma Zamanı:** {arch['ui_architecture']['runtime']}")
    dossier_lines.append(f"- **Tasarım Sistemi:** {arch['ui_architecture']['design_system']}")
    dossier_lines.append(f"- **Bilişsel Ergonomi Kuralı:** {arch['ui_architecture']['ergonomic_rule']}\n")

    if arch.get("s_tier_benchmarks"):
        dossier_lines.append("### 💎 Eşleşen S-Tier Tasarım & Bileşen Referansları (100+ Design Vault):")
        for s in arch["s_tier_benchmarks"]:
            dossier_lines.append(f"#### [{s['name']}]({s['url']}) — *{s['category']}*")
            dossier_lines.append(f"- **Tasarım Paradigması:** {s['design_paradigm']}")
            dossier_lines.append(f"- **Hero / Başlık Deseni:** {s['hero_pattern']}")
            dossier_lines.append(f"- **Bileşen Mimarisi:** {s['component_features']}")
            dossier_lines.append(f"- **Mikro-Etkileşimler:** {s['key_interactions']}")
            dossier_lines.append(f"- **Renk & Stil Tokenları:** Arka Plan: `{s['color_tokens']['background']}` | Vurgu: `{s['color_tokens']['accent']}`")
            dossier_lines.append(f"- **Önerilen UI Kütüphaneleri:** `{', '.join(s['recommended_libraries'])}`\n")

    dossier_lines.append("---")
    dossier_lines.append("## 🚀 FAZ 6: TRIZ Radikal İcatları & Dinamik Doğrulama Kapısı")
    dossier_lines.append("> 📌 **Kanıt Ayrımı:** Dokümandaki TRL ve WTP değerleri alan kısıtlarına ve mevzuat zorluklarına göre dinamik olarak hesaplanmış olup deneysel geçerleme kapıları belirtilmiştir.\n")

    for inv in inv_data["inventions"]:
        dossier_lines.append(f"### İcat #{inv['id']}: {inv['title']}")
        dossier_lines.append(f"- **TRIZ Metodolojisi:** {inv['triz_principle']}")
        dossier_lines.append(f"- **Çalışma Prensibi:** {inv['mechanism']}")
        dossier_lines.append(f"- **TRL Seviyesi:** {inv['trl_level']} {inv['trl_evidence_type']}")
        dossier_lines.append(f"- **TRL İlerleme Kapısı:** {inv.get('advancement_gate', 'Deneysel prototip doğrulaması')}")
        dossier_lines.append(f"- **ICE Skoru:** Toplam: {inv['ice_score']['total']} (Etki: {inv['ice_score']['impact']}/10 | Güven: {inv['ice_score']['confidence']}/10 | Kolaylık: {inv['ice_score']['ease']}/10)")
        dossier_lines.append(f"- **Ticari Talep & WTP:** {inv['commercial_wtp']['hypothesis']} {inv['commercial_wtp']['evidence_type']}")
        dossier_lines.append(f"- **Harekete Geçmeme Maliyeti:** {inv['commercial_wtp']['alternative_cost']}")
        dossier_lines.append("- **Kritik Hata Modları & Çözümleri:**")
        for fm in inv["failure_modes"]:
            dossier_lines.append(f"  - {fm}")
        dossier_lines.append("")

    dossier_lines.append("### Üretilen Sistem Mimarisi Şeması")
    dossier_lines.append("```mermaid")
    dossier_lines.append(inv_data["system_architecture_mermaid"])
    dossier_lines.append("```\n")

    full_dossier = "\n".join(dossier_lines)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_dossier)
        print(f"[+] 6 Fazlı Tam Araştırma Dosyası (Markdown) kaydedildi: {output_path}")

    if html_path:
        rendered_html = export_to_html(full_dossier, title=f"Zobar Skill: {topic}")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(rendered_html)
        print(f"[+] Güvenlik zırhlı görsel Dashboard (HTML/Mermaid) kaydedildi: {html_path}")

    if not output_path and not html_path:
        print(full_dossier)

def main():
    parser = argparse.ArgumentParser(description="Zobar Skill Full-Spectrum 6-Phase Autonomous Engine")
    parser.add_argument("topic", nargs="?", help="Araştırılacak ve inovasyon yapılacak konu")
    parser.add_argument("--output", "-o", help="Çıktının kaydedileceği Markdown dosya yolu (örn: dossier.md)")
    parser.add_argument("--html", help="Görsel HTML Dashboard olarak kaydedilecek yol (örn: report.html)")
    args = parser.parse_args()

    topic = args.topic
    if not topic:
        topic = input("Lütfen araştırılacak veya inovasyon yapılacak konuyu girin: ").strip()
        if not topic:
            print("[-] Konu belirtilmedi. Çıkılıyor.")
            sys.exit(1)

    generate_dossier(topic, args.output, args.html)

if __name__ == "__main__":
    main()
