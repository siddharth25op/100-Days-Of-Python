print("Welcome to ODD EVEN checker.")
number = int(input("Enter a number to check weather it is odd or even:"))
div = number % 2

if div == 0:
    print(f"Yes, {number} is an even number.")
else:
    print(f"{number} is an odd number")