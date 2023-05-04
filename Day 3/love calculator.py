print("Welcome to Love Calculator.")

name1 = input("Enter the first name:").lower()
name2 = input("Enter the second name:").lower()

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")
l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

true = str(t + r + u + e)
love = str(l + o + v + e)
truelove = true + love

if int(truelove) <= 10 or int(truelove) >= 90:
    print("You go together like coke and mentos.")
elif int(truelove) > 40 or int(truelove) < 50:
    print("You are alright together.")

print(f"{truelove}%")