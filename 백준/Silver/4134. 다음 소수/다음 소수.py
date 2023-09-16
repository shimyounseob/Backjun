import sys
N = int(sys.stdin.readline())

arr = []
for i in range(N) :
    word = int(sys.stdin.readline())
    arr.append(word)

def prime_number (x) :
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for i in arr :
    while True :
        if i == 0 or i == 1 :
            print(2)
            break
        numb = prime_number(i)
        if numb == True :
            print(i)
            break
        else :
            i += 1
