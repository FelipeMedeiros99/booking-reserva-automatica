from pyautogui import locateCenterOnScreen
from time import sleep, time
from PySimpleGUI import Popup

def verificar_se_janela_esta_aberta():
    tempo_inicio = time()
    while True:
        try: 
            posicao_imagem = locateCenterOnScreen('tela_cadastro.png')
            if(posicao_imagem):
                print('imagem achada')
                break
    
        except Exception:
            if(time() - tempo_inicio > 5):
                Popup("Tela de cadastro não encontrada")
                raise

        finally:
            sleep(1)

if __name__ == "__main__":
    verificar_se_janela_esta_aberta()