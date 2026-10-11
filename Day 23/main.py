import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()
screen.onkey(key = " ",fun = player.go)
game_is_on = True
no_of_cars = random.randint(40,50)
all_cars = []
select_cars = []
car_speed = 5
for c in range(no_of_cars):
    c = CarManager()
    all_cars.append(c)
print(len(all_cars))
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for crashed_car in all_cars:
        if player.distance(crashed_car) < 30 and player.ycor() - crashed_car.ycor() < 5:
            scoreboard.end()
            game_is_on = False
    if player.ycor() > 280:
        player.reset_position()
        car_speed += 10
        scoreboard.update_score()

    car = random.choice(all_cars)
    rand = random.randint(1,6)
    if rand == 1:
        select_cars.append(car)
    for current_car in all_cars:
        current_car.speed(car_speed)
        if current_car in select_cars:
            if current_car.xcor() <= -340:
                select_cars.remove(current_car)
                current_car.replace()
            current_car.move()
screen.exitonclick()

