from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass - Password Manager")
window.minsize(500, 600)
canvas = Canvas(window, width=200,height=220)
tomato_image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1,column=0, padx=5, pady=5)

website_input = Entry(width=50)
website_input.grid(row=1, column=1)

username_label = Label(text="Email/Username:")
username_label.grid(row=2,column=0, padx=5, pady=5)

username_input = Entry(width=50)
username_input.grid(row=2, column=1)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0, padx=5, pady=5)

password_input = Entry(width=25)
password_input.grid(row=3, column=1)

password_generate_button = Button(text="Generate Password", width=25)
password_generate_button.grid(row=3, column=2)

window.mainloop()