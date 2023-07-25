numb = int(input())

result = []
unit = [25,10,5,1]

# for 문을 통해 입력값을 numb 만큼 받음
for i in range(numb) :
    change = int(input())

# for 문을 통해 25, 10, 5, 1을 차례로 나누기 해줌
# 몫을 list에 append 해줌

    for j in unit :

       if  change >= j :
            quotient = change // j
            change = change % j
            result.append(quotient)

       else :
           result.append(0)


    print(*result)
    result =[]
