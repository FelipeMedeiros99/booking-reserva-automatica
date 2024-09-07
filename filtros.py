from re import findall
from PySimpleGUI import popup

def ajustar_data(datas):
    datas_ajustadas = []
    meses = ['jan.', 'fev.', 'mar.', 'abr.', 'mai.', 'jun.', 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.']
    num = [c for c in range(1, 13)]

    for data in datas:
        data_temporaria = []
        data_extensa = data.split()
        if len(data_extensa[0]) == 1:
            data_temporaria.append(f'0{data_extensa[0]}')
        else:
            data_temporaria.append(str(data_extensa[0]))


        for c in range(12):
            if meses[c] == data_extensa[2]:
                if len(str(num[c])) == 1:
                    data_temporaria.append(f'0{num[c]}')
                else:
                    data_temporaria.append(str(num[c]))

        data_temporaria.append(str(data_extensa[-1]))
        datas_ajustadas.append('/'.join(data_temporaria))

    return datas_ajustadas


def filtrar_data(informacoes):
    padrao = r"\d?\d? de \w{3}\. de \d{4}"

    data = findall(padrao, informacoes)

    if len(data)<2:
        popup("Não foi possível identificar as datas")
        data = ['0', '0', '0']
        return data

    return ajustar_data(data)


def filtrar_nome(informacoes):
    todas_palavras = ['Check-in', 'Check-out', 'Duração da estadia:', 'Total de hóspedes:', 'Total de unidades:', 'Preço total', 'Nome do hóspede:', 'br', 'Mostrar o telefone', 'Idioma de preferência', 'Português (Brasil)', 'Canal:', 'Booking.com', 'Código IATA/TIDS:', 'PC029090', 'Número da reserva:', '2606351492', 'Valor comissionável:', 'Recebida', 'Comissão:', 'R$ 64', 'Observações (uso interno) Editar', 'Informações importantes sobre este hóspede', 'BED PREFERENCE:Standard  Double Room: 1 de casal', 'Horário previsto de chegada']
    
    lista_de_dados = []

    informacoes = informacoes.split('\n')

    for dados in informacoes:
        if len(dados)>0:
            lista_de_dados.append(dados.strip())

    nome = []
    for informacao in lista_de_dados:
        if not informacao in todas_palavras:
            somente_letra = True
            for letra in informacao:
                if letra.isnumeric():
                    somente_letra = False
            if somente_letra:
                nome.append(informacao)
        # nome.append(informacao)

    if len(nome)<1:
        popup('Não foi possivel identificar o nome')
        nome = ['none']

    return nome
    

def filtrar_voucher(informacoes):
    modelo = r'\d{10}'
    voucher = findall(modelo, informacoes)
    if len(voucher)<1:
        popup('Não foi possível identificar o voucher')
        voucher = ['0']
    return voucher


def filtrar_email(informacoes):
    modelo = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email = findall(modelo, informacoes)
    if len(email)<1:
        popup('Não foi possível identificar o email')
        email = ['n@n.com']

    return email


def filtrar_numero(informacoes):
    modelo = r'\d{2} \d?\d{4} \d{4}'
    numero = findall(modelo, informacoes)
    if len(numero) == 0:
        popup('Não foi possível localizar o telefone')
        numero = ['99 99999 9999']

    return numero


if __name__ == "__main__":

    texto = '''Check-in

ter., 19 de dez. de 2023

Check-out

qua., 20 de dez. de 2023

Duração da estadia:

1 diária

Total de hóspedes:

2

Total de unidades:

1

Preço total

R$ 245
Nome do hóspede:

Helem Mesquita Castro Serra
 br
hserra.214256@guest.booking.com
Mostrar o telefone
Idioma de preferência

Português (Brasil)

Canal:

Booking.com

Código IATA/TIDS:

PC029090

Número da reserva:

4040953413

Valor comissionável:

R$ 245

Recebida

seg., 18 de dez. de 2023

Comissão:

R$ 39,20
Observações (uso interno) Editar

22331

Informações importantes sobre este hóspede

BED PREFERENCE:Standard  Double Room: 1 double'''


    print(filtrar_nome(texto))
    # filtrar_voucher(texto)

