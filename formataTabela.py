def formatarTabelaOutput(colunas):
    print("[[RANDOM]]\n")
    #cabecalho = ["n", "Insertion", "Merge", "Heap", "Quick", "Counting"]
    cabecalho = '{:>{col1}} {:^{col2}} {:^{col3}} {:^{col4}} {:^{col5}} {:^{col6}} {:^{col7}}'
    print(cabecalho.format('n', ' ', 'Selection', 'Insertion', 'Merge', 'Heap', 'Quick', 'Counting', **colunas))
    print("-------------------------------------------------------------------------------")

def saida(dados, colunas):
    formato = '{:>{col1}} {:^{col2}} {:^{col3}} {:^{col4}.6f} {:^{col5}} {:^{col6}.6f} {:^{col7}}'
    print(formato.format(dados[0], ' ', 'fazer', dados[1], 'fazer', dados[2], 'fazer', **colunas))

formatarTabelaOutput({'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12})

def table(dados):
    colunas = {'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12}
    saida(dados, colunas)

