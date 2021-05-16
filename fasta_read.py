#!/usr/bin/env python
"""
Basicamente este pequeno programa foi só para pegar em ficheiros FASTA do NUCLEOTIDE e traduzi-los
"""
import os
from os import listdir as ls
from os.path import isfile, join, isdir
import subprocess
from typing import Tuple

"""
1-> usar os para escolher logo os ficheiros que estão na pasta ✔
2-> Buscar mais ficheiros para testar o programa ✔
"""

DNA_CODONS = {
    # '_Start_' - START, '_Stop_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "_Start_",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_Stop_", "TAG": "_Stop_", "TGA": "_Stop_"
}

def path_standart() -> dict:
	current = os.getcwd()

	gener = (join(current, i) for i in ls(current) if i == 'data' and isdir(i))
	
	global data_folder
	data_folder = next(gener)
	
	return {n:filum  for n, filum in enumerate(ls(data_folder), 1) if filum.endswith('.fa') or filum.endswith('.fasta') }

def reading_frame() -> Tuple[str, list]:
    """
    Definir o reading frame da sequencia que queremos ler sendo 0 'usual'
    """
    dictiona = path_standart()
    choice = int(input('Name the file with the sequence you wish to translate -> '))
    shift = int(input('Reading frame (-3,-2,-1,0,+1,+2,+3) -> '))
    if choice in dictiona.keys():
        fasta_file = dictiona.get(choice)
        
    with open(f'{join(data_folder,fasta_file)}', 'r') as gen:
        seq_id = gen.readline()
        remove_newline = lambda x: x.replace('\n', '')
        seq = remove_newline(gen.read())

    
    seq = seq[::-1] if shift < 0 else seq
    
    return seq_id, [seq[i : i+3] for i in range(abs(shift), len(seq) + shift, 3)]


def sequence_translation(sequence : list) -> str:
    """
    Função para traduzir a sequencia para sequência de aminoacidos.  
    Para no momento que encontrar um "codão" que não tem 3 nucleótidos
    """
    a_a = [DNA_CODONS[cod] for cod in sequence if cod in DNA_CODONS.keys()]

    def metionine_replacerinator() -> None:
        start_count = 0
        switch = lambda x: x.replace('_Start_', 'M')
        for n,i in enumerate(a_a):
            if i == '_Start_' and start_count == 0:
                start_count +=1

            elif i == '_Start_' and start_count == 1:
                a_a[n] = switch(i)

    metionine_replacerinator()

    return '-'.join(a_a)

def main():
    subprocess.run('clear')
    only_files = path_standart()
    [print(count, '-', i) for count, i in only_files.items()]
    seq_id , sequence = reading_frame()
    translation = sequence_translation(sequence)
    subprocess.run('clear')
    print(f'Sequence translated: {seq_id}\n{translation}')

if __name__ == "__main__":
    main()
