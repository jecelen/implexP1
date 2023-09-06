#Problema em que os algoritmos ordenam um vetor já ordenado de forma crescente.

import algoritmosOrdenacao.insertion as ins
import algoritmosOrdenacao.merge as merge
import algoritmosOrdenacao.heap as hp
import algoritmosOrdenacao.selection as selec
import algoritmosOrdenacao.counting as coun
import algoritmosOrdenacao.quick as quick
import funcoesAuxiliares as aux
import formatacaoOutput as ft

def addListaTempo(tempo, lista):
    return lista.append(tempo)

def problema(inc, fim, stp, rpt):
    print("\n\n[[SORTED]]\n")
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
        dados = []
        vetorAleatorio = aux.geraVetor(i)
        vetorOrd = sorted(vetorAleatorio, reverse=False) #aplicação de função própria para gerar vetor ordenado crescente
        tempoIns = (aux.tempoAlg(vetorOrd, ins.insertionSort))
        tempoHeap = (aux.tempoAlg(vetorOrd, hp.heapsort))
        tempoMerge = (aux.tempoAlg(vetorOrd, merge.tempoMerge))
        tempoSelec = (aux.tempoAlg(vetorOrd, selec.selection_sort))
        tempoCount = (aux.tempoAlg(vetorOrd, coun.counting_sort))
        tempoQuick = (aux.tempoAlg(vetorOrd, quick.quicksort))
        addListaTempo(tempoIns, temposIns)
        addListaTempo(tempoMerge, temposMerge)
        addListaTempo(tempoSelec, temposSelec)
        addListaTempo(tempoHeap, temposHeap)
        addListaTempo(tempoCount, temposCount)
        addListaTempo(tempoQuick, temposQuick)
        dados.append(i)
        tamVetores.append(i)
        dados = aux.addDados(tempoIns, tempoHeap, tempoMerge, tempoSelec, tempoCount, tempoQuick, dados)
        ft.table(dados)
    
    
    #Função que gera gráfico
    #ft.geraGrafico(tamVetores, temposSelec, temposIns, temposMerge, temposHeap, temposQuick, temposCount)