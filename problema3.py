#Problema em que os algoritmos ordenam um vetor já ordenado de forma crescente

import algoritmosOrdenacao.insertion as ins
import algoritmosOrdenacao.merge as merge
import algoritmosOrdenacao.heap as hp
import algoritmosOrdenacao.selection as selec
import algoritmosOrdenacao.counting as coun
import algoritmosOrdenacao.quick as quick
import funcoesAuxiliares as aux
import formatacaoTabela as ft
import sys

sys.setrecursionlimit(10000)
def problema(inc, fim, stp, rpt):
    print("\n\n[[ORDENADO]]\n")
    ft.gerarCabecalho()
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        tempoMerge = 0
        tempoSelec = 0
        tempoCount = 0
        tempoQuick = 0
        dados = []
        for j in range(rpt):
            vetorAleatorio = aux.geraVetor(i)
            vetorOrd = sorted(vetorAleatorio, reverse=False) #aplicação de função própria para gerar vetor ordenado crescente
            tempoInsertion += aux.tempoAlg(vetorOrd, ins.insertionSort)
            tempoHeap += aux.tempoAlg(vetorOrd, hp.heapsort)
            tempoMerge += aux.tempoAlg(vetorOrd, merge.mergeSort)
            tempoSelec += aux.tempoAlg(vetorOrd, selec.selection_sort)
            tempoCount += aux.tempoAlg(vetorOrd, coun.counting_sort)
            tempoQuick += quick.quick_sort(vetorOrd, 0, len(vetorOrd) -1)
        dados.append(i)
        dados = aux.calculaMedias(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, tempoCount, tempoQuick, dados)
        ft.table(dados)