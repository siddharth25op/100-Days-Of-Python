import random
from turtle import Turtle, Screen
is_race_on = False
screen = Screen()
screen.setup(width=1000, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "blue", "green", "yellow", "purple", "pink"]
pos = -180
all_turtles = []
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle])
    new_turtle.penup()
    pos += 40
    new_turtle.goto(x=-480, y=pos)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 460:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won, {winning_color} turtle did it for you.")
            else:
                print(f"You Lost, {user_bet} turtle was not able to do it.")
                print(f"{winning_color} turtle won the race.")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
