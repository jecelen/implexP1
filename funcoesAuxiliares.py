import numpy as np

def calculaMedias(insertion, heap, merge, selec, dados):
    dados.append(insertion/10)
    dados.append(heap/10)
    dados.append(merge/10)
    dados.append(selec/10)
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
    formato = '{:>{col1}} {:^{col2}} {:^{col3}.6f} {:^{col4}.6f} {:^{col5}.6f} {:^{col6}.6f} {:^{col7}}'
    print(formato.format(dados[0], ' ', dados[4], dados[1], dados[3], dados[2], 'fazer', **colunas))


def table(dados):
    colunas = {'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12}
    saida(dados, colunas)


def media(tempo):   #acho que essa função nao está sendo usada
    return tempo/10

