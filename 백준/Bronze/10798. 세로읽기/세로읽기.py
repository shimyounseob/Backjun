# list matrix 선언
matrix = []

# 다섯 줄의 입력이 주어짐
for i in range(5) :
    letters = list(input())
    matrix.append( letters)

# column이 같은 값들 끼리 모은 뒤 담아줌
same_column = ""

# row가 다르고 column이 같아야 하기 때문에 for column 내부에 for row가 위치함
# range가 최대인 15글자를 넘을 경우, 처리하지 않음

for column in range(15) :
    for row in range(5) :
        if len(matrix[row]) > column:
            new_letter = matrix[row][column]

            same_column += new_letter

print(same_column)


