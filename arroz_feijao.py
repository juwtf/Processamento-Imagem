import cv2
import numpy

img = cv2.imread('arroz&feijao.png')


def sem_arroz(imagem):
    imagem[imagem>130] = 255
    return imagem

def sem_feijao(imagem):
    imagem[imagem<130] = 255
    return imagem


canalBlue = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalGreen = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalRed = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8) 



canalBlue[:, :, 0] = img[:, :, 0]
canalGreen[:, :, 1] = img[:, :, 1]
canalRed[:, :, 2] = img[:, :, 2]


canalGrey = (img[:, :, 0]//3) + (img[:, :, 0]//3) + (img[:, :, 0]//3)

 
 
semFeijao = sem_feijao(canalGrey)
cv2.imshow('Sem Feijão', semFeijao)
 
 
canalBlue = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalGreen = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalRed = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8) 



canalBlue[:, :, 0] = img[:, :, 0]
canalGreen[:, :, 1] = img[:, :, 1]
canalRed[:, :, 2] = img[:, :, 2]


canalGrey = (img[:, :, 0]//3) + (img[:, :, 0]//3) + (img[:, :, 0]//3) 
 
 
semArroz = sem_arroz(canalGrey)
cv2.imshow('Sem Arroz', semArroz)
 
 
cv2.waitKey(0)    
 