from pyautogui import press, write
from time import sleep

def selecionar_opcoes_cabecalho():
    # selecionando a empresa
    write('3', interval=0.2)
    press('tab', 3, 0.2)
    # seleciona o tipo
    write('3', interval=0.2)
    press('tab', interval=0.2)
    # seleciona o portal
    write("2", interval=0.2)
    press("enter", interval=0.2)
