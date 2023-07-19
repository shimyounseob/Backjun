# list matrix 선언
matrix = []

# 9X9 격자판에 자연수 삽입
for i in range(9):
    numb = list(map(int,input().split()))
    matrix.append(numb)

# matrix list내의 각 list별로 max 값을 찾아냄
# max_list 내에서 max 값을 가져옴
max_list = []

for j in range(9) :
    max_thing = max(matrix[j])
    max_list.append(max_thing)
    the_biggest = max(max_list)

print(the_biggest)

# max값의 인덱스를 찾음

for row in range(9) :
    for column in range(9):
        if matrix [row][column] == the_biggest :
            print(row+1,column+1)
        else :
            pass