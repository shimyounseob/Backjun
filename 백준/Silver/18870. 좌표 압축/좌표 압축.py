import sys

def merge_sort(unsorted) :
    if len(unsorted) <= 1 :
        return unsorted
    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list, right_list)
def merge (left, right) :
        i = 0
        j = 0
        arr = []

        while len(left)> i and len(right)> j :
            if left[i] <= right[j] :
                arr.append(left[i])
                i += 1
            else :
                arr.append(right[j])
                j += 1

        while len(left) > i :
            arr.append(left[i])
            i = i + 1
        while len(right) > j :
            arr.append(right[j])
            j = j + 1

        return arr

numb = int(sys.stdin.readline())
unsorted = list(map(int, sys.stdin.readline().split()))
unsorted_noneduple = list(set(unsorted))

sorted = merge_sort(unsorted_noneduple)

compression = {}

for i in range(len(sorted)) :
    key = sorted[i]
    compression[key] = i

result = []
for i in unsorted :
    a = compression[i]
    result.append(a)

print(*result)
