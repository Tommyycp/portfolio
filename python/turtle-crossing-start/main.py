# Finished TODO 1: A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
# Finished TODO 2: Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
# Finished TODO 3: When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.
# Finished TODO 4: When the turtle collides with a car, it's game over and everything stops.

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
level = 0
cars = CarManager(600, 600, level)
score = Scoreboard(600, 600, level)
player = Player()

game_is_on = True
game_loop = 0
frequency = 6


while game_is_on:
    screen.tracer(0)
    screen.listen()
    screen.onkeypress(player.move, 'w')
    if cars.is_crash(player):
        print ("test")
        game_is_on = False
    elif player.ycor() >= 280:
        level += 1
        screen.clearscreen()
        cars.clear_cars()
        cars = CarManager(600, 600, level)
        player = Player()
        score = Scoreboard(600, 600, level)
    elif game_loop == frequency:
        car = cars.create()
        game_loop = 0
    else:
        cars.move()
        time.sleep(0.05)
        screen.update()
        game_loop +=1

screen.exitonclick()