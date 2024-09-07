
from janelas import janela_principal, janela_com_os_filtros
from filtros import filtrar_data, filtrar_nome, filtrar_voucher, filtrar_email, filtrar_numero

if __name__ == "__main__":
    informacoes_booking = ''
    while True:

        try:
            informacoes_booking = janela_principal(informacoes_booking)
            
            datas = filtrar_data(informacoes_booking)
            nome = filtrar_nome(informacoes_booking)
            voucher = filtrar_voucher(informacoes_booking)
            email = filtrar_email(informacoes_booking)
            telefone = filtrar_numero(informacoes_booking)

            janela_com_os_filtros(check_in=datas[0], check_out=datas[1], nome=nome[0], numero=telefone[0], voucher=voucher[0], email=email[0], dados_booking=informacoes_booking)
        
        except Exception as err:
            break