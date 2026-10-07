# AkıllıCV

NLP tabanlı CV analizi ve çok modlu aday değerlendirme sistemi — bitirme projesi.

## Proje ne yapıyor?

AkıllıCV, bir CV'yi iş ilanıyla otomatik karşılaştırıp uyum skoru çıkarıyor ve mülakat sırasında
konuşma ile yüz ifadesini analiz ederek adayı daha bütünlüklü şekilde değerlendiriyor. Amaç,
tek bir metin eşleştirmesinden ibaret kalmayıp CV, ses ve görüntü verisini tek bir sistemde
birleştiren, kararlarını açıklayabilen ve adil çalışıp çalışmadığı test edilmiş bir değerlendirme
aracı ortaya koymak.

## İçerdiği modüller

### 1. CV analizi
CV'den beceri, eğitim ve deneyim bilgisi Türkçe NER ile çıkarılır; ilan metniyle TF-IDF ve
BERTurk gömme vektörleri üzerinden karşılaştırılır. İlanda olup CV'de olmayan beceriler
adaya öneri olarak sunulur.

- `pdfplumber` / `python-docx` — CV dosyasından metin çıkarma
- BERTurk tabanlı Türkçe NER — varlık tanıma
- TF-IDF + BERTurk gömme, kosinüs benzerliği — eşleştirme skoru

### 2. Ses analizi
Mülakat kaydından konuşma metne çevrilir ve konuşma tarzı analiz edilir.

- Whisper — Türkçe konuşma → metin
- librosa — konuşma hızı, duraksama süresi, pitch analizi

### 3. Görüntü işleme
Yüz tespiti ve duygu sınıflandırması, hazır/pretrained modeller kullanılmadan **sıfırdan
eğitilen** iki ayrı CNN ile yapılıyor.

- Yüz tespiti: sliding window + kendi eğittiğimiz CNN (WIDER FACE veri setiyle)
- Duygu sınıflandırma: kendi eğittiğimiz CNN (FER-2013 veri setiyle)
- Grad-CAM — modelin kararını görselleştirme (hangi bölgeye bakarak karar verdiği)

### 4. Değerlendirme motoru
CV, ses ve görüntü modüllerinden gelen sonuçlar ağırlıklı bir skorda birleştirilir, JSON
formatında saklanır ve aday/işveren panellerine ayrı görünümler olarak sunulur.

### 5. Adalet ve KVKK testi
Aynı CV'nin kimlikli ve anonimleştirilmiş (isim/cinsiyet/yaş maskelenmiş) versiyonları
sisteme verilip skor farkı ölçülüyor — sistemin kimlik bilgilerinden etkilenip
etkilenmediğini test ediyoruz.

### 6. Değerlendirme deneyi
Sistemin ürettiği aday sıralaması, insanların elle yaptığı sıralamayla
(`scipy.stats.spearmanr`) karşılaştırılıyor.

## Kullanılan teknolojiler

| Alan | Araç/Yöntem |
|---|---|
| CV metin analizi | BERTurk, TF-IDF, Türkçe NER |
| Ses analizi | Whisper, librosa |
| Görüntü işleme | Kendi eğitilen CNN modelleri, Grad-CAM |
| Değerlendirme | pandas, scipy |

## Yol haritası

- [x] Sistem mimarisinin ve modüllerin planlanması
- [ ] CV metin analizi modülünün geliştirilmesi (NER + eşleştirme)
- [ ] Değerlendirme deneyi için veri toplama (anonim CV + insan sıralaması)
- [ ] Yüz tespiti modelinin WIDER FACE ile eğitilmesi
- [ ] Duygu sınıflandırma modelinin FER-2013 ile eğitilmesi
- [ ] Ses analizi modülünün entegrasyonu (Whisper + librosa)
- [ ] Grad-CAM ile açıklanabilirlik katmanının eklenmesi
- [ ] Adalet / KVKK testinin uygulanması
- [ ] Tüm modüllerin tek bir değerlendirme motorunda birleştirilmesi
- [ ] Aday ve işveren panellerinin geliştirilmesi

## Proje bilgisi

- **Öğrenci:** Ayşe Ak
- **Üniversite:** Kayseri Üniversitesi, Yazılım Mühendisliği
- **Danışman:** Ayhan Renklier
