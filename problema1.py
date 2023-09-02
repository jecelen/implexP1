#Problema em que os algoritmos ordenam um vetor aleatório
import sys
import algoritmosOrdenacao.insertion as ins
import algoritmosOrdenacao.merge as merge
import algoritmosOrdenacao.heap as hp
import algoritmosOrdenacao.selection as selec
import algoritmosOrdenacao.counting as coun
import algoritmosOrdenacao.quick as quick
import funcoesAuxiliares as aux
import formatacaoTabela as ft
import matplotlib as plt

sys.setrecursionlimit(10000)
def problema(inc, fim, stp, rpt):
    print("\n[[RANDOM]]\n")
    ft.gerarCabecalho()
    tamVetores = []
    temposIns = []
    temposHeap = []
    temposMerge = []
    temposSelec = []
    temposCount = []
    temposQuick = []
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        tempoMerge = 0
        tempoSelec = 0
        tempoCount = 0
        tempoQuick = 0
        dados = []
        for j in range(10):
            vetorAleatorio = aux.geraVetor(i)
            tempoInsertion += aux.tempoAlg(vetorAleatorio, ins.insertionSort)
            tempoHeap += aux.tempoAlg(vetorAleatorio, hp.heapsort)
            tempoMerge += aux.tempoAlg(vetorAleatorio, merge.mergeSort)
            tempoSelec += aux.tempoAlg(vetorAleatorio, selec.selection_sort)
            tempoCount += aux.tempoAlg(vetorAleatorio, coun.counting_sort)
            tempoQuick += quick.quick_sort(vetorAleatorio, 0, len(vetorAleatorio)-1)
        dados.append(i)
        tamVetores.append(i)
        aux.calculaMedias2(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, tempoCount, tempoQuick, temposIns, temposHeap, temposMerge, temposSelec, temposCount, temposQuick)
        dados = aux.calculaMedias(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, tempoCount, tempoQuick, dados)
        ft.table(dados)

        plt.plot(tamVetores, temposIns, label='Inserion', marker='o')
        plt.plot(tamVetores, temposHeap, label='Heap', marker='o')
        plt.plot(tamVetores, temposMerge, label='Merge', marker='o')
        plt.plot(tamVetores, temposSelec, label='Selection', marker='o')
        plt.plot(tamVetores, temposCount, label='Counting', marker='o')
        plt.plot(tamVetores, temposQuick, label='Quick', marker='o')
    
