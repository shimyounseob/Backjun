import sys

array = []

for i in range(10) :
    numb = int(sys.stdin.readline())
    divide = numb % 42
    array.append(divide)

differ = set(array)
differ = len(differ)

print(differ)