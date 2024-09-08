from pyautogui import  press, write

def preencher_datas(dados):
    # preenchendo datas da reserva
    write(dados["check-in"].replace("/",""))
    press('tab', interval=0.2)
    write(dados['check-out'].replace("/", ""))



if __name__ == "__main__":
    pass