CV_DOSYASI = "ornek_cv.pdf"
ILAN_DOSYASI = "ilan.txt"
EN_ONEMLI_KELIME_SAYISI = 8  # ortak kelimelerden kaç tanesinin gösterileceği
# Anlam taşımayan sık kelimeler (puana ve listeye girmesin)
GEREKSIZ_KELIMELER = ["ile", "ve", "bir", "için", "gibi", "olan", "olmak", "daha", "veya", "çok"]

import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def metni_hazirla(metin):
    # Türkçede büyük İ ve I harfleri küçültülürken bozulur,bunu düzeltiyoruz
    metin = metin.replace("İ", "i").replace("I", "ı")
    return metin.lower()


def pdf_oku(dosya_yolu):
    tum_metin = ""
    with pdfplumber.open(dosya_yolu) as pdf:
        for sayfa in pdf.pages:
            tum_metin += sayfa.extract_text() + "\n"
    return tum_metin


# 1) CV ve ilan metnini oku
cv_metni = metni_hazirla(pdf_oku(CV_DOSYASI))
with open(ILAN_DOSYASI, encoding="utf-8") as dosya:
    ilan_metni = metni_hazirla(dosya.read())

# 2) TF-IDF: iki metni sayısal vektörlere çevir
#    char_wb: kelimeleri harf parçalarına böler, Türkçe ekleri (python'u, python'da) aynı sayar
vektorlestirici = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5))
matris = vektorlestirici.fit_transform([cv_metni, ilan_metni])

# 3) Kosinüs benzerliği: 0 = hiç benzemiyor, 1 = aynı
benzerlik = cosine_similarity(matris[0], matris[1])[0][0]
print(f"CV - ilan uyum skoru: %{benzerlik * 100:.1f}")

# 4) Kelime bazında bak (ilanda geçen hangi kelimeler CV'de de var?)
kelime_vektorlestirici = TfidfVectorizer(token_pattern=r"(?u)\b\w{3,}\b",
                                         stop_words=GEREKSIZ_KELIMELER)
kelime_matrisi = kelime_vektorlestirici.fit_transform([cv_metni, ilan_metni])
kelimeler = kelime_vektorlestirici.get_feature_names_out()
cv_agirliklari = kelime_matrisi[0].toarray()[0]
ilan_agirliklari = kelime_matrisi[1].toarray()[0]

ortak = [
    (kelimeler[i], cv_agirliklari[i] * ilan_agirliklari[i])
    for i in range(len(kelimeler))
    if cv_agirliklari[i] > 0 and ilan_agirliklari[i] > 0
]
ortak.sort(key=lambda cift: cift[1], reverse=True)

print("\nCV ve ilanda ortak geçen en önemli kelimeler:")
for kelime, puan in ortak[:EN_ONEMLI_KELIME_SAYISI]:
    print(f"  {kelime}")