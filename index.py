# janelas 
from janelas.janela_principal import janela_principal
from janelas.janela_com_os_filtros import janela_com_os_filtros


if __name__ == "__main__":
    informacoes_booking = ''
    while True:
        try:
            informacoes_booking = janela_principal(informacoes_booking)
            janela_com_os_filtros(informacoes_booking)
        
        except Exception as err:
            print(err)
            break