import sys
K = int(sys.stdin.readline())
stack = []

for _ in range(K):
    numb = int(sys.stdin.readline())
    if stack != [] :
        if numb == 0 :
            stack.pop()

        else :
            stack.append(numb)

    else :
        stack.append(numb)


if stack == [] :
    print(0)

else :
    res = 0
    for i in stack :
        res += i

    print(res)