# Heuristic Frameworks & Mental Models for Frontier Innovator

Bu referans dokümanı, `frontier-innovator` skill'inin analizlerinde başvuracağı zihinsel modelleri, akademik sorgulama araçlarını ve pazar stratejilerini içerir.

---

## 1. Düşünce Modelleri (Mental Models)

### A. İlk İlkelerden Akıl Yürütme (First Principles Thinking — Feynman & Musk)
- Bir sorunu çözerken başkalarının çözümlerini taklit etmek (analojiyle düşünmek) yerine, sorunu fiziksel ve mantıksal en küçük yapıtaşlarına ayır.
- *Soru:* "Bu sistemin mutlak kesin olan gerçekleri nelerdir? Diğer her şey birer varsayım mıdır?"

### B. Jobs-to-be-Done (JTBD — Clayton Christensen)
- İnsanlar ürünleri satın almazlar; hayatlarında bir ilerleme kaydetmek için onları "işe alırlar".
- Kullanıcının yüzeysel isteği ile bilinçaltındaki gerçek "iş" (job) arasındaki farkı yakala.

### C. 10x Proprietary Advantage (Peter Thiel — Zero to One)
- Bir pazara girerken rakibe göre %10 veya %20 daha iyi olmak yetmez; geçiş maliyetini (switching cost) kırmak için en az bir dikeyde **10 kat daha hızlı, 10 kat daha ucuz veya 10 kat daha kolay** olmak zorundasınız.

---

## 2. Akademik Bilgi Süzme Matrisi (Academic Extraction Matrix)

Ajan literatürü tararken şu hiyerarşiyi takip eder:

1. **Temel Bilgisayar Bilimi & Matematik:**
   - Algoritmik karmaşıklık ($O(n)$, amortized cost).
   - Veri yapıları (LSM-trees, Vector Indexes, Directed Acyclic Graphs).
   - Dağıtık sistem teorileri (CAP teoremi, Paxos/Raft konsensüs, Eventual Consistency).

2. **İnsan-Bilgisayar Etkileşimi (HCI - Human-Computer Interaction):**
   - Fitts Yasası, Hick Yasası, Miller'ın 7±2 Kuralı.
   - Bilişsel yük teorisi (Cognitive Load Theory) — Arayüz kullanıcının dikkatini tüketmemeli.

3. **Davranışsal Ekonomi:**
   - Daniel Kahneman: Hızlı ve Yavaş Düşünme (Sistem 1 ve Sistem 2).
   - Kayıptan kaçınma (Loss Aversion) ve varsayılan seçenek etkisi (Default Effect).

---

## 3. Kullanıcı Duygusu & Yorum Madenciliği Formülü

Kullanıcı yorumlarını incelerken şu 4 duygu kümesini ayrıştır:

| Duygu Kümesi | İşaretler / Anahtar Kelimeler | İnovasyon Fırsatı |
| :--- | :--- | :--- |
| **Öfke & Çaresizlik** | "Sürekli çöküyor", "Destek cevap vermiyor", "Verilerimi kilitledi" | Sıfır kilitlenme (Zero-vendor-lockin), offline-first mimari |
| **Bilişsel Yorgunluk** | "Arayüz çok karışık", "Nerede ne var bulamıyorum", "Eğitimsiz kullanılmıyor" | Sıfır konfigürasyon (Zero-config), niyet odaklı UI |
| **Fiyat/Değer İsyanı** | "Her özelliğe ayrı para istiyorlar", "Küçük ekip için aşırı pahalı" | Şeffaf, kullanım bazlı veya açık çekirdek (open-core) model |
| **Gizli Arzu (Unspoken Desire)** | "Keşke şunu benim yerime tek tuşla halletseydi" | Otonom ajan entegrasyonu |

---

## 4. İcat Üretiminde Çapraz Döllenme (Cross-Pollination)

Radikal bir icat üretmek için genelde **farklı iki dünyanın kavramları** çarpıştırılır:
- *Örnek:* Oyun motoru mimarisini (ECS - Entity Component System) alıp bir veritabanı sorgulayıcısına entegre etmek.
- *Örnek:* Biyolojik bağışıklık sistemi modelini alıp bir yazılım güvenlik duvarına (firewall) dönüştürmek.
- *Örnek:* Müzik prodüksiyonundaki timeline/mixer mantığını alıp bir kod diff/refactor arayüzüne uyarlamak.
