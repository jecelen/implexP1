
def gerarCabecalho():
    colunas = {'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12, 'col8': 12}
    formatarTabelaOutput(colunas)


def formatarTabelaOutput(colunas):
    cabecalho = '{:>{col1}} {:^{col2}} {:^{col3}} {:^{col4}} {:^{col5}} {:^{col6}} {:^{col7}} {:^{col8}}'
    print(cabecalho.format('n', ' ', 'Selection', 'Insertion', 'Merge', 'Heap', 'Quick', 'Counting', **colunas))
    print("----------------------------------------------------------------------------------------------")


def saida(dados, colunas):
    formato = '{:>{col1}} {:^{col2}} {:^{col3}.6f} {:^{col4}.6f} {:^{col5}.6f} {:^{col6}.6f} {:^{col7}.6f} {:^{col8}.6f}'
    print(formato.format(dados[0], ' ', dados[4], dados[1], dados[3], dados[2], dados[6], dados[5], **colunas))


def table(dados):
    colunas = {'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12, 'col8' : 12}
    saida(dados, colunas)

