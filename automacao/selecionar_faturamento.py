from pyautogui import press, click

def selecionar_faturamento():
    
    dropdown_faturamento = (274, 205)
    tipo_empresa = (291, 244)

    # navegar até o dropdown
    click(dropdown_faturamento, interval=0.2)
    # seleciona opcão empresa
    click(tipo_empresa, interval=0.2)
    # confirma
    press("enter", interval=0.2)




