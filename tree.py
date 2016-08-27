# -*- coding: utf-8 -*-

import features


def tree(data):


	folha4_0_0_data = []
	folha4_0_1_data = []
	folha4_0_2_data = []
	folha4_0_3_data = []
	folha4_0_4_data = []
	folha4_0_5_data = []
	folha4_0_6_data = []
	folha4_0_7_data = []
	folha4_0_8_data = []
	folha4_0_9_data = []
	folha4_0_10_data = []
	folha4_0_11_data = []
	folha4_0_12_data = []
	folha4_0_13_data = []
	folha4_0_14_data = []
	folha4_0_15_data = []

	folha4_1_0_data = []
	folha4_1_1_data = []
	folha4_1_2_data = []
	folha4_1_3_data = []
	folha4_1_4_data = []
	folha4_1_5_data = []
	folha4_1_6_data = []
	folha4_1_7_data = []
	folha4_1_8_data = []
	folha4_1_9_data = []
	folha4_1_10_data = []
	folha4_1_11_data = []
	folha4_1_12_data = []
	folha4_1_13_data = []
	folha4_1_14_data = []
	folha4_1_15_data = []

	folha4_2_0_data = []
	folha4_2_1_data = []
	folha4_2_2_data = []
	folha4_2_3_data = []
	folha4_2_4_data = []
	folha4_2_5_data = []
	folha4_2_6_data = []
	folha4_2_7_data = []
	folha4_2_8_data = []
	folha4_2_9_data = []
	folha4_2_10_data = []
	folha4_2_11_data = []
	folha4_2_12_data = []
	folha4_2_13_data = []
	folha4_2_14_data = []
	folha4_2_15_data = []

	for x in data:

		#raiz
		if features.pixels_por_imagem(x[0]) == 0:

			#patamar 2
			if features.pixels_em_cima(x[0]) == 0:

				#patamar 3
				if features.quantidade_por_quadrante(x[0]) == 0:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_0
						folha4_0_0_data.append(x)
					else:
						#fola4_0_1
						folha4_0_1_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_2
						folha4_0_2_data.append(x)
					else:
						#folha4_0_3
						folha4_0_3_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 2:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_4
						folha4_0_4_data.append(x)
					else:
						#folha4_0_5
						folha4_0_5_data.append(x)

				#else quer dizer que retorna o quadrante 3
				else:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_6
						folha4_0_6_data.append(x)
					else:
						#folha4_0_7
						folha4_0_7_data.append(x)

			#patamar 2
			elif features.pixels_em_cima(x[0]) == 1:

				#patamar 3
				if features.quantidade_por_quadrante(x[0]) == 0:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_8
						folha4_0_8_data.append(x)
					else:
						#folha4_0_9
						folha4_0_9_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_10
						folha4_0_10_data.append(x)
					else:
						#folha4_0_11
						folha4_0_11_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 2:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_12
						folha4_0_12_data.append(x)
					else:
						#folha4_0_13
						folha4_0_13_data.append(x)

				#else quer dizer que retorna o quadrante 3
				else:

					if features.side_pixels(x[0]) == 0:
						#folha4_0_14
						folha4_0_14_data.append(x)
					else:
						#folha4_0_15
						folha4_0_15_data.append(x)

		#raiz
		elif features.pixels_por_imagem(x[0]) == 1:

			#patamar 2
			if features.pixels_em_cima(x[0]) == 0:

				#patamar 3
				if features.quantidade_por_quadrante(x[0]) == 0:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_0
						folha4_1_0_data.append(x)
					else:
						#folha4_1_1
						folha4_1_1_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_2
						folha4_1_2_data.append(x)
					else:
						#folha4_1_3
						folha4_1_3_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 2:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_4
						folha4_1_4_data.append(x)
					else:
						#folha4_1_5
						folha4_1_5_data.append(x)

				#else quer dizer que retorna o quadrante 3
				else:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_6
						folha4_1_6_data.append(x)
					else:
						#folha4_1_7
						folha4_1_7_data.append(x)

			#patamar 2
			elif features.pixels_em_cima(x[0]) == 1:

				#patamar 3
				if features.quantidade_por_quadrante(x[0]) == 0:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_8
						folha4_1_8_data.append(x)
					else:
						#folha4_1_9
						folha4_1_9_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_10
						folha4_1_10_data.append(x)
					else:
						#folha4_1_11
						folha4_1_11_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 2:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_12
						folha4_1_12_data.append(x)
					else:
						#folha4_1_13
						folha4_1_13_data.append(x)

				#else quer dizer que retorna o quadrante 3
				else:

					if features.side_pixels(x[0]) == 0:
						#folha4_1_14
						folha4_1_14_data.append(x)
					else:
						#folha4_1_15
						folha4_1_15_data.append(x)
		

		#raiz
		#else quando retorna 2
		else:

			#patamar 2
			if features.quantidade_por_quadrante(x[0]) == 0:
				#nao chegam dados aqui
				#patamar 3
				if features.pixels_em_cima(x[0]) == 0:

					if features.side_pixels(x[0]) == 0:
						#folha4_2_0
						folha4_2_0_data.append(x)
					else:
						#folha4_2_1
						folha4_2_1_data.append(x)

				elif features.pixels_em_cima(x[0]) == 1:

					if features.side_pixels(x[0]) == 0:
						#folha4_2_2
						folha4_2_2_data.append(x)
					else:
						#folha4_2_3
						folha4_2_3_data.append(x)

			#patamar 2
			elif features.quantidade_por_quadrante(x[0]) == 1:

				#patamar 3
				if features.pixels_em_cima(x[0]) == 0:

					if features.side_pixels(x[0]) == 0:
						#folha4_2_4
						folha4_2_4_data.append(x)
					else:
						#folha4_2_5
						folha4_2_5_data.append(x)

				elif features.pixels_em_cima(x[0]) == 1:

					if features.side_pixels(x[0]) == 0:
						#folha4_2_6
						folha4_2_6_data.append(x)
					else:
						#folha4_2_7
						folha4_2_7_data.append(x)



			#patamar 2
			elif features.quantidade_por_quadrante(x[0]) == 2:

				#patamar 3
				if features.side_pixels(x[0]) == 0:
					#mais informacao do lado esquerdo

					if features.pixels_em_cima(x[0]) == 0:
						#folha4_2_8
						folha4_2_8_data.append(x)

					else:
						#folha4_2_9
						folha4_2_9_data.append(x)

				elif features.side_pixels(x[0]) == 1:
					#mais informacao do lado direito
					if features.pixels_em_cima(x[0]) == 0:
						#folha4_2_10
						folha4_2_10_data.append(x)

					else:
						#folha4_2_11
						folha4_2_11_data.append(x)

			#patamar 2
			#else quer dizer que retorna o quadrante 3
			else:

				#patamar 3
				if features.pixels_em_cima(x[0]) == 0:

					if features.side_pixels(x[0]) == 0:
						#folha4_2_12
						folha4_2_12_data.append(x)
					else:
						#folha4_2_13
						folha4_2_13_data.append(x)

				elif features.pixels_em_cima(x[0]) == 1:

					if features.side_pixels(x[0]) == 0:
						#folha4_2_14
						folha4_2_14_data.append(x)
					else:
						#folha4_2_15
						folha4_2_15_data.append(x)

	print 'O numero que sai mais para a folha 4_0_0 : '
	contador_num_folha(folha4_0_0_data)

	print 'O numero que sai mais para a folha 4_0_1 : '
	contador_num_folha(folha4_0_1_data)

	print 'O numero que sai mais para a folha 4_0_2 : '
	contador_num_folha(folha4_0_2_data)

	print 'O numero que sai mais para a folha 4_0_3 : '
	contador_num_folha(folha4_0_3_data)

	print 'O numero que sai mais para a folha 4_0_4 : '
	contador_num_folha(folha4_0_4_data)

	print 'O numero que sai mais para a folha 4_0_5 : '
	contador_num_folha(folha4_0_5_data)

	print 'O numero que sai mais para a folha 4_0_6 : '
	contador_num_folha(folha4_0_6_data)

	print 'O numero que sai mais para a folha 4_0_7 : '
	contador_num_folha(folha4_0_7_data)

	print 'O numero que sai mais para a folha 4_0_8 : '
	contador_num_folha(folha4_0_8_data)

	print 'O numero que sai mais para a folha 4_0_9 : '
	contador_num_folha(folha4_0_9_data)

	print 'O numero que sai mais para a folha 4_0_10 : '
	contador_num_folha(folha4_0_10_data)

	print 'O numero que sai mais para a folha 4_0_11 : '
	contador_num_folha(folha4_0_11_data)

	print 'O numero que sai mais para a folha 4_0_12 : '
	contador_num_folha(folha4_0_12_data)

	print 'O numero que sai mais para a folha 4_0_13 : '
	contador_num_folha(folha4_0_13_data)

	print 'O numero que sai mais para a folha 4_0_14 : '
	contador_num_folha(folha4_0_14_data)

	print 'O numero que sai mais para a folha 4_0_15 : '
	contador_num_folha(folha4_0_15_data)

	print 'O numero que sai mais para a folha 4_1_0 : '
	contador_num_folha(folha4_1_0_data)

	print 'O numero que sai mais para a folha 4_1_1 : '
	contador_num_folha(folha4_1_1_data)

	print 'O numero que sai mais para a folha 4_1_2 : '
	contador_num_folha(folha4_1_2_data)

	print 'O numero que sai mais para a folha 4_1_3 : '
	contador_num_folha(folha4_1_3_data)

	print 'O numero que sai mais para a folha 4_1_4 : '
	contador_num_folha(folha4_1_4_data)

	print 'O numero que sai mais para a folha 4_1_5 : '
	contador_num_folha(folha4_1_5_data)

	print 'O numero que sai mais para a folha 4_1_6 : '
	contador_num_folha(folha4_1_6_data)

	print 'O numero que sai mais para a folha 4_1_7 : '
	contador_num_folha(folha4_1_7_data)

	print 'O numero que sai mais para a folha 4_1_8 : '
	contador_num_folha(folha4_1_8_data)

	print 'O numero que sai mais para a folha 4_1_9 : '
	contador_num_folha(folha4_1_9_data)

	print 'O numero que sai mais para a folha 4_1_10 : '
	contador_num_folha(folha4_1_10_data)

	print 'O numero que sai mais para a folha 4_1_11 : '
	contador_num_folha(folha4_1_11_data)

	print 'O numero que sai mais para a folha 4_1_12 : '
	contador_num_folha(folha4_1_12_data)

	print 'O numero que sai mais para a folha 4_1_13 : '
	contador_num_folha(folha4_1_13_data)

	print 'O numero que sai mais para a folha 4_1_14 : '
	contador_num_folha(folha4_1_14_data)

	print 'O numero que sai mais para a folha 4_1_15 : '
	contador_num_folha(folha4_1_15_data)

	print 'O numero que sai mais para a folha 4_2_0 : '
	contador_num_folha(folha4_2_0_data)

	print 'O numero que sai mais para a folha 4_2_1 : '
	contador_num_folha(folha4_2_1_data)

	print 'O numero que sai mais para a folha 4_2_2 : '
	contador_num_folha(folha4_2_2_data)

	print 'O numero que sai mais para a folha 4_2_3 : '
	contador_num_folha(folha4_2_3_data)

	print 'O numero que sai mais para a folha 4_2_4 : '
	contador_num_folha(folha4_2_4_data)

	print 'O numero que sai mais para a folha 4_2_5 : '
	contador_num_folha(folha4_2_5_data)

	print 'O numero que sai mais para a folha 4_2_6 : '
	contador_num_folha(folha4_2_6_data)

	print 'O numero que sai mais para a folha 4_2_7 : '
	contador_num_folha(folha4_2_7_data)

	print 'O numero que sai mais para a folha 4_2_8 : '
	contador_num_folha(folha4_2_8_data)

	print 'O numero que sai mais para a folha 4_2_9 : '
	contador_num_folha(folha4_2_9_data)

	print 'O numero que sai mais para a folha 4_2_10 : '
	contador_num_folha(folha4_2_10_data)

	print 'O numero que sai mais para a folha 4_2_11 : '
	contador_num_folha(folha4_2_11_data)

	print 'O numero que sai mais para a folha 4_2_12 : '
	contador_num_folha(folha4_2_12_data)

	print 'O numero que sai mais para a folha 4_2_13 : '
	contador_num_folha(folha4_2_13_data)

	print 'O numero que sai mais para a folha 4_2_14 : '
	contador_num_folha(folha4_2_14_data)

	print 'O numero que sai mais para a folha 4_2_15 : '
	contador_num_folha(folha4_2_15_data)



