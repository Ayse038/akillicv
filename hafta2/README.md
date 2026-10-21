# AkıllıCV — Hafta 2

Bu hafta CV analizi modülünün ikinci adımını yaptım: bir CV'yi bir iş ilanıyla karşılaştırıp
aralarındaki uyumu yüzde olarak hesaplamak.

## Bu hafta neler yaptım?

1. **İş ilanı metnini hazırladım.** Örnek bir staj ilanını `ilan.txt` dosyasına yazıp koda okuttum.
2. **CV ve ilanı sayılara çevirdim.** Bilgisayar yazıyı doğrudan karşılaştıramadığı için
   iki metni TF-IDF yöntemiyle sayısal vektörlere çevirdim.
3. **Uyum skorunu hesapladım.** İki vektör arasındaki benzerliği kosinüs benzerliği ile
   ölçüp yüzde olarak yazdırdım.
4. **Ortak kelimeleri listeledim.** CV ve ilanda birlikte geçen en önemli kelimeleri
   göstererek skorun neden öyle çıktığını görünür hale getirdim.

## Dosyalar

| Dosya | Ne yapıyor? |
|---|---|
| `eslestirme_tfidf.py` | CV ile ilanı TF-IDF ile karşılaştırıp uyum skorunu ve ortak kelimeleri yazdırıyor |
| `ilan.txt` | Denemek için kullandığım örnek iş ilanı |

`ornek_cv.pdf` ve `requirements.txt` ana klasörde duruyor.

## Kullandığım araçlar

- **scikit-learn** — TF-IDF ve kosinüs benzerliği hesaplamak için
- **pdfplumber** — CV'den metin çıkarmak için (Hafta 1'den)

## Nasıl çalıştırılır?

1. Kütüphaneleri yükle:
```
   pip install -r requirements.txt
```
2. `eslestirme_tfidf.py`, `ilan.txt` ve `ornek_cv.pdf` aynı klasörde olacak şekilde çalıştır:
```
   python eslestirme_tfidf.py
```

## Sonuç

Örnek CV ile örnek ilan karşılaştırıldığında çıktı:

```
CV - ilan uyum skoru: %41.0

CV ve ilanda ortak geçen en önemli kelimeler:
  yazılım
  işleme
  mühendisliği
  git
  veri
  python
  geliştirme
  dil
```

Ortak kelimelerin ilanın istediği becerilerle (Python, Git, veri, yazılım) örtüşmesi,
skorun mantıklı çıktığını gösteriyor.

## Dikkat ettiğim noktalar

- Türkçede büyük `İ` ve `I` harfleri küçültülürken bozulduğu için metinleri karşılaştırmadan
  önce bu harfleri ayrıca düzelttim.
- Türkçe ekler yüzünden "Python'u" ve "Python'da" farklı kelime sayılmasın diye metni harf
  parçalarına bölerek (3-5 harflik) karşılaştırdım.

## Bu hafta öğrendiklerim

- TF-IDF'in bir kelimenin bir metindeki önemini sayıya çevirdiğini
- Kosinüs benzerliğinin iki metin arasındaki benzerliği 0 ile 1 arasında verdiğini
- Anlam taşımayan sık kelimeleri (ve, ile, bir) listeden çıkarmanın sonucu iyileştirdiğini
- Bir sonucun nedenini görmek için ortak kelimelere bakmanın işe yaradığını
