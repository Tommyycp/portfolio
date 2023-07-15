from turtle import Turtle, Screen
FONT = ('Times News Roman', 24, 'normal')

class ScoreBoard(Turtle):

    def __init__(self, screen_width, screen_height, object_name):
        self.screen_width = screen_width / 2
        self.screen_height = screen_height / 2
        super().__init__()
        self.up()
        self.shapesize(10,10,10)
        self.ht()
        self.color('white')
        self.goto(x=0, y=self.screen_height - 75)
        self.write(object_name, False, align='center', font=FONT)