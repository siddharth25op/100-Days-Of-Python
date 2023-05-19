student_scores = {
    "Angela": "91",
    "Siddharth": "95",
    "Rohan": "41",
    "Sohan": "30",
    "Dhoni": "89"
}

student_grades = {}

for student in student_scores:
    score = int(student_scores[student])
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expections"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)