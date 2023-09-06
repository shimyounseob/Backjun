import sys
N, M = map(int,sys.stdin.readline().split())

pocketmon_dic = {}
pocketmonindex_dic = {}
for i in range(N) :
    pocketmon = sys.stdin.readline().rstrip()
    pocketmon_dic[i+1] = pocketmon
    pocketmonindex_dic[pocketmon] = i + 1

question_list = []
for i in range(M) :
    question = sys.stdin.readline().rstrip()
    question_list.append(question)

for i in question_list :
    if i.isdigit() :
        print(pocketmon_dic.get(int(i)))
    else :
        print(pocketmonindex_dic.get(i))





