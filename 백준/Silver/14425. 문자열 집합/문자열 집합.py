N, M = map(int, input().split())
set_s = {}

for i in range(N):
    string = input()
    set_s[string]= 1

result = 0

for i in range(M):
    string_2 = input()
    if string_2 in set_s :
        result += 1

print(result)
