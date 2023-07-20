numb = int(input())

# 100 X 100 도화지 크기의 행렬 생성
matrix = [[0] * 100 for _ in range(100)]

# 가로 값, 세로 값 받음
for i in range(numb) :
    a,b = map(int, input().split())

    # for 문을 통해 받은 a +10 까지와 b +10을 1로 변경함
    # 겹치지 않는 부분은 1, 겹치는 부분은 2로 바꾼다
    for row in range(10) :
        for column in range (10) :
            if matrix[a+row][b+column] == 0 :
                matrix[a+row][b+column] = 1

            else :
                matrix[a + row][b + column] = 2

# 리스트 내부를 반복문으로 돌리면서 2의 갯수를 count함

area = 0

for j in range(100) :
    count_two = matrix[j].count(2)
    count_one = matrix[j].count(1)
    area += count_two + count_one

print(area)