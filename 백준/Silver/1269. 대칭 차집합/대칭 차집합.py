import sys
A_len, B_len = map(int, sys.stdin.readline().split())

A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(map(int, sys.stdin.readline().split()))

A = set(A_list)
B = set(B_list)

AB = A^B

print(len(AB))