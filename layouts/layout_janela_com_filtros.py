from PySimpleGUI import Text, Input, Button

def layout_janela_com_filtros(dados):
    check_in = dados['checkin']
    check_out = dados['checkout']
    nome = dados['nome']
    voucher = dados['voucher']
    email = dados['email']
    telefone = dados['telefone']

    layout = [
                [Text('Check-in:', size=(10)), Text('Check-out:'),],
                [Input(check_in, size=(13), key='check-in'), 
                Input(check_out, size=(13), key='check-out')],
                [Text('Nome:')],
                [Input(nome, size=(28), key='nome')],
                [Text('Telefone:', size=(13)), Text('Voucher:')],
                [Input(telefone, size=(15),  key='telefone'), 
                Input(voucher, size=(11), key='voucher')],
                [Text('Email:')],
                [Input(email, size=(28), key='email')],
                [Button("Reservar"), Button('Fechar')]
                ]
    
    return layout