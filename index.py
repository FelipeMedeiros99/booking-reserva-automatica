# janelas 
from janelas.janela_principal import janela_principal
from janelas.janela_com_os_filtros import janela_com_os_filtros


if __name__ == "__main__":
    while True:
        try:
            dados_filtrados = janela_principal(dados_filtrados)
            janela_com_os_filtros(dados_filtrados)

        except Exception as err:
            print(err)
            break
        