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

# TRADUZ E SEPARA AS SEQUENCIAS DE POLIPEPTÍDEOS COM BASE NOS CÓDONS DE PARADA E INICIO,
# COM POSSIBILIDADE DE PERSONALIZAÇÃO DO FRAME, OU SEJA, DA BASE INICIAL.

def splitpolypeps(sequence, frame):
    polypeps = []
    stopCodons = ['UAA', 'UAG', 'UGA']
    i = frame
    for item in range(i, len(sequence) - 2, 4):
        codon = sequence[item:item+3]
        if codon == 'AUG': # achou o códon de início.
            for nextt in range(item, len(sequence) - 2, 4):
                proximocodon = sequence[nextt:nextt+3]
                if proximocodon in stopCodons:
                    traduzido = translate(sequence[item:nextt+3])
                    polypeps.append(traduzido)
                    break
    return polypeps


# TRANSFORMA A LETRA CORRESPONDENTE DO AMINOÁCIDO EM SUA SIGLA DE 3 LETRAS

def translation(list):
    sequences = []
    abbs = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp',
              'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly',
              'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys',
              'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser',
              'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}
    for p in list:
        a = ''
        for aminoacid in p:
            for s in abbs.keys():
                if aminoacid == s:
                    a += f'{abbs[s]}-'
        s = a[:-1]
        sequences.append(s)
    return sequences

