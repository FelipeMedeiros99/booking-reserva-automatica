def ler_arquivo():
    nome_arquivo = "informacoes.txt"
    texto= ''
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()

    return texto


if __name__ == "__main__":
    print(ler_arquivo())