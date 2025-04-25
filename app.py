from flask import Flask, request, jsonify
from flask_cors import CORS
from utilities import cleanseq, transcript, translation, splitpolypeps

app = Flask(__name__)
CORS(app)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
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
        string = content.decode('utf-8')
        for l in string.splitlines():
            line = l
            if line[0] == '>':
                continue
            sequence += line
        print(sequence)
    elif textsequence and len(textsequence.strip()) > 0:
        sequence = textsequence.strip()
    # ------------------------------------------------------------------------------------------ /

    # Remove os espaços e tira qualquer letra que não seja A, T, C ou G da sequência.

    dna = cleanseq(sequence)

    # ------------------------------------------------------------------------------------------ /

    # Realiza a transcrição da sequência de DNA para RNA.

    rna = transcript(dna)

    # ------------------------------------------------------------------------------------------ /

    # Fazem a tradução em aminoácidos, a depender da base inicial

    polypeptides_frame0 = translation(splitpolypeps(rna, frame=0))

    # ------------------------------------------------------------------------------------------ /

    # Retornando o arquivo .JSON contendo a análise:

    if not polypeptides_frame0:
        result = {"Sequências encontradas": 'Nenhuma sequência encontrada...'}
    else:
        result = {'Sequencias encontradas': polypeptides_frame0,
                  'Número de aminoácidos': polypeptides_frame0.count('-') - 1}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

