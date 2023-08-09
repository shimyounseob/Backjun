import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

prime_numb = []

for k in range(m, n+1) :
    if k == 1 :
        pass
    else :
        prime_numb.append(k)



for i in range(m,n+1) :
    for j in range(2, i) :
        if i % j == 0 :
            prime_numb.remove(i)
            break

if prime_numb == [] :
    print(-1)

else :
    result = 0

    for numb in prime_numb :
        result += numb

    print(result)
    print(min(prime_numb))