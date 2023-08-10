n = int(input())

x_collection = []
y_collection = []

for i in range(n) :
    x, y = map(int, input().split())
    x_collection.append(x)
    y_collection.append(y)

min_x = []

for x_one in x_collection :
    if min_x == [] :
        min_x.append(x_one)

    elif min_x[0] > x_one :
        min_x.remove(min_x[0])
        min_x.append(x_one)

max_x = []

for x_one in x_collection:
    if max_x == []:
        max_x.append(x_one)

    elif max_x[0] < x_one:
        max_x.remove(max_x[0])
        max_x.append(x_one)

min_y = []

for y_one in y_collection:
    if min_y == []:
        min_y.append(y_one)

    elif min_y[0] > y_one:
        min_y.remove(min_y[0])
        min_y.append(y_one)

max_y = []

for y_one in y_collection:
    if max_y == []:
        max_y.append(y_one)

    elif max_y[0] < y_one:
        max_y.remove(max_y[0])
        max_y.append(y_one)

x_width = max_x[0] - min_x[0]
y_width = max_y[0] - min_y[0]

print(x_width * y_width)
