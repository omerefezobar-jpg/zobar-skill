---
name: frontier-innovator
description: >-
  Use this skill whenever conceptualizing, researching, benchmarking, or architecting a product, software system, or revolutionary feature from the ground up.
  Executes an uncompromising 6-phase master protocol: academic ground truth (top university syllabi, seminal textbooks, professor mental models), raw user sentiment & pain point extraction, competitor teardown & 10x moat creation, legal/regulatory risk mapping, optimal tech stack & UI component engineering, and radical boundary-pushing inventions backed by visual architecture diagrams.
---

# Frontier Innovator: Deep-Tech, Market & Radical Invention Engine

> **Aforizma:** *"Sıradanlık en büyük risktir. Bir sistem inşa edilecekse; bilimin en uç teorisiyle temellenmeli, sokaktaki kullanıcının en derin acısını çözmeli, hukuki olarak zırhlı olmalı ve daha önce kimsenin cüret etmediği radikal icatları bünyesinde barındırmalıdır."*

---

## 1. Temel Felsefe ve Çalışma İlkeleri

1. **Sıfır Vasatlık (Zero Mediocrity):** "Herkes böyle yapıyor" cevabı kesinlikle yasaktır. Standart şablonlar, modası geçmiş öneriler ve klişeler reddedilir.
2. **Bilgiyi Sömür, Hizmet Etme (Extract, Don't Serve):** Üniversitelere eğitim projesi yapılmaz; üniversitelerin (MIT, Stanford, Oxford, ETH Zürich vb.), dünyanın en seçkin profesörlerinin ve düşünürlerinin ürettiği saf bilgi süzülüp ürüne aktarılır.
3. **Filtresiz Kullanıcı Gerçeği (Unfiltered Truth):** Kullanıcıların cilalı anket cevaplarına değil; Reddit'te, mağaza şikayetlerinde, forumlarda haykırdıkları gerçek nefret ve hayal kırıklıklarına odaklanılır.
4. **Hukuki Zırh (Legal Shield):** Kanunları ihlal etmek veya gri alanda tökezlemek yok; sistem baştan telif, IP, KVKK/GDPR ve regülasyonlara göre kurşun geçirmez tasarlanır.
5. **İcat Zorunluluğu (Mandatory Invention):** Bu skill her çalıştığında, mevcut çözümlerin hiçbirinde bulunmayan, sınırları zorlayan **en az 2-3 özgün mekanizma / icat** üretmek ve sisteme entegre etmek zorundadır.
6. **Görsel Zorunluluk (Visual Imperative):** Her analiz en az bir adet kapsamlı **Mermaid mimari veya kullanıcı akış şeması** içermelidir.

---

## 2. Altı Fazlı İcra Protokolü (The 6-Phase Protocol)

Bu yetenek tetiklendiğinde analizi aşağıdaki 6 fazı sırasıyla ve eksiksiz işleterek sunar:

```mermaid
flowchart TD
    A["FAZ 1: Akademik & Teorik Zemin<br/>(Üniversiteler, Seminal Kitaplar, Profesörler)"] --> B["FAZ 2: Filtresiz Kullanıcı Duygusu<br/>(Acılar, Şikayetler, Gizli Talepler)"]
    B --> C["FAZ 3: Rakip Teardown & 10x Moat<br/>(Rakiplerin Acziyeti, Bizim Üstünlüğümüz)"]
    C --> D["FAZ 4: Hukuki Sınırlar & Regülasyon<br/>(Telif, Lisans, KVKK/GDPR, IP)"]
    D --> E["FAZ 5: Teknik Yığın & Bileşen Mimarisi<br/>(Diller, Kütüphaneler, UI Component'leri)"]
    E --> F["FAZ 6: Radikal İcat & Sınırları Zorlama<br/>(Yeni Mekanikler, Patentlik Fikirler, Görsel Şema)"]
```

---

### FAZ 1: Akademik & Teorik Zemin (Academic Ground Truth)
* **Kaynak Havuzu & Yardımcı Araç:**
  - Canlı makale taraması için `./scripts/fetch_academic_papers.py` betiğini çalıştır:
    ```bash
    python ./scripts/fetch_academic_papers.py "<konu>" --max 5
    ```
  - Dünyanın önde gelen üniversite kürsüleri (bilgisayar bilimleri, insan-bilgisayar etkileşimi - HCI, davranışsal ekonomi, sistem mühendisliği), çığır açan ders kitapları ve vizyoner akademisyenler/düşünürler (örn. Donald Knuth, Yann LeCun, Andrew Ng, Clayton Christensen, Daniel Kahneman).
* **Görev:**
  - Bu alanın matematiksel, algoritmik ve bilimsel temelleri nelerdir?
  - En güncel ArXiv makaleleri ve üniversite müfredatları bu problem hakkında ne diyor?
  - Bilimin belirlediği teorik sınırlar ve fırsatlar nelerdir?

### FAZ 2: Filtresiz Kullanıcı Duygusu & Gizli Talepler (User Sentiment)
* **Kaynak Havuzu & Yardımcı Araç:**
  - Canlı kullanıcı eleştirisi madenciliği için `./scripts/mine_user_sentiment.py` betiğini çalıştır:
    ```bash
    python ./scripts/mine_user_sentiment.py "<ürün/konu>" --max 5
    ```
  - Forum tartışmaları, Reddit (`r/technology`, niş alt forumlar), App Store / Play Store 1-2 yıldızlı yorumları, Trustpilot şikayetleri, GitHub issue tartışmaları.
* **Görev:**
  - İnsanlar bu konudaki mevcut araçlarda neye öfkeleniyor?
  - En çok hangi hatalar, yavaşlıklar veya karmaşık adımlar insanları bezdiriyor?
  - Kullanıcıların açıkça dile getiremediği ama davranışlarından anlaşılan "gizli arzuları" neler?

### FAZ 3: Rakip Teardown & 10x Rekabet Üstünlüğü (Competitor Moat)
* **Görev:**
  - Mevcut pazar liderleri ve güçlü oyuncular tek tek masaya yatırılır.
  - Güçlü yönleri ve özellikle **yapısal kör noktaları (hantallıkları, legacy kodları, ticari kısıtları)** tespit edilir.
  - *"Biz hangi alanda (hız, sadelik, zeka, ergonomi, maliyet) rakiplerden 10 kat daha iyi olacağız?"* sorusunun cevabı ("Unfair Advantage") tanımlanır.

### FAZ 4: Hukuki Çerçeve & Regülasyon Kalkanı (Legal Fortress)
* **Kaynak Havuzu & Yardımcı Araç:**
  - Canlı patent ve önceki teknik (prior art) taraması için `./scripts/search_prior_art.py` betiğini çalıştır:
    ```bash
    python ./scripts/search_prior_art.py "<teknoloji/icat konusu>" --max 5
    ```
* **Görev:**
  - Fikri Mülkiyet (IP), patent ihlali riskleri ve açık kaynak lisans uyumlulukları (MIT, Apache 2.0, GPL sınırları).
  - Veri koruma yasaları (KVKK, GDPR, CCPA) ve yapay zeka regülasyonları (EU AI Act vb.).
  - Sistemin yasal olarak sıfır riskle ölçeklenmesini sağlayacak mimari önlemler belirlenir.

### FAZ 5: Teknik Yığın & UI/UX Bileşen Mimarisi (Tech & Design Blueprint)
* **Kodlama Dilleri & Altyapı:**
  - Sadece trend olduğu için değil; hız, bellek verimliliği, concurrency ve sürdürülebilirlik kriterlerine göre dil ve framework seçimi (Rust, Go, TypeScript, Python vb.).
  - Veri mimarisi, cache katmanları, API protokolleri (gRPC, WebSocket, tRPC).
* **Tasarım & UI/UX Bileşenleri:**
  - Kullanılacak en modern bileşen kütüphaneleri (shadcn/ui, Radix, Tailwind, Canvas/WebGL mikro-etkileşimleri).
  - Kullanıcı ergonomisi: Bilişsel yükü sıfıra indiren arayüz felsefesi.

### FAZ 6: Radikal İcat & Sınırları Zorlama (Breakthrough Invention Lab)
* **Kılavuz:** İcat üretirken [triz-invention-engine.md](./references/triz-invention-engine.md) prensiplerini (özellikle Tersine Çevirme, Önceden Eylem ve Kendi Kendine İyileşme) temel al.
* **Görev:**
  - Sektörde daha önce hiç kimsenin birleştirmediği iki veya daha fazla disiplini birleştiren **2-3 adet radikal yenilik/icat** kurgula.
  - Bu icatların yazılıma nasıl entegre edileceğini, hangi algoritma ve arayüz mekaniğiyle çalışacağını teknik detaylarıyla açıkla.
  - **Görselleştirme:** Sistemin veya icadın çalışma dinamiğini gösteren detaylı bir **Mermaid mimari/akış diyagramı** üret.

---

## 3. Standart Çıktı Rapor Formatı

Her analiz yapıldığında aşağıdaki şablon takip edilmelidir:

```markdown
# [PROJE/KONU ADI] — Uç Nokta İnovasyon & Mimari Raporu

## 📌 Yönetici Özeti & Çekirdek Tez
(Problemin özü, çözümsüzlük paradoksu ve bizim radikal çözümümüz.)

---

## 🏛️ 1. Akademik & Teorik Zemin
- **Teorik Temel:** ...
- **Üniversite & Literatür Görüşü:** ...
- **Büyük Düşünürlerin / Profesörlerin Perspektifi:** ...

---

## 💬 2. Filtresiz Kullanıcı Duygusu & Pazarın Çığlığı
- **En Büyük Şikayetler & Nefret Sebepleri:** ...
- **Karşılanmamış Gizli Talepler:** ...
- **Psikolojik Sürtünme Noktaları:** ...

---

## ⚔️ 3. Rakip Teardown & 10x Moat
| Rakip | Zayıf Karın (Kör Nokta) | Bizim 10x Karşı Hamlemiz |
| :--- | :--- | :--- |
| Rakip A | ... | ... |
| Rakip B | ... | ... |

---

## ⚖️ 4. Hukuki Zırh & Regülasyon
- **Fikri Mülkiyet & Patent Koruma:** ...
- **KVKK / GDPR / Veri Egemenliği:** ...
- **Etik & Regülasyon Kontrol Listesi:** ...

---

## 🛠️ 5. Teknik Mimari & UI/UX Bileşenleri
- **Dil ve Teknoloji Yığını:** (Seçim gerekçeleriyle)
- **UI/UX Bileşenleri & Etkileşimler:** (Component bazında döküm)

---

## 🚀 6. Radikal İcatlar & Sınırları Zorlayan Mekanikler
- **İcat #1:** [İsim] — [Çalışma Prensibi] — [Sisteme Entegrasyonu]
- **İcat #2:** [İsim] — [Çalışma Prensibi] — [Sisteme Entegrasyonu]
- **İcat #3:** [İsim] — [Çalışma Prensibi] — [Sisteme Entegrasyonu]

### Sistem & İnovasyon Mimarisi (Mermaid)
```mermaid
...
\```
```
