# -*- coding: utf-8 -*-

def informacao_por_numero(data):
	# funçao auxiliar que permite estudar/saber uma media de informaçao
	# de cada numero

	information_0 = 0
	information_1 = 0
	information_2 = 0
	information_3 = 0
	information_4 = 0
	information_5 = 0
	information_6 = 0
	information_7 = 0
	information_8 = 0
	information_9 = 0

	#countador de numeros

	counter_0 = 0
	counter_1 = 0
	counter_2 = 0
	counter_3 = 0
	counter_4 = 0
	counter_5 = 0
	counter_6 = 0
	counter_7 = 0
	counter_8 = 0
	counter_9 = 0

	for x in data:
		if x[1][0] == 1:
			for y in x[0]:
				information_0 = information_0 + y
			counter_0 = counter_0 + 1
		elif x[1][1] == 1:
			for y in x[0]:
				information_1 = information_1 + y
			counter_1 = counter_1 + 1
		elif x[1][2] == 1:
			for y in x[0]:
				information_2 = information_2 + y
			counter_2 = counter_2 + 1
		elif x[1][3] == 1:
			for y in x[0]:
				information_3 = information_3 + y
			counter_3 = counter_3 + 1
		elif x[1][4] == 1:
			for y in x[0]:
				information_4 = information_4 + y
			counter_4 = counter_4 + 1
		elif x[1][5] == 1:
			for y in x[0]:
				information_5 = information_5 + y
			counter_5 = counter_5 + 1
		elif x[1][6] == 1:
			for y in x[0]:
				information_6 = information_6 + y
			counter_6 = counter_6 + 1
		elif x[1][7] == 1:
			for y in x[0]:
				information_7 = information_7 + y
			counter_7 = counter_7 + 1
		elif x[1][8] == 1:
			for y in x[0]:
				information_8 = information_8 + y
			counter_8 = counter_8 + 1
		elif x[1][9] == 1:
			for y in x[0]:
				information_9 = information_9 + y
			counter_9= counter_9 + 1

	print 'Media de Informacao de 0: ' + str(information_0/counter_0)
	print 'Media de Informacao de 1: ' + str(information_1/counter_1)
	print 'Media de Informacao de 2: ' + str(information_2/counter_2)
	print 'Media de Informacao de 3: ' + str(information_3/counter_3)
	print 'Media de Informacao de 4: ' + str(information_4/counter_4)
	print 'Media de Informacao de 5: ' + str(information_5/counter_5)
	print 'Media de Informacao de 6: ' + str(information_6/counter_6)
	print 'Media de Informacao de 7: ' + str(information_7/counter_7)
	print 'Media de Informacao de 8: ' + str(information_8/counter_8)
	print 'Media de Informacao de 9: ' + str(information_9/counter_9)