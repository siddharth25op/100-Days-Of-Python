from turtle import Turtle
ALINGMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 200)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

    def gameover(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYour Score is {self.score}", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALINGMENT, font=FONT)

