

Bu hafta CV analizi modülünü tamamladım: ilan ile CV'yi anlam düzeyinde karşılaştırdım ve
CV'de eksik olan becerileri buldum.

## Bu hafta neler yaptım?

1. **BERTurk ile anlamsal eşleştirme yaptım.** İlanın her maddesi için CV'deki anlamca en
   yakın satırı buldum. Bunun için BERTurk tabanlı bir cümle modeli kullandım.
2. **Eksik beceri analizi yaptım.** İlanın istediği becerileri bulup CV'de olup olmadığına
   baktım, olmayanları eksik olarak listeledim.
3. **CV analizi modülünü tamamladım.** Metin çıkarma, NER, TF-IDF eşleştirme, BERTurk
   eşleştirme ve eksik beceri analizi artık çalışıyor.

## Dosyalar

| Dosya | Ne yapıyor? |
|---|---|
| `berturk_eslestirme.py` | İlan maddelerini CV satırlarıyla BERTurk gömme vektörleri üzerinden eşleştirip skor çıkarıyor |
| `beceri_analizi.py` | İlanın istediği becerileri bulup CV'de olmayanları listeliyor |

## Kullandığım araçlar

- **sentence-transformers** — cümleleri vektöre çevirmek için
- **emrecan/bert-base-turkish-cased-mean-nli-stsb-tr** — Hugging Face'ten aldığım, BERTurk tabanlı Türkçe cümle modeli

## Nasıl çalıştırılır?

1. Kütüphaneleri yükle:
   ```
   pip install -r requirements.txt
   ```
2. `ilan.txt` ve `ornek_cv.pdf` ile aynı klasörde çalıştır:
   ```
   python beceri_analizi.py
   python berturk_eslestirme.py
   ```
   `berturk_eslestirme.py` ilk çalıştırmada modeli indirdiği için biraz zaman alır.

## Sonuçlar

**Eksik beceri analizi:** İlanın istediği 9 beceriden 5'i CV'de bulundu (%56).

- CV'de olanlar: Python, SQL, Git, GitHub, NLP
- Eksik olanlar: Docker, REST API, Makine öğrenmesi, Derin öğrenme

**BERTurk eşleştirme:** Örnek CV ve ilan için uyum skoru %66,5 çıktı. En yüksek benzerlik
"Git ile versiyon kontrolü" maddesinde (0,85), en düşük benzerlik CV'de karşılığı olmayan
"Docker ve REST API" maddesinde (0,48) çıktı.

## Dikkat ettiğim noktalar

- BERTurk skorları yüksek çıkma eğiliminde, alakasız cümleler bile 0,45 civarı alıyor. Bu
  yüzden skoru tek başına yüzde olarak yorumlamak yerine farklı CV'leri birbiriyle
  sıralamak için kullanmayı düşünüyorum.
- PDF'ten gelen satırlar bazen yarım kalıyor, bu eşleştirmeyi etkileyebiliyor.
- Eksik beceri analizi, koda yazdığım beceri listesiyle çalışıyor, listede olmayan becerileri
  bulamıyor.
- Büyük `İ`/`I` harfleri yüzünden `API`, `GIT` gibi yazılışlar kaçmasın diye metni
  karşılaştırmadan önce düzelttim.

## Bu hafta öğrendiklerim

- Gömme (embedding) vektörlerinin kelimeyi değil anlamı sayıya çevirdiğini
- TF-IDF'in kelimeye, BERTurk'ün anlama baktığını
- Bir yöntemin skorunun tek başına değil, karşılaştırmalı yorumlanması gerektiğini
- Bir kelimeyi metinde ararken başka kelimenin içinde geçmemesine (MySQL içindeki SQL gibi)
  dikkat etmek gerektiğini
