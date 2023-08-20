import insertion as ins
import formataTabela as out
import numpy as np
import heap as hp

def geraVetor():
    np.random.seed()
    return np.random.randint(0, 20000, i)

def tempoAlg(vetorAleatorio, algoritmo):
    return algoritmo(vetorAleatorio)

def media(tempo):
    tempo/10



#definicao do n inicial e final e do tamanho do passo
inc = 100
fim = 101
stp = 1
dados = []

for i in range(inc, fim, stp):
    n = i + stp
    tempoInsertion = 0
    tempoHeap = 0
    for j in range(10):
        vetorAleatorio = geraVetor()
        tempoInsertion += tempoAlg(vetorAleatorio, ins.insertionSort)
        tempoHeap += tempoAlg(vetorAleatorio, hp.heapsort)
    mediaInsertion = media(tempoInsertion)
    mediaHeap = media(tempoHeap)
    dados.append(n)
    dados.append(mediaInsertion)
    dados.append(mediaHeap)
    out.table(dados)
    
