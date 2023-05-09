student_height = input("Enter the height of students: ").split()
for i in range(0, len(student_height)):
    student_height[i] = int(student_height[i])
print(student_height)

total_height = 0
for height in student_height:
    total_height += height
print(total_height)
number_of_heights = 0

for student in student_height:
    number_of_heights += 1
print(number_of_heights) 

average_height = int(total_height/number_of_heights)
print(round(average_height))