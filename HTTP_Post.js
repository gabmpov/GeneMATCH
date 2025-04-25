document.addEventListener("DOMContentLoaded", function() {

    const button = document.getElementById('analisebutton');
    button.addEventListener('click', function (event) {
        event.preventDefault();

        const resultarea = document.getElementById('result');
        resultarea.innerHTML = '';

        const textdna = document.getElementById('text').value.trim();
        const fastafile = document.getElementById('fileinput').files[0];

        // Criar o formdata para o envio por HTTP
        const submission = new FormData();

        // Dar prioridade ao arquivo FASTA
        if (fastafile) {
            submission.append('fileseq', fastafile);
            console.log('Enviando arquivo...');
        } else if (textdna !== '') {
            submission.append('textseq', textdna);
            console.log('Enviando texto...');
        } else {
            alert('Por favor, preencha um dos campos.');
            return;
        }

        // Tenta enviar a sequência de DNA para o backend
        try {
            fetch('http://127.0.0.1:5000/analyze', {
                method: 'POST',
                body: submission,
            })
            .then(response => response.json()) // Converte a resposta para JSON
            .then(results => {
                console.log('Resposta do servidor:', results);

                const resultarea = document.getElementById('result');
                resultarea.innerHTML = JSON.stringify(results, null, 2); // Exibe a resposta na tela

                // Botão de download
                const downloadbutton = document.getElementById('download');
                downloadbutton.addEventListener("click", function() {

                    // Cria o Blob com os resultados da análise em formato JSON
                    const blob = new Blob([JSON.stringify(results, null, 2)], { type: 'application/json' });

                    // Cria um link de download
                    const link = document.createElement('a');
                    link.href = URL.createObjectURL(blob);  // Cria um URL para o Blob
                    link.download = 'analise.json';  // Nome do arquivo a ser baixado
                    link.click();  // Dispara o download
                });
            })
            .catch(error => {
                console.error('Erro na requisição fetch:', error);
            });
        }
        catch (error) {
            console.error('Erro no envio de dados:', error);
            alert('Ocorreu um erro ao tentar enviar os dados. Tente novamente.');
        }
    });
});
