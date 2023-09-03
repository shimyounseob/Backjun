N = int(input())
N_numb = list(map(int, input().split()))

M = int(input())
M_numb = list(map(int, input().split()))

# 병합 정렬
def merge_sort(unsorted) :
    if len(unsorted) <= 1 :
        return unsorted
    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    left_list = merge_sort (left)
    right_list = merge_sort (right)

    return merge(left_list, right_list)

def merge (left, right) :
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right) :
        if left[i] <= right [j]:
            arr.append(left[i])
            i += 1
        else :
            arr.append(right[j])
            j += 1

    while i < len(left) :
        arr.append(left[i])
        i = i + 1

    while j < len(right) :
        arr.append(right[j])
        j = j + 1

    return arr

N_sorted =merge_sort(N_numb)

def binary(arr, target) :
    low = 0
    high = len(arr) - 1
    key = 0

    while low <= high :
        mid = (low + high) // 2
        if target == arr[mid] :
            key = 1
            break
        elif target < arr[mid] :
            high = mid - 1
        else :
            low = mid + 1

    return key

result = []

for i in M_numb :
    result.append(binary(N_sorted, i))

print(*result)