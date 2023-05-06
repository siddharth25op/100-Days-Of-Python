import random
rock = "Rock"
paper = "Paper"
scissor = "Scissor"

print(f"{rock}\n{paper}\n{scissor}")

rps_user = input("What you want to choose? :").lower()


list = ("Rock, Paper, Scissor").split(", ")
len = len(list)
computer_chooses = random.randint(0, len - 1)
final_com_choose = list[computer_chooses]
print(f"Computer Chooses > {final_com_choose}")
new_final_com_choose = final_com_choose.lower()
if rps_user == new_final_com_choose:
    print("Match Draw")
elif rps_user == "rock" and new_final_com_choose == "paper":
    print("You Lose")
elif rps_user == "rock" and new_final_com_choose == "scissor":
    print("You Won")
elif rps_user == "paper" and new_final_com_choose == "rock":
    print("You Won")
elif rps_user == "paper" and new_final_com_choose == "scissor":
    print("You Lose")
elif rps_user == "scissor" and new_final_com_choose == "rock":
    print("You Lose")
elif rps_user == "scissor" and new_final_com_choose == "paper":
    print("You Won")





