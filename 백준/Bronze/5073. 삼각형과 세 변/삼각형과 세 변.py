while True :
    a, b, c = map(int, input().split())

    list_abc = [a, b, c]
    max_abc = max(list_abc)
    list_abc.remove(max(list_abc))
    another_list = list_abc

    if a == 0 and b == 0 and c ==0 :
        break

    if max_abc < another_list[0] + another_list[1] :
        if a == b == c :
            print("Equilateral")

        elif a == b or b == c or a == c :
            print("Isosceles")

        else :
            print("Scalene")

    else :
        print("Invalid")