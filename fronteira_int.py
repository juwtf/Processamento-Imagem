import cv2

import numpy as np

import matplotlib.pyplot as plt
 
def fronteira_interna_manual(imagem_binaria, elemento_estruturante):
 
    es_h, es_w = elemento_estruturante.shape
    es_center = (es_h // 2, es_w // 2)
    h, w = imagem_binaria.shape
    imagem_erodida = np.zeros_like(imagem_binaria)
 
 
    for i in range(es_center[0], h - es_center[0]):
        for j in range(es_center[1], w - es_center[1]):

            regiao = imagem_binaria[i - es_center[0]:i + es_center[0] + 1,
                                    j - es_center[1]:j + es_center[1] + 1]
 
            if np.all((regiao == 255)[elemento_estruturante == 1]):

                imagem_erodida[i, j] = 255
 
 
    fronteira = imagem_binaria - imagem_erodida
 
    return fronteira
 
#imagem binária

imagem_binaria = cv2.imread('bin.png', cv2.IMREAD_GRAYSCALE)
 
 
elemento_estruturante = np.array([[0, 1, 0],

                                   [1, 1, 1],

                                   [0, 1, 0]], dtype=np.uint8)
 
fronteira = fronteira_interna_manual(imagem_binaria, elemento_estruturante)
 
 
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Imagem Binária')
plt.imshow(imagem_binaria, cmap='gray')
plt.axis('off')
 
plt.subplot(1, 2, 2)
plt.title('Fronteira Interna')
plt.imshow(fronteira, cmap='gray')
plt.axis('off')
 
plt.tight_layout()

plt.show()

 