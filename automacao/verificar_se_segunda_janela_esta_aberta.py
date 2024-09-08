from pyautogui import locateCenterOnScreen
from time import sleep, time
from PySimpleGUI import Popup

def verificar_se_segunda_janela_esta_aberta():
    while True:
        try: 
            posicao_imagem = locateCenterOnScreen('segunda_tela.png')
            if(posicao_imagem):
                break
    
        except Exception:
                pass
        finally:
            sleep(1.5)

if __name__ == "__main__":
     verificar_se_segunda_janela_esta_aberta()