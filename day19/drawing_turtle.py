import turtle as t

tim = t.Turtle()
screen = t.Screen()


def right():
    tim.setheading(0)
    tim.forward(10)

def up():
    tim.setheading(90)
    tim.forward(10)

def left():
    tim.setheading(180)
    tim.forward(10)

def down():
    tim.setheading(270)
    tim.forward(10)

def pen_up():
    tim.penup()

def pen_down():
    tim.pendown()

def position_start():
    tim.penup()
    tim.setheading(180)
    tim.forward(400)
    tim.pendown()
    tim.setheading(0)

def clean():
    tim.clear()

position_start()
screen.listen()
screen.onkey(key="d", fun=right)
screen.onkey(key="w", fun=up)
screen.onkey(key="a", fun=left)
screen.onkey(key="s", fun=down)
screen.onkey(key="q", fun=pen_up)
screen.onkey(key="r", fun=pen_down)
screen.onkey(key="space", fun=clean)

screen.exitonclick()