from PySimpleGUI import Text, Window, Multiline, WINDOW_CLOSED, Button


def janela_principal(dados=''):
    
    layout = [[Text('Elementos da reserva')],
            [Multiline(dados, size=(40, 7), key='informacoes')],
            [Button('confirmar'), Button('Limpar'), Button('Fechar')]]

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
