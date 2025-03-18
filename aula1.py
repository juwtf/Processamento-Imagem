import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("oxossi.jpg")
 

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
 

cv2.imshow("Fotografa - Canal Blue", canalBlue)
cv2.waitKey(0)

cv2.imshow("Fotografa - Canal Green", canalGreen)
cv2.waitKey(0)

cv2.imshow("Fotografa - Canal Red", canalRed)
cv2.waitKey(0)




pixel = 256*[0]
for i in range(256):
    
    pixel[i] = i
    

plt.xlabel('Pixel')
plt.ylabel('Quantidade')

plt.title('Histograma de imagem em tons de cinza')

def hist(imagem, canal):
    histograma = numpy.zeros(256, dtype=numpy.uint)
    
    #histograma = 256*[0]



    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] +=1
            
            
    return histograma
            

azul = hist(img[:, :, 0], "Blue")
plt.bar(pixel, azul, color='blue')
plt.show()

verde = hist(img[:, :, 1], "Green")
plt.bar(pixel, verde, color='green')
plt.show()

vermelho = hist(img[:, :, 2], "Red")
plt.bar(pixel, vermelho, color='red')
plt.show()


#cv2.imwrite("saida.jpg", img)