FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.teleport(-200,250)
        self.level = 1
        self.write(arg = f"Level: {self.level}",align = "Center",font = ("Courier", 24, "normal"))
    def update_score(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="Center", font=("Courier", 24, "normal"))
    def end(self):
        self.teleport(0, 0)
        self.write("Game Over", False, align="center", font=FONT)

