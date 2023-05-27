import random
print("Logo Here")

user_selected_level = input("Enter e for easy level and h for hard level :")
random_number = random.randint(1, 100)
if user_selected_level == "e":
    attempts = 0
    while not attempts == 10:
        user_number = int(input("Enter a number to guess :"))
        if user_number < random_number:
            print("Too Low")
            attempts = attempts + 1
            if attempts == 10:
                print("You are out of attempts.\nQuitting the game now.")
        elif user_number > random_number:
            print("Too High")
            attempts = attempts + 1
            if attempts == 10:
                print("You are out of attempts.\nQuitting the game now.")
        elif user_number == random_number:
            print("Yes, you guessed right number.\nYou Win")
            attempts = 10
elif user_selected_level == "h":
    attempts = 0
    while not attempts == 5:
        user_number = int(input("Enter a number to guess :"))
        if user_number < random_number:
            print("Too Low")
            attempts = attempts + 1
            if attempts == 5:
                print("You are out of attempts.\nQuitting the game now.")
        elif user_number > random_number:
            print("Too High")
            attempts = attempts + 1
            if attempts == 5:
                print("You are out of attempts.\nQuitting the game now.")
        elif user_number == random_number:
            print("Yes, you guessed right number.\nYou Win")
            attempts = 5
else:
    print("Wrong Input")

