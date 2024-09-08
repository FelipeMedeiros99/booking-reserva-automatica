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

