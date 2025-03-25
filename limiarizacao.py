import cv2
import numpy
import matplotlib.pyplot as plt

#LE A IMAGEM
img = cv2.imread("casa.jpg")

def sem_arroz(imagem):
    imagem[imagem>140] = 255
    return imagem

def sem_feijao(imagem):
    imagem[imagem<150] = 255
    return imagem


canalGrey = (img[:, :, 0]//3) + (img[:, :, 1]//3) + (img[:, :, 2]//3) 
 
semFeijao = sem_feijao(canalGrey)
cv2.imshow('Sem Feijao', semFeijao)

canalGrey = (img[:, :, 0]//3) + (img[:, :, 1]//3) + (img[:, :, 2]//3)  


semArroz = sem_arroz(canalGrey)
cv2.imshow('Sem Arroz', semArroz)
 
 
cv2.waitKey(0)    