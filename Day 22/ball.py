from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.movespeed = 0.1

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.movespeed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.movespeed = 0.1
        self.bounce_x()
