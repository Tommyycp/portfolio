# TODO 1: Create the screen
# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep score

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Pong")

screen.tracer(0)
paddle = Paddle(1000, 600)
ball = Ball()
scoreboard = Scoreboard(1000, 600)

screen.listen()
screen.onkeypress(paddle.left_paddle_up, 'w')
screen.onkeypress(paddle.left_paddle_down, 's')
screen.onkeypress(paddle.right_paddle_up, 'Up')
screen.onkeypress(paddle.right_paddle_down, "Down")

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(0.1)
    if ball.xcor() > 500 or ball.xcor() < -500:
        game_is_on = False
    elif not -270 < ball.ycor() < 270:
        ball.bounce_wall()
    elif ball.is_collide(paddle.left_paddle):
        scoreboard.add_score('left')
        ball.bounce_paddle()
    elif ball.is_collide(paddle.right_paddle):
        scoreboard.add_score('right')
        ball.bounce_paddle()
    screen.update()

screen.exitonclick()
