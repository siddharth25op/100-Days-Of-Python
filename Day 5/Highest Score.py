student_score = input("Enter the student score:").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
total_score = 0
for total in student_score:
    total_score += 1
print(total_score)

highest_score = 0
for highest in student_score:
    if highest > highest_score:
        highest_score = highest
print(f"Highest score in the list is: {highest_score}")