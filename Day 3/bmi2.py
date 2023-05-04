print("Welcome to BMI intrepreter.")
height = float(input("Enter Your Height:"))
weight = int(input("Enter Your weight:"))
bmi = weight / height ** 2

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 or bmi < 25:
    print("Your weight is normal.")
elif bmi >= 25 or bmi < 30:
    print("You are overweight.")
elif bmi >= 30 or bmi < 35:
    print("Your weight is obese.")
else:
    print("You are clinically obese.")
    
print(round(bmi, 2))