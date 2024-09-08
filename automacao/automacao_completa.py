from automacao.verificar_se_janela_esta_aberta import verificar_se_janela_esta_aberta
from automacao.selecionar_faturamento import selecionar_faturamento
from automacao.selecionar_opcoes_cabecalho import selecionar_opcoes_cabecalho

def automacao_completa():
    try:
        verificar_se_janela_esta_aberta()
        selecionar_faturamento()
        selecionar_opcoes_cabecalho()
        

    
    except:
        pass


if __name__ == "__main__":
    pass