import time

def partition(arr, low, high):
    pivot = arr[high]  # Escolha do pivô
    i = low - 1  # Índice do elemento menor

    for j in range(low, high-1):
        if arr[j] <= pivot:
            i = i+1
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    aux = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = aux  # Coloca o pivô no lugar correto
    return i + 1

def quick_sort(arr, low, high):
    start = time.time()
    if low < high:
        pivot_index = partition(arr, low, high)  # Encontra o índice do pivô correto
        quick_sort(arr, low, pivot_index - 1)  # Ordena os elementos menores que o pivô
        quick_sort(arr, pivot_index + 1, high)  # Ordena os elementos maiores que o pivô
    endTime = time.time()
    tempoExec = (endTime-start)
    return tempoExec







  