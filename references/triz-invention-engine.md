# TRIZ & Sistematik İcat Motoru (Yazılım ve Yapay Zeka İçin)

> **Genrich Altshuller:** *"Buluş ve icat bir ilham tesadüfü değildir; çözülemez gibi görünen çelişkilerin belirli prensiplerle sistematik olarak ortadan kaldırılması bilimidir."*

`frontier-innovator` skill'inin **Faz 6 (Radikal İcat)** aşamasında başvurduğu temel icat metodolojisi TRIZ'dir (Theory of Inventive Problem Solving).

---

## 1. Yazılımdaki Temel Çelişkiler (Technical Contradictions)

Yazılım dünyasındaki neredeyse tüm sınır krizleri şu 4 temel çelişkiden kaynaklanır:

1. **Hız vs. Doğruluk:** Sistemi daha hızlı yaparsan (örn. async, probabilistic), veri tutarlılığını veya doğruluğu kaybedersin.
2. **Özellik Zenginliği vs. Sadeliği (Bilişsel Yük):** Sisteme ne kadar çok yetenek eklersen, arayüz o kadar karmaşıklaşır ve kullanıcı boğulur.
3. **Güvenlik / Gizlilik vs. Kolaylık (Ergonomi):** Güvenliği artırdıkça (2FA, şifreleme, sandbox), geliştirici deneyimi ve kullanıcı akışı felç olur.
4. **Ölçeklenebilirlik vs. Maliyet:** Milyonlarca kullanıcıyı desteklemek için sunucu ve model maliyetleri katlanarak artar.

---

## 2. Yazılım ve Sistemler İçin Uyarlanmış 10 Kritik TRIZ Prensibi

Ajan, Faz 6'da yeni bir icat üretirken aşağıdaki prensiplerden en az ikisini melezleyerek çözüme ulaşır:

### Prensip #1: Segmentasyon (Micro-Isolation & Modularity)
* **Mantık:** Bir bütünü bağımsız parçalara böl veya parçalanabilirliğini artır.
* **Yazılım İcadı:** Monolitik LLM çağrılarını mikro-ajanlara bölmek; her fonksiyonu izole bir WASM sandbox'ında çalıştırmak.

### Prensip #2: Çıkarma / Ayırma (Taking Out / Decoupling)
* **Mantık:** Sistemin zararlı veya gereksiz görünen parçasını sistemden söküp ayır.
* **Yazılım İcadı:** Ağır analizleri kullanıcı makinesinde değil, uç noktada (edge) veya arka planda sessizce yürütmek; UI thread'inden iş mantığını tamamen izole etmek.

### Prensip #10: Önceden Eylem (Prior Action / Speculative Execution)
* **Mantık:** Bir eylemi ihtiyaç duyulmadan önce kısmen veya tamamen gerçekleştir.
* **Yazılım İcadı:** Kullanıcı tıklamadan önce olası sonraki 3 aksiyonu arka planda önceden simüle eden ve sonuçları hazır tutan spekülatif arayüz mimarisi.

### Prensip #13: Tersi Yapmak (The Other Way Round / Inversion)
* **Mantık:** Sorunu çözmek için uygulanan geleneksel yönün tam tersini uygula.
* **Yazılım İcadı:** Kullanıcının yapay zekaya komut vermesi yerine; yapay zekanın kod tabanını dinleyip geliştiriciye sadece "onayla/reddet" şeklinde eylem sunması (Passive listening to Proactive synthesizing).

### Prensip #15: Dinamiklik / Esneklik (Dynamism / Adaptive Systems)
* **Mantık:** Sistemin özelliklerini çalışma anında dış çevre koşullarına göre otomatik ayarla.
* **Yazılım İcadı:** Cihazın şarjına, ağ gecikmesine ve kullanıcının bilişsel hızına göre kendini optimize eden (Full LLM -> Quantized SLM -> Cache Lookup) dinamik model geçişi.

### Prensip #25: Kendi Kendine Hizmet (Self-Service & Autonomic Healing)
* **Mantık:** Bir sistemin kendi fonksiyonlarını ve bakımını kendi başına halletmesini sağla.
* **Yazılım İcadı:** Hata yakalandığında geliştiriciye hata logu atmak yerine, hatayı çözen PR'ı oluşturup test edip onay için bekleten otonom sistem.

### Prensip #28: Mekaniği Değiştirme (Mechanics Substitution)
* **Mantık:** Fiziksel veya klasik bir mekanizmayı sensör, optik veya dalga tabanlı bir alanla değiştir.
* **Yazılım İcadı:** Regex veya statik kural bazlı filtrelemeyi kaldırıp yerine Vektör Alanı (Vector Embeddings) ve Soyut Sözdizim Ağacı (AST) analizi koymak.

---

## 3. İcat Değerlendirme Formülü (Ideality Equation)

Bir icat ancak **İdeallik Katsayısı** arttığında değerlidir:

$$
\text{İdeallik (I)} = \frac{\sum \text{Faydalar (Benefits)}}{\sum \text{Maliyetler (Costs)} + \sum \text{Zararlar / Sürtünmeler (Harms)}}
$$

* **Kural:** Yeni icat hiçbir zaman kullanıcıya ek konfigürasyon, yeni bir şifre veya ek bir bekleme süresi getirmemelidir. İdeal bir sistem; varlığı hissedilmeyen ama işi eksiksiz bitiren sistemdir.
