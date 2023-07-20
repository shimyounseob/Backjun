# 첫째 줄에 N과 B가 주어짐
n, b = input().split()
b = int(b)

# 알파벳을 숫자로 변환 >> alphabet[b-11]
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numb = '0123456789'


# 십진법 체계에 맞게 변환
# trans_list에 변환된 숫자들 저장

trans_list = []

for char in n :
    if char in alphabet :
        char_index = alphabet.index(char) + 10
        trans_list.append(char_index)

    else :
        char = int(char)
        trans_list.append(char)

# 십진법 계산을 용이하게 하기 위해 reverse
trans_list = trans_list[::-1]

# trans_list에 있는 숫자들을 십진법 계산법에 맞게 계산
# ex) 36 X 36^4 + 36 X 36^3 + 36 X 36^2 + 36 X 36^1 + 36 X 36^0

result = 0

for i in range(len(trans_list)) :
    result += trans_list[i] * (b ** i)

print(result)