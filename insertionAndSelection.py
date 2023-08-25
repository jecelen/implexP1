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

def selection_sort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    endTime = time.time()
    tempoExec = (endTime-start)
    return tempoExec