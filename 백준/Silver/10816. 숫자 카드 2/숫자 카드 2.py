import sys
N = int(sys.stdin.readline())
SG_card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Q_card = list(map(int, sys.stdin.readline().split()))

SGCard_numb = {}
for i in SG_card :
    if i not in SGCard_numb :
        SGCard_numb[i] = 1
    else :
        SGCard_numb[i] += 1

result = []
for i in Q_card :
    if i in SGCard_numb :
        value = SGCard_numb.get(i)
        result.append(value)
    else :
        result.append(0)

print(*result)
