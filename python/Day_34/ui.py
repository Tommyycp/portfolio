from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.current_score = 0
        self.score = Label(self.window, text=f"Score:{self.current_score}")
        self.score.grid(column=1, row=0)

        self.display = Canvas(self.window, width=300, height=250, bg="white")
        self.question = self.display.create_text(150, 125, width=280, fill="black", font=("Arial", 20, "italic"))
        self.display.grid(column=0, row=1, columnspan=2, pady=50)

        self.tick_object = PhotoImage(file="./images/true.png")
        self.tick = Button(self.window, image=self.tick_object, command=self.tick)
        self.tick.grid(column=0, row=2)

        self.cross_object = PhotoImage(file="./images/false.png")
        self.cross = Button(self.window, image=self.cross_object, command=self.wrong)
        self.cross.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.display.itemconfig(self.question, text=q_text)
        self.display.config(bg="white")

    def tick(self):
        if self.quiz.check_answer("True"):
            self.display.config(bg="green")
            self.current_score += 1
            self.score.config(text=f"Score:{self.current_score}")
        else:
            self.display.config(bg="red")

        if self.quiz.still_has_questions():
            self.window.after(3000, self.get_next_question)
        else:
            self.display.itemconfig(self.question, text="The End")

    def wrong(self):
        if self.quiz.check_answer("false"):
            self.display.config(bg="green")
            self.current_score += 1
            self.score.config(text=f"Score:{self.current_score}")
        else:
            self.display.config(bg="red")

        if self.quiz.still_has_questions():
            self.window.after(3000, self.get_next_question)
        else:
            self.display.itemconfig(self.question, text="The End")
