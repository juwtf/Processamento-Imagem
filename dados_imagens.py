import cv2
import numpy
import matplotlib.pyplot as plt

#LE A IMAGEM
img = cv2.imread("iansa.jpg")


print('Largura em pixels: ', end='')
print(img.shape[1])

print('Altura em pixels: ', end='')
print(img.shape[0])

print('Quantidade de canais: ', end='')
print(img.shape[2])