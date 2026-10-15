
CV_DOSYASI = "ornek_cv.pdf"

import pdfplumber

with pdfplumber.open(CV_DOSYASI) as pdf:
    tum_metin = ""
    for sayfa in pdf.pages:
        tum_metin += sayfa.extract_text()

print(tum_metin)