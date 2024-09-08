from PySimpleGUI import Text, Input, Button

def layout_janela_com_filtros(check_in='', check_out='', nome='', numero='', voucher='', email=''):
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
    
    return layout