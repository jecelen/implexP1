import insertionAndSelection as ins
import funcoesAuxiliares as out
import heap as hp
import merge as mer

#def reverte(vetor):                  #retirar essa função e usar o reverse da função sorted()
#    for j in range(1, len(vetor)):
#       valor = vetor[j]
#        i = j - 1
#        while i >= 0 and vetor[i] < valor:
#            vetor[i + 1] = vetor[i]
#            i = i - 1
#        vetor[i + 1] = valor
#    return vetor         

def tempoAlg(vetor, algoritmo):  #essa função se repete em todos os problemas, podemos jogar ela pro arquivo "funcoesaux"
    return algoritmo(vetor)

def problema(inc, fim, stp, rpt):
    print("\n\n[[REVERSE]]\n")
    out.gerarCabecalho()
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        tempoMerge = 0
        tempoSelec = 0
        dados = []
        for j in range(rpt):
            vetorAleatorio = out.geraVetor(i)
            vetorReverso = sorted(vetorAleatorio, reverse=True) #fica mais clean usar isso
            tempoInsertion += tempoAlg(vetorReverso, ins.insertionSort)
            tempoHeap += tempoAlg(vetorReverso, hp.heapsort)
            tempoMerge += tempoAlg(vetorReverso, mer.mergeSort)
            tempoSelec += tempoAlg(vetorReverso, ins.selection_sort)
        dados.append(i)
        dados = out.calculaMedias(tempoInsertion, tempoHeap, tempoMerge, tempoSelec, dados)
        out.table(dados)
    
