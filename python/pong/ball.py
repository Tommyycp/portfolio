from turtle import Turtle, Screen
import random as r


class Ball(Turtle):

    '''
    Exiting bug: The ball will be stuck infinitely when the angle is at 356 degree. Such angle is currently unsolvable.
    Will revisit with more knowledge in geometry and math.
    '''

    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.up()
        self.shape('circle')
        self.color('pink')

    def move(self):
        self.fd(10)

    def bounce_paddle(self):
        if 91 <= self.heading() <= 269:
            randomness = r.randrange(-50,50)
            self.seth(randomness)
        elif 270 <= self.heading() <= 360 or 0 <= self.heading() <= 90:
            randomness = r.randrange(120, 250)
            self.seth(randomness)
        self.fd(10)

    def bounce_wall(self):
        if 0 < self.heading() < 90:
            self.seth(360 - self.heading())
            print(f"{self.pos()}, {self.heading()}")
        elif 180 < self.heading() < 270:
            self.seth(self.heading() - 45)
            print(f"{self.pos()}, {self.heading()}")
        else:
            self.seth(self.heading() + 45)
            print(f"{self.pos()}, {self.heading()}")


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