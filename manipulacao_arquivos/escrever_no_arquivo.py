def escrever_no_arquivo(texto):
    nome_arquivo = "informacoes.txt"
    with open(nome_arquivo, 'w+') as arquivo:
        arquivo.write(texto)