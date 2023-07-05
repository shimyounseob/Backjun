n = int(input())
s = list(input())

new = []

for i in range(n) :
    integer = int(s[i])
    new.append(integer)

result = sum(new)
print(result)
