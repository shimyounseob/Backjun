numb = list(map(int, input().split()))

eq_1 = numb[0:3]
eq_2 = numb[3:6]

eq_x = []
eq_y = []

for x in range(-999,1000) :
    for y in range (-999,1000) :
        if eq_1[0] * x + eq_1[1] * y == eq_1[2] and eq_2[0] * x + eq_2[1] * y == eq_2[2]:
            eq_x.append(x)
            eq_y.append(y)

print(*eq_x, *eq_y)

