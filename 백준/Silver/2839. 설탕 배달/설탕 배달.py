sugar = int(input())

min_bag = []

for i in range(0,1001) :
    for j in range(0,1668) :
        if (i * 5) + (j * 3) == sugar :
            sum_bag = i + j

            if min_bag == [] :
                min_bag.append(sum_bag)

            elif  min_bag[0] > sum_bag :
                min_bag.remove(min_bag[0])
                min_bag.append(sum_bag)


if min_bag == [] :
    print(-1)

else:
    print(*min_bag)

