students = ["Student 1", "Student 2", "Student 3", "Student 4"]
subjects = ["Python", "Maths", "Web Development"]
marks = [
    [80, 75, 90],
    [65, 70, 60],
    [95, 92, 88],
    [72, 85, 78]
]

averages = []
for i, row in enumerate(marks):
    total = sum(row)
    average = total / len(row)
    averages.append(average)
    print(students[i], "- total:", total, "average:", round(average, 2))

top_index = averages.index(max(averages))
print("Top performer:", students[top_index])

for j, subject in enumerate(subjects):
    subject_total = 0
    for i in range(len(marks)):
        subject_total += marks[i][j]
    subject_average = subject_total / len(marks)
    print(subject, "average:", round(subject_average, 2))
    if subject_average < 70:
        print("Low-performing subject:", subject)
