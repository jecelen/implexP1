import insertion as ins
import formataTabela as out
import numpy as np
import heap as hp

def tempoAlg(vetorAleatorio, algoritmo):
    return algoritmo(vetorAleatorio)

def media(tempo):
    return tempo/10

#definicao do n inicial e final e do tamanho do passo
inc = 100
fim = 1000
stp = 10


for i in range(inc, fim+1, stp):
    tempoInsertion = 0
    tempoHeap = 0
    dados = []
    for j in range(10):
        vetorAleatorio = out.geraVetor(i)
        tempoInsertion += tempoAlg(vetorAleatorio, ins.insertionSort)
        tempoHeap += tempoAlg(vetorAleatorio, hp.heapsort)
    dados.append(i)
    dados = out.calculaMedias(tempoInsertion, tempoHeap, dados)
    out.table(dados)
    
