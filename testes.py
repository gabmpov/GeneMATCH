from Bio.Seq import Seq, translate


def traduzir(sequencia):
    cadeias = []
    stopCodons = ['UAA', 'UAG', 'UGA']
    i = 0
    while i < (len(sequencia) - 2):
        codon = sequencia[i:i + 3]
        if codon == 'AUG':
            for j in range(i, (len(sequencia) - 2), 3):
                prox = sequencia[j:j + 3]
                if prox in stopCodons:
                    valido = translate(sequencia[i:j + 3])
                    cadeias.append(valido)
                    i = j + 3
                    break
        i += 3
    return cadeias


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

print(aa_names(traduzir('AUGCGGAUUCGACUUGCAUGAGUUAUGGAAGGCGAGUGACUUCGAUAAGGCUACAUUGAGAAACGGCUAGUGAAGGCUGA')))





