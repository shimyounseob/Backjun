import sys

grade_list = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0','F']
grade_score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

num_sum = 0
total = 0

for i in range(20):
    #avg_grades = []
    _, num, grade = sys.stdin.readline().split()

    if grade == 'P':
        continue

    num = float(num)
    num_sum += num

    idx = grade_list.index(grade)
    total += num*grade_score_list[idx]

    #idx = grade_list.index(grade)
    #avg_grades.append(num*grade_score_list[idx])

print("%.6f" % (total/num_sum))