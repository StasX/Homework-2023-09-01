students_grades = []
for i in range(3):
    students_grades.append([])
    line = i+1
    for j in range(1, 5):
        user_input = input(f"Please enter grade #{j} of student #{line}: ")
        grade = int(user_input)
        students_grades[i].append(grade)


for student_grades in students_grades:
    for grade in student_grades:
        print(grade, end=" ")
    print()


avg_grades = []
for student_grades in students_grades:
    total = 0
    for grade in student_grades:
        total += grade
    avg = total/len(student_grades)
    avg_grades.append(avg)


max_avg = avg_grades[0]
for avg in avg_grades:
    if avg > max_avg:
        max_avg = avg

print(f"Max average grade is: {max_avg}")

avg_grades = []
for student_grades in students_grades:
    total = 0
    for grade in student_grades:
        total += grade
    avg = total/len(student_grades)
    avg_grades.append((avg, student_grades))


min_avg = avg_grades[-1]
for i in range(len(avg_grades)-1, 1, -1):
    if avg_grades[i][0] < min_avg[0]:
        min_avg = avg_grades[i][0]

avg = min_avg[0]
grades = min_avg[1]
stringified_grades = []

for grade in grades:
    stringified_grades.append(str(grade))

grades = " ".join(stringified_grades)

print(f"Min average of grades ({grades}) is {avg}")
