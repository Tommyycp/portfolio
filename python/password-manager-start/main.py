from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pyperclip
import random as r
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator(letter=8, number=5, symbols=3):
    password_textbox.delete(0, END)
    password = r.choices(LETTERS, k=letter) + r.choices(NUMBERS, k=number) + r.choices(SYMBOLS, k=symbols)
    password = r.sample(password, k=len(password))
    password = "".join(password)
    password_textbox.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Success!", message=f"{password} is now in your clipboard and ready for use.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_text.get()
    username = user_name_text.get()
    password = password_text.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You've left some fields blank")
    else:
        is_okay = messagebox.askyesno(title="Please confirm the entry", message=f"Website: {website} \n" \
                                                                      f"username: {username} \n"
                                                                      f"password: {password}\n"
                                                                      f"Click Yes to confirm entry")
        if is_okay:
            with open(file="./password_content.txt", mode="a", encoding="utf-8") as f:
                f.write(f"Website: {website} | Username: {username} | Password: {password}\n")
                website_textbox.delete(0, END)
                user_name_textbox.delete(0, END)
                password_textbox.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password manager")
root.geometry('600x400')
# root.config(padx= 100, pady=100)

lock_img_frame = ImageTk.PhotoImage(file='logo.png')
padlock_img = Label(image=lock_img_frame)
padlock_img.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_text = StringVar()
website_textbox = Entry(textvariable=website_text, width=52)
website_textbox.grid(column=1, row=1, columnspan=2, sticky='we')
website_textbox.focus()

user_name_label = Label(text='Email/Username:')
user_name_label.grid(column=0, row=2)

user_name_text = StringVar()
user_name_textbox = Entry(textvariable=user_name_text, width=52)
user_name_textbox.grid(column=1, row=2, columnspan=2, sticky='we')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_text = StringVar()
password_textbox = Entry(textvariable=password_text, width=35)
password_textbox.grid(column=1, row=3, sticky='we')

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

root.mainloop()