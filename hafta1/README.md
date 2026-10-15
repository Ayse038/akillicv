# AkıllıCV — Hafta 1

Bu klasörde bitirme projem AkıllıCV için ilk hafta yaptığım çalışmalar var. Bu hafta
projenin ilk modülü olan **CV analizinin** başlangıç kısmını yaptım: bir CV'den metni
çıkarmak ve o metindeki önemli bilgileri (isim, kurum, yer gibi) otomatik bulmak.

## Bu hafta neler yaptım?

1. **Çalışma ortamını kurdum.** PyCharm'da yeni bir proje açıp sanal ortam (venv) oluşturdum.
2. **CV'den metin çıkardım.** `pdfplumber` kütüphanesiyle bir PDF CV'yi okuyup içindeki
   yazıyı metne çevirdim.
3. **NER (varlık tanıma) denedim.** Hazır bir Türkçe BERT modeliyle (BERTurk tabanlı)
   CV metnindeki varlıkları buldurdum.
4. **Test için örnek bir CV hazırladım.** Kodları denemek için kendi bilgilerimle bir
   PDF CV oluşturdum.

## Dosyalar

| Dosya | Ne yapıyor? |
|---|---|
| `metin_cikarma.py` | CV'yi (PDF) açıp içindeki metni ekrana yazdırıyor |
| `ner_analizi.py` | CV metnini NER modeline verip bulunan varlıkları kategorileriyle birlikte yazdırıyor |
| `ornek_cv.pdf` | Kodları denemek için kullandığım örnek CV |
| `requirements.txt` | Gerekli Python kütüphaneleri |

## Kullandığım araçlar

- **Python 3.12** ve **PyCharm**
- **pdfplumber** — PDF'ten metin çıkarmak için
- **transformers** ve **torch** — hazır NER modelini çalıştırmak için
- **savasy/bert-base-turkish-ner-cased** — Hugging Face'ten aldığım Türkçe NER modeli

## Nasıl çalıştırılır?

1. Kütüphaneleri yükle:
   ```
   pip install -r requirements.txt
   ```
2. CV'den metin çıkarmak için:
   ```
   python metin_cikarma.py
   ```
3. NER'i çalıştırmak için:
   ```
   python ner_analizi.py
   ```

## Karşılaştığım sorunlar

- **`FileNotFoundError`:** Kod `ornek_cv.pdf` dosyasını bulamadı. Sebebi, PDF'in yanlışlıkla
  `.venv` klasörünün içinde kalmasıydı. Dosyayı proje klasörünün ana dizinine (kodla aynı
  yere) taşıyınca çözüldü.

## Bu hafta öğrendiklerim

- Sanal ortamın (venv) ne işe yaradığını ve kütüphanelerin projeye nasıl kurulduğunu
- Python'da bir PDF'in sayfalarını döngüyle gezip metin çıkarmayı
- NER'in bir metindeki kişi, kurum, yer gibi özel öğeleri otomatik etiketlediğini
- Hazır bir modeli `transformers` ile birkaç satırda çalıştırmayı
- Bir dosya yolu hatasında dosyanın gerçekte nerede durduğuna bakmak gerektiğini
