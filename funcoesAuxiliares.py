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


#recebe um vetor e ordena apenas 10% dele, sendo esses 10% no início
def ordenacaoParcial(vetor):   
    # Calcula o tamanho do vetor 10%
    tamanho_10_porcento = len(vetor) // 10
    
    # Ordena apenas os primeiros 10% do vetor
    vetor[:tamanho_10_porcento] = sorted(vetor[:tamanho_10_porcento])
    
    return vetor



