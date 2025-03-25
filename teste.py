import cv2
import numpy
import matplotlib.pyplot as plt

#LE A IMAGEM
img = cv2.imread("jamaica.png")

plt.xlabel('Pixel')
plt.ylabel('Quantidade')


#HISTOGRAMA DE TONS CINZA DA IMAGEM
pixel = 256*[0]
for i in range(256):
    
    pixel[i] = i
 

canalGrey = (img[:, :, 0]//3) + (img[:, :, 1]//3) + (img[:, :, 2]//3)

def hist(imagem):
    #histograma = numpy.zeros(256, dtype=numpy.uint8)
    
    histograma = 256*[0]

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] +=1
            
            
    return histograma

def inicio(imagem):
    imagem_saida = numpy.zeros_like(imagem)
    imagem_saida[imagem<150] = 255
    return imagem_saida

def meio(imagem):
    imagem_saida = numpy.zeros_like(imagem)
    imagem_saida[imagem>=100] = 0
    imagem_saida[imagem<50] = 255
    return imagem_saida

def final(imagem):
    imagem_saida = numpy.zeros_like(imagem)
    imagem_saida[imagem>50] = 255
    return imagem_saida

cv2.imshow("Canal Cinza", canalGrey)

cinza = hist(canalGrey)
plt.bar(pixel, cinza, color='gray')
plt.title('Histograma da imagem')
plt.show()
 

limiarizacao = inicio(canalGrey)
cv2.imshow('Inicio - Limiarizacao Multinivel', limiarizacao)

limiarizacao = meio(canalGrey)
cv2.imshow('Meio - Limiarizacao Multinivel', limiarizacao)
 
limiarizacao = final(canalGrey)
cv2.imshow('Final - Limiarizacao Multinivel', limiarizacao) 

cv2.waitKey(0)    