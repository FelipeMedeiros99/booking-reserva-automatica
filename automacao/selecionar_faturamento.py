from pyautogui import hotkey, press, click
from time import sleep

def selecionar_faturamento():
    
    dropdown_faturamento = (274, 205)
    tipo_empresa = (291, 244)

    # navegar até o dropdown
    click(dropdown_faturamento)
    # seleciona opcão empresa
    click(tipo_empresa)
    # confirma
    press("enter")


if __name__ == "__main__":
    sleep(3)
    selecionar_faturamento()

