import sys

n, m = map(int, sys.stdin.readline().split())

bucket = []

for allocation in range(n) :
    bucket.append(allocation+1)

for s in range(m) :
    i, j = map(int, sys.stdin.readline().split())
    temp = bucket[i-1]
    bucket[i-1] = bucket [j-1]
    bucket[j-1] = temp

print (*bucket)