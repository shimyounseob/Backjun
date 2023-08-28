import sys

numb = int(sys.stdin.readline().rstrip())
xy_list = []

for _ in range(numb):
    x, y = map(int, sys.stdin.readline().split())
    xy_list.append((y, x))  

def heapify(unsorted, index, heap_size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # 기존 코드와 달리 y 좌표를 비교하여 정렬
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)

def heap_sort(unsorted):
    n = len(unsorted)

    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)

    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

heap_sort(xy_list)

for i in range(len(xy_list)):
    print(xy_list[i][1], xy_list[i][0])  
