from re import findall
from PySimpleGUI import popup


def filtrar_numero(informacoes):
    modelo = r'\d{2} \d?\d{4} \d{4}'
    numero = findall(modelo, informacoes)
    if len(numero) == 0:
        popup('Não foi possível localizar o telefone')
        numero = ['99 99999 9999']

    return numero
