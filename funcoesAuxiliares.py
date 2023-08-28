import numpy as np

def tempoAlg(vetorAleatorio, algoritmo):
    return algoritmo(vetorAleatorio)


def calculaMedias(insertion, heap, merge, selec, dados):
    dados.append(insertion/10)
    dados.append(heap/10)
    dados.append(merge/10)
    dados.append(selec/10)
    return dados


def geraVetor(n):
    np.random.seed()
    return np.random.randint(0, 20000, n)



