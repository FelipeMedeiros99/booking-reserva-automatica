from filtros.filtrar_data import filtrar_data
from filtros.filtrar_email import filtrar_email
from filtros.filtrar_nome import filtrar_nome
from filtros.filtrar_numero import filtrar_numero
from filtros.filtrar_voucher import filtrar_voucher


def organizar_filtros_em_objeto(dados):
    datas = filtrar_data(dados)
    nome = filtrar_nome(dados)[0]
    voucher = filtrar_voucher(dados)[0]
    email = filtrar_email(dados)[0]
    telefone = filtrar_numero(dados)[0]

    # criando um objeto
    dados_filtrados = {
        "checkin": datas[0],
        "checkout": datas[1],
        "nome": nome,
        "voucher": voucher,
        "email": email,
        "telefone": telefone
    }

    return dados_filtrados