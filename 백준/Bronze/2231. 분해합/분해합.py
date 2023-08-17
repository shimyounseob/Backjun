numb = int(input())

real_result = []

# 모든 숫자를 for문을 돌려서 str으로 변환해줌
for i in range(1,1000001) :
    str_i = str(i)

    sum_numb = 0

    for j in range(len(str_i)) :
        sum_numb += int(str_i[j])

        result = i + sum_numb

    if result == numb :
        real_result.append(i)



if real_result == [] :
    print(0)
else :
    print(min(real_result))

