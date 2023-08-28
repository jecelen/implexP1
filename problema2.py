import algoritmosOrdenacao.insertion as ins
import algoritmosOrdenacao.merge as merge
import algoritmosOrdenacao.heap as hp
import algoritmosOrdenacao.selection as selec
import funcoesAuxiliares as aux
import formatacaoTabela as ft


def problema(inc, fim, stp, rpt):
    print("\n\n[[REVERSE]]\n")
    ft.gerarCabecalho()
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        tempoMerge = 0
        tempoSelec = 0
        dados = []
        for j in range(rpt):
            vetorAleatorio = aux.geraVetor(i)
            vetorReverso = sorted(vetorAleatorio, reverse=True) #aplicação de função propria para gerar vetor reverso
            tempoInsertion += aux.tempoAlg(vetorReverso, ins.insertionSort)
            tempoHeap += aux.tempoAlg(vetorReverso, hp.heapsort)
            tempoMerge += aux.tempoAlg(vetorReverso, merge.mergeSort)
            tempoSelec += aux.tempoAlg(vetorReverso, selec.selection_sort)
        dados.append(i)
        dados = aux.calculaMedias(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, dados)
        ft.table(dados)
    
