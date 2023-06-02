from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        game_is_on = False
        score.gameover()

    for monster in snake.monster[1:]:
        if snake.head.distance(monster) < 10:
            game_is_on = False
            score.gameover()


screen.exitonclick()
