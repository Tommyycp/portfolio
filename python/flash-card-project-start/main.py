from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkmacosx import Button as NewButton
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_BACK = "#9BC0B0"
SCORE = 0
CURRENT_WORD = None
GUESSED_WORD = []


# Operation
try:
    df = pd.read_csv("./data/missed_words.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
finally:
    data_dict = {r.French: r.English for i, r in df.iterrows()}
    french = list(data_dict.keys())

def flip_front():
    global CURRENT_WORD
    guess = r.choice(french)
    if guess in GUESSED_WORD:
        flip_front()
    else:
        card_front_label.config(image=card_front_img)
        title.config(text="French", bg='white')
        CURRENT_WORD = guess
        word.config(text=guess, bg='white')


def tick():
    global SCORE
    global GUESSED_WORD
    if CURRENT_WORD in GUESSED_WORD:
        pass
    else:
        GUESSED_WORD.append(CURRENT_WORD)
        SCORE += 1


def wrong():
    global CURRENT_WORD
    GUESSED_WORD.append(CURRENT_WORD)
    field = {"French": [CURRENT_WORD], "English": [data_dict[CURRENT_WORD]]}
    try:
        missed_words = pd.read_csv("./data/missed_words.csv")
        french_list = list(missed_words["French"])
    except FileNotFoundError:
        new_df = pd.DataFrame(field)
        new_df.to_csv(path_or_buf="./data/missed_words.csv", mode="w",index=False)
    else:
        if CURRENT_WORD not in french_list:
            append_df = pd.DataFrame(field)
            append_df.to_csv(path_or_buf="./data/missed_words.csv", mode="a", header=False, index=False)

def flip_back():
    global CURRENT_WORD
    translation = data_dict[CURRENT_WORD]
    card_front_label.config(image=card_back_img)
    title.config(text='English', bg=BACKGROUND_COLOR_BACK)
    word.config(text=translation, bg=BACKGROUND_COLOR_BACK)


def main_game(number=1):
    if len(GUESSED_WORD) == len(french):
        messagebox.showinfo(title="Game Over", message=f"You've exhausted  the list. Your score is {SCORE}.")
        return True
    else:
        if number > 0:
            flip_back()
        elif number < 0:
            flip_front()
        root.after(3000, main_game, number * -1)


# GUI

root = Tk()
root.config(bg=BACKGROUND_COLOR)
root.title("French Word Flashcard")

card_front_img = ImageTk.PhotoImage(Image.open("./images/card_front.png"))
card_back_img = ImageTk.PhotoImage(Image.open("./images/card_back.png"))

card_front_label = Label(root, image=card_front_img, width=800, height=526)
card_front_label.grid(column=0, row=0, columnspan=2, padx=50, pady=50)

title = Label(text='French', font=('Ariel', 60, 'italic'), bg='white', fg='black', )
title.place(x=360, y=150)

word = Label(text='Word', font=('Ariel', 80, 'bold'), bg='white', fg='black')
word.place(x=340, y=300)

wrong_img = ImageTk.PhotoImage(Image.open("./images/wrong.png"))
button_cross = NewButton(root, image=wrong_img, command=wrong, bg=BACKGROUND_COLOR)
button_cross.grid(column=0, row=1)

tick_img = ImageTk.PhotoImage(Image.open("./images/right.png"))
button_tick = NewButton(root, image=tick_img, command=tick, bg=BACKGROUND_COLOR)
button_tick.grid(column=1, row=1)

root.after(1000, flip_front)
root.after(3000, main_game)

root.mainloop()
