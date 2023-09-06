#Problema em que os algoritmos ordenam um vetor parcialmente ordenado.

import algoritmosOrdenacao.insertion as ins
import algoritmosOrdenacao.merge as merge
import algoritmosOrdenacao.heap as hp
import algoritmosOrdenacao.selection as selec
import algoritmosOrdenacao.counting as coun
import algoritmosOrdenacao.quick as quick
import funcoesAuxiliares as aux
import formatacaoOutput as ft

def problema(inc, fim, stp, rpt):
    print("\n\n[[NEARLY SORTED]]\n")
    ft.gerarCabecalho()
    #Os Vetores abaixo irão armazenar os dados necessários para a construção dos gráficos.
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
        #laço que representa quantos testes serão feitos para posteriormente calcular a média.
        for j in range(rpt):
            vetorAleatorio = aux.geraVetor(i)
            vetorOrd = sorted(vetorAleatorio, reverse=False) 
            vetorParcial = aux.ordenacaoParcial(vetorOrd)
            tempoInsertion += aux.tempoAlg(vetorParcial, ins.insertionSort)
            tempoHeap += aux.tempoAlg(vetorParcial, hp.heapsort)
            tempoMerge += aux.tempoAlg(vetorParcial, merge.tempoMerge)
            tempoSelec += aux.tempoAlg(vetorParcial, selec.selection_sort)
            tempoCount += aux.tempoAlg(vetorParcial, coun.counting_sort)
            tempoQuick += aux.tempoAlg(vetorParcial, quick.quicksort)
        dados.append(i)
        tamVetores.append(i)
        dados = aux.calculaMedias(rpt, tempoInsertion, tempoHeap, tempoMerge, tempoSelec, tempoCount, tempoQuick, dados, temposIns, temposHeap, temposMerge, temposSelec, temposCount, temposQuick)
        ft.table(dados)

    #Função que gera gráfico
    #ft.geraGrafico(tamVetores, temposSelec, temposIns, temposMerge, temposHeap, temposQuick, temposCount)