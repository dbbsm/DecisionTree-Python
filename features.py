# -*- coding: utf-8 -*-

import numpy as np

def pixels_em_cima(image):
    """funcao que retorna 1 se a imagem tiver mais informacao
    em cima do que em baixo, 0 caso contrario"""
    up_sum = 0
    down_sum = 0

    for x in range(len(image)/2):
        up_sum = up_sum + image[x][0]

    for y in range(len(image)/2, len(image)):
        down_sum = down_sum + image[y][0]

    if up_sum >= down_sum:
        return 1
    else:
        return 0

def side_pixels(img):
    #feature que ve qual o lado da imagem com mais informaçao
    image = np.reshape(img, (28,28))
    left_side = image[0:28,0:14]
    right_side = image[0:28, 14:28]

    left_linear = np.reshape(left_side, (392,1))
    right_linear = np.reshape(right_side, (392,1))

    quantidade_left_side = 0
    quantidade_right_side = 0

    #qual dos lados tem mais informaçao
    quantidade_max = quantidade_left_side
    max_side = 0 #0 para o lado esquerdo e 1 para o lado direito

    for x in left_linear:
        quantidade_left_side = quantidade_left_side+x

    for x in right_linear:
        quantidade_right_side = quantidade_right_side+x

    if quantidade_left_side >= quantidade_max:
        quantidade_max = quantidade_left_side
        max_side = 0

    if quantidade_right_side >= quantidade_max:
        quantidade_max = quantidade_right_side
        max_side = 1

    return max_side


def quantidade_por_quadrante(image):
    """funcao que devolve o quadrante(0:3) com o maior valor de informacao"""
    #divide a imagem no quadrante
    image = np.reshape(image, (28, 28))
    up_left = image[0:14, 0:14]
    up_right = image[0:14, 14:28]
    down_left = image[14:28, 0:14]
    down_right = image[14:28, 14:28]
    
    #depois de dividida em quatro e necessario redimensionar as partes outra vez para manipualacao
    up_left_linear = np.reshape(up_left, (196, 1))
    up_right_linear = np.reshape(up_right, (196, 1))
    down_left_linear = np.reshape(down_left, (196, 1))
    down_right_linear = np.reshape(down_right, (196, 1))

    quantidade_up_left = 0
    quantidade_up_right = 0
    quantidade_down_left = 0
    quantidade_down_right = 0
    
    #pretendemos saber quais dos quadrantes tem mais informacao
    quantidade_max = quantidade_up_left
    max_quadrante = 0
    
    for x in up_left_linear:
        quantidade_up_left= quantidade_up_left + x
    
    for x in up_right_linear:
        quantidade_up_right = quantidade_up_right + x
    
    for x in down_left_linear:
        quantidade_down_left = quantidade_down_left + x
    
    for x in down_right_linear:
        quantidade_down_right = quantidade_down_right + x
    
    if quantidade_up_right >= quantidade_max:
        quantidade_max = quantidade_up_right
        max_quadrante = 1
    if quantidade_down_left >= quantidade_max:
        quantidade_max = quantidade_down_left
        max_quadrante = 2
    if quantidade_down_right >= quantidade_max:
        quantidade_max = quantidade_down_right
        max_quadrante = 3
    
    return max_quadrante

def pixels_por_imagem(image):
    """funcao que nos permite devolver a classe do atributo "amount_per_image"
    a que a imagem em questao pertence"""
    amount = 0
   

    for x in image:
        amount = amount + x
    
    if (amount >= 0) & (amount <= 60):
        return 0 #geralmente o numero 1
    elif (amount > 60) & (amount <= 110):
        return 1 #geralmente o numero 4,5,6,7,9
    else:
        return 2 #geralmente o numero 0,2,3,8