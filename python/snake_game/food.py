from turtle import Turtle
import random as r


class Food:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.food = self.create_food()

    def create_food(self):
        food = Turtle(shape='circle')
        food.color('pink')
        x_cor = r.randint(-self.screen_width/2+30, self.screen_width/2-30)
        y_cor = r.randint(-self.screen_height/2+30, self.screen_height/2-30)
        food.penup()
        food.goto(x=x_cor, y=y_cor)
        return food

    def random(self):
        x_cor = r.randint(-self.screen_width/2+30, self.screen_width/2-30)
        y_cor = r.randint(-self.screen_height/2+30, self.screen_height/2-30)
        self.food.goto(x=x_cor, y=y_cor)