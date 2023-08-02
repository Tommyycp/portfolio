from tkinter import *
from PIL import ImageTk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password manager")
root.geometry('600x400')
# root.config(padx= 100, pady=100)

lock_img_frame = ImageTk.PhotoImage(file='logo.png')
padlock_img = Label(image=lock_img_frame)
padlock_img.grid(column=1,row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_text = StringVar()
website_textbox = Entry(textvariable=website_text, width=52)
website_textbox.grid(column=1, row=1, columnspan=2, sticky='we')

user_name_label = Label(text='Email/Username:')
user_name_label.grid (column=0, row=2)

user_name_text = StringVar()
user_name_textbox = Entry(textvariable=user_name_text, width=52)
user_name_textbox.grid(column=1, row=2, columnspan=2, sticky='we')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_text = StringVar()
Password_textbox = Entry(textvariable=password_text, width=35)
Password_textbox.grid(column=1, row=3, sticky='we')

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44)
add_button.grid(column=1, row=4, columnspan=2)






root.mainloop()