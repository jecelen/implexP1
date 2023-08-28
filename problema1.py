import algoritmosOrdenacao.insertion as ins
import algoritmosOrdenacao.merge as merge
import algoritmosOrdenacao.heap as hp
import algoritmosOrdenacao.selection as selec
import funcoesAuxiliares as aux
import formatacaoTabela as ft


def problema(inc, fim, stp, rpt):
    print("\n[[RANDOM]]\n")
    ft.gerarCabecalho()
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        tempoMerge = 0
        tempoSelec = 0
        dados = []
        for j in range(10):
            vetorAleatorio = aux.geraVetor(i)
            tempoInsertion += aux.tempoAlg(vetorAleatorio, ins.insertionSort)
            tempoHeap += aux.tempoAlg(vetorAleatorio, hp.heapsort)
            tempoMerge += aux.tempoAlg(vetorAleatorio, merge.mergeSort)
            tempoSelec += aux.tempoAlg(vetorAleatorio, selec.selection_sort)
        dados.append(i)
        dados = aux.calculaMedias(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, dados)
        ft.table(dados)
    
