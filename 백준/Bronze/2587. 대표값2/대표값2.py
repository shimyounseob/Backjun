def quick_sort (arr) :
    def sort (low, high) :
        if high <= low :
            return

        mid = partition(low, high)
        sort(low, mid -1)
        sort(mid, high)

    def partition (low, high) :
        pivot = arr[(low + high) // 2]
        while low <= high :
            while arr[low] < pivot :
                low += 1
            while arr[high] > pivot :
                high -= 1
            if low <= high :
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low +1, high -1

                # low는 partition의 위치 
            return low

    return sort(0, len(arr)-1)

numbers = []

for _ in range(5) :
    numb = int(input())
    numbers.append(numb)

quick_sort(numbers)

# 중앙값
median = numbers[2]

# 평균
sum = 0
for i in numbers :
   sum += i
average = sum / 5

print(int(average))
print(median)
