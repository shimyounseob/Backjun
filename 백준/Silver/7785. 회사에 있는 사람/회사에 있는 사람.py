import sys
numb = int(sys.stdin.readline())

log_tally = []
for _ in range(numb) :
    name, onoff = sys.stdin.readline().rstrip().split()
    log_tally.append((name, onoff))

def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    return merge (left_list, right_list)
def merge (left, right) :
    i = 0
    j = 0
    arr = []
    while i < len(left) and j < len(right) :
        if left[i][0] <= right[j][0] :
            arr.append(left[i])
            i += 1
        else :
            arr.append(right[j])
            j += 1

    while i < len(left) :
        arr.append(left[i])
        i = i + 1
    while j < len(right) :
        arr.append(right[j])
        j = j + 1

    return arr

log_tally = merge_sort(log_tally)

log_dic = {}
for i in range(len(log_tally)) :
    name, onoff = log_tally[i]
    if onoff == 'enter':
        log_dic[name] = onoff
    if onoff ==  'leave' :
        if name in log_dic :
            del log_dic[name]

result = []
for key, value in log_dic.items() :
    if value == 'enter':
        result.append(key)

for i in range(len(result)-1, -1, -1) :
    print(result[i])