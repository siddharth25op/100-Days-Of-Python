from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
Move_Distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.monster = []
        self.create_snake()
        self.head = self.monster[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_monster(position)

    def add_monster(self, position):
        mon = Turtle(shape="square")
        mon.color("white")
        mon.penup()
        mon.goto(position)
        self.monster.append(mon)

    def extend(self):
        self.add_monster(self.monster[-1].position())

    def move(self):
        for sna_num in range(len(self.monster) - 1, 0, -1):
            newx = self.monster[sna_num - 1].xcor()
            newy = self.monster[sna_num - 1].ycor()
            self.monster[sna_num].goto(newx, newy)
        self.head.forward(Move_Distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
