a,b,c = map(int,input().split())

list_abc = [a,b,c]
max_abc = max(list_abc)
list_abc.remove(max_abc)


if list_abc[0]+list_abc[1] > max_abc :
    result = list_abc[0]+list_abc[1] + max_abc

else :
    list_abc = [a, b, c]
    max_abc = max(list_abc)
    list_abc.remove(max_abc)
    two = list_abc[0] + list_abc[1]
    result = two + (two - 1)


print(result)