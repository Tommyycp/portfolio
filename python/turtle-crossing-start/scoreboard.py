FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, screen_width, screen_height, level):
        super().__init__()
        self.color('black')
        self.up()
        self.ht()
        self.goto(x= -screen_width/2+100, y=screen_height/2-100)
        self.level = level + 1
        self.output = f"Level {self.level}"
        self.write(arg=self.output, align='center', font = FONT)


