import numpy as np
import random as rd

def tempoAlg(vetorAleatorio, algoritmo):
    return algoritmo(vetorAleatorio)


def calculaMedias(QtdTestes,insertion, heap, merge, selec, count, quick, dados, ti, th, tm, ts, tc, tq):
    dados.append(insertion/QtdTestes)
    dados.append(heap/QtdTestes)
    dados.append(merge/QtdTestes)
    dados.append(selec/QtdTestes)
    dados.append(count/QtdTestes)
    dados.append(quick/QtdTestes)
    ti.append(insertion/QtdTestes)
    th.append(heap/QtdTestes)
    tm.append(merge/QtdTestes)
    ts.append(selec/QtdTestes)
    tc.append(count/QtdTestes)
    tq.append(quick/QtdTestes)
    return dados

    

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





