t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)

    for j in s:
        p_comp = j * r
        print(p_comp, end='')

    print()