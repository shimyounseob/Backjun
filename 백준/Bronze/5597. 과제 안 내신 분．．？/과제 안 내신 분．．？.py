import sys

attendance = [0] * 30

for i in range(28) :
    check = int(sys.stdin.readline())
    attendance[check-1] = check

for i in range(len(attendance)) :
    if attendance[i] == 0:
        print (i+1)

    else :
        continue

