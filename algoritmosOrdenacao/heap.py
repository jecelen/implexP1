import time
import sys

def pai(pos):
  if pos == 0:
    return pos
  else:
    return (pos-1)//2;

def filho_dir(pos):
  return 2*pos+2

def filho_esq(pos):
  return 2*pos+1

def desceHeap(vetor, n, i):
    dir = filho_dir(i)
    esq = filho_esq(i)
    maior = i

    if esq < n and vetor[esq] > vetor[maior]:
        maior = esq

    if dir < n and vetor[dir] > vetor[maior]:
        maior = dir
  
    if maior != i:
        aux = vetor[i]
        vetor[i] = vetor[maior]
        vetor[maior] = aux
        desceHeap(vetor, n, maior)
  
  
def heapsort(vetor):
    sys.setrecursionlimit(10000)
    start = time.time()
    n = len(vetor)
    i = n
    for i in range(pai(n-1), -1, -1):
        desceHeap(vetor, n, i)
    for i in range(n-1, 0, -1):
        aux = vetor[i]
        vetor[i] = vetor[0]
        vetor[0] = aux
        desceHeap(vetor, i, 0)
    endTime = time.time()
    tempoExec = (endTime-start)
    return tempoExec
