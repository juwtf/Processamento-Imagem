import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('casa.jpg', cv2.IMREAD_GRAYSCALE)



def equalizar_imagem(img):
    # Verifica se a imagem está em escala de cinza
    if len(img.shape) == 3:
        # Converte para escala de cinza, se necessário
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplica a equalização de histograma
    img_equ = cv2.equalizeHist(img)
    
    return img_equ
    
    
img_equ = equalizar_imagem(img)

# Mostrar as imagens original e equalizada
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Equalizada', img_equ)
  
cv2.waitKey(0) 
cv2.destroyAllWindows() 
