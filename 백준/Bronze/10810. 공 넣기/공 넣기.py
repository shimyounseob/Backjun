import sys

n, m = map(int, sys.stdin.readline().split())

list = [0] * n

for s in range(m) :
    i, j, k = map(int, sys.stdin.readline().split())
    list[i-1:j] = [k] * (j-i+1)

print(*list)