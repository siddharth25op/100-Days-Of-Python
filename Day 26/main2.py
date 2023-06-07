# with open("file1.txt") as file1:
#     list1 = []
#     for ele in file1:
#         list1.append(int(ele))
#
# with open("file2.txt") as file2:
#     list2 = []
#     for ele in file2:
#         list2.append(int(ele))
#
# result = []
# for num in list1:
#     for num1 in list2:
#         if num == num1:
#             result.append(num)
#
# print(result)

with open("file1.txt") as file1:
    file1_data = file1.readlines()
with open("file2.txt") as file2:
    file2_data = file2.readlines()

result = [int(num) for num in file1_data if num in file2_data]

print(result)
