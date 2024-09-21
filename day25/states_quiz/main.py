import turtle
from os import write

import pandas

from day18.main import color

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

screen = turtle.Screen()
screen.setup(width=800, height=550)
screen.title("US States Quiz")
image = "blank_states_img.gif"

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()


screen.addshape(image)
turtle.shape(image)

state_counter = 0

data = pandas.read_csv("50_states.csv")


def write_state(state, x, y):
    writer.setposition(x, y)
    writer.write(state)

def take_user_guess():
    answer_state = screen.textinput("Guess the state", "Enter the name of the state")
    return answer_state

def check_if_state_exists(user_answer):
    try:
        temp_check = data[data.state == user_answer].state.values[0]
        if user_answer == temp_check:
            return True
    except:
        return False
    return False

while True:
    writer.setposition(-250, 250)
    writer.write("To exit type: ''Exit '' ",align=ALIGNMENT, font=FONT)
    user_input = take_user_guess()
    checker = check_if_state_exists(user_input)
    if checker:
        write_state(data[data.state == user_input].state.values[0], data[data.state == user_input].x.values[0],
                    data[data.state == user_input].y.values[0])
        state_counter += 1
        if state_counter == 50:
            break
    if user_input == "Exit":
        writer.setposition(0,0)
        writer.write(f"Your score is {state_counter} / 50", align=ALIGNMENT, font=FONT)
        break


screen.mainloop()