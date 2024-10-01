from tkinter import *
from data import Data

THEME_COLOR = "#375362"
GREEN = "#90ee90"
RED = "#FF474C"
FONT = ("Helvetica", 12, "bold")
TIMER = 2000
CURRENT_SCORE = 0

def check_answer(choice):
    global CURRENT_SCORE
    if choice == (new_question.question["answer"] == "True"):
        CURRENT_SCORE += 1
        canvas.config(bg=GREEN)
    else:
        canvas.config(bg=RED)

    canvas.itemconfig(score, text=f"Score: {CURRENT_SCORE}")

    window.after(TIMER, get_new_question)

def get_new_question():
    global new_question
    new_question = Data()

    canvas.config(bg=THEME_COLOR)
    canvas.itemconfig(question_text, text=new_question.question["question"])


window = Tk()
window.title("Quizzer")
window.config(padx=50, pady=50, bg=THEME_COLOR)

wrong_image = PhotoImage(file="images/false.png")
right_image = PhotoImage(file="images/true.png")

canvas = Canvas(window, width=250, height=400, bg=THEME_COLOR, highlightthickness=0)
score = canvas.create_text(200, 10, text="Score: 0", font=FONT)
question_text = canvas.create_text(125, 200, text="", font=FONT, width=250)  # Initially empty
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong_image, highlightthickness=0, bg=THEME_COLOR, command=lambda: check_answer(False))
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_image, highlightthickness=0, bg=THEME_COLOR, command=lambda: check_answer(True))
right_button.grid(row=1, column=1)

get_new_question()

window.mainloop()
