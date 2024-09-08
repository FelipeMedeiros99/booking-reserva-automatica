from PySimpleGUI import Text, Window, Multiline, WINDOW_CLOSED, Button

# modulos internos
from layouts.layout_janela_principal import layout_janela_principal
from ferramentas.organizar_filtros_em_objeto import organizar_filtros_em_objeto



def janela_principal(dados=''):
    
    layout = layout_janela_principal(dados)
    janela = Window("Automação booking", layout)

    while True:
        botoes, dados = janela.read()

        if botoes == WINDOW_CLOSED or botoes == 'Fechar':
            raise 
        
        elif botoes == 'Limpar':
            janela['informacoes'].update('')

        if botoes == 'confirmar':

            dados_organizados = organizar_filtros_em_objeto(dados["informacoes"])
            
            janela.close()
            
            return dados_organizados
