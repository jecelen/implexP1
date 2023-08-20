def formatarTabelaOutput(colunas):
    print("[[RANDOM]]\n")
    #cabecalho = ["n", "Insertion", "Merge", "Heap", "Quick", "Counting"]
    cabecalho = '{:>{col1}} {:^{col2}} {:^{col3}} {:^{col4}} {:^{col5}} {:^{col6}} {:^{col7}}'
    print(cabecalho.format('n', ' ', 'Selection', 'Insertion', 'Merge', 'Heap', 'Quick', 'Counting', **colunas))
    print("-------------------------------------------------------------------------------")

def saida(dados, colunas):
    formato = '{:>{col1}} {:^{col2}.6f} {:^{col3}.6f}'
    print(formato.format(dados[0], dados[1], dados[2], **colunas))

#formatarTabelaOutput({'col1': 8, 'col2': 2, 'col3': 12, 'col4': 12, 'col5': 12, 'col6': 12, 'col7': 12})

def table(dados):
    colunas = {'col1': 8, 'col2': 17, 'col3': 12}
    saida(dados, colunas)

