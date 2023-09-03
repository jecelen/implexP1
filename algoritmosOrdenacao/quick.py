import time
import random
import sys

def partition(arr, low, high):
    random_index = random.randint(low, high)

    arr[random_index], arr[high] = arr[high], arr[random_index]
    pivot = arr[high] 
    i = low - 1 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
    aux = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = aux 
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)  
        quick_sort(arr, low, pivot_index - 1) 
        quick_sort(arr, pivot_index + 1, high)

def quicksort(arr):
    sys.setrecursionlimit(10000)
    start = time.time()
    quick_sort(arr, 0, len(arr)-1)
    endTime = time.time()
    tempo = endTime - start
    return tempo








  