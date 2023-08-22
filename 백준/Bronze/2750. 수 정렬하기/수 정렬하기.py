def quick_sort (arr):
    # 재귀 알고리즘 sort
    def sort(low,high):
        if high <= low :
            return
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)

    #pivot을 기준으로 좌우측 값을 정렬함
    def partition (low, high):
        pivot = arr[(low + high)//2]
        while low <=high :
            while arr[low] < pivot :
                low += 1
            while arr[high] > pivot :
                high -= 1
            if low <= high :
                 arr[low], arr[high] = arr[high], arr[low]
                 low, high = low +1, high -1
        return low

    return sort(0,len(arr)-1)

N = int(input())
numbs = []

for k in range(N):
    numb = int(input())
    numbs.append(numb)

# 퀵 소트 함수를 통한 정렬
quick_sort(numbs)

# 결과 출력
for h in numbs :
    print(h)