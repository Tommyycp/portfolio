from turtle import Screen
from snakes import Snake
import time
from food import Food

snake = Snake(3, 600, 600)
screen = Screen()
screen.setup(width=600, height=600)
f = Food(600, 600)
f.create_food()
screen.bgcolor('black')
screen.title("Tommy's snake game.")
screen.tracer(0)

screen.listen()
screen.onkey(snake.north, 'Up')
screen.onkey(snake.south, 'Down')
screen.onkey(snake.west, 'Left')
screen.onkey(snake.east, 'Right')

game_is_on = True
while game_is_on:
    if f.x_cor - 10 <= snake.snake_head.xcor() <= f.x_cor + 10:
        if f.y_cor - 10 <= snake.snake_head.ycor() <= f.y_cor + 10:
            snake.add_snake()
            f.random()
    time.sleep(0.2)
    snake.move()
    screen.update()
    if snake.self_bite():
        game_is_on = False
    elif snake.is_snake_out_of_bounds():
        game_is_on = False

screen.exitonclick()