def contador_num_folha(data):

	contador_0 = 0
	contador_1 = 0
	contador_2 = 0
	contador_3 = 0
	contador_4 = 0
	contador_5 = 0
	contador_6 = 0
	contador_7 = 0
	contador_8 = 0
	contador_9 = 0

	maximo_num = 0
	max_temp = contador_0

	if len(data) == 0:

		print " nao ha dados nesta folha"
	
	else:

		for x in data:
			if(x[1][0] == 1):        	
				contador_0 = contador_0 + 1
			elif(x[1][1] == 1):
				contador_1 = contador_1 + 1
			elif(x[1][2] == 1):
				contador_2 = contador_2 + 1
			elif(x[1][3] == 1):
				contador_3 = contador_3 + 1
			elif(x[1][4] == 1):
				contador_4 = contador_4 + 1   
			elif(x[1][5] == 1):
				contador_5 = contador_5 + 1
			elif(x[1][6] == 1):
				contador_6 = contador_6 + 1
			elif(x[1][7] == 1):
				contador_7 = contador_7 + 1
			elif(x[1][8] == 1):
				contador_8 = contador_8 + 1
			elif(x[1][9] == 1):
				contador_9 = contador_9 + 1

		if contador_1 > max_temp:
			max_temp = contador_1
			maximo_num = 1

		if contador_2 > max_temp:
			max_temp = contador_2
			maximo_num = 2

		if contador_3 > max_temp:
			max_temp = contador_3
			maximo_num = 3

		if contador_4 > max_temp:
			max_temp = contador_4
			maximo_num = 4

		if contador_5 > max_temp:
			max_temp = contador_5
			maximo_num = 5

		if contador_6 > max_temp:
			max_temp = contador_6
			maximo_num = 6

		if contador_7 > max_temp:
			max_temp = contador_7
			maximo_num = 7

		if contador_8 > max_temp:
			max_temp = contador_8
			maximo_num = 8

		if contador_9 > max_temp:
			max_temp = contador_9
			maximo_num = 9

		print " %d com percentagem: %f" % (maximo_num,float(max_temp)/float(len(data)))