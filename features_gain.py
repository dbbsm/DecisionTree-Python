# -*- coding: utf-8 -*-

import math
import features

def pixels_em_cima_gain(data):
    """funcao que mostra o ganho de informacao do atributo
    "ter mais quantidade de informacao em cima" do que em baixo"""
    up_counter = 0
    down_counter = 0
    up_data = []
    down_data = []
    entropia_up = 0
    entropia_down = 0
    data_entropia = 0
    gain = 0

    if len(data) == 0:
        return 0

    for x in data:
        if features.pixels_em_cima(x[0]) == 1:
            up_counter = up_counter + 1
            up_data.append(x)
        else:
            down_counter = down_counter + 1
            down_data.append(x)

    #entropia de todo o conjunto
    data_entropia = calc_entropia(data)
    #entropia do conjunto mais informacao em cima
    entropia_up = calc_entropia(up_data)
    #entropia do conjunto mais informacao em baixo
    entropia_down = calc_entropia(down_data)
    #probabilidade mais informacao em cima
    p_up = float(up_counter)/float(len(data))
    #probabilidade mais informacao em baixo
    p_down = float(down_counter)/float(len(data))
    #ganho de informacao
    gain = data_entropia -p_up*entropia_up -p_down*entropia_down
    return gain

def side_pixels_gain(data):
    #funçao que mostra o ganho de informaçao da feature ter mais informaçao do lado esquerdo do que do lado direito
    right_counter = 0
    left_counter = 0

    right_data = []
    left_data = []

    entropia_right = 0
    entropia_left = 0

    gain = 0

    if len(data) == 0:
        return 0

    for x in data:
        if features.side_pixels(x[0]) == 0:
            left_counter = left_counter + 1
            left_data.append(x)
        elif features.side_pixels(x[0]) == 1:
            right_counter = right_counter + 1
            right_data.append(x)

    data_entropia = calc_entropia(data)
    entropia_left = calc_entropia(left_data)
    entropia_right = calc_entropia(right_data)
    percentagem_left = float(left_counter) / float(len(data))
    percentagem_right = float(right_counter) / float(len(data))
    gain = data_entropia -percentagem_left*entropia_left -percentagem_right*entropia_right
    return gain

def quantidade_por_quadrante_gain(data):
    """funcao de ganho de informacao para o atributo "amount_per_image" """
    class0_counter = 0
    class1_counter = 0
    class2_counter = 0
    class3_counter = 0
    class0_data = []
    class1_data = []
    class2_data = []
    class3_data = []
    entropia_class0 = 0
    entropia_class1 = 0
    entropia_class2 = 0
    entropia_class3 = 0
    
    if len(data) == 0:
        return 0

    gain = 0
    for x in data:
        if features.quantidade_por_quadrante(x[0]) == 0:
            class0_counter = class0_counter + 1
            class0_data.append(x)
        elif features.quantidade_por_quadrante(x[0]) == 1:
            class1_counter = class1_counter + 1
            class1_data.append(x)
        elif features.quantidade_por_quadrante(x[0]) == 2:
            class2_counter = class2_counter + 1
            class2_data.append(x)
        else:
            class3_counter = class3_counter + 1
            class3_data.append(x)

    data_entropia = calc_entropia(data)
    entropia_class0 = calc_entropia(class0_data)
    entropia_class1 = calc_entropia(class1_data)
    entropia_class2 = calc_entropia(class2_data)
    entropia_class3 = calc_entropia(class3_data)
    p_class0 = float(class0_counter)/float(len(data))
    p_class1 = float(class1_counter)/float(len(data))
    p_class2 = float(class2_counter)/float(len(data))
    p_class3 = float(class3_counter)/float(len(data))
    gain = data_entropia -p_class0*entropia_class0 -p_class1*entropia_class1 -p_class2*entropia_class2 -p_class3*entropia_class3
    return gain


