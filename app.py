from flask import Flask, request, jsonify
from flask_cors import CORS
from utilities import cleanseq, transcript, translation, aa_names

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return 'OK!'


@app.route('/analyze', methods=['POST'])
def main():
    # O código abaixo verifica a presença de um arquivo ou de um texto e transforma a sequência de DNA em string.
    sequence = ''
    filesequence = request.files.get('fileseq')
    textsequence = request.form.get('textseq')
    if filesequence:
        content = filesequence.read()
        sequence = content.decode('utf-8')
    elif textsequence and len(textsequence.strip()) > 0:
        sequence = textsequence.strip()
    # ------------------------------------------------------------------------------------------ /

    # Remove os espaços e tira qualquer letra que não seja A, T, C ou G da sequência.

    dna = cleanseq(sequence)

    # ------------------------------------------------------------------------------------------ /

    # Realiza a transcrição da sequência de DNA para RNA.

    rna = transcript(dna)

    # ------------------------------------------------------------------------------------------ /

    # Fazem a tradução em aminoácidos, a depender da base inicial, e os escrevem em forma de sua sigla correspondente.

    polypeptides_frame0 = aa_names(translation(rna, frame=0))
    polypeptides_frame1 = aa_names(translation(rna, frame=1))
    polypeptides_frame2 = aa_names(translation(rna, frame=2))

    # ------------------------------------------------------------------------------------------ /

    # Retornando o arquivo .JSON contendo a análise:

    result = {"Sequûencia encontrada a partir da primeira base (5' - 3')": polypeptides_frame0,

              "Sequência encontrada a partir da segunda base (5' - 3')": polypeptides_frame1,

              "Sequência encontrada a partir da terceira base (5' - 3')": polypeptides_frame2}

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

