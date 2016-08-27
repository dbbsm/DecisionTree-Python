# -*- coding: utf-8 -*-

import features
import features_gain

def construcao_patamar2(data):


	classe0_data = []
	classe1_data = []
	classe2_data = []


	for x in data:

		if features.pixels_por_imagem(x[0]) == 0:
			classe0_data.append(x)

		elif features.pixels_por_imagem(x[0]) == 1:
			classe1_data.append(x)

		else:
			classe2_data.append(x)


	print '---O ganho de informacao no ramo classe0 do atributo quantidade_por_quadrante: ' +str(features_gain.quantidade_por_quadrante_gain(classe0_data))
	print '---O ganho de informacao no ramo classe0 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe0_data))
	print '---O ganho de informacao no ramo classe0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_data))
	print '---O ganho de informacao no ramo classe1 do atributo quantidade_por_quadrante: ' +str(features_gain.quantidade_por_quadrante_gain(classe1_data))
	print '---O ganho de informacao no ramo classe1 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe1_data))
	print '---O ganho de informacao no ramo classe1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_data))
	print '---O ganho de informacao no ramo classe2 do atributo quantidade_por_quadrante: ' +str(features_gain.quantidade_por_quadrante_gain(classe2_data))
	print '---O ganho de informacao no ramo classe2 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_data))
	print '---O ganho de informacao no ramo classe2 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_data))


def construcao_patamar3(data):

	classe0_0_data = []
	classe0_1_data = []
	classe1_0_data = []
	classe1_1_data = []
	classe2_0_data = []
	classe2_1_data = []
	classe2_2_data = []
	classe2_3_data = []


	for x in data:
	
		if features.pixels_por_imagem(x[0]) == 0:
			
			if features.pixels_em_cima(x[0]) == 0:
				classe0_0_data.append(x)
			
			#else quer dizer que faz return de 1
			else:
				classe0_1_data.append(x)

		elif features.pixels_por_imagem(x[0]) == 1:
			
			if features.pixels_em_cima(x[0]) == 0:
				classe1_0_data.append(x)

			else:
				classe1_1_data.append(x)

		else:
			
			if features.quantidade_por_quadrante(x[0]) == 0:
				classe2_0_data.append(x)

			elif features.quantidade_por_quadrante(x[0]) == 1:
				classe2_1_data.append(x)
			
			elif features.quantidade_por_quadrante(x[0]) == 2:
				classe2_2_data.append(x)

			#else quer dizer que fez return de 3
			else:
				classe2_3_data.append(x)


	print 'O ganho de informacao no ramo classe0_0 do atributo quantidade_por_quadrante: ' + str(features_gain.quantidade_por_quadrante_gain(classe0_0_data))
	print 'O ganho de informacao no ramo classe0_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_0_data))
	
	print 'O ganho de informacao no ramo classe0_1 do atributo quantidade_por_quadrante: ' +str(features_gain.quantidade_por_quadrante_gain(classe0_1_data))
	print 'O ganho de informacao no ramo classe0_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_1_data))

	print 'O ganho de informacao no ramo classe1_0 do atributo quantidade_por_quadrante: ' +str(features_gain.quantidade_por_quadrante_gain(classe1_0_data))
	print 'O ganho de informacao no ramo classe1_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_0_data))

	print 'O ganho de informacao no ramo classe1_1 do atributo quantidade_por_quadrante: ' +str(features_gain.quantidade_por_quadrante_gain(classe1_1_data))
	print 'O ganho de informacao no ramo classe1_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_1_data))

	print 'O ganho de informacao no ramo classe2_0 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_0_data))
	print 'O ganho de informacao no ramo classe2_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_0_data))

	print 'O ganho de informacao no ramo classe2_1 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_1_data))
	print 'O ganho de informacao no ramo classe2_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_1_data))

	print 'O ganho de informacao no ramo classe2_2 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_2_data))
	print 'O ganho de informacao no ramo classe2_2 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_2_data))

	print 'O ganho de informacao no ramo classe2_3 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_3_data))
	print 'O ganho de informacao no ramo classe2_3 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_3_data))

