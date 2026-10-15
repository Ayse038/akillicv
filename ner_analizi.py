CV_DOSYASI = "ornek_cv.pdf"
NER_MODELI = "savasy/bert-base-turkish-ner-cased"


import pdfplumber
from transformers import pipeline


with pdfplumber.open(CV_DOSYASI) as pdf:
    tum_metin = ""
    for sayfa in pdf.pages:
        tum_metin += sayfa.extract_text()


ner = pipeline("ner", model=NER_MODELI, aggregation_strategy="simple")


sonuclar = ner(tum_metin)


for varlik in sonuclar:
    kelime = varlik["word"]
    kategori = varlik["entity_group"]
    guven = varlik["score"]
    print(f"{kelime}  ->  {kategori}  (güven: {guven:.2f})")