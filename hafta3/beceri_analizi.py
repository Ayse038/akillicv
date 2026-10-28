CV_DOSYASI = "ornek_cv.pdf"
ILAN_DOSYASI = "ilan.txt"

# Aranacak beceriler. Sol taraf ekranda ad görünecek, sağ taraf metinde aranacak yazılışlar.
BECERILER = {
    "Python": ["python"],
    "C#": ["c#"],
    "Java": ["java"],
    "JavaScript": ["javascript"],
    "SQL": ["sql"],
    "Git": ["git"],
    "GitHub": ["github"],
    "Docker": ["docker"],
    "REST API": ["rest api", "restful"],
    "ASP.NET Core": ["asp.net"],
    "Entity Framework": ["entity framework"],
    "Makine öğrenmesi": ["makine öğrenmesi", "makine öğrenimi", "machine learning"],
    "Derin öğrenme": ["derin öğrenme", "deep learning"],
    "NLP": ["nlp", "doğal dil işleme"],
    "Görüntü işleme": ["görüntü işleme"],
    "MATLAB": ["matlab"],
    "Linux": ["linux"],
    "Veri analizi": ["veri analizi"],
}

import re
import pdfplumber


def metni_hazirla(metin):
    # Türkçede büyük İ ve I harfleri küçültülürken bozulur, önce onları düzelttik
    metin = metin.replace("İ", "i").replace("I", "ı").lower()
    # Karşılaştırmayı kolaylaştırmak için ı'yı i'ye çeviriyoruz
    return metin.replace("ı", "i")


def pdf_oku(dosya_yolu):
    tum_metin = ""
    with pdfplumber.open(dosya_yolu) as pdf:
        for sayfa in pdf.pages:
            tum_metin += sayfa.extract_text() + "\n"
    return tum_metin


def beceri_var_mi(metin, yazilislar):
    for yazilis in yazilislar:
        yazilis = metni_hazirla(yazilis)
        # Kelimenin başında harf olmasın: "mysql" içindeki "sql" sayılmasın
        desen = r"(?<![\w#+])" + re.escape(yazilis)
        # Kısa becerilerde sonda da harf olmasın: "git", "github"ı yanlışlıkla yakalamasın
        if len(yazilis) <= 4:
            desen += r"(?![\w#+])"
        if re.search(desen, metin):
            return True
    return False


cv_metni = metni_hazirla(pdf_oku(CV_DOSYASI))
with open(ILAN_DOSYASI, encoding="utf-8") as dosya:
    ilan_metni = metni_hazirla(dosya.read())

# İlanın istediği becerileri bul, sonra bunların CV'de olup olmadığına bak
ilan_becerileri = [ad for ad, yazilislar in BECERILER.items() if beceri_var_mi(ilan_metni, yazilislar)]
var_olanlar = [ad for ad in ilan_becerileri if beceri_var_mi(cv_metni, BECERILER[ad])]
eksikler = [ad for ad in ilan_becerileri if ad not in var_olanlar]

print(f"İlanın istediği beceri sayısı: {len(ilan_becerileri)}")
print("\nCV'de olanlar:")
for ad in var_olanlar:
    print(f"  + {ad}")

print("\nCV'de bulunamayanlar (eksik beceriler):")
for ad in eksikler:
    print(f"  - {ad}")

if ilan_becerileri:
    oran = len(var_olanlar) / len(ilan_becerileri) * 100
    print(f"\nBeceri uyumu: %{oran:.0f}  ({len(var_olanlar)}/{len(ilan_becerileri)})")