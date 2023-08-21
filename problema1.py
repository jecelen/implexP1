import insertion as ins
import formataTabela as out
import numpy as np
import heap as hp
import time

start = time.time()
def geraVetor():
    np.random.seed()
    return np.random.randint(0, 20000, i)

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
        vetorAleatorio = geraVetor()
        tempoInsertion += tempoAlg(vetorAleatorio, ins.insertionSort)
        tempoHeap += tempoAlg(vetorAleatorio, hp.heapsort)
    mediaInsertion = media(tempoInsertion)
    mediaHeap = media(tempoHeap)
    dados.append(i)
    dados.append(mediaInsertion)
    dados.append(mediaHeap)
    out.table(dados)

end = time.time()
print(end-start)
    
