#Problema em que os algoritmos ordenam um vetor já ordenado de forma decrescente.

import algoritmosOrdenacao.insertion as ins
import algoritmosOrdenacao.merge as merge
import algoritmosOrdenacao.heap as hp
import algoritmosOrdenacao.selection as selec
import algoritmosOrdenacao.counting as coun
import algoritmosOrdenacao.quick as quick
import funcoesAuxiliares as aux
import formatacaoOutput as ft

def problema(inc, fim, stp, rpt):
    print("\n\n[[REVERSE]]\n")
    ft.gerarCabecalho()
    tamVetores = []
    temposIns = []
    temposHeap = []
    temposMerge = []
    temposSelec = []
    temposCount = []
    temposQuick = []
    #Laço que representa os tamanhos de entradas (inc = início, fim = final -1, stp = distância entre eles).
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        tempoMerge = 0
        tempoSelec = 0
        tempoCount = 0
        tempoQuick = 0
        dados = []
        #laço que representa quantos testes serão feitos para posteriormente calcular a média
        for j in range(rpt):
            vetorAleatorio = aux.geraVetor(i)
            vetorReverso = sorted(vetorAleatorio, reverse=True) #aplicação de função própria para gerar vetor decrescente
            tempoInsertion += aux.tempoAlg(vetorReverso, ins.insertionSort)
            tempoHeap += aux.tempoAlg(vetorReverso, hp.heapsort)
            tempoMerge += aux.tempoAlg(vetorReverso, merge.tempoMerge)
            tempoSelec += aux.tempoAlg(vetorReverso, selec.selection_sort)
            tempoCount += aux.tempoAlg(vetorReverso, coun.counting_sort)
            tempoQuick += aux.tempoAlg(vetorReverso, quick.quicksort)
        dados.append(i)
        tamVetores.append(i)
        dados = aux.calculaMedias(rpt, tempoInsertion, tempoHeap, tempoMerge, tempoSelec, tempoCount, tempoQuick, dados, temposIns, temposHeap, temposMerge, temposSelec, temposCount, temposQuick)
        ft.table(dados)

    ft.geraGrafico(tamVetores, temposSelec, temposIns, temposMerge, temposHeap, temposQuick, temposCount)
