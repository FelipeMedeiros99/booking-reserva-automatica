from PySimpleGUI import Text, Multiline, Button


def layout_janela_principal(dados):
    layout = [
            [Text('Elementos da reserva')],
            [Multiline(dados, size=(40, 7), key='informacoes')],
            [Button('confirmar'), Button('Limpar'), Button('Fechar')]
            ]
    
    return layout