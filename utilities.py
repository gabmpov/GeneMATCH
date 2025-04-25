import re

from Bio.Seq import Seq, translate

# TRANSFORMA EM CAIXA ALTA, ELIMINA ESPAÇOS E REMOVE QUALQUER LETRA QUE NÃO CORRESPONDA A BASES NITROGENADAS DE DNA

def cleanseq(seq):
    pattern = r'[^ATCG]'
    sequence = seq.upper().replace(' ', '')
    dna = re.sub(pattern, '', sequence)
    return dna

# TRANSCREVE A SEQUÊNCIA DE DNA PARA mRNA

def transcript(sequence):
    dna = Seq(sequence)
    rna = dna.transcribe()
    return rna

# REALIZA A TRADUÇÃO EM AMINOÁCIDOS, COM POSSIBILIDADE DE PERSONALIZAÇÃO DO FRAME, OU SEJA, DA BASE INICIAL.

def translation(sequence, frame):
    polypeps = []
    stopCodons = ['UAA', 'UAG', 'UGA']
    startCodon = 'AUG'
    i = frame
    while i < (len(sequence) - 2):
        codon = sequence[i:i+3]
        if codon == startCodon:
            j = i
            while j < (len(sequence) - 2):
                nextCodon = sequence[j:j+3]
                if nextCodon in stopCodons:
                    valid = translate(sequence[i:j+3])
                    polypeps.append(valid)
                    i = j
                    break
                else:
                    j += 3
        else:
            i += 3
    return polypeps


# TRANSFORMA A LETRA CORRESPONDENTE DO AMINOÁCIDO EM SUA SIGLA DE 3 LETRAS

def aa_names(seq):
    sequences = []
    abbs = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp',
              'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly',
              'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys',
              'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser',
              'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}
    for p in seq:
        a = ''
        for aminoacid in p:
            for s in abbs.keys():
                if aminoacid == s:
                    a += f'{abbs[s]}-'
        s = a[:-1]
        sequences.append(s)
    return sequences

