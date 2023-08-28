import time

def insertionSort(vetor):
  start = time.time()
  for j in range(1, len(vetor)):
    valor = vetor[j]
    i = j - 1
    while i >= 0 and vetor[i] > valor:
      vetor[i + 1] = vetor[i]
      i = i - 1
    vetor[i + 1] = valor
  endTime = time.time()
  tempoExec = (endTime-start)
  return tempoExec