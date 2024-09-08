# modulos externos
from PySimpleGUI import  Window, WINDOW_CLOSED
from pyperclip import copy

# modulos internos
from layouts.layout_janela_com_filtros import layout_janela_com_filtros



def janela_com_os_filtros(dados):

    # layout da janela secundário
    layout = layout_janela_com_filtros(dados)

    janela = Window('Copiar informações', layout)

    while True:
        botoes, dados = janela.read()

        if botoes == WINDOW_CLOSED or botoes == 'Fechar':
            janela.close()
            break

        if botoes == 'Reservar': 
            janela.close()
            
            print("partiu")
