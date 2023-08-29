import sys
numb = int(sys.stdin.readline().rstrip())
roll_book = []

for i in range(numb) :
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    roll_book.append((age, name))

# 병합 정렬
def merge_sort (unsorted) :
    if len(unsorted) <= 1 :
        return unsorted
    mid = len(unsorted) // 2
    left = unsorted[:mid]
    right = unsorted[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge(left_list, right_list)

def merge(left, right) :
    i = 0
    j = 0
    arr = []

    while i < len(left) and j < len(right) :
        if left[i][0] <= right[j][0] :
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

roll_book = merge_sort(roll_book)

for i in roll_book :
    print(*i)

