import sys
n, k = map(int,sys.stdin.readline().split())

factor = []

for i in range(n+1) :
    if i !=0 and n % i == 0 :
        factor.append(i)

if len(factor) < k :
    print("0")

else :
    print(factor[k-1])

