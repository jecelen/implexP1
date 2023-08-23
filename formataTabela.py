import numpy as np

def calculaMedias(insertion, heap, dados):
    dados.append(insertion/10)
    dados.append(heap/10)
    return dados

def gerarCabecalho():
    colunas = {'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12, 'col8': 12}
    formatarTabelaOutput(colunas)


def geraVetor(n):
    np.random.seed()
    return np.random.randint(0, 20000, n)

def formatarTabelaOutput(colunas):
    #cabecalho = ["n", "Insertion", "Merge", "Heap", "Quick", "Counting"]
    cabecalho = '{:>{col1}} {:^{col2}} {:^{col3}} {:^{col4}} {:^{col5}} {:^{col6}} {:^{col7}} {:^{col8}}'
    print(cabecalho.format('n', ' ', 'Selection', 'Insertion', 'Merge', 'Heap', 'Quick', 'Counting', **colunas))
    print("----------------------------------------------------------------------------------------------")

def saida(dados, colunas):
    formato = '{:>{col1}} {:^{col2}} {:^{col3}} {:^{col4}.6f} {:^{col5}} {:^{col6}.6f} {:^{col7}}'
    print(formato.format(dados[0], ' ', 'fazer', dados[1], 'fazer', dados[2], 'fazer', **colunas))


def table(dados):
    colunas = {'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12}
    saida(dados, colunas)

