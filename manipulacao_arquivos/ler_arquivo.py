def ler_arquivo():
    nome_arquivo = "informacoes.txt"
    texto= ''
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.readlines()

    return texto