def construcao_patamar4(data):

	classe0_0_0_data = []
	classe0_0_1_data = []
	classe0_0_2_data = []
	classe0_0_3_data = []
	classe0_1_0_data = []
	classe0_1_1_data = []
	classe0_1_2_data = []
	classe0_1_3_data = []
	classe1_0_0_data = []
	classe1_0_1_data = []
	classe1_0_2_data = []
	classe1_0_3_data = []
	classe1_1_0_data = []
	classe1_1_1_data = []
	classe1_1_2_data = []
	classe1_1_3_data = []
	classe2_0_data = []
	classe2_1_0_data = []
	classe2_1_1_data = []
	classe2_2_0_data = []
	classe2_2_1_data = []
	classe2_3_0_data = []
	classe2_3_1_data = []


	for x in data:
	
		if features.pixels_por_imagem(x[0]) == 0:
			
			if features.pixels_em_cima(x[0]) == 0:
				
				if features.quantidade_por_quadrante(x[0]) == 0:
					classe0_0_0_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:
					classe0_0_1_data.append(x)					
			
				elif features.quantidade_por_quadrante(x[0]) == 2:
					classe0_0_2_data.append(x)

				#else quer dizer que fez return de 3
				else:
					classe0_0_3_data.append(x)
			
			#else quer dizer que faz return de 1
			else:

				if features.quantidade_por_quadrante(x[0]) == 0:
					classe0_1_0_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:
					classe0_1_1_data.append(x)					
			
				elif features.quantidade_por_quadrante(x[0]) == 2:
					classe0_1_2_data.append(x)

				#else quer dizer que fez return de 3
				else:
					classe0_1_3_data.append(x)

		elif features.pixels_por_imagem(x[0]) == 1:
			
			if features.pixels_em_cima(x[0]) == 0:
				
				if features.quantidade_por_quadrante(x[0]) == 0:
					classe1_0_0_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:
					classe1_0_1_data.append(x)					
			
				elif features.quantidade_por_quadrante(x[0]) == 2:
					classe1_0_2_data.append(x)

				#else quer dizer que fez return de 3
				else:
					classe1_0_3_data.append(x)

			else:
				
				if features.quantidade_por_quadrante(x[0]) == 0:
					classe1_1_0_data.append(x)

				elif features.quantidade_por_quadrante(x[0]) == 1:
					classe1_1_1_data.append(x)					
			
				elif features.quantidade_por_quadrante(x[0]) == 2:
					classe1_1_2_data.append(x)

				#else quer dizer que fez return de 3
				else:
					classe1_1_3_data.append(x)

		else:
			
			if features.quantidade_por_quadrante(x[0]) == 0:
				classe2_0_data.append(x)

			elif features.quantidade_por_quadrante(x[0]) == 1:
				
				if features.pixels_em_cima(x[0]) == 0:
					classe2_1_0_data.append(x)
				else:
					classe2_1_1_data.append(x)
			
			elif features.quantidade_por_quadrante(x[0]) == 2:
				
				if features.side_pixels(x[0]) == 0:
					classe2_2_0_data.append(x)
				
				else:
					classe2_2_1_data.append(x)

			#else quer dizer que fez return de 3
			else:

				if features.pixels_em_cima(x[0]) == 0:
					classe2_3_0_data.append(x)
				else:
					classe2_3_1_data.append(x)


	print 'O ganho de informacao no ramo classe0_0_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_0_0_data))
	print 'O ganho de informacao no ramo classe0_0_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_0_1_data))
	print 'O ganho de informacao no ramo classe0_0_2 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_0_2_data))
	print 'O ganho de informacao no ramo classe0_0_3 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_0_3_data))
	
	print 'O ganho de informacao no ramo classe0_1_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_1_0_data))
	print 'O ganho de informacao no ramo classe0_1_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_1_1_data))
	print 'O ganho de informacao no ramo classe0_1_2 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_1_2_data))
	print 'O ganho de informacao no ramo classe0_1_3 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe0_1_3_data))

	print 'O ganho de informacao no ramo classe1_0_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_0_0_data))
	print 'O ganho de informacao no ramo classe1_0_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_0_1_data))
	print 'O ganho de informacao no ramo classe1_0_2 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_0_2_data))
	print 'O ganho de informacao no ramo classe1_0_3 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_0_3_data))

	print 'O ganho de informacao no ramo classe1_1_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_1_0_data))
	print 'O ganho de informacao no ramo classe1_1_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_1_1_data))
	print 'O ganho de informacao no ramo classe1_1_2 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_1_2_data))
	print 'O ganho de informacao no ramo classe1_1_3 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe1_1_3_data))

	print 'O ganho de informacao no ramo classe2_0 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_0_data))
	print 'O ganho de informacao no ramo classe2_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_0_data))

	print 'O ganho de informacao no ramo classe2_1_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_1_0_data))
	print 'O ganho de informacao no ramo classe2_1_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_1_1_data))

	print 'O ganho de informacao no ramo classe2_2_0 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_2_0_data))
	print 'O ganho de informacao no ramo classe2_2_1 do atributo pixels_em_cima: ' +str(features_gain.pixels_em_cima_gain(classe2_2_1_data))

	print 'O ganho de informacao no ramo classe2_3_0 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_3_0_data))
	print 'O ganho de informacao no ramo classe2_3_1 do atributo side_pixels: ' +str(features_gain.side_pixels_gain(classe2_3_1_data))