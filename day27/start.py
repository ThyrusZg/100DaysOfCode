import tkinter

window = tkinter.Tk()
window.title("Tkinter start code title")
window.minsize(width=500,height=300)
my_label = tkinter.Label(text="Label text", font=("Arial", 24, "bold"))
my_label.pack()
window.mainloop()