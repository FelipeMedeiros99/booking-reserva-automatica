from PySimpleGUI import Popup
from automacao.verificar_se_janela_esta_aberta import verificar_se_janela_esta_aberta
from automacao.selecionar_faturamento import selecionar_faturamento
from automacao.selecionar_opcoes_cabecalho import selecionar_opcoes_cabecalho
from automacao.preencher_datas import preencher_datas
from automacao.preencher_nome import preencher_nome
from automacao.preencher_dados_da_segunda_janela import preencher_dados_da_segunda_janela
from automacao.verificar_se_segunda_janela_esta_aberta import verificar_se_segunda_janela_esta_aberta
from time import sleep


"""
{
    'check-in': '07/09/2024', 
    'check-out': '08/09/2024', 
    'nome': 'Lourival Pereira Araujo Filho', 
    'telefone': '98 99134 1964', 
    'voucher': '4467161846', 
    'email': 'lfilho.377882@guest.booking.com'}
"""


def automacao_completa(dados):
    try:
        verificar_se_janela_esta_aberta()
        selecionar_faturamento()
        selecionar_opcoes_cabecalho()
        preencher_datas(dados)
        preencher_nome(dados["nome"])
        verificar_se_segunda_janela_esta_aberta()
        preencher_dados_da_segunda_janela(dados)
    except:
        pass


if __name__ == "__main__":
    sleep(3)
    automacao_completa()