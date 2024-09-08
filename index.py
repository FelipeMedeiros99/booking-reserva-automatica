# modulos internos 
from janelas.janela_principal import janela_principal
from janelas.janela_com_os_filtros import janela_com_os_filtros
from manipulacao_arquivos.criar_arquivo_se_nao_existir import criar_arquivo_se_nao_existir
from manipulacao_arquivos.ler_arquivo import ler_arquivo

if __name__ == "__main__":
    # criando arquivo para armazenar dados
    criar_arquivo_se_nao_existir()

    while True:
        try:
            dados_filtrados = janela_principal(ler_arquivo())
            janela_com_os_filtros(dados_filtrados)
        
        except Exception as err:
            print(err)
            break
        
    # pyinstaller --onefile --windowed --icon=booking.ico index.py