import sys

N, M = map(int, sys.stdin.readline().split())

Deuddo = set()
Bodo = set()

for _ in range(N) :
    a = sys.stdin.readline().rstrip()
    Deuddo.add(a)

for _ in range(M) :
    a = sys.stdin.readline().rstrip()
    Bodo.add(a)

DeudBo = Deuddo & Bodo

DB_list = []
for i in DeudBo :
    DB_list.append(i)

def heapify (arr, index, heap_size) :
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and arr[left_index] > arr[largest] :
        largest = left_index
    if right_index < heap_size and arr[right_index] > arr[largest] :
        largest = right_index
    if index != largest :
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)

def heap_sort (arr) :
    n = len(arr)
    for i in range(n // 2, -1, -1) :
        heapify(arr, i , n)

    for i in range(n - 1, 0, -1) :
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr

DB_list = heap_sort(DB_list)

print(len(DB_list))
for i in DB_list :
    print(i)

