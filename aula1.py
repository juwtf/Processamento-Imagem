import cv2
import numpy

img = cv2.imread("fotografa.jpg")
 

print('Largura em pixels: ', end='')
print(img.shape[1])

print('Altura em pixels: ', end='')
print(img.shape[0])

print('Quantidade de canais: ', end='')
print(img.shape[2])
 

 
canalBlue = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)

canalGreen = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)

canalRed = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
 
 
canalBlue[:, :, 0] = img[:, :, 0]

canalGreen[:, :, 1] = img[:, :, 1]

canalRed[:, :, 2] = img[:, :, 2]
 
canalGrey = (img[:, :, 0]//3) + (img[:, :, 0]//3) + (img[:, :, 0]//3)


cv2.imshow("Fotografa - Canal Azul", canalBlue)
cv2.imshow("Fotografa - Canal Verde", canalGreen)
cv2.imshow("Fotografa - Canal Vermelho", canalRed)
cv2.imshow("Fotografa - Canal Cinza", canalGrey)
cv2.waitKey(0)

#cv2.imwrite("saida.jpg", img)