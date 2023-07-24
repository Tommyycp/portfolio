from turtle import Screen
from snakes import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Tommy's snake game.")
screen.tracer(0)
difficulty = 0

snake = Snake(3, 600, 600)
f = Food(600, 600)
board = ScoreBoard(600, 600)

prompt = screen.textinput("Select a difficulty level", "Easy, normal, or hard?")
prompt = prompt.lower()

if prompt == 'easy':
    difficulty = 0.25
elif prompt == 'normal':
    difficulty = 0.15
elif prompt == 'hard':
    difficulty = 0.1

screen.listen()
screen.onkeypress(snake.north, 'Up')
screen.onkeypress(snake.south, 'Down')
screen.onkeypress(snake.west, 'Left')
screen.onkeypress(snake.east, 'Right')

while True:
    time.sleep(difficulty)
    snake.move()
    screen.update()
    if snake.snake_head.distance(f.pos()) < 20:
        snake.add_snake()
        f.move_to_random()
        board.add()
    elif snake.self_bite():
        snake.reset()
        board.reset()
    elif snake.is_snake_out_of_bounds():
        snake.reset()
        board.reset()


screen.exitonclick()
