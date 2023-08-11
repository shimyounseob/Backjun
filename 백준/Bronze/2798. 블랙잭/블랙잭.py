N, M = map(int, input().split())

numb = list(map(int,input().split()))

result = []

for i in numb :
    for j in numb :
        for k in numb :
            if i == j or i == k or j == k :
                pass
            else :
                sum_ijk = i + j + k
                if sum_ijk <= M:
                    result.append(sum_ijk)
                else :
                    pass

print(max(result))
