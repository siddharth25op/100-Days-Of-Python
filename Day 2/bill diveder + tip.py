print("Welcome to the tip calculator.")
amt_bill = input("What is the total bill? :")
tip_per = input("What percentage tip would you like to give? :")
bill_split = input("Number of people to split the bill? :")
a = float(tip_per)
b = float(amt_bill)
c = int(bill_split)
final_tip = a / 100
amt_with_tip = b * final_tip
final_bill = b + amt_with_tip
each_person_bill = final_bill / c
print(f"{round(each_person_bill, 2)}")