import cv2
import numpy

#LE A IMAGEM
img = cv2.imread("fotografa.jpg")

 
canalBlue = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalGreen = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalRed = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
 
 
canalBlue[:, :, 0] = img[:, :, 0]
canalGreen[:, :, 1] = img[:, :, 1]
canalRed[:, :, 2] = img[:, :, 2]
 

cv2.imshow("Fotografa - Canal Blue", canalBlue)
cv2.imshow("Fotografa - Canal Green", canalGreen)
cv2.imshow("Fotografa - Canal Red", canalRed)

cv2.waitKey(0)