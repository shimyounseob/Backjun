angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

sum_angle = angle3 + angle2 + angle1

if sum_angle == 180:
    if angle3 == angle2 == angle1 :
        print("Equilateral")

    elif angle3 == angle2 or angle1 == angle2 or angle1 == angle3 :
        print("Isosceles")

    else:
        print("Scalene")

else :
    print("Error")