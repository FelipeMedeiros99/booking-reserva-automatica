from os.path import exists

def criar_arquivo_se_nao_existir():
    nome_arquivo = "informacoes.txt"
    arquivo_existe = exists(nome_arquivo)

    if not arquivo_existe:
        with open(nome_arquivo, '+w') as arquivo:
            pass
