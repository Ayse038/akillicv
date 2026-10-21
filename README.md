AkıllıCV

NLP tabanlı CV analizi ve çok modlu aday değerlendirme sistemi — bitirme projesi.

Proje ne yapıyor?

AkıllıCV, bir CV'yi iş ilanıyla otomatik karşılaştırıp uyum skoru çıkarıyor ve mülakat sırasında konuşma ile yüz ifadesini analiz ederek adayı daha bütünlüklü şekilde değerlendiriyor. Amaç, tek bir metin eşleştirmesinden ibaret kalmayıp CV, ses ve görüntü verisini tek bir sistemde birleştiren, kararlarını açıklayabilen ve adil çalışıp çalışmadığı test edilmiş bir değerlendirme Aracı ortaya koymak.

İçerdiği modüller
1. CV analizi

CV'den beceri, eğitim ve deneyim bilgisi Türkçe NER ile çıkarılır; ilan metniyle TF-IDF ve BERTurk gömme vektörleri üzerinden karşılaştırılır. İlanda olup CV'de olmayan beceriler adaya öneri olarak sunulur.

pdfplumber / python-docx — CV dosyasından metin çıkarma
BERTurk tabanlı Türkçe NER — varlık tanıma
TF-IDF + BERTurk gömme, kosinüs benzerliği — eşleştirme skoru

2. Ses analizi

Mülakat kaydından konuşma metne çevrilir ve konuşma tarzı analiz edilir.

Fısıltı — Türkçe konuşma → metin
librosa — konuşma hızı, duraksama süresi, pitch analizi

3. Görüntü işleme

Yüz tespiti ve duygu sınıflandırması, hazır/pretrained modeller kullanılmadan sıfırdan eğitilen iki ayrı CNN ile yapılıyor.

Yüz tespiti: sliding window + kendi eğittiğimiz CNN (WIDER FACE veri setiyle)
Duygu sınıflandırma: kendi eğittiğimiz CNN (FER-2013 veri setiyle)
Grad-CAM — modelin kararını görselleştirme (hangi bölgeye bakarak karar verdiği)

4. Değerlendirme motoru

CV, ses ve görüntü modüllerinden gelen sonuçlar ağırlıklı bir skorda birleştirilir, JSON formatında saklanır ve aday/işveren panellerine ayrı görünümler olarak sunulur.

5. Adalet ve KVKK testi

Aynı CV'nin kimlikli ve anonimleştirilmiş (isim/cinsiyet/yaş maskelenmiş) versiyonları Sisteme verilip skor farkı ölçülüyor — sistemin kimlik bilgilerinden etkilenip etkilenmediğini test ediyoruz.

6. Değerlendirme deneyi

Sistemin ürettiği aday sıralaması, insanların elle yaptığı sıralamayla () karşılaştırılıyor.scipy.stats.spearmanr

Kullanılan teknolojiler
Alan	Araç/Yöntem
CV metin analizi	BERTurk, TF-IDF, Türk NER
Ses analizi	Fısılda, librosa
Görüntü işleme	Kendi eğitilen CNN modelleri, Grad-CAM
Değerlendirme	Pandas, Scipy
Şu anki dosyalar
Dosya	Ne işe yarıyor?
metin_cikarma.py	CV'yi (PDF) okuyup içindeki yazıyı metne çeviriyor (pdfplumber)
ner_analizi.py	CV metnini Türkçe NER modeline verip içindeki varlıkları (kişi, kurum, yer vb.) buluyor
eslestirme_tfidf.py	CV ile iş ilanını TF-IDF ve kosinüs benzerliğiyle karşılaştırıp uyum skoru çıkarıyor
ilan.txt	Eşleştirmeyi denemek için kullanılan örnek iş ilanı
ornek_cv.pdf	Kodları denemek için hazırlanmış örnek CV
requirements.txt	Projenin ihtiyaç duyduğu Python kütüphaneleri
Nasıl çalıştırılır?
Python 3.12 ve (isteğe bağlı) bir sanal ortam kur.
Gerekli kütüphaneleri yükle:
   pip install -r requirements.txt
Dosyaları çalıştır:
   python metin_cikarma.py
   python ner_analizi.py
   python eslestirme_tfidf.py

ner_analizi.py ilk çalıştırmada Hugging Face'ten NER modelini indirir, bu yüzden biraz zaman alabilir.

Yol haritası
 Sistem mimarisinin ve modüllerin planlanması
 CV metin analizi modülünün geliştirilmesi
 CV'den metin çıkarma (pdfplumber)
 Türkçe NER ile varlık çıkarma (BERTurk tabanlı model)
 İş ilanı ile CV'yi TF-IDF ve kosinüs benzerliğiyle eşleştirme
 BERTurk gömme vektörleriyle anlamsal eşleştirme
 Eksik beceri analizi
 Değerlendirme deneyi için veri toplama (anonim CV + insan sıralaması)
 Yüz tespiti modelinin WIDER FACE ile eğitilmesi
 Duygu sınıflandırma modelinin FER-2013 ile eğitilmesi
 Ses analizi modülünün entegrasyonu (Whisper + librosa)
 Grad-CAM ile açıklanabilirlik katmanının eklenmesi
 Adalet / KVKK testinin uygulanması
 Tüm modüllerin tek bir değerlendirme motorunda birleştirilmesi
 Aday ve işveren panellerinin geliştirilmesi
Geliştirme günlüğü

Her hafta yapılan çalışmalar burada kısaca kaydediliyor.

Hafta 1 — 10 Ekim 2026
Proje GitHub'a yüklendi, README ve yol haritası oluşturuldu.
Python ortamı kuruldu (PyCharm + sanal ortam), ve yüklendi.pdfplumberpython-docx
metin_cikarma.py yazıldı: örnek bir CV'den (PDF) metin başarıyla çıkarıldı.
transformers ve kuruldu, yazıldı: Türkçe NER modeli CV metni üzerinde çalıştırıldı ve varlıklar listelendi.torchner_analizi.py
Karşılaşılan sorun: PDF dosyası yanlışlıkla klasörünün içinde kaldığı için kod dosyayı bulamadı (). Dosya proje klasörüne taşınınca sorun çözüldü..venvFileNotFoundError
Sıradaki adım: iş ilanı metnini aynı şekilde işleyip TF-IDF ile CV–ilan eşleştirmesi yapmak.
Hafta 2 — 21 Ekim 2026
Örnek bir iş ilanı hazırlandı ().ilan.txt
eslestirme_tfidf.py yazıldı: CV ve ilan TF-IDF ile sayısal vektörlere çevrilip kosinüs benzerliğiyle karşılaştırıldı. Örnek CV için uyum skoru %41,0 çıktı.
CV ve ilanda ortak geçen önemli kelimeler (python, git, veri, yazılım vb.) listelendi.
Türkçe büyük / harfi sorunu ve ek problemi (harf parçalarıyla karşılaştırma) ele alındı.İI
requirements.txt'e eklendi. Haftanın detayları içinde.scikit-learnhafta2/README.md
Sıradaki adım: BERTurk gömme vektörleriyle anlamsal eşleştirme ve eksik beceri analizi.
Proje bilgisi
Öğrenci: Ayşe Ak
Üniversite: Kayseri Üniversitesi, Yazılım Mühendisliği
Danışman: Ayhan Renklier
