import insertion as ins
import formataTabela as out
import heap as hp

def reverte(vetor):
    for j in range(1, len(vetor)):
        valor = vetor[j]
        i = j - 1
        while i >= 0 and vetor[i] < valor:
            vetor[i + 1] = vetor[i]
            i = i - 1
        vetor[i + 1] = valor
    return vetor

def tempoAlg(vetor, algoritmo):
    return algoritmo(vetor)

def problema(inc, fim, stp, rpt):
    print("\n\n[[REVERSE]]\n")
    out.gerarCabecalho()
    for i in range(inc, fim+1, stp):
        tempoInsertion = 0
        tempoHeap = 0
        dados = []
        for j in range(rpt):
            vetorAleatorio = out.geraVetor(i)
            vetorReverso = reverte(vetorAleatorio)
            tempoInsertion += tempoAlg(vetorReverso, ins.insertionSort)
            tempoHeap += tempoAlg(vetorReverso, hp.heapsort)
        dados.append(i)
        dados = out.calculaMedias(tempoInsertion, tempoHeap, dados)
        out.table(dados)
    
