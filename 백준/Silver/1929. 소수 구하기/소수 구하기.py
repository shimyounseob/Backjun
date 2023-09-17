import sys
N, M = map(int, sys.stdin.readline().split())

def isPrimeNumber(x) :
    for i in range(2, int(x ** 0.5)+ 1):
        if x % i == 0 :
            return False
    return True

for i in range(N, M+1) :
    boolean = isPrimeNumber(i)
    if boolean == True and i != 1 :
        print(i)
