from turtle import Turtle, Screen
import random as r

START_ANGLE = r.randrange(150, 210)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.up()
        self.shape('circle')
        self.color('white')
        self.seth(START_ANGLE)

    def move(self):
        self.fd(10)

    def bounce_paddle(self):
        if 91 <= self.heading() <= 269:
            randomness = r.randrange(-30,30)
            self.seth(randomness)
        elif 270 <= self.heading() <= 360 or 0 <= self.heading() <= 90:
            randomness = r.randrange(145, 215)
            self.seth(randomness)
        self.fd(10)

    def bounce_wall(self):
        if 270 < self.heading() < 360:
            randomness = r.randrange(20, 40)
        elif 90 < self.heading() < 180:
            randomness = r.randrange(210, 250)
        elif 180 < self.heading() < 270:
            randomness = r.randrange(110, 160)
        elif 0 < self.heading() < 90:
            randomness = r.randrange(290, 350)
        self.seth(randomness)
        self.fd(20)

    def is_collide(self, paddle_list):
        for paddle_object in paddle_list:
            if self.distance(paddle_object.pos()) < 15:
                return True
        return False
#
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=600, height=600)
#
# ball = Ball()
#
# while True:
#     ball.move()
#     if not -280 < ball.xcor() < 280:
#         ball.bounce_paddle()
#     elif not -280 < ball.ycor() < 280:
#         ball.bounce_wall()
#
# screen.exitonclick()