# 과목 평점 설정 (A+ = 4.5... etc)
grade_rank = ["A+","A0","B+","B0","C+","C0","D+","D0","F"]
grade_score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어짐

credit_sum = 0
list_grade = []
listcrd = []

for i in range(20) :
    name, credit,grade = input().split()
    credit = float(credit)


    # 전공 이름 및 성적 리스트
    # P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 함
    if grade == 'P' :
        pass
    else :
        list_grade.append(grade)
        listcrd.append(credit)

# 전공 평점 (전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값) 구하기

numerator = 0

for j in range(len(list_grade)):

    # 과목 grade의 score가 몇점인지 불러옴
    grade_index = grade_rank.index(list_grade[j])
    score = grade_score [grade_index]

    crd = listcrd[j]
    crd = float(crd)

    credit_sum += crd

    numerator += crd * score

result = numerator / credit_sum

print("%.6f" % result)

