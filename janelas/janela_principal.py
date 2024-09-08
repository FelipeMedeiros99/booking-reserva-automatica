from PySimpleGUI import Text, Window, Multiline, WINDOW_CLOSED, Button
from layouts.layout_janela_principal import layout_janela_principal

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
            janela.close()
            return dados['informacoes']
