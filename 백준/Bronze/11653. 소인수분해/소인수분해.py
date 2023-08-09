numb = int(input())

spare = numb
divisor = []

for i in range(2, numb+1):
    divisor.append(i)

while True :
    if spare == 1 :
        break
    for i in divisor :
        if spare % i == 0 :
            print(i)
            spare = spare // i
            break
        elif spare  % i != 0 :
            pass