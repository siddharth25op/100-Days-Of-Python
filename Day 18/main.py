import turtle as t
import random
squirtle = t.Turtle()
t.colormode(255)
squirtle.shape("turtle")
squirtle.pensize(3)
squirtle.speed("fastest")
direction = [0, 90, 180, 270]
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     col = (r, g, b)
#     return col
# squirtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
# for _ in range(200):
#     # squirtle.pencolor(random_color())
#     squirtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     squirtle.forward(random.randint(1, 100))
#     squirtle.right(random.choice(direction))
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         squirtle.forward(100)
#         squirtle.right(angle)
# for shape_side in range(3, 11):
#     squirtle.color(random.choice(color))
#     draw_shape(shape_side)
def spirograp(size_of_gap):
    while True:
        for _ in range(int(360/size_of_gap)):
            squirtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            squirtle.circle(200)
            squirtle.setheading(squirtle.heading() + size_of_gap)


spirograp(5)
t.exitonclick()
