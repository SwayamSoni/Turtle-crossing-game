COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_car()
    def create_car(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.teleport(350, random.randint(-250,250))
        self.left(180)
        self.color(random.choice(COLORS))
        self.all_cars.append(self)
    def move(self):
        if self.xcor() > -350:
            self.forward(5)
    def replace(self):
        self.teleport(350, random.randint(-250, 250))
        self.color(random.choice(COLORS))
