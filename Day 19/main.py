from turtle import Turtle, Screen, clearscreen

poke = Turtle()
mon = Turtle()
pikachu = Turtle()
pikachu.color("yellow")
screen = Screen()
mon.pensize(15)
mon.pencolor("cyan")
def mf():
    mon.forward(10)
def mb():
    mon.backward(10)
def ac():
    mon.left(10)
def cw():
    mon.right(10)
def clear():
    mon.clear()
    mon.penup()
    mon.home()
    mon.pendown()
screen.listen()
screen.onkey(key="w", fun=mf)
screen.onkey(key="s", fun=mb)
screen.onkey(key="a", fun=ac)
screen.onkey(key="d", fun=cw)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
