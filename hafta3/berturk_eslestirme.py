CV_DOSYASI = "ornek_cv.pdf"
ILAN_DOSYASI = "ilan.txt"
MODEL_ADI = "emrecan/bert-base-turkish-cased-mean-nli-stsb-tr"  # BERTurk tabanlı cümle modeli
EN_KISA_CV_SATIRI = 20  # bundan kısa CV satırları (başlık, tarih vb.) atlanır

import pdfplumber
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


def pdf_oku(dosya_yolu):
    tum_metin = ""
    with pdfplumber.open(dosya_yolu) as pdf:
        for sayfa in pdf.pages:
            tum_metin += sayfa.extract_text() + "\n"
    return tum_metin


def satiri_temizle(satir):
    # PDF'ten gelen madde işaretlerini ve boşlukları temizler
    for isaret in ["(cid:127)", "•"]:
        satir = satir.replace(isaret, "")
    return satir.strip()


def gomme_al(model, cumleler):
    # Her cümleyi anlamını temsil eden bir sayı listesine (vektöre) çevirir
    return model.encode(cumleler, convert_to_tensor=True)


# 1) CV'yi satırlara, ilanı maddelere böl
cv_satirlari = [satiri_temizle(s) for s in pdf_oku(CV_DOSYASI).split("\n")]
cv_satirlari = [s for s in cv_satirlari if len(s) >= EN_KISA_CV_SATIRI]

with open(ILAN_DOSYASI, encoding="utf-8") as dosya:
    ilan_maddeleri = [s.strip()[1:].strip() for s in dosya if s.strip().startswith("-")]

# 2) Modeli yükle
model = SentenceTransformer(MODEL_ADI)
cv_gommeleri = gomme_al(model, cv_satirlari)
ilan_gommeleri = gomme_al(model, ilan_maddeleri)

# 3) Her ilan maddesi için CV'deki en çok benzeyen satırı bul
benzerlikler = cos_sim(ilan_gommeleri, cv_gommeleri)  # satır: ilan maddesi, sütun: CV satırı

skorlar = []
for i, madde in enumerate(ilan_maddeleri):
    en_iyi = int(benzerlikler[i].argmax())
    skor = float(benzerlikler[i][en_iyi])
    skorlar.append(skor)
    print(f"İlan maddesi : {madde}")
    print(f"En yakın CV  : {cv_satirlari[en_iyi]}")
    print(f"Benzerlik    : {skor:.2f}\n")

# 4) Genel skor: maddelerin ortalaması
genel = sum(skorlar) / len(skorlar)
print(f"BERTurk uyum skoru: %{genel * 100:.1f}")