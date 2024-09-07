from re import findall
from PySimpleGUI import popup


def filtrar_voucher(informacoes):
    modelo = r'\d{10}'
    voucher = findall(modelo, informacoes)
    if len(voucher)<1:
        popup('Não foi possível identificar o voucher')
        voucher = ['0']
    return voucher
