import sys
def isPrimeNumber (x) :
    for i in range(2, int(x ** 0.5) + 1) :
        if x % i == 0 :
            return False
    return True

while (True) :
    numb = int(sys.stdin.readline())
    if numb == 0 :
        break

    count = 0
    for i in range(numb + 1, 2 * numb+1) :
        isNumbPN = isPrimeNumber(i)
        if isNumbPN == True :
            count += 1
    print(count)
