from turtle import Screen
from snakes import Snake
import time
from food import Food
from scoreboard import ScoreBoard

snake = Snake(3, 600, 600)
screen = Screen()
screen.setup(width=600, height=600)
f = Food(600, 600)
screen.bgcolor('black')
screen.title("Tommy's snake game.")
screen.tracer(0)

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

game_is_on = True
score = 0

while game_is_on:
    text_output = f"Your current score is {score}"
    board = ScoreBoard(600, 600, text_output)
    # Each time the while-loop class is called, a new ScoreBoard object is created.
    time.sleep(difficulty)
    snake.move()
    screen.update()
    board.clear()
    if snake.snake_head.distance(f.pos()) < 20:
        snake.add_snake()
        f.move_to_random()
        score += 1
    elif snake.self_bite():
        game_is_on = False
        board.clear()
        board = ScoreBoard(600, 600, f"You bit yourself! Final Score {score}")
    elif snake.is_snake_out_of_bounds():
        game_is_on = False
        board.clear()
        board = ScoreBoard(600, 600, f"You hit the wall! Final Score {score}")

screen.exitonclick()
