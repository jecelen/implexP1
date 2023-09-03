import numpy as np
import random as rd

def tempoAlg(vetorAleatorio, algoritmo):
    return algoritmo(vetorAleatorio)


def calculaMedias(insertion, heap, merge, selec, count, quick, dados, ti, th, tm, ts, tc, tq):
    dados.append(insertion/10)
    dados.append(heap/10)
    dados.append(merge/10)
    dados.append(selec/10)
    dados.append(count/10)
    dados.append(quick/10)
    ti.append(insertion/10)
    th.append(heap/10)
    tm.append(merge/10)
    ts.append(selec/10)
    tc.append(count/10)
    tq.append(quick/10)
    return dados

#def calculaMedias2(insertion, heap, merge, selec, count, quick, ):
    

def addDados(insertion, heap, merge, selec, count, quick, dados): #problema3 - vetor ordenado
    dados.append(insertion)
    dados.append(heap)
    dados.append(merge)
    dados.append(selec)
    dados.append(count)
    dados.append(quick)
    return dados


def geraVetor(n):
    np.random.seed()
    return np.random.randint(0, 20000, n)


#recebe um vetor e ordena apenas 10% dele, sendo esses 10% no início
def ordenacaoParcial(vetor):   
    # Calcula o tamanho do vetor 10%
    desord = []
    tamanho_10_porcento = len(vetor) // 10
    for i in range(tamanho_10_porcento):
        desord.append(vetor[i])
    for i in range(tamanho_10_porcento):
        vetor = np.delete(vetor, i)
    # Ordena apenas os primeiros 10% do vetor
    rd.shuffle(desord)
    desord.extend(vetor)
    return desord





