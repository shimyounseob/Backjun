x,y, w,h = map (int, input().split())

distance = []

if x <= w  :
    distance.append(x - w)

elif  x > w  :
    distance.append(x - w)

if x <= 0  :
    distance.append(x - w)

elif  x > 0  :
    distance.append(x - 0)

if y <= h  :
    distance.append(y - h)

elif  y > h  :
    distance.append(h - y)

if y <= 0  :
    distance.append(y - 0 )

elif  y > 0  :
    distance.append(0 - y)

new_distance = []

for j in distance :
    if j < 0 :
        new_distance.append(j * -1)
    else :
        new_distance.append(j)

find_min = []

for k in new_distance :
    if find_min == [] :
        find_min.append(k)
    else :
        if find_min[0] > k :
            find_min.remove(find_min[0])
            find_min.append(k)

print(*find_min)