import pandas as pd

from comunes.model.automata import Automata
from comunes.model.input import Input
from comunes.model.recognize_row import RecognizeRow
from comunes.model.state import State
from comunes.model.step import Step
from comunes.model.transicion import Transicion


def get_automata(df: pd.DataFrame) -> Automata:

    states = []
    for state in list(df.head().index):
        states.append(State(state, df['R'][state] == '1'))

    inputs = list(df.columns[:-1])

    transicions = []

    for row in df.index:
        ins = []
        for column in df.columns[:-1]:
            ins.append(Input(column, df[column][row]))
        transicions.append(Transicion(row, ins))

    return Automata(0, states, inputs, transicions)


def get_dataFrame_from_automata(automata: object) -> pd.DataFrame:
    states = list(map(lambda x: x['name'], automata['states']))
    acceptances = list(
        map(lambda x: "1" if x['acceptance'] else "0", automata['states']))
    df = pd.DataFrame(columns=automata['inputs'], index=states)
    df['R'] = acceptances

    for transicion in automata['transicions']:
        for input in transicion['inputs']:
            df[input['value']][transicion['state']] = input['to']

    return df


def get_estado_inicial(df: pd.DataFrame, estado_inicial: str = "") -> str:
    if estado_inicial == "":
        return df.index[0]
    else:
        for l in df.index.to_list():
            if estado_inicial in l:
                return l


def get_serie(estado: str, dataFrame: pd.DataFrame) -> pd.Series:
    if estado in dataFrame.index:
        lista = dataFrame.loc[estado].to_list()
    else:
        estados_spl = estado.split(",")
        lista = []
        for input in dataFrame.columns[:-1]:
            valores = []
            r = '0'
            for est_spl in estados_spl:
                if not est_spl in valores:
                    new_v = dataFrame[input][est_spl]
                    if not new_v in valores:
                        valores.append(new_v)
                if dataFrame['R'][est_spl] == '1':
                    r = '1'
            valor = ",".join(valores)
            lista.append(valor)
        lista.append(r)
    return pd.Series(lista, index=dataFrame.columns, name=estado)


def hacer_deterministico_eliminar_extranos(dataFrame: pd.DataFrame) -> pd.DataFrame:
    estado_inicial = get_estado_inicial(dataFrame)
    estados = [estado_inicial]
    dataFrame1 = pd.DataFrame(columns=dataFrame.columns)
    while(len(estados) > 0):
        estado = estados.pop(0)
        a_series = get_serie(estado, dataFrame)
        dataFrame1 = dataFrame1.append(a_series)
        for n_estado in a_series[:-1]:
            if not n_estado in dataFrame1.index and not n_estado in estados:
                estados.append(n_estado)
    df = dataFrame1.applymap(limpiar)
    indexes = dataFrame1.index.tolist()
    new_indexes = [x.replace(',', '') for x in indexes]
    df = df.set_axis(new_indexes, axis='index')
    return df


def limpiar(x: str):
    return x.replace(',', '')


def agrupar_semejantes(dataFrame: pd.DataFrame) -> pd.DataFrame:
    grs = []
    groups = dataFrame.groupby(dataFrame.R)
    grs.append(groups.get_group("0"))
    grs.append(groups.get_group("1"))

    particiones = [[], []]

    for index, row in dataFrame.iterrows():
        if row["R"] == "0":
            particiones[0].append(index)
        else:
            particiones[1].append(index)

    finalizado = False
    while(not finalizado):
        division = dividir(particiones, dataFrame)
        finalizado = division[0]
        particiones = division[1]
    return get_min_DF(particiones, dataFrame)


def dividir(particiones: list[list], dataFrame: pd.DataFrame) -> tuple[bool, list[list]]:
    h = 0
    while h < len(particiones):
        particion = particiones[h]
        for c in dataFrame.columns[:-1]:
            dataFrameP = pd.DataFrame(columns=["estado", "valor", "particion"])
            vals = set()
            for estado in particion:
                valor = dataFrame.loc[estado, c]
                for i in range(0, len(particiones)):
                    if valor in particiones[i]:
                        a_series = pd.Series(
                            [estado, valor, i], index=dataFrameP.columns)
                        dataFrameP = dataFrameP.append(
                            a_series, ignore_index=True)
                        vals.add(i)
                dividir = len(vals) > 1
            if dividir:
                particiones.remove(particion)
                groups = dataFrameP.groupby(dataFrameP.particion)
                for r in vals:
                    g = groups.get_group(r)
                    gl = g.loc[:, "estado"].to_list()
                    particiones.append(gl)
                particion = particiones[0]
                return (False, particiones)
        h = h + 1
    return (True, particiones)


def get_min_DF(particiones: list[list], dataFrame: pd.DataFrame) -> pd.DataFrame:
    dataFrameF = pd.DataFrame(columns=dataFrame.columns)
    for p in particiones:
        estado = p[0]
        valores = dataFrame.loc[estado].to_list()
        lista_v = []
        for valor in valores[:-1]:
            new_estado = "".join(p)[0:3]
            for p2 in particiones:
                if valor in p2:
                    lista_v.append("".join(p2)[0:3])
        lista_v.append(valores[-1:][0])
        a_series = pd.Series(lista_v, index=dataFrame.columns, name=new_estado)
        dataFrameF = dataFrameF.append(a_series, ignore_index=False)
    return dataFrameF


def validar(df: pd.DataFrame, expresion: str) -> RecognizeRow:
    oldState = get_estado_inicial(df)
    steps = []

    for l in expresion:
        newState = df.loc[oldState, l]
        print(f"{oldState} => {l} => {newState}")
        step = Step(oldState, newState, l)
        steps.append(step)
        oldState = newState

    accepted = df.loc[oldState, "R"] == "1"
    return RecognizeRow(accepted, steps)
