while True :

    numb = int(input())

    if numb == -1 :
        break

    factor = []

    for i in range(1, numb) :
        if numb % i == 0 :
            factor.append(i)

    match = 0

    for j in factor :
       if j != numb:
           match += j

    if match != numb :
        print("%d is NOT perfect." %numb)

    elif match == numb :
        result = " + ".join(map(str, factor))
        print("%d = %s" %(numb,result))


