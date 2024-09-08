from PySimpleGUI import Window, WINDOW_CLOSED

# modulos internos
from layouts.layout_janela_principal import layout_janela_principal
from ferramentas.organizar_filtros_em_objeto import organizar_filtros_em_objeto
from manipulacao_arquivos.limpar_arquivo import limpar_arquivo
from manipulacao_arquivos.ler_arquivo import ler_arquivo
from manipulacao_arquivos.escrever_no_arquivo import escrever_no_arquivo


def janela_principal(dados):
    
    layout = layout_janela_principal(dados)
    janela = Window("Automação booking", layout)
    
    while True:
        botoes, dados = janela.read()
        
        escrever_no_arquivo(dados['informacoes'])

        if botoes == WINDOW_CLOSED or botoes == 'Fechar':
            raise 
        
        elif botoes == 'Limpar':
            limpar_arquivo()
            janela['informacoes'].update(ler_arquivo())

        if botoes == 'confirmar':
            print(dados)
            dados_organizados = organizar_filtros_em_objeto(dados["informacoes"])
            janela.close()

            return dados_organizados
