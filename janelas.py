from PySimpleGUI import Text, Window, Multiline, Input, WINDOW_CLOSED, Button
from pyperclip import copy


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


def janela_com_os_filtros(check_in='', check_out='', nome='', numero='', voucher='', email='', dados_booking=''):
    layout = [
              [Text('Check-in:', size=(16)), Text('Check-out:'),],
              [Input(check_in, size=(12), key='check-in'), Button('Copiar', key='check-in'), 
               Input(check_out, size=(12), key='check-out'), Button('Copiar', key='check-out')],
              [Text('Nome:')],
              [Input(nome, size=(34), key='nome'), Button('Copiar', key='nome')],
              [Text('Telefone:', size=(20)), Text('Voucher:')],
              [Input(numero, size=(15),  key='telefone'), Button('Copiar', key='telefone'), 
               Input(voucher, size=(9), key='voucher'), Button('Copiar', key='voucher')],
              [Text('Email:')],
              [Input(email, size=(34), key='email'), Button('Copiar', key='email')],
              [Button('Fechar')]
              ]
    
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



if '__main__' == __name__:
    janela_principal()
    janela_com_os_filtros()
