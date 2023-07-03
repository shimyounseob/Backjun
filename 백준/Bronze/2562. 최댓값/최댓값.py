import sys

list = []

for i in range(9) :
    num = int(sys.stdin.readline())
    list.append(num)

max = max(list)
index = list.index(max)

print(max)
print(index+1)

