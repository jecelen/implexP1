import numpy as np

def tempoAlg(vetorAleatorio, algoritmo):
    return algoritmo(vetorAleatorio)


def calculaMedias(insertion, heap, merge, selec, count, quick, dados):
    dados.append(insertion/10)
    dados.append(heap/10)
    dados.append(merge/10)
    dados.append(selec/10)
    dados.append(count/10)
    dados.append(quick/10)
    return dados


def geraVetor(n):
    np.random.seed()
    return np.random.randint(0, 20000, n)



