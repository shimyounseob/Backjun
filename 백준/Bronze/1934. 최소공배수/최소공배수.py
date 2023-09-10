import sys

numb = int(sys.stdin.readline())
arr = []

for _ in range(numb) :
    A, B = map(int, sys.stdin.readline().split())
    largest = max(A, B)
    smallest = min(A, B)

    while (True) :
        remainder = largest % smallest
        if remainder == 0 :
            res = int(A*B / smallest)
            print(res)
            break
        else :
            largest = smallest
            smallest = remainder

