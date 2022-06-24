# Desafio Visão Computacional-Python
# Projeto RasCapture

#Ana Luiza Maciel e Juliane Coimbra

#Primeiro é necessária a instalação de algumas bibliotecas: opencv-python, pytesseract e pillow que podem ser instaladas
#Pelo comando de pip install direto do terminal de comando do computador, elas serão importadas respectivamente como: cv2, 
#pytesseract e PIL
import cv2   #faz o tratamento da imagem
import pytesseract #consegue ler os caracteres da imagem
from cv2 import THRESH_BINARY
from PIL import Image  #voltada para manipulação de imagens em outros formatos como png

#Tratamento da imagem

#Primeiro incluímos a imagem na análise e mostramos sua forma original
img=cv2.imread('placa3.png') 
cv2.imshow('img',img)

cinza= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Transforma a imagem em tons de cinza

final = cv2.threshold(cinza, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #a thresh binary binariza a imagem, transformando-a
cv2.imshow("Otsu", final)                                                       #em preto e branco e a otsu elima as interferências/
                                                                                 #ruídos na imagem
cv2.waitKey(0)                                                                 
cv2.destroyAllWindows()

#Leitura da imagem 

#Primeiro tive que configurar a forma de leitura dos caracteres, de forma que leia números e letras, a partir da função custom_config

custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'

#Em seguida, toda a imagem depois de todo tratamento será escrita para ser lida pela biblioteca Tesseract
cv2.imwrite("placa.jpg", final)

#Detalhe: tive que criar um caminho a partir da função abaixo para que a biblioteca tesseract possa ser importada e usada direto 
#da pasta do computador (aparentemente se o sistema operacional não for Windows, esse problema não acontece)
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

#Por fim, usando a função image_to_string a mensagem pode ser lida e depois printada na tela
caracteres = pytesseract.image_to_string(Image.open("placa.jpg"), config = custom_config)
print(" A placa analisada na imagem é: " + caracteres)

#OBS: o sistema funciona a partir de imagens em formato png ou jpeg e lendo placas do formato anterior a do Mercosul, devido a 
#modificação da aparencia dos caracteres na plca (possuem muito mais interferência)
