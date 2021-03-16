import io
import os.path
import json
import cv2
import numpy as np
import requests
from pdf2image import convert_from_path
from PIL import Image
import PIL


# Nome dado para os arquivos a serem utilizados

# Arquivo de saída
nome_arquivo = "saida"
# Arquivo Entrada
pdf_entrada = "C_FP23.pdf"


# Primeira Etapa: Converter páginas para fomato de imagem como .jpg ou .png

pages = convert_from_path(pdf_entrada, 200, poppler_path = r'/home/edwiges/PycharmProjects/ProjetoCS/CS_PDF/C_FP23.pdf')
for i, image in enumerate(pages):
    fname = 'image'+str(i)+'.jpg'
    image.save(fname)

# Segunda Etapa: Abrir imagem e realizar detecção pelo openCV

img = cv2.imread("image0.jpg")
height, width, _ = img.shape

# Cutting image
roi = img[0: height, 400: width]

# Terceira Etapa: utilipar API de OCR
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api,
              files = {"image0.jpg": file_bytes},  # converte imagem para bytes
              data = {"apikey": "helloworld", "language": "por"})   #define linguagem do pdf


#cv2.imshow("roi", roi)
#cv2.imshow("Img", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Quarta Etapa: Gerar arquivo .txt de saída
result = result.content.decode ()
result_dict = json.loads(result)
text_detected = result_dict.get("ParsedResults")[0].get("ParsedText")

#gerador de nomes
i = 0
while (os.path.isfile(nome_arquivo + str(i) + ".txt")):
    i += 1
nome_arquivo = nome_arquivo + str(i) + '.txt'

arquivo = open(nome_arquivo, "w")
print(text_detected)
arquivo.write(text_detected)

"""NotADirectoryError: [Errno 20] Not a directory: '/home/edwiges/PycharmProjects/ProjetoCS/CS_PDF/C_FP23.pdf/pdfinfo'
"""

"""pdf2image.exceptions.PDFInfoNotInstalledError: Unable to get page count. Is poppler installed and in PATH?
"""

