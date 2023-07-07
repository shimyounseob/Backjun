import sys
k,q,r,b,kn,p = map(int, sys.stdin.readline().split())

dh_chess = [k,q,r,b,kn,p]
standard = [1,1,2,2,2,8]

needed = []

for i in range(6) :
    if dh_chess[i] != standard[i]:
        needed.append(standard[i] - dh_chess[i])
    else:
        needed.append(0)

print(*needed)