from PySimpleGUI import popup

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
    
