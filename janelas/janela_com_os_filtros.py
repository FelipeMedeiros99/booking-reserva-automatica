# modulos externos
from PySimpleGUI import  Window, WINDOW_CLOSED
from pyperclip import copy

# modulos internos
from layouts.layout_janela_com_filtros import layout_janela_com_filtros
from filtros.filtrar_data import filtrar_data
from filtros.filtrar_email import filtrar_email
from filtros.filtrar_nome import filtrar_nome
from filtros.filtrar_numero import filtrar_numero
from filtros.filtrar_voucher import filtrar_voucher


def janela_com_os_filtros(dados=""):

    # filtrando dados
    datas = filtrar_data(dados)
    checkin = datas[0]
    checkout = datas[1]
    nome = filtrar_nome(dados)[0]
    voucher = filtrar_voucher(dados)[0]
    email = filtrar_email(dados)[0]
    telefone = filtrar_numero(dados)[0]

    # layout da janela secundário
    layout = layout_janela_com_filtros(checkin, checkout, nome, telefone, voucher, email)

    janela = Window('Copiar informações', layout)

    while True:
        botoes, dados = janela.read()

        if botoes == WINDOW_CLOSED or botoes == 'Fechar':
            janela.close()
            break

        

        elif botoes == 'check-in0':
            copy(dados['check-in'])

        elif botoes == 'check-out1':
            copy(dados['check-out'])

        elif botoes == 'nome2':
            copy(dados['nome'])
            
        elif botoes == 'telefone3':
            copy(dados['telefone'])

        elif botoes == 'voucher4':
            copy(dados['voucher'])

        elif botoes == 'email5':
            copy(dados['email'])
