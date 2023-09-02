#Problema em que os algoritmos ordenam um vetor já  10% ordenado de forma crescente

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
    print("\n\n[[PARCIALMENTE ORDENADO]]\n")
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
            vetorOrd = sorted(vetorAleatorio, reverse=False) 
            vetorParcial = aux.ordenacaoParcial(vetorOrd)
            tempoInsertion += aux.tempoAlg(vetorParcial, ins.insertionSort)
            tempoHeap += aux.tempoAlg(vetorParcial, hp.heapsort)
            tempoMerge += aux.tempoAlg(vetorParcial, merge.mergeSort)
            tempoSelec += aux.tempoAlg(vetorParcial, selec.selection_sort)
            tempoCount += aux.tempoAlg(vetorParcial, coun.counting_sort)
            tempoQuick += quick.quick_sort(vetorParcial, 0, len(vetorParcial) -1)
        dados.append(i)
        dados = aux.calculaMedias(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, tempoCount, tempoQuick, dados)
        ft.table(dados)