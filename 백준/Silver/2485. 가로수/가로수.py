import sys
# 이미 심어져 있는 가로수의 갯수
N = int(sys.stdin.readline())
street_trees = []
# 심어져 있는 모든 가로수의 위치
for i in range(N) :
    tree = int(sys.stdin.readline())
    street_trees.append(tree)

# 가로수들 간의 거리 배열에 저장
tree_distance = []
for i in range(1, N) :
    distance = street_trees[i] - street_trees[i-1]
    tree_distance.append(distance)

# 최대공약수 함수
def greatest_common_divisor (numb1, numb2):
    while numb2 :
        numb1, numb2 = numb2, numb1 % numb2
    return numb1

gcd = tree_distance[0]
for i in range(1, len(tree_distance)):
    gcd = greatest_common_divisor(gcd, tree_distance[i])

# 가로수 간격사이에 심을 가로수 갯수 : 간격 // 최대공약수 -1
result = 0
for i in tree_distance:
    result += i // gcd - 1
print(result)

