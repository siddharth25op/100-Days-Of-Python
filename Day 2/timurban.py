age = input("What is your age? :")
int_age = int(age)
left_years = 90 - int_age
left_days = left_years * 365
left_weeks = left_years * 52
left_months = left_years * 12
print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")

