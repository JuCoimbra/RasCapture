import  urllib.request
import cv2
import numpy as np
import databaselib


#Lê a URL da imagem e carrega com urllib3
while True:
    #Iniciando uma conexão WEB
    #http = urllib3.PoolManager()
    
    #Pedindo a URL ao usuário
    imageUrl = input('Insira a url da imagem a ser examinada: ')

    #Enquanto uma URL valida não é colocada, o loop segue
    try:
        loadURLImage = urllib.request.urlopen(imageUrl)

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
imageArray = np.array(bytearray(loadURLImage.read()), dtype=np.uint8)
image = cv2.imdecode(imageArray, -1)
cv2.imshow('image', image)
cv2.waitKey()

#Código de tratamento da imagem

#Cração da tabela car_table. Não precisa usar, já está criado
#databaselib.createTable("DBPlacas.db")

#Apaga todas as tuplas da tabela car_table. Descomentar caso for usar
#deletCar_table("DBPlacas.db")

#Inserindo dados no banco de dados. Parametros: Placa do carro e nome do banco. Está comentado pois não tem as informações ainda
#idDataPlaca = databaselib.stringTratment(placa, localidade, "DBPlacas.db")

#Mostra em tela a placa e o id do resgistro no banco de dados. Comentado pois não tem os valores necessários ainda.
#print('O veiculo de placa '+ placa +' foi inserido na posição'+ idDataPlaca +'.')
