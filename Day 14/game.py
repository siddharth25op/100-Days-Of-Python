import random
import data
import art
import os

def game():
    print(art.logo)
    game_end = False
    score = 0
    while not game_end:
        random_person_1 = random.choice(data.data)
        print(f"Compare A: {random_person_1['name']}, a {random_person_1['description']}, from {random_person_1['country']}.")

        print(art.vs)

        random_person_2 = random.choice(data.data)
        print(f"Against B: {random_person_2['name']}, a {random_person_2['description']}, from {random_person_2['country']}.")

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_input == "a" and random_person_1['follower_count'] > random_person_2['follower_count'] or user_input == "b" and random_person_2['follower_count'] > random_person_1['follower_count']:
                os.system("clear")
                score = score + 1
                print(art.logo)
                print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_end = True
game()