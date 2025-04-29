import cv2
import numpy
import matplotlib.pyplot as plt

#LE A IMAGEM
img = cv2.imread("iansa.jpg")

 
canalBlue = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalGreen = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
canalRed = numpy.zeros((img.shape[0], img.shape[1], img.shape[2]), dtype=numpy.uint8)
 
 
canalBlue[:, :, 0] = img[:, :, 0]
canalGreen[:, :, 1] = img[:, :, 1]
canalRed[:, :, 2] = img[:, :, 2]
 
canalGrey = (img[:, :, 0]//3) + (img[:, :, 0]//3) + (img[:, :, 0]//3) 

plt.xlabel('Pixel')
plt.ylabel('Quantidade')


#HISTOGRAMA DE TONS CINZA DA IMAGEM
pixel = 256*[0]
for i in range(256):
    
    pixel[i] = i

 

#HISTOGRAMA DE TONS RGB DA IMAGEM
def hist(imagem, canal):
    histograma = numpy.zeros(256, dtype=numpy.uint8)
    
    #histograma = 256*[0]

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] +=1
            
            
    return histograma
            
#PLOTA OS HISTOGRAMAS
cinza = hist(canalGrey, "Cinza")
plt.bar(pixel, cinza, color='gray')
plt.title('Histograma da imagem em tons de cinza')
plt.show()

azul = hist(canalBlue, "Azul")
plt.bar(pixel, azul, color='blue')
plt.title('Histograma da imagem em tons azul')
plt.show()

verde = hist(canalGreen, "Verde")
plt.bar(pixel, verde, color='green')
plt.title('Histograma da imagem em tons verde')
plt.show()

vermelho = hist(canalRed, "Vermelho")
plt.bar(pixel, vermelho, color='red')
plt.title('Histograma da imagem em tons vermelho')
plt.show()

#SALVA A IMAGEM
#cv2.imwrite("saida.jpg", img)