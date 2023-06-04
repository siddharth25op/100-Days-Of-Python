from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-220, 260)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.goto(-220, 260)
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over\nYour score was {self.score}", align="center", font=("Arial", 25, "normal"))
