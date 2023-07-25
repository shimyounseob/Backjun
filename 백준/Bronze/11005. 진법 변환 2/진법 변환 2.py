n, b = map(int, input().split())

# 10 - 35 까지의 값을 A - Z로 변환해줌

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

reminder = ''

# 10진수 수 N을 B 진법으로 출력하는 방법
# 10진수 수를 B로 나눈 나머지 값을 문자열에 추가하고 [::-1]을 통해 reverse 해줌

quotient = n

while quotient > 0 :
    rem = quotient % b
    quotient = quotient // b

    # alphabet의 나미지-10으로 수를 표현해줌
    if rem > 9 :
        rem = alphabet[rem-10]

    # 나머지 값을 reminder에 추가해줌

    rem = str(rem)
    reminder += rem

reminder = reminder[::-1]

print(reminder)
