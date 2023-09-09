import sys
word = sys.stdin.readline().rstrip()

string = set()
for i in range(len(word)) :
    for j in range(len(word)) :
        string.add(word[i:j+1])

print(len(string)-1)