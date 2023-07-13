from turtle import Screen
from snakes import Snake
import time
from food import Food

snake = Snake(3, 600, 600)
screen = Screen()
screen.setup(width=600, height=600)
f = Food(600, 600)
screen.bgcolor('black')
screen.title("Tommy's snake game.")
screen.tracer(0)

screen.listen()
screen.onkeypress(snake.north, 'Up')
screen.onkeypress(snake.south, 'Down')
screen.onkeypress(snake.west, 'Left')
screen.onkeypress(snake.east, 'Right')

game_is_on = True
while game_is_on:
    if snake.is_snake_on_cake(f.food.xcor(), f.food.ycor()):
        snake.add_snake()
        f.random()
    time.sleep(0.1)
    snake.move()
    screen.update()
    if snake.self_bite():
        game_is_on = False
    elif snake.is_snake_out_of_bounds():
        game_is_on = False

screen.exitonclick()
