from pyautogui import  press, write, click, hotkey

def preencher_dados_da_segunda_janela(dados):
    
    caixa_de_email = (426, 314)
    
    click(caixa_de_email, interval=0.2)
    hotkey('ctrl', 'a')
    write(dados['email'])

    press("tab", interval=0.2)
    write(dados['telefone'])

    press("tab", presses=2, interval=0.2)
    write(dados['telefone'])

    press("tab", interval=0.2)
    write(dados['voucher'])

    press("tab", interval=0.2)
    write("booking")


if __name__ == "__main__":
    pass