import time
def counting_sort(arr):
    start = time.time()

    # Encontra o valor máximo no vetor
    max_value = max(arr)

    # Inicializa um vetor de contagem com zeros
    count = [0] * (max_value + 1)

    # Conta a ocorrência de cada elemento no vetor
    for num in arr:
        count[num] += 1

    # Reconstrói o vetor ordenado usando as contagens
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    endTime = time.time()
    tempoExec = (endTime-start)

    return tempoExec
