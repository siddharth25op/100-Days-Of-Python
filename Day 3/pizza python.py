print("Welcome to python pizza.")
print("Small Pizza: $20\nMedium Pizza: $30\nLarge Pizza: $40")
size = input("What size of pizza do you want?\nS, M, L :")
bill = 0
origano = input("Do you want origano with your pizza?\nIt will cost you additional $2 for small pizza and $3 for medium and large pizza.\nY, N :")

extra_cheese = input("Do you want extra cheese with your pizza?\nIt will cost you additional $5.\nY, N :")

if size == "S":
    bill += 20
elif size == "M":
    bill += 30
elif size == "L":
    bill += 40
if origano == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 5

print(f"Your final bill is ${bill}")