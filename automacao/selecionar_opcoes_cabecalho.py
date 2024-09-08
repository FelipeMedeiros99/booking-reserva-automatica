from pyautogui import press, write
from time import sleep

def selecionar_opcoes_cabecalho():
    # selecionando a empresa
    write('3')
    press('tab', 3, 0.2)
    # seleciona o tipo
    write('3')
    press('tab')
    # seleciona o portal
    write("2")
    press("enter")


if __name__=="__main__":
    sleep(2)
    selecionar_opcoes_cabecalho()