from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(colors))
        self.penup()
        self.setheading(180)
        self.goto(random.randint(320,1200),random.randint(-240,260))
        self.speed = 10

    def move(self):
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.ycor())

    def reset_car(self, position):
        self.goto(position)

    def increase_speed(self):
        self.speed = self.speed + 2