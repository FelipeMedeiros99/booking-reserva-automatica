from re import findall
from PySimpleGUI import popup

def filtrar_email(informacoes):
    modelo = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = findall(modelo, informacoes)
    if len(email)<1:
        popup('Não foi possível identificar o email')
        email = ['n@n.com']

    return email
