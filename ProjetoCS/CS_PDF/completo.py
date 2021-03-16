import io
import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import PIL
# Google Text to Speech API
#from gtts import gTTS

# Nome dado para os arquivos a serem utilizados
# Arquivo de saída
nome_arquivo = "saida"
# Arquivo Entrada
pdf_entrada = "lunalovegood.pdf"

# Primeira Etapa: Converter páginas para fomato de imagem como .jpg ou .png
pages = convert_from_path(pdf_entrada, 500)
for i, image in enumerate(pages):
    fname = 'image'+str(i)+'.jpg'
    image.save(fname)

# Segunda Etapa: Abrir imagem e realizar detecção pelo openCV
img = cv2.imread("image0.jpg")
height, width, _ = img.shape

# Cutting image
roi = img[0: height, 400: width]

# Terceira Etapa: utilipar API de OCR
data = pytesseract.image_to_string(roi, lang='por', config='--psm 6')
print(data)
print(pytesseract.get_languages(config=''))

# Quarta Etapa: Gerar string p/ arquivo .txt de saída
# Gerador de Audio
#language = 'pt'
#myobj = gTTS(text=text_detected, lang=language, slow=False)
#myobj.save("completo.mp3")

#gerador de nomes
nome_arquivo = nome_arquivo + '_' + pdf_entrada
arquivo = open(nome_arquivo, "w")
print(data)
arquivo.write(data)
