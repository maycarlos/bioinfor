#!/usr/bin/env python3

import time
import os
from os.path import isdir, join
from alive_progress import alive_bar


def path_standart() -> dict:
	current = os.getcwd()

	gener = (join(current, i) for i in os.listdir(current) if i == 'data' and isdir(i))
	
	global data_folder
	data_folder = next(gener)
	
	return {n:filum  for n, filum in enumerate(os.listdir(data_folder), 1) if filum.endswith('.fa') or filum.endswith('.fasta') }

def distance(sequence_1 : str, sequence_2 : str) -> float:
	"""
	Função que verifica o grau de similaridade entre as duas strings.
	o número de letras que são iguais
	parecido com hamming distance mas aqui n quero saber de tamanho de string
	"""
	def bigger_one(sequence_1,sequence_2):

		if len(sequence_1)>len(sequence_2):
			return sequence_1
		else:
			return sequence_2

	letters_shared = sum(i==j for i, j in zip(sequence_1, sequence_2))

	percentage_similarity = letters_shared/len(bigger_one(sequence_1,sequence_2))*100

	return round(percentage_similarity, 2)

def main():
	data_files = path_standart()

	for i, j in data_files.items():
		print(f'{i}-{j}')

	while True:
		choice_1 = int(input('Introduza a sequência de letras que quer testar: '))
		choice_2 = int(input('Introduza a segunda sequência de letras que quer testar: '))

		try:
			with open(f'{join(data_folder, data_files.get(choice_1))}', 'r') as jessie, open(f'{join(data_folder, data_files.get(choice_2))}', 'r') as james:
				
				remove_newline = lambda x: x.replace('\n', '')

				jessie.readline()
				seq_1 = remove_newline(jessie.read())

				james.readline()
				seq_2 = remove_newline(james.read())
				
		except:
			print('Algo de errado não está certo')
			break
	
		with alive_bar(100) as progress:
			for i in range(100):
				time.sleep(0.01)
				progress()
	
		print('Done!')

		global percentage
		percentage = distance(seq_1, seq_2)

		print(f'Similaridade entre sequências: {percentage}%') 

		if input('Quer continuar a comparar strings? (y/n): ') == 'y':	
			return main()

		else:	
			print('Obrigado pela atenção!')
			break
	
if __name__ == '__main__':
	main()
