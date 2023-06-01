# import colorgram
# # color = colorgram.Color('Heading.jpg', 20)
# color = colorgram.extract('Heading.jpg', 20)
# for col in color:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)
import random
import turtle as t
rgb_color = [(252, 249, 243), (218, 151, 92), (44, 103, 140), (155, 56, 91), (225, 69, 96), (240, 207, 94), (137, 80, 65), (23, 45, 65), (218, 121, 160), (114, 175, 211), (145, 184, 156), (50, 32, 28), (205, 229, 221), (42, 182, 154), (251, 168, 154), (165, 20, 73), (189, 144, 33), (122, 44, 35), (235, 74, 71), (201, 231, 244)]
mon = t.Turtle()
screen = t.Screen()

mon.pensize(10)
t.colormode(255)
mon.speed("fastest")
for stop in range(5):
    for _ in range(10):
        mon.dot(25, random.choice(rgb_color))
        mon.penup()
        mon.forward(60)
    for ag in range(1):
        mon.hideturtle()
        mon.left(90)
        mon.forward(60)
        mon.left(90)
        mon.forward(600)
        mon.right(180)
        mon.showturtle()
mon.hideturtle()
mon.setpos(0, 0)
screen.exitonclick()
