from turtle import Screen
from player import Player
from car import Car
from score import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING")
screen.tracer(0)


scoreboard = Scoreboard()
player = Player()
cars = []
for i in range (20):
    car = Car()
    cars.append(car)

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_active = True

while game_is_active:
    screen.update()
    time.sleep(0.1)
    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.reset_car((320, random.randint(-240, 260)))
        if car.distance(player) < 15:
            scoreboard.game_over()
            game_is_active = False
    if player.ycor() > 280:
        scoreboard.increase_score()
        player.go_to_start()



screen.exitonclick()