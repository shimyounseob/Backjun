import sys
N = int(sys.stdin.readline())

stack = []
for i in range(N) :
    word = list(sys.stdin.readline().split())

    if word[0]  == "1" :
        stack.append(word[1])

    if word [0] == "2" :
        if stack == [] :
            print(-1)

        else:
            print(stack.pop())

    if word [0] == "3" :
        print(len(stack))

    if word[0] == "4" :
        if stack ==[]  :
            print(1)
        else :
            print(0)

    if word[0] == "5" :
        if stack == []:
            print(-1)

        else :
            print(stack[-1])



