import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move , "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    if player.finish_line():
        car.increase_speed()
        score.increase_level()

    for each_car in car.all_car:
        if each_car.distance(player.turtle) < 25:
            game_is_on = False
            score.game_over()# Game stop


















screen.exitonclick()