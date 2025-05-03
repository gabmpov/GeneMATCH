import json
from flask import Flask, request, Response
from flask_cors import CORS
from utilities import spliceossome, rnaPolymerase, ribossome, analyze, aa_lens

app = Flask(__name__)
CORS(app)


app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
@app.route('/')
def home():
    return 'OK!'


@app.route('/analyze', methods=['POST'])
def main():
    sequence = ''
    filesequence = request.files.get('fileseq')
    textsequence = request.form.get('textseq')

    # DAR PRIORIDADE AO ARQUIVO EM CASO DE ENVIO DE TEXTO E ARQUIVO ------------------------------------------------//

    if filesequence:
        content = filesequence.read()
        filestring = content.decode('utf-8')

        for l in filestring.splitlines():
            if l[0] == '>':
                continue
            sequence += l

    elif textsequence and len(textsequence) > 0:
        sequence = textsequence

    # ---------------------------------------------------------------------------------------------------------------//

    # CHAMADA DE FUNÇÕES PARA TRATAR A STRING

    clean = spliceossome(sequence) # --> Funciona!
    rna = rnaPolymerase(clean)     # --> Funciona!
    transl = ribossome(rna)        # --> Funciona!
    aminoacids = analyze(transl)   # --> Funciona!

    # CHAMADA DE FUNÇÕES PARA ANÁLISES EXTRAS

    counts = aa_lens(transl)       # --> Funciona!

    response = {
        'Tradução': transl,
        'Aminoácidos formados': aminoacids,
        'Contagem de aminoácidos': counts,
        'Observação': 'São ignorados quaisquer caracteres que não codifiquem nenhuma base nitrogenada, isto é, quaisuqer'
                      'caracteres diferentes de A (Adenina), T (Timina), C (Citosina) ou G (Guanina).',
    }

    return Response(json.dumps(response, indent=2), mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True)

