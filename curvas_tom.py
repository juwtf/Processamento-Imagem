import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Função para aplicar a transformação linear f(r) = c * r + l
def aplicar_transformacao_linear(imagem, c=1, l=0):
    # Converter a imagem para um array numpy
    imagem_array = np.array(imagem, dtype=np.float32)
    
    # Aplicar a transformação linear (c * r + l)
    imagem_transformada = c * imagem_array + l
    
    # Garantir que os valores fiquem dentro do intervalo [0, 255]
    imagem_transformada = np.clip(imagem_transformada, 0, 255)
    
    return imagem_transformada.astype(np.uint8)  # Garantir que a imagem modificada seja do tipo uint8

# Função para exibir as imagens e seus histogramas
def exibir_imagem_com_histograma(imagem_original, imagem_modificada):
    # Plotando a imagem original e a modificada
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Exibindo a imagem original
    axes[0, 0].imshow(imagem_original)
    axes[0, 0].set_title("Imagem Original")
    axes[0, 0].axis('off')
    
    # Exibindo a imagem modificada
    axes[0, 1].imshow(imagem_modificada)
    axes[0, 1].set_title("Imagem Modificada")
    axes[0, 1].axis('off')
    
    # Plotando os histogramas
    axes[1, 0].hist(imagem_original.flatten(), bins=256, color='gray', alpha=0.5)
    axes[1, 0].set_title("Histograma da Imagem Original")

    
    axes[1, 1].hist(imagem_modificada.flatten(), bins=256, color='gray', alpha=0.5)
    axes[1, 1].set_title("Histograma da Imagem Modificada")

    plt.tight_layout()
    plt.show()

# Carregar a imagem
imagem = Image.open("casa.jpg")

# Aplicar a transformação linear (exemplo com c=1.2 e l=20)
imagem_modificada = aplicar_transformacao_linear(imagem, c=1.2, l=40)

# Exibir a imagem original e a modificada com seus histogramas
exibir_imagem_com_histograma(np.array(imagem), imagem_modificada)
