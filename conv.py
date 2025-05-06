import matplotlib.pyplot as plt
import cv2
import numpy as np


img = cv2.imread('imagem.jpg')

imagem = (img[:, :, 0]//3) + (img[:, :, 1]//3) + (img[:, :, 2]//3)


def adicionar_padding(imagem, pad):
    altura_imagem = len(imagem)
    largura_imagem = len(imagem[0])

    imagem_padded = []
    for _ in range(altura_imagem + 2 * pad):
        linha_padded = [0] * (largura_imagem + 2 * pad)
        imagem_padded.append(linha_padded)

    for i in range(altura_imagem):
        for j in range(largura_imagem):
            imagem_padded[i + pad][j + pad] = imagem[i][j]
    return imagem_padded


def convolucao(imagem, filtro):
    altura_imagem = len(imagem)
    largura_imagem = len(imagem[0])
    altura_filtro = len(filtro)
    largura_filtro = len(filtro[0])

    pad = altura_filtro // 2
    imagem_padded = adicionar_padding(imagem, pad)

    imagem_saida = [[0] * largura_imagem for _ in range(altura_imagem)]

    for i in range(altura_imagem):
        for j in range(largura_imagem):
            soma = 0
            for m in range(altura_filtro):
                for n in range(largura_filtro):
                    soma += imagem_padded[i + m][j + n] * filtro[m][n]
            imagem_saida[i][j] = min(max(soma, 0), 255)
    return imagem_saida



filtro = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

filtro_desfoque = np.array([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
], dtype=np.float32)/26


imagem_convoluida = convolucao(imagem, filtro_desfoque)

def exibir_imagem(imagem, titulo):
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.axis('off')

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
exibir_imagem(imagem, "Imagem Original")

plt.subplot(1, 2, 2)
exibir_imagem(imagem_convoluida, "Imagem Convoluída")

plt.show()
