# 단어의 개수 N이 들어옴
numb = int(input())

# 그룹 단어의 갯수 셈
group_word = 0

# 단어 input의 반복
for i in range(numb):
    word = input()

    # 그룹 단어인지가 false가 나왔을 시에는 group_word를 +1 해줌
    GWornot = True

    # 이전 문자를 기록할 변수를 추가
    prev_word = ''

    for j in range(len(word)):
        # 현재 문자와 이전 문자가 같은 경우 pass
        if word[j] == prev_word:
            continue

        # 이전 문자와 현재 문자가 다르면
        # 현재 문자가 이전 문자 다음에 나오지 않은 경우 그룹 단어가 아님
        if prev_word != '' and word.find(prev_word, j + 1) != -1:
            GWornot = False
            break

        prev_word = word[j]


    if GWornot:
        group_word += 1

print(group_word)