import re
from Bio.Seq import Seq


# O nome das funções abaixo são inspirados em estruturas/enzimas reais, por realizarem ações >PARECIDAS< ou iguais às
# delas.

def spliceossome(sequence=''):
    pattern = r'[^ATGC]'
    remspaces = sequence.replace(' ', '').upper()
    cleansequence = re.sub(pattern, '', remspaces)
    return cleansequence


def rnaPolymerase(sequence):
    seq = Seq(sequence)
    rnaseq = seq.transcribe()
    rna = ''
    for l in rnaseq:
        rna += l
    return rna


def ribossome(mrna):
    chains = []
    stopcodons = ['UAA', 'UAG', 'UGA']
    i = 0
    for item in range(i, len(mrna) - 2, 3):
        codon = mrna[item:item+3]
        if codon == 'AUG':
            for p in range(item, len(mrna) - 2, 3):
                nxtcodon = mrna[p: p+3]
                if nxtcodon in stopcodons:
                    c = mrna[item:p+3]
                    polypep = Seq(c)
                    aa = polypep.translate()
                    chains.append(str(aa))
                    break
    return chains

# A função abaixo transforma as letras em siglas de 3 letras para os aminoácidos. --------------------------------- //

def analyze(aminoacids):
    abbs = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp',
              'C': 'Cys', 'E': 'Glu', 'Q': 'Gln', 'G': 'Gly',
              'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys',
              'M': 'Met', 'F': 'Phe', 'P': 'Pro', 'S': 'Ser',
              'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}
    aa_seq = []
    for i in aminoacids:
        s = ''
        for p in i:
            for a in abbs.keys():
                if a == p:
                    s += f'{abbs[a]}-'
        sequence = s[:-1]
        sequence += '*'
        aa_seq.append(sequence)
    return aa_seq


def aa_lens(sequence):
    counts = {}
    sum = 0
    for pos, a in enumerate(sequence):
        sum += len(a) - 1 # Retira os códons de parada da contagem total
        counts[f'Seq{pos}'] = f'{len(a) - 1} aminoácidos'
    counts['Aminoácidos_totais'] = sum
    return counts



    


