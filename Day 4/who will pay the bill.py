import random
print("Welcome to the bill calculator.")
names = input("Who will pay the bill? :")

op = names.split(" ,")

len = len(op)

final_name = random.randint(0,len-1)

paying_person = op[final_name]
print(f"{paying_person} is going to pay the bill.")
