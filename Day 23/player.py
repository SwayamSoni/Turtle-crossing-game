STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.left(90)
        self.teleport(0,-280)
    def go(self):
        self.forward(10)

    def reset_position(self):
            self.teleport(0,-280)