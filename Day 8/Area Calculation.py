height = int(input("Enter the height of the wall: "))
width  = int(input("Enter the widht of the wall: "))

coverage = 5

def can(height, width, coverage):
    area = (height * width) / coverage
    print(f"You will need {round(area)} cans of paint.")

can(height, width, coverage)