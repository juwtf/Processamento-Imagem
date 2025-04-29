import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread('rj.jpg', cv2.IMREAD_GRAYSCALE)



# Função de Equalização de Histograma manual
def equalizar_histograma(imagem):
    imagem = np.array(imagem, dtype=np.uint8)
    
    histograma = hist(imagem)

    histograma_normalizado = histograma / histograma.sum()

    cdf = histograma_normalizado.cumsum()

    cdf_normalizado = np.uint8(255 * cdf)

    imagem_equalizada = cdf_normalizado[imagem]

    return imagem_equalizada

def hist(imagem):
    histograma = np.zeros(256, dtype=int)
    

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] +=1
            
            
    return histograma

imagem_equalizada = equalizar_histograma(imagem)

# Exibe as imagens
def exibir_imagem(imagem, titulo):
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.axis('off')

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
exibir_imagem(imagem, "Imagem Original")

plt.subplot(1, 2, 2)
exibir_imagem(imagem_equalizada, "Imagem Equalizada")

plt.show()
