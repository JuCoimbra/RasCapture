import cv2
from cv2 import THRESH_BINARY


img=cv2.imread('carro2.jpg') #Baixa a imagem 
cv2.imshow('img',img)

cinza= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Transforma a imagem a tons de cinza
cv2.imshow('cinza',cinza)

ret,bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY) #A partir dos limites minimos de preto(90) e máximo de branco(255) transforma a imagem para preto e branco
cv2.imshow('bin',bin)

desfoque= cv2.GaussianBlur(bin, (5,5),0) #por meio do desfoque da imagem, é possível eliminar parte do ruído e ressaltar as formas geométricas
cv2.imshow('desf',desfoque)

contornos, hier = cv2.findContours (desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img, contornos, -1, (0,255,0),2)
#cv2.imshow('cont', img)

for c in contornos:
    perimetro = cv2.arcLength(c, True)
    aprox = cv2.approxPolyDP(c, 0.03*perimetro, True)

    if len(aprox) == 4:
        (x,y,lar,alt)= cv2.boundingRect(c)
        cv2.rectangle(img, (x,y), (x+alt, y+lar),(0,255,0),2)

cv2.imshow('draw',img)

cv2.waitKey(0)
cv2.destroyAllWindows()