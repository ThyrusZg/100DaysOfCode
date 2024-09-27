from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    length = random.randint(8, 18)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_input.insert(0, password)
    pyperclip.copy(password)

def password_checker(password):
    if 8 <= len(password) <= 18:
        if string.ascii_letters in password:
            if string.digits in password:
                if string.punctuation in password:
                    return  True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get()
    user_username = username_input.get()
    user_password = password_input.get()
    if user_website == "" or user_username == "":
        error_window = messagebox.showerror(title="Data Error", message="Username or website is empty!")
        if not password_checker(user_password):
            error_window = messagebox.showerror(title="Password Error", message="Password is not matching criteria!")
    else:
        display_message = (f"Is this correct ?\nWebsite: {user_website},\nUsername/Email: {user_username},"
                           f"\nPassword: {user_password}")
        new_window = messagebox.askquestion(title="Is data correct?", message=display_message)
        if new_window == "yes":
            with open("data.txt", "a") as fin:
                fin.write(f"{user_website} | {user_username} | {user_password}\n")
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)
        else:
           return None

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass - Password Manager")
window.minsize(450, 400)
canvas = Canvas(window, width=200,height=220)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=lock_image)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1,column=0, pady=5)

website_input = Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username:")
username_label.grid(row=2,column=0, pady=5)

username_input = Entry(width=50)
username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0, pady=5)

password_input = Entry(width=25)
password_input.grid(row=3, column=1)

password_generate_button = Button(text="Generate Password", width=20, command=generate_password)
password_generate_button.grid(row=3, column=2)

password_save_button = Button(text="Save Password", width=40, command=save)
password_save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

