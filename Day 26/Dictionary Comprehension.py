#####  new = {new_key:new_value for item in list} #####

##### new = {new_key:new_value for (key,value) in dict.items()}  #####

##### new = {new_key:new_value for (key,value) in dict.items() if test} #####

# import random
# names = ["Siddharth", "Tanjiro", "Nezuko", "Genya", "Zinitsu", "Muzan", "Gyoko", "Mitsuri"]
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)

# passed_students = {
#     'Siddharth': 55,
#     'Tanjiro': 42,
#     'Nezuko': 78,
#     'Genya': 80,
#     'Zinitsu': 57,
#     'Muzan': 60,
#     'Gyoko': 50,
#     'Mitsuri': 63
# }
#
# new = {student: score for (student,score) in passed_students.items() if score >= 60}
#
# print(new)
#
# String = "Tanjiro is awesome."
#
# result = {word: len(word) for word in String.split()}
#
# print(result)

# passed_students = {
#     'Siddharth': 12,
#     'Tanjiro': 14,
#     'Nezuko': 15,
#     'Genya': 14,
#     'Zinitsu': 21,
#     'Muzan': 22,
#     'Gyoko': 24,
#     'Mitsuri': 21
# }
#
# fare = {names: (passed_students[names] * 9/5) + 32 for names in passed_students}
#
# print(fare)

import pandas
student_dict = {
    "students": ["Siddharth", "Tanjiro", "Nezuko"],
    "Score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


##### Loop through a data frame #####

for (index, row) in student_data_frame.iterrows():
    print(row.Score)
