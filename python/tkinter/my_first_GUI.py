# Import all Classes from the module tkinter
from tkinter import *

# tkinter.TK() calling the TK class to initialize a window object
window = Tk()
# title.method, passing "Tommy's First GUI Program" as a positional argument
window.title("Tommy's First GUI Program")
# minsize method, passing in height and width as keywords arguments
window.minsize(height=500, width=500)
window.config(padx=20, pady=20)

# tkinter.Label method, passing in keyword arguments, text and font.
my_label = Label(text="New Button", font=("Times", 36, "bold"))
# Introduces a geometry manager
my_label.grid(row=0, column=0)


# Setting up an event for what happened when the button is clicked
def button_clicked():
    my_label.config(text=prompt.get())

# Button
button = Button(text="Button")
button.grid(row=1, column=1)

# Entry
prompt = Entry(width=10)
prompt.grid(column =3, row=2)

# Button2
button_two =Button(text="New Button")
button_two.grid(column=2, row=0)


# This is a while-true statement that keeps running to listen for events
window.mainloop()
