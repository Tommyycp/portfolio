from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        super().__init__()
        self.up()
        self.shape('circle')
        self.speed('fastest')
        self.color('pink')
        self.move_to_random()

    def move_to_random(self):
        x_cor = r.randint(-self.width / 2 + 30, self.width / 2 - 30)
        y_cor = r.randint(-self.height / 2 + 30, self.height / 2 - 30)
        self.goto(x=x_cor, y=y_cor)