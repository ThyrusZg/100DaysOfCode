import colorgram
import turtle as t
import random



tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

colors = colorgram.extract('image.png', 15)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    extracted_color = (r,g,b)
    rgb_colors.append(extracted_color)


tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.pendown()

number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tim.dot(20,random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if dot_count % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()

screen = t.Screen()
screen.exitonclick()