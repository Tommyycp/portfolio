from tkinter import *
from PIL import ImageTk, Image
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
check_marks = []
RESET = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def jump_front():
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


def reset():
    global check_marks
    global REPS
    global RESET
    check_marks = [mark.destroy() for mark in check_marks]
    check_marks.clear()
    REPS = 1
    RESET = 1

def adding_marks():
    global check_marks
    new_mark = Label(root, text="√", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
    new_mark.grid(column=1, row=3 + REPS // 2)
    check_marks.append(new_mark)


def count_down(total_second=WORK_MIN * 60):
    global REPS
    global RESET
    if RESET:
        RESET = 0
        timer.config(text=f"00:00")
        title.config(text=f"Reset successfully")
        return True
    elif REPS == 1:
        title.config(text="Work!", fg=RED)

    if total_second < 0:
        REPS += 1
        if REPS > 8:
            jump_front()
            title.config(text="You've completed a cycle", fg=PINK)
            return True
        elif REPS == 8:
            count_down(LONG_BREAK_MIN * 60)
            title.config(text="Long break!!", fg=GREEN)
            adding_marks()
            jump_front()
        elif REPS % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            title.config(text="Short break!", fg=GREEN)
            adding_marks()
            jump_front()
        else:
            count_down(WORK_MIN * 60)
            title.config(text="Work!", fg=RED)

    if total_second >= 0:
        minutes = total_second // 60
        second = total_second % 60
        if second < 10:
            second = f"0{second}"
        timer.config(text=f"{minutes}:{second}")
        root.after(1000, count_down, total_second - 1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Time Management Thingy")
root.config(padx=200, pady=100, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 38, 'bold'), bg=YELLOW)
title.grid(column=1, row=0)

apple_img_frame = ImageTk.PhotoImage(file="./tomato.png")
apple_img = Label(image=apple_img_frame, bg=YELLOW)
apple_img.grid(column=1, row=1)

start_button = Button(root, text="Start", highlightbackground=YELLOW, command=count_down)
start_button.grid(column=0, row=2)

reset_button = Button(root, text="Reset", highlightbackground=YELLOW, command=reset)
reset_button.grid(column=2, row=2)

timer = Label(text="00:00", font=(FONT_NAME, 38, 'bold'))
timer.grid(column=1, row=1)

root.mainloop()