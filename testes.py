from Bio.Seq import Seq, translate


def traduzir(sequence):
    polypeps = []
    stopCodons = ['UAA', 'UAG', 'UGA']
    i = 0
    for item in range(i, len(sequence) - 2, 3):
        codon = sequence[item:item+3]
        if codon == 'AUG': # achou o códon de início.
            for nextt in range(item, len(sequence) - 2, 3):
                proximocodon = sequence[nextt:nextt+3]
                if proximocodon in stopCodons:
                    traduzido = translate(sequence[item:nextt+3])
                    polypeps.append(traduzido)
                    break
    return polypeps


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

print(traduzir('AUGCGGAUUCGACUUGCAUGAGUUAUGGAAGGCGAGUGACUUCGAUAAGGCUACAUUGAGAAACGGCUAGUGAAGGCUGA'))





