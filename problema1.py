import insertionAndSelection as ins
import funcoesAuxiliares as aux
import numpy as np
import heap as hp
import merge as mer

def tempoAlg(vetorAleatorio, algoritmo): #essa função se repete em todos os problemas, podemos jogar ela pro arquivo "funcoesaux"
    return algoritmo(vetorAleatorio)


def problema(inc, fim, stp, rpt):
    print("\n[[RANDOM]]\n")
    aux.gerarCabecalho()
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        tempoMerge = 0
        tempoSelec = 0
        dados = []
        for j in range(10):
            vetorAleatorio = aux.geraVetor(i)
            tempoInsertion += tempoAlg(vetorAleatorio, ins.insertionSort)
            tempoHeap += tempoAlg(vetorAleatorio, hp.heapsort)
            tempoMerge += tempoAlg(vetorAleatorio, mer.mergeSort)
            tempoSelec += tempoAlg(vetorAleatorio, ins.selection_sort)
        dados.append(i)
        dados = aux.calculaMedias(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, dados)
        aux.table(dados)
    
