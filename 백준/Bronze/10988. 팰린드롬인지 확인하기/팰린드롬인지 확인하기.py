word = list(input())

n = len(word)-1
check = 0

for i in range(len(word)//2) :
    if word[i] == word[n-i] :
        check += 1
    else :
        break

if check == len(word)//2 :
    print(1)
else :
    print(0)



