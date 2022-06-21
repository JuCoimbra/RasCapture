from urllib import request
import cv2
import numpy as np
import urllib3
import traceback

#Lê a URL da imagem e carrega com urllib3
while True:
    #Iniciando uma conexão WEB
    http = urllib3.PoolManager()
    
    #Pedindo a URL ao usuário
    imageUrl = input('Insira a url da imagem a ser examinada: ')

    #Enquanto uma URL valida não é colocada, o loop segue
    try:
        loadURLImage = http.urlopen('GET', imageUrl)

    #Erro no requerimento web
    except Exception as e:
        print("Ocorreu um erro. Por favor, tente novamente.")
    else:
        break

#Imagens são matrizes cujo elemneto de preenchimento é a variavel do tipo uint8
#uint8 são variaveis com valores entre 0 e 255 que definem a cor do pixel
#Para que a OpenCV2 leia a imagem, é preciso converte-la em uma array uint8
#Mais informações 
#https://professor.luzerna.ifc.edu.br/ricardo-antonello/wp-content/uploads/sites/8/2017/02/Livro-Introdu%C3%A7%C3%A3o-a-Vis%C3%A3o-Computacional-com-Python-e-OpenCV-1.pdf
imageArray = np.asarray(bytearray(loadURLImage.read()), dtype=np.uint8)