def pixels_por_imagem_gain(data):
    """funcao de ganho de informacao para o atributo "amount_per_image" """
    class0_counter = 0
    class1_counter = 0
    class2_counter = 0
    class0_data = []
    class1_data = []
    class2_data = []
    class0_entropia = 0
    class1_entropia = 0
    class2_entropia = 0
    gain = 0

    if len(data) == 0:
        return 0
        
    for x in data:
        if features.pixels_por_imagem(x[0]) == 0:
            class0_counter = class0_counter + 1
            class0_data.append(x)
        elif features.pixels_por_imagem(x[0]) == 1:
            class1_counter = class1_counter + 1
            class1_data.append(x)
        else:
            class2_counter = class2_counter + 1
            class2_data.append(x)

    data_entropia = calc_entropia(data)
    class0_entropia = calc_entropia(class0_data)
    class1_entropia = calc_entropia(class1_data)
    class2_entropia = calc_entropia(class2_data)
    p_class0 = float(class0_counter)/float(len(data))
    p_class1 = float(class1_counter)/float(len(data))
    p_class2 = float(class2_counter)/float(len(data))
    gain = data_entropia -p_class0*class0_entropia -p_class1*class1_entropia -p_class2*class2_entropia
    return gain   


def calc_entropia(data):
    """funcao que calcula a entropia de para um certo conjunto de dados"""
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    #se nao houver data entropia=0
    if len(data) == 0:
        return 0
    
    for x in data:
        if(x[1][0] == 1):
            count_0 = count_0 + 1
        elif(x[1][1] == 1):
            count_1 = count_1 + 1
        elif(x[1][2] == 1):
            count_2 = count_2 + 1
        elif(x[1][3] == 1):
            count_3 = count_3 + 1
        elif(x[1][4] == 1):
            count_4 = count_4 + 1   
        elif(x[1][5] == 1):
            count_5 = count_5 + 1
        elif(x[1][6] == 1):
            count_6 = count_6 + 1
        elif(x[1][7] == 1):
            count_7 = count_7 + 1
        elif(x[1][8] == 1):
            count_8 = count_8 + 1
        elif(x[1][9] == 1):
            count_9 = count_9 + 1
    
    
    p0 = float(count_0)/float(len(data))
    p1 = float(count_1)/float(len(data))
    p2 = float(count_2)/float(len(data))
    p3 = float(count_3)/float(len(data))
    p4 = float(count_4)/float(len(data))
    p5 = float(count_5)/float(len(data))
    p6 = float(count_6)/float(len(data))
    p7 = float(count_7)/float(len(data))
    p8 = float(count_8)/float(len(data))
    p9 = float(count_9)/float(len(data))
    
    #garantir que nao é executado log de 0
    if p0 == 0:
        calc0 = 0
    else:
        calc0 = -p0*math.log(p0, 2)
    if p1 == 0:
        calc1 = 0
    else:
        calc1 = -p1*math.log(p1, 2)
    if p2 == 0:
        calc2 = 0
    else:
        calc2 = -p2*math.log(p2, 2)
    if p3 == 0:
        calc3 = 0
    else:
        calc3 = -p3*math.log(p3, 2)
    if p4 == 0:
        calc4 = 0
    else:
        calc4 = -p4*math.log(p4, 2)
    if p5 == 0:
        calc5 = 0
    else:
        calc5 = -p5*math.log(p5, 2)
    if p6 == 0:
        calc6 = 0
    else:
        calc6 = -p6*math.log(p6, 2)
    if p7 == 0:
        calc7 = 0
    else:
        calc7 = -p7*math.log(p7, 2)
    if p8 == 0:
        calc8 = 0
    else:
        calc8 = -p8*math.log(p8, 2)
    if p9 == 0:
        calc9 = 0
    else:
        calc9 = -p9*math.log(p9, 2)
    
    
    entropy = calc0 + calc1 + calc2 + calc3 +calc4 +calc5 +calc6 +calc7 +calc8 +calc9
    return entropy