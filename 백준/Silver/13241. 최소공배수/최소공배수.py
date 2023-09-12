import sys

A,B = map(int, sys.stdin.readline().split())
arr = []

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

