from tkinter import *

window = Tk()
window.title("Tkinter start code title")
window.minsize(width=500,height=300)


def button_clicked():
    print("I got clicked")
    entry_text = input.get()
    my_label.config(text=entry_text)

#Label
my_label = Label(text="Label text", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New text"
my_label.config(text="New text")

#Button
my_button = Button(text="Click me", command=button_clicked)
my_button.pack()

#Entry
input = Entry()
input.pack()


window.mainloop()