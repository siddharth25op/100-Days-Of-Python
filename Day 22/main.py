from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((390, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lpoint()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint()

screen.exitonclick()
