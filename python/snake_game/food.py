from turtle import Turtle
import random as r


class Food:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.food = None
        self.x_cor = None
        self.y_cor = None

    def create_food(self):
        food = Turtle(shape='circle')
        food.color('pink')
        self.x_cor = r.randint(-self.screen_width/2+30, self.screen_width/2-30)
        self.y_cor = r.randint(-self.screen_height/2+30, self.screen_height/2-30)
        food.penup()
        food.goto(x=self.x_cor, y=self.y_cor)
        self.food = food

    def random(self):
        self.x_cor = r.randint(-self.screen_width/2+30, self.screen_width/2-30)
        self.y_cor = r.randint(-self.screen_height/2+30, self.screen_height/2-30)
        self.food.goto(x=self.x_cor, y=self.y_cor)