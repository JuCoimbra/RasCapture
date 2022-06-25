import cv2  #faz o tratamento da imagem
import numpy as np
import pytesseract #consegue ler os caracteres da imagem
from PIL import Image  #voltada para manipulação de imagens em outros formatos como png
import databaselib #Biblioteca criada para o banco de dados

print('''Seja bem-vindo(a). Esse programa lê imagens com placas antigas e armazena seus dados em um banco de dados.\n
    Ao longo do programa a imagem selecionada irá ser mostrada em tela, de forma que, para sair da imagem, você deve 
    clicar em qualquer tecla.
    Se quiser ler outras placas, altere o nome do arquivo para um dos outros nomes contidos na pasta. Vamos começar!''')

image= cv2.imread('placa1.jpeg') 
cv2.imshow('Image', image)
cv2.waitKey()
cv2.destroyAllWindows()

#Tratamento da imagem
#Transforma a imagem em tons de cinza
cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

#a thresh binary binariza a imagem, transformando-a
#em preto e branco e a otsu elima as interferências/ruídos na imagem
blur=cv2.GaussianBlur(cinza,(3,3),0)
final = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
tratando= cv2.imread('IMG1.png')
tamanho= cv2.resize(tratando, (400,200))
cv2.imshow('tratando', tamanho)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow('Imagem tratada', final) 
cv2.waitKey()
cv2.destroyAllWindows()                                                        

#Configuração da forma de leitura dos caracteres, de forma que leia números e letras, a partir da função custom_config

custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz'

#A imagem depois de todo tratamento será escrita para ser lida pela biblioteca Tesseract
cv2.imwrite("placa.jpg", final)

#Caminho a partir da função abaixo para que a biblioteca tesseract possa ser importada e usada direto 
#da pasta do computador (aparentemente se o sistema operacional não for Windows, esse problema não acontece)
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

#Por fim, usando a função image_to_string a mensagem pode ser lida e depois printada na tela
placa = pytesseract.image_to_string(Image.open("placa.jpg"), config = custom_config)
print(" A placa analisada na imagem é: " + placa)

#OBS: o sistema funciona a partir de imagens em formato png ou jpeg e lendo placas do formato anterior a do Mercosul, devido a 
#modificação da aparencia dos caracteres na plca (possuem muito mais interferência)

#Cração da tabela car_table. Não precisa usar, já está criado
databaselib.createTable("DBPlacas.db")

#Apaga todas as tuplas da tabela car_table. 
deletCar_table("DBPlacas.db")

#Inserindo dados no banco de dados. Parametros: Placa do carro e nome do banco.
idDataPlaca = databaselib.stringTratment(placa, 'Brasil', "DBPlacas.db")

#Mostra em tela a placa e o id do resgistro no banco de dados.
print('O veiculo de placa '+ placa +' foi inserido na posição'+ idDataPlaca +'.')
