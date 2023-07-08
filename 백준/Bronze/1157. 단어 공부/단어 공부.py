# 입력 문자를 대문자(upper) 또는 소문자(lower)로 변경하기
word = input().upper()

# set 집합 자료형을 이용한 자료형의 중복 제거
# set는 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용됨

word_list = list(set(word))

# word에서 각 문자가 얼마나 포함되어 있는지 count를 이용해 셀 수 있음
# count list에 각 문자당 등장 횟수 append

count = []

for i in word_list :
    a = word.count(i)
    count.append(a)

# count list에서 가장 큰 값을 셈
# 가장 큰 값이 1개를 초과하면 print ('?')을 출력
# 그렇지 않다면 가장 큰 값의 인덱스를 구함
# 그리고 word_list의 그 인덱스를 출력해줌

if count.count(max(count)) > 1 :
    print ('?')

else :
    themax = count.index(max(count))
    print(word_list[themax])