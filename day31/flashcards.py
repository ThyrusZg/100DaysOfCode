from tkinter import *
import pandas
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
TIMER = 3000
FONT_WORD = ("Ariel", 60, "bold")
FONT_LANGUAGE = ("Ariel", 40, "italic")
FRENCH = "French"
ENGLISH = "English"
WORD = None
KNOWN_WORDS = []
# ---------------------------- FLIP CARDS ------------------------------- #
def flip_french_card_side():
    words = words_finder()
    global WORD
    WORD = words.values[0][0]
    canvas.itemconfig(card_image,image=card_front_image)
    canvas.itemconfig(langauge_text, text=FRENCH)
    canvas.itemconfig(word_text, text=words.values[0][0])
    window.after(TIMER, flip_english_card_side, words)

def flip_english_card_side(words):
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(langauge_text, text=ENGLISH)
    canvas.itemconfig(word_text, text=words.values[0][1])

# ---------------------------- CORRECT ANSWER ------------------------------- #
def correct_answer():
    global WORD
    global KNOWN_WORDS
    KNOWN_WORDS.append(WORD)
    print(KNOWN_WORDS)
    WORD = None
    flip_french_card_side()

# ---------------------------- FIND WORDS ------------------------------- #
def words_finder():
    global KNOWN_WORDS
    try:
        data = pandas.read_csv("data/french_words.csv")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found")
    else:
        while True:
            row = data.sample()
            if row.values[0][0] not in KNOWN_WORDS:
                break
            elif len(data) == len(KNOWN_WORDS):
                done_message = "You know all words, please update csv in order to play more"
                if messagebox.showinfo(title="DONE",message=done_message):
                    window.destroy()
            else:
                continue
    return row

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

canvas = Canvas(window, width=800,height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(0, 0, image=card_back_image, anchor="nw")
langauge_text = canvas.create_text(400, 150, text="FRENCH", font=FONT_LANGUAGE)
word_text = canvas.create_text(400, 263, text="word", font=FONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button=Button(image=wrong_image, highlightthickness=0,bg=BACKGROUND_COLOR, command=flip_french_card_side)
wrong_button.grid(row=1, column=0)

right_button=Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=correct_answer)
right_button.grid(row=1, column=1)
flip_french_card_side()

window.mainloop()