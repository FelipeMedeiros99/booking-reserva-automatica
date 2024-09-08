from pyautogui import click, write, press
from time import sleep

def preencher_nome(nome):
    adicionar_hospede = (1090, 344)
    botao_ok = (589, 555)
    click(adicionar_hospede, interval=0.2)
    write(nome)
    click(botao_ok, interval=0.2)
    press('esc', interval=0.2)
    