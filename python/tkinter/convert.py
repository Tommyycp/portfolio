from tkinter import *

window = Tk()
window.title("This is my converter program")
window.minsize(height=500, width=300)


def calculate():
    value = int(mile_input.get()) * 1.60934
    km_display.config(text=f"{value}")


start = Label()
start.config(width=10)
start.grid(column=0, row=0)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

mile_text = Label(text="Miles")
mile_text.grid(column=2, row=0)

is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(column=0, row=1)

km_display = Label(text=0)
km_display.grid(column=1, row=1)

km_unit = Label(text='km')
km_unit.grid(column=2, row=1)

calculate_button = Button(text='calculate', command=calculate)
calculate_button.grid(column=1, row=2)

mainloop()
