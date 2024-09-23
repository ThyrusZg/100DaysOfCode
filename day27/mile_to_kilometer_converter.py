from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=200,height=100)
window.maxsize(width=200,height=100)
window.config(padx=15, pady=15)

def convert():
    calculated_value = round(float(input.get()) * 1.6, 3)
    km_value_label.config(text=calculated_value)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)
# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
# is equal to Label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
# km value label
km_value_label = Label()
km_value_label.grid(column=1, row=1)
# km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
#Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()