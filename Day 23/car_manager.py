from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle("square")
            new_cars.color(random.choice(COLORS))
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            new_cars.penup()
            newy = random.randint(-230, 230)
            new_cars.goto(300, newy)
            self.cars.append(new_cars)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.cars_speed)

    def speedup(self):
        self.cars_speed += MOVE_INCREMENT
