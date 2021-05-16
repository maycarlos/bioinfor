#!usr/bin/env python

import os
from os import listdir as ls
from os.path import isfile, join, isdir
import random

# Fazer algo para saber se uma sequencia é boa para PCR
def path_standart() -> dict:
	current = os.getcwd()

	gener = (join(current, i) for i in os.listdir(current) if i == 'data' and isdir(i))
	
	global data_folder
	data_folder = next(gener)
	
	return {n:filum  for n, filum in enumerate(os.listdir(data_folder), 1) if filum.endswith('.fa') or filum.endswith('.fasta') }

def get_sequence():
    data_files = path_standart()

    for i, j in data_files.items():
        print(f'{i}-{j}')

    choice = int(input('Name the file with the sequence you wish to mutate -> '))

    if choice in data_files.keys():
        fasta_file = data_files.get(choice)

    with open(f'{join(data_folder,fasta_file)}', 'r') as fast:
        seq_id = fast.readline()
        remove_newline = lambda x: x.replace('\n', '')
        seq = remove_newline(fast.read())

    return seq

def mutations(sequence: str, number_of_mutations: int) -> list:

    mutate = {'I':'Insert','D':'Delete', 'S':'Substitute'}
    bases = ('A','C','T','G',)
    
    mutate_keys = [i for i in mutate.keys()]
    changes = []

    while number_of_mutations != 0:

        base = random.choice(bases)
        form = random.choice(mutate_keys)
        i = random.randint(0,len(sequence))

        if form == 'I':
            sequence = sequence[i:] + base + sequence[:i]

        elif form == 'D':
            sequence = list(sequence)
            del sequence[i]
            sequence = ''.join(sequence)

        elif form == 'S':
            sequence = sequence[:i] + base + sequence[i+1:]

        changes.append((mutate[form], i))
        number_of_mutations -= 1

    return changes


def main():
  
    seq = get_sequence()
    n_mutations = int(input('Please enter the number of mutations you wish to introduce: '))


    results = mutations(seq, n_mutations)

    for i in results:
        print(f'{i[0]} @ position {i[1]}')

    print(seq)


if __name__ == '__main__':
    main()
