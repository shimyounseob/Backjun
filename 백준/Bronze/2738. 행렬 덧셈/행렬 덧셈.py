# 행렬 행x렬 입력
N,M = map (int, input().split())

matrix_a = []
matrix_b = []

for i in range(N) :
    row = list(map(int, input().split()))
    matrix_a.append(row)

for j in range(N) :
    row = list(map(int, input().split()))
    matrix_b.append(row)


for row in range(N):
    for column in range(M):
        result = matrix_a[row][column] + matrix_b[row][column]
        print(result,end=" ")
    print()
