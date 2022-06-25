import  urllib.request #Para requerimentos WEB na busca da imagem
import cv2  #faz o tratamento da imagem
import numpy as np
import pytesseract #consegue ler os caracteres da imagem
from PIL import Image  #voltada para manipulação de imagens em outros formatos como png
import databaselib #Biblioteca criada para o banco de dados
import sys #Para forçar a saida do programa

print('''Seja bem-vindo(a). Esse programa lê imagens com placas antigas e armazena seus dados em um banco de dados.\n
    Ao longo do programa a imagem selecionada ira ser mostrada em tela, de forma que, para sair da imagem, você deve clicar
    em qualquer tecla. Vamos começar.''')

#Lê a URL da imagem e carrega com urllib3
while True:
    #Iniciando uma conexão WEB
    #http = urllib3.PoolManager()
    
    #Pedindo a URL ao usuário
    imageUrl = input('Insira a url da imagem a ser examinada ou X para encerrar o programa: ')

    #Enquanto uma URL valida não é colocada, o loop segue
    try:
        loadURLImage = urllib.request.urlopen(imageUrl)

    #Erro no requerimento web
    except Exception as e:
        if imageUrl.upper() == 'X':
            sys.exit('Encerrando programa...\nAté a próxima!')
        else:
            print("Ocorreu um erro. Por favor, tente novamente.")
    else:
        #Imagens são matrizes cujo elemneto de preenchimento é a variavel do tipo uint8
        #uint8 são variaveis com valores entre 0 e 255 que definem a cor do pixel
        #Para que a OpenCV2 leia a imagem, é preciso converte-la em uma array uint8
        #Mais informações 
        #https://professor.luzerna.ifc.edu.br/ricardo-antonello/wp-content/uploads/sites/8/2017/02/Livro-Introdu%C3%A7%C3%A3o-a-Vis%C3%A3o-Computacional-com-Python-e-OpenCV-1.pdf
        imageArray = np.array(bytearray(loadURLImage.read()), dtype=np.uint8)
        image = cv2.imdecode(imageArray, -1)
        cv2.imshow('Image', image)
        cv2.waitKey()
        cv2.destroyAllWindows()
        resp = input('Essa é a imagem escolhida? Aperte:\nY - Sim\nN- Não')
        if resp.upper() == 'Y' or '':
            break
        elif resp.upper() == 'N' or 'NÃO' or 'NAO':
            continue
        else: 
            print('Não entendemos sua resposta, vamos tentar movamente.')

#Tratamento da imagem
#Transforma a imagem em tons de cinza
cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

#a thresh binary binariza a imagem, transformando-a
#em preto e branco e a otsu elima as interferências/ruídos na imagem
blur=cv2.GaussianBlur(cinza,(3,3),0)
final = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow("final", final)                                                       

#Configuração da forma de leitura dos caracteres, de forma que leia números e letras, a partir da função custom_config

custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz'

#A imagem depois de todo tratamento será escrita para ser lida pela biblioteca Tesseract
cv2.imwrite("placa.jpg", final)

#Caminho a partir da função abaixo para que a biblioteca tesseract possa ser importada e usada direto 
#da pasta do computador (aparentemente se o sistema operacional não for Windows, esse problema não acontece)
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

#Por fim, usando a função image_to_string a mensagem pode ser lida e depois printada na tela
caracteres = pytesseract.image_to_string(Image.open("placa.jpg"), config = custom_config)
print(" A placa analisada na imagem é: " + caracteres)

#OBS: o sistema funciona a partir de imagens em formato png ou jpeg e lendo placas do formato anterior a do Mercosul, devido a 
#modificação da aparencia dos caracteres na plca (possuem muito mais interferência)

#Cração da tabela car_table. Não precisa usar, já está criado
#databaselib.createTable("DBPlacas.db")

#Apaga todas as tuplas da tabela car_table. Descomentar caso for usar
#deletCar_table("DBPlacas.db")

#Inserindo dados no banco de dados. Parametros: Placa do carro e nome do banco. Está comentado pois não tem as informações ainda
#idDataPlaca = databaselib.stringTratment(placa, localidade, "DBPlacas.db")

#Mostra em tela a placa e o id do resgistro no banco de dados. Comentado pois não tem os valores necessários ainda.
#print('O veiculo de placa '+ placa +' foi inserido na posição'+ idDataPlaca +'.')
